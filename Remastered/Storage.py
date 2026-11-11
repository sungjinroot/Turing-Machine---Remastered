
class Cell:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class Tape:
    def __init__(self):
        self.head = Cell("_")
        self.leftBorder = self.head 
    
    def left(self):
        if self.head.left != None:
            self.head = self.head.left

            if self.head.right.right == None:
                if self.head.right.data == "_":
                    self.head.right = None
        self.printTape()
        print()

    def right(self):
        if self.head.right == None:
            newCell = Cell("_")
            self.head.right = newCell
            newCell.left = self.head
            self.head = self.head.right
        else:
            self.head = self.head.right
        self.printTape()
        print()

    def write(self,char):
        self.head.data = char
        self.printTape()
        print()
    
    def read(self):
        return self.head.data
    
    def printTape(self):
        current = self.leftBorder
        while current != None:
            if current == self.head:
                print(f"[{current.data}]",end=" ")
            else:
                print(current.data,end=" ")
            current = current.right

