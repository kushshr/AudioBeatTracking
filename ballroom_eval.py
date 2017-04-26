import os
import re


for root, dirs, files in os.walk("/media/kushagra/529EC5229EC50009/Users/kushagra/Master_Datasets/BallroomData"):
	for f in files:
		if '.wav' in f:
			command = root+'/'+f 	
			os.system("python MMBeatTracker single " + str(command) + " >" +  "./Ballroom_Results/" + str(f) + ".txt")
		

