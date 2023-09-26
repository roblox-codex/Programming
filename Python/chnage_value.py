myDict = {'student1': {'name': 'Aniket', 'age': 22},
          'student2': {'name': 'Shiv', 'age': 25},
          'student3': {'name': 'Aviral', 'age': 23}
          }

print("The dictionary before changing:", myDict)

student_key = input("Enter the student key: ")
value_key = input("Enter the value key: ")
new_value = input("Enter the new value: ")

myDict[student_key][value_key] = new_value

print("The dictionary after changing:", myDict)
