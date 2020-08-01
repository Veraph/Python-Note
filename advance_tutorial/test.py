class Student():

    #当使用self.birth时报错的原因是跟方法的名字一样了
    def __init__(self, birth):
        self._birth = birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value


sarah = Student(1000)