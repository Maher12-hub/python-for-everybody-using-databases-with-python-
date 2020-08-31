class partyanimal:
    x=0
    def __init__(self,z):
        self.name=z
        print(self.name,'constructed')
    def party(self):
        self.x=self.x+1
        print(self.name,'party count',self.x)
name1=partyanimal('maher')
name1.party()
name2=partyanimal('sunny')
name2.party()
name1.party()