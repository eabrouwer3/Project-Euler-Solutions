class Node():
    
    num = None
    left = None
    right = None

    def setNum(self, num):
        self.num = num

    def getNum(self):
        return self.num

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

def recurseTree(root):
    if root is None:
        return
    print root.getNum()
    recurseTree(root.getLeft())
    recurseTree(root.getRight())

def add(root, left, right):
    return

string = "75\n95 64\n17 47 82\n18 35 87 10\n20 04 82 47 65\n19 01 23 75 03 34\n88 02 77 73 07 63 67\n99 65 04 28 06 16 70 92\n41 41 26 56 83 40 80 70 33\n41 48 72 33 47 32 37 16 94 29\n53 71 44 65 25 43 91 52 97 51 14\n70 11 33 28 77 73 17 78 39 68 17 57\n91 71 52 38 17 14 91 43 58 50 27 29 48\n63 66 04 68 89 53 67 30 73 16 69 87 40 31\n04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
rows = list.reverse([dict(list(enumerate(s.split(), start=1))) for s in string.split("\n")])
root = Node()

root.setNum(rows[14][1])
left = Node()
left.setNum(rows[13][1])
left2 = Node()
left2.setNum(rows[12][1])
right2 = Node()
right2.setNum(rows[12][2])
left.setLeft(left2)
left.setRight(right2)
right = Node()
right.setNum(rows[13][2])
left3 = Node()
left3.setNum(rows[12][2])
right3 = Node()
right3.setNum(rows[12][3])
right.setLeft(left3)
right.setRight(right3)
root.setLeft(left)
root.setRight(right)

recurseTree(root)
