"""
c13.py

Cryptopals Set 2, Challenge 13
"""

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def pkcs7(bs, block_size):
    """
    An implementation of pkcs#7 padding.
    """
    # Find the amount needed to pad to correct length.
    pad = block_size - len(bs)%block_size
    if pad == 0:
        pad = block_size

    # Pad with padding length and return.
    return bs.encode() + bytearray([pad]*pad)


def pkcs7_unpad(bs, block_size):
    """
    An implementation of pkcs#7 unpadding.
    """
    # Check whether valid pkcs#7 padding.
    if not is_pkcs7(bs, block_size):
        raise Exception('Invalid pkcs#7 padding.')

    last = ord(bs[-1])
    return bs[:-last]


def is_pkcs7(bs, block_size):
    """
    Determines if a byte array is pkcs7 padded.
    """
    # Length must be a multiple of the block size.
    if len(bs) % block_size != 0:
        return False

    # Last byte cannot be greater than 15 or less than 1.
    last = ord(bs[-1])
    if last < 1 or last > block_size-1 or last > len(bs):
        return False

    # Check whether all padding is the same byte.
    return len([i for i in bs[-last:] if ord(i) != last]) == 0

secret_key = get_random_bytes(16)


def main():
    # email=aaaaaaaaaa
    # aaaaaaaaa@gmail.
    # com&uid=10&role=
    # user------------
    email = 'a'*19 + '@gmail.com'
    ##Above makes sure that the role= part is at the end of its block

    # This gives us the first part of our privilege escalation.
    p1 = profile_for(email)[:48]

    # email=aaaaaaaaaa
    # admin-----------
    # @gmail.com&uid=1
    # 0&role=user
    email = 'a'*10 + str(pkcs7('admin', 16))[2:-1] + '@gmail.com'

    ##above makes sure that the second block is made up of admin and then a bunch of dashes

    # This gives us the second part of our privilege escalation.
    p2 = profile_for(email)[16:32]
    print(p1)
    print(p2)
    print(p1 + p2)
    print(type(p1 + p2))
    print (dec_profile(p1 + p2))
    
    ##above will then be equals to
    # email=aaaaaaaaaa
    # aaaaaaaaa@gmail.
    # com&uid=10&role= admin-----------


def kv_parser(inp):
    """
    Converts a url-encoded string to a dictionary object.
    """
    return {obj[0]:obj[1]
            for obj in (obj.split('=') for obj in inp.split('&'))
            if len(obj) == 2}


def profile_for(email):
    """
    Generates an encrypted user profile based on an input email, without
    admin privileges.
    """
    # Input sanitization.
    email = email.replace('&', '')
    email = email.replace('=', '')
    return enc_profile('email=%s&uid=10&role=user' % email)


def enc_profile(profile):
    """
    Encrypts a url-encoded user profile.
    """
    profile = pkcs7(profile, 16)
    return AES.new(secret_key, AES.MODE_ECB).encrypt(profile)


def dec_profile(profile):
    """
    Decrypts and parses an encrypted url-encoded user profile.
    """
    profile = AES.new(secret_key, AES.MODE_ECB).decrypt(profile)

    try:
        return kv_parser(pkcs7_unpad(str(profile)[2:-1], 16))
    except:
        try:
            return kv_parser(profile)
        except:
            return profile


main()