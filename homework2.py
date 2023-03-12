studentList = ["Hakkı Burak","Ahmet Kazan","Salih Doğru","Uğur Kalan"]

print(studentList)

def addStudent(*nameSurname):
    studentList.extend(nameSurname)




def deleteStudent(nameSurname):
    studentList.remove(nameSurname)



def showStudent():
  
    for i in range(len(studentList)):
        print(studentList[i])
        i += 1





def numberOfStudent():
    i = 0
    while i < len(studentList):
        print(str(i+1) +" Nolu Öğrenci "+studentList[i])
        i +=1






addStudent("Yavuz Çağrı") 
print(studentList)   
addStudent("Harun Yıld","Ömer Faruk","Sedat Diz") 
print(studentList)   
deleteStudent("Ahmet Kazan")
print(studentList)
showStudent()
print("****************************")
numberOfStudent()
print(studentList)




