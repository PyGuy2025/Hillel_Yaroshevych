class GroupFullError(Exception):
    pass

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