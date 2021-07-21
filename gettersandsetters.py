


class user:
    def __init__(self,username,email):
        self.username= username
        self.email = email

    def getUsername(self):
        return self.username
    def setUsername(self,username):
        self.__username = username

class student(user):
    pass

newuSER = student("derrick","derrickragui@gamil.com")
newuSER.__username="chloe"

print(newuSER.getUsername())