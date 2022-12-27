from ex1 import Human

class Student(Human):
    def __init__(
            self, name, age, food, hunger, weight, height, 
            is_fluffy, gender, intelligence, discipline, count_passed_homeworks):
        super().__init__(name, age, food, hunger, weight, height, is_fluffy, gender, intelligence)
        self.discipline = discipline
        self.count_passed_homeworks = count_passed_homeworks

    def __lt__(self, other):
        return self.count_passed_homeworks < other.count_passed_homeworks

    def __le__(self, other):
        return self.count_passed_homeworks <= other.count_passed_homeworks
    
    def __eq__(self, other):
        return self.count_passed_homeworks == other.count_passed_homeworks
    
    def __ne__(self, other):
        return self.count_passed_homeworks != other.count_passed_homeworks
    
    def __gt__(self, other):
        return (self.count_passed_homeworks > other.count_passed_homeworks)
    
    def __ge__(self, other):
        return self.count_passed_homeworks >= other.count_passed_homeworks

stud1 = Student("Petya", 20, "Makarony", 5, 70, 170, False, "Male", 180, "Math", 7)
stud2 = Student("Masha", 21, "Kartoshka", 5, 75, 175, False, "Female", 170, "math", 9)


print(f'Count passed homeworks Petya > Masha count passed homeworks: {stud1>stud2}')
print(f'Count passed homeworks Petya < Masha count passed homeworks: {stud1<stud2}')
print(f'Count passed homeworks Petya == Masha count passed homeworks: {stud1==stud2}')
print(f'Count passed homeworks Petya != Masha count passed homeworks: {stud1!=stud2}')
print(f'Count passed homeworks Petya >= Masha count passed homeworks: {stud1>=stud2}')
print(f'Count passed homeworks Petya <= Masha count passed homeworks: {stud1<=stud2}')

stud2.count_passed_homeworks = 7
print(f"Make Masha's homeworks = 7, Tests:")

print(f'Count passed homeworks Petya == Masha count passed homeworks: {stud1==stud2}')
print(f'Count passed homeworks Petya != Masha count passed homeworks: {stud1!=stud2}')
print(f'Count passed homeworks Petya >= Masha count passed homeworks: {stud1>=stud2}')
print(f'Count passed homeworks Petya <= Masha count passed homeworks: {stud1<=stud2}')
