
class MATH:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):

        print('the sumation is:',self.a+self.b)
    def mul(self):
        print('the sumation is:',self.a*self.b)
    def sub(self):
        print('the sumation is:',self.a-self.b) 
    def div(self):
        print('the sumation is:',self.a/self.b)

obj=MATH(100,200)
obj.add()
obj.mul()   
obj.sub()
obj.div()
