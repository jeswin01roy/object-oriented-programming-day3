#encapsulasion
#access modifiers
#public
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def sum(self):
        return self.m1 + self.m2
    
s1=student(6,7)
print(s1.sum())

#protected
class calculator:
    def __init__(self,n1,n2):
        self._n1 = n1 #protected asssigned by _
        self._n2 = n2
    
    def add(self):
        return self.n1 + self.n2
    
class sum:
    def __init__(self):
        pass
    def add(self):
        return
    
s1=student(6,7)
print(s1.sum())




    

        