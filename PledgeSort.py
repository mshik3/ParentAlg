import csv
import math
from random import shuffle

#populate pledge list from CSV
freshmen = []
sophomores = []
juniors = []
seniors = []

with open('Database/CSV/example.csv', 'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
        #pledges.append(row)
        if "freshman" in row[0]:
          freshmen.append(row)
        elif "sophomore" in row[0]:
          sophomores.append(row)
        elif "junior" in row[0]:
          juniors.append(row)
        elif "senior" in row[0]:
          seniors.append(row)

shuffle(freshmen)
shuffle(sophomores)
shuffle(juniors)
shuffle(seniors)

pledges = [None] * (len(freshmen)+len(sophomores)+len(juniors)+len(seniors))*200
length = (len(freshmen)+len(sophomores)+len(juniors)+len(seniors))*200



print 'freshmen:',len(freshmen)
print 'sophomores:',len(sophomores)
print 'juniors:',len(juniors)
print 'seniors:',len(seniors)


i = 0
if(len(freshmen)>0):
  iterator = length/len(freshmen)
  while(len(freshmen)>0):
    if(pledges[i] is None):
      pledges[i]=freshmen.pop()[0]
    i+=iterator
i = 4
if(len(sophomores)>0):
  iterator = length/len(sophomores)
  while(len(sophomores)>0):
    if(pledges[i] is None):
      pledges[i]=sophomores.pop()[0]
    i+=iterator

i = 8
if(len(juniors)>0):
  iterator = length/len(juniors)
  while(len(juniors)>0):
    if(pledges[i] is None):
      pledges[i]=juniors.pop()[0]
    i+=iterator

i = 12
if(len(seniors)>0):
  iterator = length/len(seniors)
  while(len(seniors)>0):
    if(pledges[i] is None):
      pledges[i]=seniors.pop()[0]
    i+=iterator

pledges = filter(None, pledges)



dynasties = ["Eagles","Torches","FMNs","Scouts","Diamonds","Oaks"]
percentages = []

#sum must be less than or equal to 1
percentages.append(0.16) #Eagles
percentages.append(0.16) #Torches
percentages.append(0.16) #FMNs
percentages.append(0.16) #Scouts
percentages.append(0.16) #Diamonds
percentages.append(0.16) #Oaks

#Pledge placing
results = [None] * 6
count = 0
for i in range(len(percentages)):
  results[i] = [None] * int(percentages[i]*len(pledges))
  for j in range(len(results[i])):
    results[i][j] = pledges[count]
    count+=1
leftover = len(pledges)-count
for i in range(leftover):
  results[i%6].append(pledges[count])
  count+=1

#Output to files
for i in range(len(dynasties)):
	fo = open("Database/Pledges/"+dynasties[i]+".txt", "w+")
	fo.write(dynasties[i]+": \n")
	for index in range(len(results[i])):
	   fo.write(results[i][index]+"\n")
	fo.write("\n\n")
	# Close opend file
	fo.close()
