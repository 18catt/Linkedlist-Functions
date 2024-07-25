class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #empty linkedlist
        self.n = 0 #number of nodes
    
    def __len__(self):
        return self.n
    
    def insertHead(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

    def insertTail(self, val): #append function
        newnode = Node(val)
        
        if self.head==None: #empty
            self.head = newnode
            self.n += 1
            return
        curr = self.head
        while(curr.next!=None):
            curr = curr.next
        curr.next = newnode
        self.n += 1

    def insertPos(self, pos, val):
        newnode = Node(val)
        curr = self.head
        while curr!= None:
            if (curr.data == pos):
                break
            curr = curr.next
        if curr == None:
            print("Item not found")
        else:
            newnode.next = curr.next
            curr.next = newnode
            self.n += 1

    def clear(self):
        self.head = None
        self.n = 0
    
    def del_head(self):
        if self.head != None:
            self.head = self.head.next
            self.n -= 1
        else:
            print("Empty Linked List")

    def del_tail(self):
        if self.head.next == None:
            self.head = None
            self.n -= 1
            return
        if self.head != None:
            curr = self.head
            while (curr.next.next!=None):
                curr = curr.next
            curr.next = None
            self.n -= 1
        else:
            print("Empty Linked List")
    
    def del_val(self, val):
        curr = self.head
        while curr.next != None:
            if curr.next.data == val:
                break
            curr = curr.next
        if curr.next == None:
            print("Item not found")
        else:
            curr.next = curr.next.next
        self.n -= 1

    def search(self, data):
        curr = self.head
        pos = 0
        if self.head == None:
            print("empty ll")
        
        while curr.next != None:
            if curr.data == data:
                return pos
            curr = curr.next
            pos += 1
        return "ValueError: Element not found"
    
    def idx(self, index):
        pos = 0
        curr = self.head
        if pos<n:
            while(pos!=index):
                curr = curr.next
                pos += 1
            return curr.data
        else:
            return "IndexError: Index out of bound"

    def __str__(self):
        curr = self.head
        res = ''
        while curr != None:
            res = res + str(curr.data) + '->'
            curr = curr.next
        self.n += 1     
        return res[:-2]
    

L = LinkedList()
L.insertHead(1)
L.insertHead(2)
L.insertHead(3)
L.insertHead(4)
L.insertTail(0)
L.insertPos(2, 20)
L.insertPos(28, 20)
print(L)
L.del_head()
print(L)
L.del_tail()
L.del_val(20)
print(L.search(20))
print(L)



        