import os
import essentia.standard as ess 

for root, dirs, files in os.walk("/media/kushagra/529EC5229EC50009/Users/kushagra/Master_Datasets/SMC_MIREX/SMC_MIREX/SMC_MIREX_Audio"):
	for f in files:
		#Use Essentia to load the method
		command = root + '/' + f
		audioLoader = ess.MonoLoader(filename = str(command))
		audio = audioLoader()
		filt = ess.BandReject(bandwidth = 1700, cutoffFrequency= 300 )
		filtof = filt(audio)
		writer = ess.MonoWriter(filename = "/media/kushagra/529EC5229EC50009/Users/kushagra/Master_Datasets/SMC_MIREX/SMC_MIREX/Augmentations/" + str(f) , format="wav")
		write = writer(filtof)
