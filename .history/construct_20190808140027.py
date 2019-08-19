class Emp:
    
    def __init__(self, firstName, lasstName, uid):
        self.first_Name = firstName
        self.last_Name = lasstName
        self.UID = uid
    def showEmp(self):
        print(self.first_Name,' \n' , self.last_Name,self.UID)

def main():
    emp1 = Emp('dav','aa','123')
    emp1.showEmp()


main()