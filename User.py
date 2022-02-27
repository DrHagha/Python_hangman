class User():
    def __init__(self):
        self.name = ""
        self.score = 0
    
    def getName(self):
        return self.name
    
    def setName(self, new_name):
        self.name = new_name
    
    def getScore(self):
        return self.score
    
    def setScore(self, new_score : int):
        self.score = new_score
    
    def view(self):
        print("name : ", self.name)
        print("score : ", self.score)