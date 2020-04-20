

class SearchNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = SearchNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = SearchNode(data)
                else:
                    self.right.insert(data)
                   
        else:
            self.data = data
    
    def find(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + " Not Found"
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return str(data) + " Not Found"
            return self.right.find(data)
        else:
            print(str(self.data) + ' is found')

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


if __name__ == "__main__":
    root = SearchNode(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.printTree()
    print(root.find(7))
    print(root.find(14))