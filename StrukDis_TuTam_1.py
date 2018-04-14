def adjacency_matrix(nodes, vertices):
	adj_mtx = []

	for a in nodes: #for every element in list nodes
		adj_row = [] #create empty list
		for b in nodes: #for every element in list nodes
			if (a,b) in vertices or (b,a) in vertices: #if (a,b) or (b,a) is in list vertices
				adj_row.append(1) #add 1 to empty list adj_row
			else:
				adj_row.append(0) #add 0 to empty list adj_row
		adj_mtx.append(adj_row) #add row to result matrix

	for row in adj_mtx: #print each row
		print (row)


node = input("Input nodes (use ',' to separate values):\n") #ask input
v = node.rstrip().split(",") #strip return character (\n and \r) from string, then split string into several parts. splits marked by ','
v = [x.strip(' ') for x in v] #remove extra spaces from each element in list v

vertex = input("Input vertices (use ' ' (space) to separate values: (ex: 1,2 2,3 3,3)\n")
vertex = vertex.rstrip().split(" ")
e = []
for pair in vertex:
	vert_pair = tuple(pair.split(",")) #create tuple from every pair in list vertex, ex. turns string "1,2" into tuple ('1','2')
	e.append(vert_pair)

adjacency_matrix(v, e)

