import os
import re

#Copy in madmom/bin and run

for root, dirs, files in os.walk("/media/kushagra/529EC5229EC50009/Users/kushagra/Master_Datasets/BallroomAnnotations-master"):
	for f in files:
		command = root+'/'+f
		x = f.strip('.beats')	
		os.system("./mir_eval/mir_eval-master/evaluators/beat_eval.py -o " )
		

