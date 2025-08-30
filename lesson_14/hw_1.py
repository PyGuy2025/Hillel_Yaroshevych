class GroupFullError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.gender}, {self.age}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}"

class Group:

    def __init__(self, number, capacity=10):
        self.number = number
        self.capacity = capacity
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.capacity:
            raise GroupFullError("Group is full")
        self.group.add(student)


    def delete_student(self, last_name):
        st = self.find_student(last_name)
        if st is not None:
            self.group.discard(st)

    def find_student(self, last_name):
        for st in self.group:
            if last_name == st.last_name:
                return st
        return None

    def __str__(self):
        all_students = "\n".join(map(str, self.group))
        return f'Group number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
gr.delete_student('Taylor')
print(gr)