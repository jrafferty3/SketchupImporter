You will need HTML Agility pack to run this.
It can be found here: http://htmlagilitypack.codeplex.com/

You will also need AutoDesks FBX converter.
It can be found here: http://usa.autodesk.com/adsk/servlet/pc/item?id=10775855&siteID=123112

This is a program that finds Collada files on Google Sketchup and converts the models to a form that can be used in Unity.
The models can be placed in whatever file you want by setting it in the converter.py file. 
The program requires a models.txt file that has the name of the file followed by search terms.
There is an example of the text file that looks up a KitchenCounter model and a vase model.
All of the places to input your file paths are marked in the code.
The program assumes the .dae files are in a folder labeled models when it is unzipped.
If there is not a folder named models in the zip, then the program will not convert the .dae file.
There is also a chance that the search terms you give are too specific and there are no results that match.
The program grabs the first match on the page so there is no guarantee the model it returns will be the exact model you want.
