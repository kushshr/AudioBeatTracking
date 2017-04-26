import os
from essentia import *

# TO be run inside mir_eval/evaluators

or root, dirs, files in os.walk("Reference annotaion path goes here"):
	for f in files:
		command = root+'/'+f
		x = f.strip('.beats')	
		loader = MonoLoader(filename=str(command))
		audio = loader()
		beatT=BeatTrackingMultiFeature(audio)

		thefile = open('Temp Directory Path Goes here'+ str(x) + ".txt"  , 'w')
		for item in beatT:
			thefile.write("%s\n" % item)
		

		os.system("./beat_eval.py -o Eval/result_" + str(x) + ".json " + "Temp Directory Path Goes here" + str(x) + ".txt " + "Detected beats folder path goes here" + str(x) +".wav.txt")

