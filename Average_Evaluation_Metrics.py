import json
import os 

FMeas=0
PScore=0
GotoScore=0
Cemgil_1=0
Cemgil_2=0
AMLc=0
AMLt=0
CMLc=0
CMLt=0
InfGain=0
index = 0 


for file in os.listdir("Path to results directory"):
	if file.endswith(".json"):
		jsonFile = open('Eval/'+str(file), 'r')
		values = json.load(jsonFile)
		Cemgil_1 = Cemgil_1 + values['Cemgil']
		FMeas = FMeas + values['F-measure']
		Cemgil_2 = Cemgil_2 + values['Cemgil Best Metric Level']
		GotoScore = GotoScore + values['Goto']
		PScore = PScore + values['P-score']
		InfGain = InfGain + values['Information gain']
		CMLc = CMLc + values['Correct Metric Level Continuous']
		CMLt = CMLt + values['Correct Metric Level Total']
		AMLt = AMLt + values['Any Metric Level Total']
		AMLc = AMLc + values['Any Metric Level Continuous']
		index = index + 1
		jsonFile.close()
		

print FMeas/index
print Cemgil_1/index
print Cemgil_2/index
print CMLc/index
print CMLt/index
print AMLc/index
print AMLt/index
print GotoScore/index
print PScore/index
print InfGain/index
