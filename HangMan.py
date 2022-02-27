import random
from GameImpl import GameImpl
from User import User


class HangMan(GameImpl):
    
    def __init__(self, user : User):
        self.user = user
        self.word = self.pickOneWord("Months.txt")
        self.monitor = [False for i in range (len(self.word))]
        self.count = 0
        
    def pickOneWord(self, file_name : str):
        self.words = []
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                self.words.append(line)
        return random.choice(self.words)

     
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
        self.user.setScore(10000-self.count)
    
    
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
    