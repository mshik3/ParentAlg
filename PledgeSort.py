import csv
import math
from random import shuffle

#populate pledge list from CSV
pledges = []
with open('Database/CSV/example.csv', 'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
         pledges.append(row)
shuffle(pledges)

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
	   fo.write(results[i][index][0]+"\n")
	fo.write("\n\n")
	# Close opend file
	fo.close()
