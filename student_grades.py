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

def find(self, bodiky):
    cojee = []
    for i in range(len(self.scores)):
        if self.scores[i] == bodiky:
            cojee.append(i)
    return cojee

def get_sorted(self):
    kolik1 = self.scores.copy()
    for i in range(len(kolik1)):
        for y in range(0, len(kolik1) - i - 1):
            if kolik1[y] > kolik1[y + 1]:
                kolik1[y], kolik1[y + 1] = kolik1[y + 1], kolik1[y]
    return kolik1



def main():
    vysledky = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(f"Test psalo celkem {vysledky.count()} studentů.")
    print("-" * 30)
    for i in range(len(vysledky.scores)):
        score = vysledky.scores[i]
        grade = vysledky.get_grade(score)
        print(f"Student {i}: {score} points – {grade}")
        print("-" * 30)
    top_students = vysledky.find(100)
    print(f"Indexy studentů s plným počtem bodů: {top_students}")
    print(f"Seřazené výsledky: {vysledky.get_sorted()}")
    print("Generuji 30 náhodných výsledků...")
    random_datiky = random_numbers(30, 0, 100)
    random_vyslediky = StudentsGrades(random_datiky)

    print(f"Počet náhodných studentů: {random_vyslediky.count()}")
    print(f"Seřazené náhodné výsledky: {random_vyslediky.get_sorted()}")

if __name__ == "__main__":
        main()