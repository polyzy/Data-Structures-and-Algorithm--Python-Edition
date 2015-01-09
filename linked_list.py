# -*- coding: cp936 -*-
class Node(object):
    def __init__(self, val, p=0):   #定义一个节点，val代表节点的数值，next代表指向下一个节点的指针
        self.data = val
        self.next = p   # p只是起一个初始化的作用，不起任何作用。

class LinkList(object):
    def __init__(self):
        self.head = 0

    #def __getitem__(self, key):

     #   if self.is_empty():
    #        print "linklist is empty"
    #        return
     #   elif key



    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head           #是一个Node类对象？

        for i in data[1:]:
            node = Node(i)
            p.next = node   #赋值   p有p.data和p.next两种属性
            p = p.next      #指针指向下一位

    def getlength(self):
        p = self.head
        length = 0
        while p!=0:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0

    def append(self, item):
        q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q

    def getitem(self,index):
        j = 0
        p = self.head

        while p.next != 0 and j < index:
            p = p.next
            j += 1
        if j == index:
            return p.data
        else:
            print 'not exist'

    def insert(self,index,item):
        if index == 0:
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j+=1

        if index == j:
            q = Node(item,p)
            post.next = q
            q.next = p          #在post和p之间插入index的值


    def delete(self,index):
        if index ==0:
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j += 1

        if index == j:
            post.next = p.next

    def index(self,value):
        p = self.head
        i = 0

        while p.next != 0 and not p.data == value:
            p = p.next
            i += 1

        if p.data == value:
            return i
        else:
            return -1
            

    
