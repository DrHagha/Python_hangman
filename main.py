from HangMan import HangMan
from Rank import Rank
from User import User


if __name__ == "__main__":
    ranking_path ="./Rank.txt"
    rank = Rank(ranking_path)
    
    user = User()
    user.setName(input("input user name : "))
    
    game = HangMan(user)
    game.execute()
    game.gameOver()
    
    user.view()

'''
    rank.addUser(user)
    rank.sort()
    
    rank.view()
'''
