"""
#students = ["hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindoe","Gryffindoe","Gryffindoe","Slytherin"]
"""
# THE ABOVE DATA CAN BE REPRESENTED AS A DICTIONARIES AS FOLLOWS 
students = {
    "Harry" : "Gryffindor",
    "Hermione" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}
Mstudents ={
    "Harry" : "Gryffindor",
    "Hermione" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}



"""
print(students[0])
print(students[1])
print(students[2])

#####""
#same thing using loops
for _ in students:
    print(_)
#_ can be any variable 
# len function is used to find the lenght of the string
# and range uses integer inputs for iterating no of truns
for i in range(len(students)):
    print(students[i], houses[i],sep = "   lives at   " , end = "\n") 
#dictionaries
"""
for student in students:
    print(student , students[student]);  

