# Next, you can upgrade your Student Marks Analyzer with small improvements:
# Let the user enter student names and marks instead of hardcoding.
# Store data in a file (marks.txt) and read it back.
# Print a ranking list (all students sorted by average).
# Would you like me to guide you through Step 1: taking input from the user for this project

num_students = int(input("Enter no of students:"))
students = {}
for i in range (num_students):
    name = input(f"Enter name of student {i+1}:")
    marks = []
    for j in range(3): ## subjects marks
        mark = int(input(f"Enter mark {j+1} for {name}:"))
        marks.append(mark)
    students[name] = marks

topper=None
highest_avg=0
for name,marks in students.items():
    avg = sum(marks)/len(marks)
    if avg > highest_avg:
        highest_avg = avg
        topper = name
print("Topper",topper,"with score",highest_avg)
#
# Ranking List (sort all students by average)
# Instead of only showing the topper, we’ll print all students sorted by their average marks.

average=[]
for name,marks in students.items():
    avg=sum(marks)/len(marks)
    average.append((name,avg))
average.sort(key=lambda x:x[1],reverse=True)

# print ranking
print("\n--- Ranking List ---")

for rank,(name,avg) in enumerate(average,start=1):
    print(f"{rank}. {name}-{round(avg,2)}")

topper = average[0]
print(f"\nTopper: {topper[0]} with average {round(topper[1], 2)}")