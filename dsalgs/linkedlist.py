class Node:
    '''
    A node in a LinkedList
    '''

    def __init__(self,x):
        self.x=x
        self.next=None

    def __str__(self):
        return str(self.x)+' -> '

    def verbosestr(self):
        node='+-----+\n'
        node+='|  '+str(self.x)+'  |\n'
        node+='+-----+\n'
        node+='   |\n   |\n   V\n'

        return node

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.head:
            return  'EMPTY LINKED LIST'
        if self.get_size()<10:
            ll=''
            node=self.head
            while node:
                ll+=str(node)
                node=node.next
        return ll

    def search_and_insert(self,x,i):
        '''
        Insert value x at position i
        '''
        
        if i > self.get_size():
            print('ERROR: position %d is longer then list length %d' % (i, self.get_size()))
        if i==self.get_size():
            self.append(x)
        elif i==0:
            self.prepend(x)
        else:
            pos=0
            node=self.head
            while pos<i-1:
                pos+=1
                node=node.next
            self.insert(x,node)

    def insert_after(self,x,node):
        '''
        Insert after given node
        '''
        newnode=Node(x)
        newnode.next=node.next
        node.next=newnode

    def prepend(self,x):
        '''
        AKA "prepend"
        '''
        newhead=Node(x)
        newhead.next=self.head
        self.head=newhead

    def append(self,x):
        if self.head==None:
            self.head=Node(x)
            return
        node=self.head
        while node.next:
            node=node.next
        newnode=Node(x)
        node.next=newnode
        return

    def delete(self,x):
        '''
        Deletes first occurence of x
        '''

        if self.head.x==x:
            self.head=self.head.next
            return
        
        node=self.head
        while node.next.x != x:
            node=node.next
        node.next=node.next.next

    def search(self,x):
        '''
        Linear search algorithm to find first instance of x.
        Returns the node. Returns None if element not in list.
        '''
        
        if self.head.x==x:
            return self.head

        node=self.head.next
        while node and node.x != x:
            node=node.next

        return node
            

    def get_keys(self):
        '''
        In a linked list, number of keys is the size
        '''
        return self.get_size()
        
    def get_size(self):
        '''
        Traversal to get size?
        '''
        size=0
        
        if self.head:
            size+=1
            node=self.head
            while node.next:
                size+=1
                node=node.next
        return size

    def _set_insert(self,ins_type):
        '''
        Choose the implication of LinkedList.insert

        Arugments:
            ins_type:   'prepend', 'append'
        '''

        if ins_type=='prepend':
            self.insert=self.prepend
        if ins_type=='append':
            self.insert=self.append
