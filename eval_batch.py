import os
import re

#Copy in madmom/bin and run

command = "Annotation directory path"
for root, dirs, files in os.walk(str(command)):
	for f in files:
		x = f.strip('.beats')
		array = []
		#with open(str(command) + "/" + str(f), 'r') as foo:
		foo = open(str(command) + "/" + str(f), 'r')
		for line in foo:
			spl = line.split(" ")
			#print spl[0]
			array.insert(len(array),spl[0])
		thefile = open('Temp directory path'+ str(x) + ".txt"  , 'wb')
		for item in array:
			thefile.write("%s\n" % item)
		thefile.close()

		xy =  "./beat_eval.py -o Eval/result_" + str(x) + ".json " + "Temp directory path" + str(x) + ".txt " + "Detected Beats Directory path" + str(x) +".wav.txt"
	
		os.system(xy)


#./beat_eval.py -o 3.txt test_Albums-AnaBelen_Veneo-01.txt Albums-AnaBelen_Veneo-01.wav.txt

#./beat_eval.py -o Eval/result_Albums-AnaBelen_Veneo-01.json Temp/test_Albums-AnaBelen_Veneo-01.txt Ballroom_Results/Albums-AnaBelen_Veneo-01.wav.txt
