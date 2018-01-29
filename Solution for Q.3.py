N = int(input().strip())
arr = list(map(int, input().strip().split(",")))
Sum = int(input().strip())

dict = {}
for i in range(N):
    if (arr[i] not in dict.keys()):
        dict[arr[i]] = i

Index = [None]*3
IndexDict = {}

for i in range(N):
    for j in range(i+1, N):
        K = Sum - (arr[i]+arr[j])
        if(K in dict.keys()):
            if((i != dict[K]) and (j != dict[K])):
                Index[0] = i
                Index[1] = j
                Index[2] = dict[K]
                Index.sort()
                IndexString = str(Index[0])+str(Index[1])+str(Index[2])
                if(IndexString not in IndexDict.keys()):
                    print(i,j,dict[K])
                    IndexDict[IndexString] = 1


#Time complexity will be (3log3)*O(n^2) equivalent to O(n^2) 3log3 for sorting array of size 3
#Space complexity will be O(n) for first dictionary + O(3)for index dictionary