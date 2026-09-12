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
if __name__=="__main__":
    MATH(10,20).add()
    MATH(20,30).mul()
    MATH(30,40).sub()
    MATH(30,20).div()