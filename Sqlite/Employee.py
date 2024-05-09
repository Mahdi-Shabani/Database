class Employee:


    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    
    @property
    def email(self):
        return'{}.{}@gmail.com'.format(self.fname,self.lname)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    
    def __repr__(self):
        return 'Employee({},{},{})'.format(self.fname,self.lname,self.pay)
    
    