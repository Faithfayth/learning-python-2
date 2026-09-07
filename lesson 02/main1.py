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
    
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else: 
    grade = "F"
    
 #the match statement to compare the grade   
match grade:
    case "A":
       print("Excellent!")
    case "B":
        print("Very good!")
    case "C":
        print("Good work!")
    case "D":
        print("You passed, but you can improve.")
    case "F":
        print("You need to work harder.")
    case _:
        print("Not applicable input!")
        
        
#Use of a tupple, because this is fixed information (collection which is ordered and unchangeable. Allows duplicate members)
grade_boundaries = (80, 70, 60, 50)

#Use of a set, (collection which is unordered, unchangeable*, and unindexed. No duplicate members)
subject_categories = {"Programming", "Science", "English"}