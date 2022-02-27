from GameImpl import GameImpl
from User import User


class HangMan(GameImpl):
    
    def __init__(self, user : User):
        self.user = user
        self.word = "velog"
        self.monitor = [False for i in range (len(self.word))]
        self.count = 0

     
    def getUserName(self):
        return self.user.getUserName()
    
    def execute(self):
        while self.isEnd() == False:
            self.printMonitor()
            print()
            self.inputSpelling()
            

    def gameOver(self):
        print("단어가 완성되었습니다.")
        print("---", self.word ,"---")
        self.user
    
    
    def isEnd(self):
        if all(self.monitor):
            return True
        else:
            return False
        
    
    def printMonitor(self):
        for index in range(len(self.monitor)):
            if self.monitor[index] == True:
                print(self.word[index], end = '  ')
            else:
                print('_', end = '  ')
                
    
    def inputSpelling(self):
        spelling = input("input the alphabet : ")
        is_there = False
        for index in range(len(self.word)):
            if spelling[0] == self.word[index]:
                self.monitor[index] = True;
                is_there = True
        
        if is_there:
            print("존재합니다\n\n")
        else:
            print("존재하지 않습니다\n\n")
            self.count += 1
    