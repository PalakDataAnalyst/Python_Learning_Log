DAY 24 - Dictionary basics.py

students = {101 : "Vijay Mehra", 102 : 'Mahima Gupta', 103 : "Pankaj Mishra"}
print(type(students))
print(id(students))
print(students)
print(students[102])
students[104] = 'Rajeev Mehra'
print(id(students))
print(students)
students[101] = 'Vinay Pathak'
print(id(students))
print(students)
print("Looping through in Dictionary")
for roll_number in students:
    print(roll_number, "-", students[roll_number]) 
del students[103]
print(students)
print(102 in students)
print(102 not in students)
print(103 in students)
print(103 not in students)

 -- Dictionary Keyboard Input.py
students = {}

while True:
    roll_number = int(input("Enter roll number: "))
    
    if roll_number not in students:
        name = input("Enter name: ")
        students[roll_number] = name
        print("Student details are added successfully")
    else:
        print("Student details are already added")
        choice = input("Do you want to update student details?[yes/no]: ")
        if choice.lower() == 'yes':
            name = input("Enter new name to update: ")
            students[roll_number] = name
            print("Student details are updated successfully")
    
    choice = input("Do you want to add another student details?[yes/no]: ")
    if choice.lower() == 'no':
        break
    
print("Details of all students are")
for roll_number in students:
    print(roll_number, "-", students[roll_number])
        
    -- Dictionary method.py
employees = {'Emp101' : "Vijay Sahu", 'Emp102' : "Manik Mehta", 'Emp103' : "Roshini Mishra"}
print(employees.keys())
print(employees.values())
print(employees.items())
print(employees)
employees.update({'Emp101' : "Vijay Verma", 'Emp104' : "Mahima Gupta"})
print(employees)
employees.pop('Emp102')
print(employees)
print(employees.get('Emp102'))
print(employees.get('Emp103'))

-- Storing multiple values against key.py
student = {'Roll Number' : 101, 'Name' : "Manoj Pandey", 
"Contacts" : ['+91-9811234522', 'manoj@gmail.com'], 
'Addresses' : {'Current' : 'Greater Noida', 'Parmanant' : 'Kanpur'}}
print(student)
print(student['Roll Number'])
print(student['Name'])
print(student['Contacts'])
print(student['Addresses'])
print(student['Contacts'][0])
print(student['Contacts'][1])
print(student['Addresses']['Current'])
print(student['Addresses']['Parmanant'])

       
