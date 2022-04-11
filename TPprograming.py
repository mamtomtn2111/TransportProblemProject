def ongkosMinimum(s,d, sTot, dTot, terkecil,supply ,demand):
	table=[]
	for x in range(s):
		temp=[]
		for y in range(d):
			temp.append(0)
		table.append(temp)
	toAllocate(table,0, sTot, dTot, terkecil,supply, demand)
	return table

def toAllocate(table2,i, sTot, dTot, terkecil,supply, demand):
	if sTot==0 and dTot==0:
		return table2
	x=terkecil[i][1]
	y=terkecil[i][2]
	if supply[x]<demand[y]:
		table2[x][y]=supply[x]
		demand[y]-=supply[x]
		supply[x]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,i+1, sTot, dTot, terkecil,supply, demand)
	elif supply[x]>demand[y]:
		table2[x][y]=demand[y]
		supply[x]-=demand[y]
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,i+1, sTot, dTot, terkecil,supply, demand)
	elif supply[x]==demand[y]:
		table2[x][y]=supply[x]
		supply[x]=0
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,i+1, sTot, dTot, terkecil,supply, demand)

def sortCost(s, d, cost):
	indexCost=[]
	for x in range(s):
		for y in range(d):
			temp=[]
			temp.insert(0,cost[x][y])
			temp.insert(1,x)
			temp.insert(2,y)
			indexCost.append(temp)
	indexCost=sorted(indexCost)
	return indexCost

def main(cost, supply, demand):
	sTot=sum(supply)
	dTot=sum(demand)
	s=len(supply)
	d=len(demand)
	if sTot<dTot:
		s+=1
		supply.append(dTot - sTot)
		sTot=sum(supply)
		temp=[]
		for x in range(len(demand)):
			temp.append(0)
			cost.append(temp)

	elif sTot>dTot:
		d+=1
		demand.append(sTot - dTot)
		dTot=sum(demand)
		for x in range(len(supply)):
			cost[x].append(0)
	terkecil=sortCost(s, d, cost)
	resultTable=ongkosMinimum(s,d, sTot, dTot, terkecil, supply,demand)
	return resultTable,s,d





