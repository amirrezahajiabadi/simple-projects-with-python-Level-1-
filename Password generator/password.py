from abc import ABC,abstractmethod
import string
import random


class PasswordGeneratorAbstract(ABC):

    @abstractmethod
    def generate_password(self , length=8):
        pass


class numbricpasswordgenetartor(PasswordGeneratorAbstract):

    letters = string.digits

    def generate_password(self, length=8):
        return"".join(str(random.choice(self.letters))for _ in range(length))
    

class LetterPasswordGenerator(PasswordGeneratorAbstract):

    letters = string.ascii_letters




    def generate_password(self, length=8):

        return "".join(str(random.choice(self.letters)) for _ in range(length))



class MixedPasswordGenerator(PasswordGeneratorAbstract):

    letters = string.ascii_letters + string.digits




    def generate_password(self, length=8):

        return "".join(str(random.choice(self.letters)) for _ in range(length))
    


my_password = MixedPasswordGenerator()
print(my_password.generate_password(10))