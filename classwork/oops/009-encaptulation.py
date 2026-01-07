
class Student : 

    __name = "abc"

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name


s = Student()
s.set_name("dev")
print(s.get_name())

print(s._Student__name)
