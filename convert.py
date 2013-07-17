import os
import zipfile
import shutil
import glob

files = glob.glob('path to temp file/*.dae')
for f in files:
	os.remove(f)
	
files = glob.glob('path to models/*.dae')
for f in files:
	os.remove(f)

for line in open("models.txt","r").readlines():
	line = line[:line.find(" ")]
	#location zip files are downloaded to
	downloads = "path to download folder"
	#where to open zip files
	zip_to = "path to a temp folder"
	#where the models are located
	temp = zip_to+"/models/"
	#where to save the models as .dae files to be converted
	models = "path to where to store .dae files for conversion"
	file = line+".dae"
	zp = zipfile.ZipFile(downloads+line+".zip","r");
	zp.extractall(zip_to);
	for root,dir,filenames in os.walk(temp):
		for filename in filenames:
			if filename.endswith(".dae"):
				os.rename(os.path.join(root,filename),os.path.join(root,file))
	shutil.move(temp+line+".dae",models)
	#conversion command
	#path to FBX converter + path to .dae file + location to save .fbx file
	command = '"path to Autodesks FBX converter" path to where .dae models are/'+line+'.dae path to where you want fbx files/'+line+'.fbx'
	os.system(command);