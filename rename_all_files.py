from os import listdir, getcwd, makedirs, system
from os.path import isfile, join, exists
mypath = getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

notin = ['add_border.py','deskripsi.txt','blank.jpg','border.png','borderonly.png']
folder = getcwd()+'\\border'
if not exists(folder):
	makedirs(folder)

temp = getcwd()+'\\temp'
if not exists(temp):
	makedirs(temp)

temp = getcwd()+'\\resize'
if not exists(temp):
	makedirs(temp)

i=0
for x in onlyfiles:
	if  x not in notin and len(x) > 0:
		img_path = x
		i = i + 1
		#print(x)
		temp_path = 'temp\\'+x
		resize_path = 'resize\\'+'klakson_{}.mp3'.format(i)
		out_path = 'border\\'+x
		#border_path = 'border.png'
		#blank_path = 'blank.jpg'
		#print(resize_path)
		#resize
		cmd0 ='copy ' + img_path + ' ' + resize_path
		print(img_path)
		print(resize_path)
		print(cmd0)
		system(cmd0)
