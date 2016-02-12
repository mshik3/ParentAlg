import csv
import math

results = {}


pledges = {}
parents = {}
matched = {}

def stableMatching():
	for parent in parents:
		#find first free child on parents list
		for child in parents[parent]:
			# Child's rank of the parent
			rank = 8
			for i in range(len(pledges[child])):
				if parent == pledges[child][i]:
					rank = i
					break
			if child not in matched.keys():
				matched[child]=(parent,rank)
			else:
				if rank < matched[child][1]:
					matched[child]=(parent,rank)
	for key in matched:
		results[matched[key][0]].append(key)
		del pledges[key]
		parents[matched[key][0]].remove(key)
			


with open('TestData/TestPledgeResults.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		row.remove(row[0])
		pledges[row[0]]=row[1:len(row)]

del pledges['Full Name'];



with open('TestData/TestParentResults.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		row.remove(row[0])
		parents[row[0]]=row[1:len(row)]
del parents['Name/spouse'];
for parent in parents:
	results[parent]=[]
print(len(pledges))
stableMatching()
print(len(pledges))

for parent in results:
	print parent,": ", results[parent]

print 'pledges not sorted: ' , pledges.keys()

