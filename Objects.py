class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, GPA: {self.gpa}'


def main():
    alice = Student('Alice', 'aa1234aa', 3.4)
    bob = Student('Bob', 'bb1234bb', 3.2)
    
    print(alice.name)
    print(bob.college_id)
    alice.gpa = 4.0

    print(alice)
    print(bob)

main()