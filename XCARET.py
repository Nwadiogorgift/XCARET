import os,platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from XCARET import chigozie_YayanGanteng
    chigozie_YayanGanteng()
elif bit == '32bit':
    from XCARET import chigozie_YayanGanteng
    chigozie_YayanGanteng()
