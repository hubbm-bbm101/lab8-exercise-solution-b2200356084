import sys

file = open(sys.argv[1], "r", encoding="utf-8")
content = file.read().split("\n")
mainDict = {}
for i in content:
    person, school = i.split(":")
    mainDict[person] = str(school)
for student in sys.argv[2].split(","):
    try:
     print("Name:{} , University: {} ".format(student,mainDict[student]))
    except:
     print("No record of {} was found!".format(student))

