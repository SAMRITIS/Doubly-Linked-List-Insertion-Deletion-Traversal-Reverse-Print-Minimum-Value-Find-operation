class node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.pre = None
class dlink:

    def __init__(self):
        self.head = None
    def insert(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
            new.next = None
            new.pre = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new
            new.pre = temp
            new.next = None
    def show(self):
        lst = []
        temp = self.head
        while temp is not None:
            x = temp.data
            lst.append(x)
            temp = temp.next
        print(lst)
    def rshow(self):
        lst = []
        temp = self.head
        while temp is not None:
            x = temp.data
            lst.append(x)
            temp = temp.next
        lst.reverse()
        print(lst)
    def min(self):
        lst = []
        temp = self.head
        while temp is not None:
            x = temp.data
            lst.append(int(x))
            temp = temp.next
        print("Minimum Value of list is", min(lst))
    def hinsert(self, v):
        new = node(v)
        if self.head is None:
            self.head = new
            new.next = None
            new.pre = None
        else:
            new.next = self.head
            new.pre = None
            self.head = new
    def dele(self, v):
        temp = self.head
        if temp.data ==  v:
            self.head = self.head.next
            self.head.pre = None
        else:
            while temp.data!=v:
                temp = temp.next
            if temp.next is not None:
                temp.next.pre = temp.pre
            if temp.pre is not None:
                temp.pre.next = temp.next
h = dlink()
print("Insert Node 100 at beginning")
h.hinsert(100)
h.show()
print()
print("Insert Node 20 at end")
h.insert(20)
h.show()
print()
print("Insert Node 30 at end")
h.insert(30)
h.show()
print()
print("Insert Node 40 at end")
h.insert(40)
h.show()
print()
print("Insert Node 50 at end")
h.insert(50)
h.show()
print()
print("Insert Node 60 at end")
h.insert(60)
h.show()
print()
print("Insert Node 200 at beginning")
h.hinsert(200)
h.show()
print()
print("Reverse Traversing")
h.rshow()
print()

h.min()
print()
print("Deleting Node 200")
h.dele(200)
h.show()
print()
print("Deleting Node 40")
h.dele(40)
h.show()








