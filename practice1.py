class Card:
    def __init__ (self, value,suite):
        self.value = value
        self.suite = suite
    
card_1  = Card(3, "co")
card_2 = Card(2, "bich")
print(f'Quan bai thu nhat: {card_1.value}-{card_1.suite}')
print(f'Quan bai thu nhat: {card_2.value}-{card_2.suite}')

class Student:
    def __init__ (self, ID, Name, Python, English, Def):
        self.ID = ID
        self.Name = Name
        self.Python = Python
        self.English = English
        self.Def = Def
student_1 = Student(888, "Trinh A", 7, 7, 6)
student_2 = Student(999, "Trinh B", 9, 8, 10)
print(f'ID Sinh vien: {student_1.ID}')
print(f'Name sinh vien: {student_1.Name}')
print(f'Diem Python: {student_1.Python}')
print(f'Diem english : {student_1.English}')
print(f'Def sinh vien: {student_1.Def}')
print(f'ID Sinh vien: {student_2.ID}')
print(f'Name sinh vien: {student_2.Name}')
print(f'Diem Python: {student_2.Python}')
print(f'Diem english : {student_2.English}')
print(f'Def sinh vien: {student_2.Def}')