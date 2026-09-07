#--------------STUDENT GRADE MANAGER--------------
name = input("Enter your name: ")
age = int(input("Enter yoyr age: "))

print("\n ---------Student information ----------")
print("Name: ", name)
print("Age: ", age)

subjects = ["Math", "Python", "English", "Science"]

print("\n Subjects: ")
for subject in subjects:
    print(subject)
else: print("\n")
    
marks = {
    "Math": 50,
    "Python": 70,
    "English": 40,
    "Science": 58,
}

for subject, mark in marks.items():
    print( subject, ":", mark)

total = sum(marks.values())
average = total /  len(marks)
print("\nAverage: ", average)

if average >= 50:
    passed = True
    print("Status: PASSED")
else:
    passed = False
    print("Status: FAILED")