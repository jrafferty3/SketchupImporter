import os
import zipfile
import shutil
import glob

files = glob.glob('C:/Users/Patrick/Documents/temp/models/*.dae')
for f in files:
	os.remove(f)
	
files = glob.glob('C:/Users/Patrick/Documents/models/*.dae')
for f in files:
	os.remove(f)

for line in open("models.txt","r").readlines():
	line = line[:line.find(" ")]
	#location zip files are downloaded to
	downloads = "C:/Users/Patrick/Downloads/"
	#where to open zip files
	zip_to = "C:/Users/Patrick/Documents/temp"
	#where the models are located
	temp = zip_to+"/models/"
	#where to save the models as .dae files to be converted
	models = "C:/Users/Patrick/Documents/models/"
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
	command = '"C:/Program Files/Autodesk/FBX/FBX Converter/2013.3/bin/FBXCONVERTER" C:/Users/Patrick/Documents/models/'+line+'.dae C:/Users/Patrick/Documents/Research_models/'+line+'.fbx'
	os.system(command);