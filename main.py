'''
Instance methods 
'''
class Student:
    def __init__(self, scores = []):
        self.scores = scores
    
    def avg(self):
        return round(sum(self.scores) / len(self.scores))

# object / instance
kings  = Student(scores = [2,3,5,3,5,35])
peter  = Student(scores = [27,30,5,3,5,35])

print(kings.avg())
print(peter.avg())

'''
Static method
'''

class Student:
    def __init__(self, scores = []):
        self.scores = scores
    
    def avg(self):
        return round(sum(self.scores) / len(self.scores))

    @staticmethod
    def notice():
        return "Exams next week!"

print(Student.notice())

'''
Class Methods 
'''
class Student:
    gender = 'Female'

    def __init__(self, scores = []):
        self.scores = scores
    
    def avg(self):
        return round(sum(self.scores) / len(self.scores))

    @staticmethod
    def notice():
        return "Exams next week!"
    
    @classmethod
    def what_is_gender(cls):
        return f"I am {cls.gender}"

print(Student.what_is_gender())
print(Student.gender)