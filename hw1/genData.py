import csv, random, copy
import matplotlib.pyplot


class DayData(object):
    def __init__(self, id):
        self.id = id
        self.PM25 = [0]*24

def genTrainTimezone():
	LASTHOUR = 14
	# pickNum = 2	
	count = 0
	for i in range(0,240):
		# sectionPick = [False] * pickNum
		pick = 0
		cpList = []
		pickNum = random.randint(1,14)
		# cpList = random.sample(range(1,14),pickNum)
		# while(pick < pickNum):
		# 	cp = random.randint(0,LASTHOUR)
		# 	if(cp <= LASTHOUR/pickNum and sectionPick[0] == False):			
		# 		cpList.append(cp)
		# 		sectionPick[0] = True				
		# 	elif(cp > LASTHOUR/pickNum and sectionPick[1] == False):		
		# 		cpList.append(cp)
		# 		sectionPick[1] = True				
		# 	else:
		# 		continue
		# 	pick = pick + 1
		# 	flag = random.randint(0,1)
		# 	if(flag == 0):
		# 		break
		cpList = list(range(14))
		cpList = [x+1 for x in cpList]
		timezone.append(cpList)


def genDayObject():
	f = open('PMdata.csv', 'r')
	day = 1
	Material = ["AMB_TEMP","CO","NMHC","NO","NO2","O3","PM10","PM2.5","RAINFALL"]
	d = DayData(0)
	for row in csv.reader(f):
		row[0] = row[0][1:] # get day number	
		if(d.id != int(row[0])):
			tmp = copy.copy(d)
			data.append(tmp)
			d.id = int(d.id) + 1
			day = day + 1
		if(row[1] == "AMB_TEMP"):
			d.AMB_TEMP = row[2:]
		elif(row[1] == "CO"):
			d.CO = row[2:]
		elif(row[1] == "NMHC"):
			d.NMHC = row[2:]
		elif(row[1] == "NO"):
			d.NO = row[2:]
		elif(row[1] == "NO2"):
			d.NO2 = row[2:]
		elif(row[1] == "O3"):
			d.O3 = row[2:]
		elif(row[1] == "PM10"):
			results = list(map(float, row[2:]))
			d.PM10 = results
		elif(row[1] == "PM2.5"):		
			results = list(map(float, row[2:]))
			d.PM25 = results
		elif(row[1] == "RAINFALL"):
			d.RAINFALL = row[2:]
	data.append(d)
	f.close()

def genTrainValSample(num):
	with open("data3/training" + num + ".csv", "w", newline='') as f1:
		with open("data3/valid"+ num + ".csv", "w", newline='') as f2:
			with open("data3/all"+ num +".csv", "w", newline='') as f3:
				writer = csv.writer(f1)
				writer2 = csv.writer(f2)
				writer3 = csv.writer(f3)
				for i in range(0,240):			
						for ts in timezone[i]:
							if(-1 in data[i].PM25):
								continue
							# if(-1 in data[i].O3):
							# 	continue							
							if(i <= 168):																		
								writer.writerow(data[i].PM25[ts:ts+10])
							else:								
								writer2.writerow(data[i].PM25[ts:ts+10])							
							writer3.writerow(data[i].PM25[ts:ts+10])
						

					
timezone = []
data = []
sampleData = []
trainSet = []
validSet = []

num = input()

genTrainTimezone()
genDayObject()
genTrainValSample(num)

# avgValueList = genTrainValSet()
# print(avgValueList)



  