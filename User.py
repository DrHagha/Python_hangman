class User():
    def __init__(self):
        self.name = ""
        self.score = 0
    
    def getName(self):
        return self.name
    
    
    def setName(self, new_name : str):
        self.name = new_name
    
    
    def inputName(self):
        try:
            self.name = input("input user name(only string) : ")
            if any(char.isdigit() for char in self.name):
                raise Exception('정상적인 이름이 아닙니다')
        except Exception as e:
            print("예외가 발생했습니다 : ", e, "\n\n")
            self.setName()
    
    def getScore(self):
        return int(self.score)
    
    def setScore(self, new_score : int):
        self.score = new_score
    
    def view(self):
        print("name : ", self.name)
        print("score : ", self.score)