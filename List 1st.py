students_marks = []

print("\n\nProgram Written & Performed by SAI&D75 Vivek Harwani")

total_students = int(input("\n\nEnter Total no. of students for 'Fundamentals of Data Structure': "))

for i in range(0, total_students):
    each_mark = int(input(f"Enter Marks obtained by Students (-1 if Absent): "))
    students_marks.append(each_mark)

def average_score():
    sum = 0
    for i in students_marks:
        if i>0:
            sum += i
    avg = sum/total_students
    print("\nAverage marks obtained by students are: ", avg)

def high_low():
    highest = students_marks[0]
    lowest = students_marks[0]

    for i in students_marks:
        if i>highest:
            highest = i
        elif i<lowest and i>=0:
            lowest = i

    print("\nHighest Obtained Marks are: ", highest)
    print("Lowest Obtained Marks are: ", lowest)

def absent_students():
    count = 0
    for i in students_marks:
        if i<0:
            count += 1
    print("\nTotal students absent for the test: ", count)

def highest_frequency():
    marks = []
    freqs = []

    for i in students_marks:
        if i in marks or i<0:
            continue

        marks.append(i)
        count = 0

        for j in students_marks:
            if j == i:
                count += 1

        freqs.append(count)

    highest_freq = freqs[0]
    index_of_highest_freq = 0

    for i in range(1, len(freqs)):
        if freqs[i] > highest_freq:
            highest_freq = freqs[i]
            index_of_highest_freq = i
            
    print(f"\n{marks[index_of_highest_freq]} is the highest frequency no. and its frequency is: ", highest_freq, "\n")


average_score()
high_low()
absent_students()
highest_frequency()