import csv
import math

results = {}


pledges = {}
parents = {}

# Of the form [child, (parent, rankofparent, rankofchild)], Lower rank is better
matched = {}

def stableMatching():
	for parent in parents:
		#find first free child on parents list
		for j in range(len(parents[parent])):
			# Child's rank of the parent
			child = parents[parent][j]
			rank = 6
			for i in range(len(pledges[child])):
				if parent == pledges[child][i]:
					rank = i
					break
			if child not in matched.keys():
				matched[child]=(parent,rank,j)
			else:
				if (j+rank) < matched[child][1]+matched[child][1]:
					matched[child]=(parent,rank,j)
	print(matched)
	for i in range(len(matched.keys())-1,-1,-1):
		child = matched.keys()[i]
		if matched[child][1]>=6:
			del matched[child]
	for key in matched:
		results[matched[key][0]].append(key)
		del pledges[key]
		parents[matched[key][0]].remove(key)

	for pledge in reversed(pledges.keys()):
		results[pledges[pledge][0]].append(pledge)
		del pledges[pledge]

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
print len(pledges) , '\n'

for parent in results:
	print parent,": ", results[parent]

print 'pledges not sorted: ' , pledges.keys()

