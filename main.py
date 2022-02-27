from HangMan import HangMan
from Rank import Rank
from User import User


if __name__ == "__main__":
    ranking_path ="./Rank.txt"
    rank = Rank(ranking_path)
    
    user = User()
    user.inputName()
    
    game = HangMan(user)
    game.execute()
    game.gameOver()
    print()
    
    user.view()
    print()
    print()
    print()
    rank.addUser(user)
    rank.view()
    
