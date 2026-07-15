class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def reset(self):
        # self.x=0
        # self.y=0
        self.move(0,0)
        # print(f"points= {self.x,self.y}" )
    
    def move(self,x,y):
        self.x =x
        self.y =y
        print(f"new points= {self.x,self.y}" )
    
    def xmove(self,a):
        self.x=a
        print(f"new points= {self.x,self.y}" )

    def ymove(self,b):
        self.y=b
        print(f"new points= {self.x,self.y}" )


c=point()

a= int(input("enter the x value:"))
b= int(input("enter the y value:"))
c.move(a,b)
print("point after reset")
c.reset()
print("only move the x value:")
c.xmove(a)
c.reset()
print("only move the y value:")
c.ymove(b)

        
