#!/usr/bin/env python3

from Cryptodome.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from gmpy2.gmpy2 import iroot

e = 3

n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
ct = 1220012318588871886132524757898884422174534558055593713309088304910273991073554732659977133980685370899257850121970812405700793710546674062154237544840177616746805668666317481140872605653768484867292138139949076102907399831998827567645230986345455915692863094364797526497302082734955903755050638155202890599808147130204332030239454609548193370732857240300019596815816006860639254992255194738107991811397196500685989396810773222940007523267032630601449381770324467476670441511297695830038371195786166055669921467988355155696963689199852044947912413082022187178952733134865103084455914904057821890898745653261258346107276390058792338949223415878232277034434046142510780902482500716765933896331360282637705554071922268580430157241598567522324772752885039646885713317810775113741411461898837845999905524246804112266440620557624165618470709586812253893125417659761396612984740891016230905299327084673080946823376058367658665796414168107502482827882764000030048859751949099453053128663379477059252309685864790106

l = iroot(ct, 3)
assert l[1] == True
print(long_to_bytes(l[0]))