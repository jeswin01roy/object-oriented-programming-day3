class queue:
    def __init__(self):
        print("queue is empty!")
        self.que=[]
    
    def enque(self,e):
        self.e=e
        self.que.append(self.e)
        print("the queue is :",self.que)

    def deque(self):
        while(self.que!=[]):
            self.d=self.que.pop(0)
            print("the poped element is :",self.d)
            if (self.que==[]):
                print("the que after poping all elements:",self.que)

        
q=queue()
while(True):
    a= int(input("enter the element of the queue:"))
    q.enque(a)
    n= input("enter stop if the element is over else enter 'c' ")
    if(n=="stop"):
        break
    else:
        pass

q.deque()

