import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)  # 10 čísel v rozsahu 0–100
#print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort(values):
    values=values[:]
    for min_index in range(len(values)):
        print(values)
        min_value=values[min_index]
        min_ind=min_index
        for i in range(min_index, len(values)):
            if values[i] < min_value: #nejhorsi v algoritmu
                min_index=i
                min_value=values[i]
        values[min_ind], values[min_index]= values[min_index], values[min_ind]
    print(values)

def bubble_sort(values):
    print(values)
    plt.ion()
    plt.show()
    for index in range(len(values)):
        for y in range(0, len(values)-index - 1):
            index_highlight1 = y
            index_highlight2 = y + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if values[y]> values[y+1]:
                values[y], values[y+1]=values[y+1], values[y]
    plt.ioff()
    plt.show()
    return values

def main():
    return
if __name__ == "__main__":
    values = random_numbers(50)
    cislicka1=bubble_sort(values)
    print(cislicka1)