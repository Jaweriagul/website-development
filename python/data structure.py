classroom=["Jaweria","Fatima","Adeen","Armeen","Khadija","hania","Minhal","Ayesha","Wania"]
print("Class list:",classroom)
print("strength:",len(classroom))
print("First student:",classroom[0])
print("last student:",classroom[-1])
print("second student:",classroom[1])
print("students from 3 to 8:",classroom[2:8])

classroom.append("Huda")
print("after adding huda:",classroom)
classroom.pop(5)
print("after removing hania:",classroom)
classroom.sort()
print("sorting in alphabetical order:",classroom)
classroom.reverse()
print("sorting in reverse order:",classroom)
classroom.clear()
print("after clearing everything:",classroom)

teacher={"name":"miss ayesha","subject":"chemistry","experience":"3 years"}
print("teacher profile:",teacher)
print("name:",teacher["name"])
print("subject:",teacher["subject"])
print("experience:",teacher.get("experience","not found"))
teacher["experience"]="6"
teacher["email"]="ayesha@gmail.com"
teacher.pop("experience")
print("updated teacher profile:",teacher)

students=["jojo","adam","emma","ali"]
roll_no=[1,2,3,4]
student_dictionary=dict(zip(roll_no,students))
print("student dictionary:",student_dictionary)
print("student at roll no 3:",student_dictionary[3])