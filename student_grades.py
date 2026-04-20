from sorting import random_numbers
# tridy
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter


rectangles = [
    Rectangle(3, 5),
    Rectangle(10, 20),
    Rectangle(1, 1),
    Rectangle(7, 2),
    Rectangle(4, 8),
]

for rect in rectangles:
    print(rect.area())



class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

#print(results.scores)
#print(results.get_by_index(5))
#print(results.count())
def get_grade(self, indexik):
    score = self.scores[indexik]  # nebo self.get_by_index(index)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"
results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
def main():
    kolik=count(results) #kolik=len(results)
    for index in range(1, kolik):
        print(f"Student {index}: {results[index]} points - {results.get_grade(index)}")

    studenti100=[]
    for i, bodiky in enumerate(results, 1):
        if bodiky==100:
            studenti100.append(i)

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())