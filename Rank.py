from click import open_file
import datetime
from User import User


class Rank():
    def __init__(self, rank_path : str):
        self.rank_path = rank_path
    
    def addUser(self, newUser : User):
        now = datetime.datetime.now()
        now_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        with open_file(self.rank_path, 'a') as f:
            data = "{0} {1} {2}\n".format(newUser.getName(), newUser.getScore(), now_datetime)
            f.write(data)
            f.close()

    
    def view(self):
        print("---Rank Board---")
        user_list = []
        with open_file(self.rank_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                user = User()
                user.setName(line.split(' ')[0])
                user.setScore(int(line.split(' ')[1]))
                user_list.append(user)
            new_user_list = sorted(user_list, key = lambda x:x.getScore(), reverse=True)
            f.close()
    
        for user in new_user_list:
            print(user.getName(), user.getScore())
                