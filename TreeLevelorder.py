class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def levelorder(root):
    if(root):
        #temp = Node(None)
        Queue = []
        #temp = root
        Queue.append(root)
        #print(temp.val, ' ', temp.left, ' ', temp.right.val)
        while(len(Queue) > 0):
            temp = Queue.pop(0)
            print(temp.val, end=' ')
            #temp = Queue.pop()
            if(temp.right is not None):
                Queue.append(temp.right)
            if(temp.left is not None):
                Queue.append(temp.left)
            #print(temp.val, ' ')


levelorder(root)

#print(root.val, ' ', root.left, ' ', root.right.val)




