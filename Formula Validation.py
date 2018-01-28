# We used Topological sorting for validation of given equations in formula.
# This Topological sort function provides order of nodes in a Directed Graph based on dependency and empty list if a cycle is present
# We took input of equations and created a dictionary ‘dic’ according to dependency
# e.g. Followings are input equations:
# A = B+C
# B= I/J
# C = F*G
# These will represent following dictionary and Directed Graph structure:
#  dic = {'c': ['a'], 'f': ['c'], 'g': ['c'], 'b': ['a'], 'i': ['b'], 'j': ['b'], 'a': []}
#                     A
#                   /   \     # Assume these are arrow in upward direction (represents dependency)
#                  B     C
#                 /\     /\
#                I J    F G
# This dictionary is used in Topological sort as input
# We used one more dictionary ‘eqn’ to print output result in order provided from Topological sort
# e.g. :  In previous example eqn value will be:
# eqn = {'c': 'c = f*g', 'b': 'b = i/j', 'a': 'a = b+c'}

# Assuption Each input equation is valid equation where Left hand value is always character
# Input format:
# First line is an integer value which represents number of equations
	# After that each line represents and equation

def Topologicalsort(G):
    in_degree = {u: 0 for u in G}  # calculate in-degree value of each node
    for u in G:
        for v in G[u]:
            in_degree[v] += 1
    Q = []                         # Initialize Queue as empty list
    for u in in_degree:             # collect nodes which have zero in-degree
        if in_degree[u] == 0:
            Q.append(u)
    result = []                   # initialized output order
    while (len(Q) > 0):
        u = Q.pop(0)              # choose node which  in-degree value is zero
        result.append(u)         # 'remove' it from Graph G
        for v in G[u]:
            in_degree[v] -= 1        # Decrease degree of each adjacent node of current node
            if in_degree[v] == 0:
                Q.append(v)
    if len(result) == len(G):
        return result            # return calculated order
    else:                        # if a cycle is present
        return []                # return an empty list


# Assuption Each input equation is valid equation where Left hand value is always character
N = input("Enter number of equations ")    # Input number of equations
N = int(N)
eqn = {}                               # Initialized dictionary 'eqn' for storing equations (It helps in final output)
dic = {}                              # Initialized a dictionary to store equation with respect to dependency
for i in range(N):
    x = input().strip()
    eqn[x[0]] = x               # First character is always a Left hand side value
    if(x[0] not in dic):
        dic[x[0]] = []
    for j in range(1, len(x)):
        if(x[j].isalpha()):       # Creating nodes from alphabate characters
            dic[x[j]] = [x[0]]

order = Topologicalsort(dic)       # Output order from Topological sort function
if(len(order) == 0):
    print("Input is not a valid Formula, Cyclic in Nature")
else:
    order.reverse()                  # Reverse the order because as required Problem statement example
    print("Valid Formula - Dependency order is ")
    for i in range(len(order)):
        if (order[i] in eqn.keys()):     # Using 'eqn' dictionary to output equation sequence baesd on order
            print(eqn[order[i]])
