import os.path
os.path.exists('big_buck_bunny_480p_h264SyncLogo')

os.path.isfile('Desktop')

try:
	f = open('big_buck_bunny_480p_h264SyncLogo.mp4')
	f.close()
except FileNotFoundError:
    print('File does not exist')

# checking if a file is accesible or have access permissions

try:
    f = open('big_buck_bunny_480p_h264SyncLogo')
    f.close()
except IOError:
    print('The File not Found or Accesible')


# logic interface

import pathlib
path = pathlib.Path('big_buck_bunny_480p_h264SyncLogo.mp4')

# escribir <path> en terminal tras ejecutar el codigo
# Comprobar si el path existe path.exists() o path.is_file()
import os
os.getcwd()
from pathlib import Path
mypath = Path().absolute()
print(mypath)
