# Character = string 
# Numeric = integer 

# CadburyBox Math

# CadburyBox = 5
# CadburyBox = CadburyBox + 5

# sum(CadburyBox + 5)

CadburyBox1 = "Milk Chocolate"
#  ||             ||
# name        value=numeric or character
# change name will change all rather than all need individual change 
CadburyBox2 = "Dark Chocolate"
CadburyBox3 = "White Chocolate"

Cadburymilk = 5
Cadburydark = 3
Cadburywhite = 8

# dict = the combining of the two variable 
# {} use to define the pair data \
# also called as key pair
Chocolate1 = {"Cadburymilk":5} # (milk,5)
Chocolate2 = {"Cadburydark":8} # (dark,8)
Chocolate3 = {"Cadburywhite":3} # (white,3)

print(Chocolate1, Chocolate2, Chocolate3)
Chocolate = {"Cadburymilk":5,"Cadburydark":8,"Cadburywhite":3}
print(Chocolate)
chocolatedata = [Chocolate] #convert dict to list
print(chocolatedata)

chocolatedf = pandas.DataFrame(chocolatedata, index=["quality"]) # convert to column 
print(chocolatedf)

# practice
Steve = 32
Lia = 28
Vin = 45
Katie = 38

student1 = {"Steve":32}
student2 = {"Lia":28}
student3 = {"Vin":45}
student4 = {"Katie":38}

print(student1, student2, student3, student4)
Student = {"Steve":32,"Lia":28,"Vin":45,"Katie":38}
print(Student)
studentgender= {"Steve":"male","Vin":"male","Lia":"female","Katie":"female"}

# pandas = python analysis of data by Wes Mckinney 

import pandas
dir(pandas)

studentinfocol = pandas.Series(Student)
print(studentinfocol)
studentdata  = [Student]
studentdf = pandas.DataFrame(studentdata, index=["age"])
print(studentdata)

#test code
studentlist = [["Steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["Katie",38,"female"]]
studentlistdf = pandas.DataFrame(studentlist,columns=["name","age","gender"],index=["1","2","3","4"])
print(studentlistdf)

students = {"Steve":32,"Lia":28,"Vin":45,"Katie":38}
studentdata2 = [students]
print(studentdata2)

studentsdf = pandas.DataFrame(studentdata,index=["age"])
print(studentsdf)

# pandas practice
chocolatecol = pandas.Series(Chocolate)
print(Chocolate)

studentgendercol = pandas.Series(studentgender)
print(studentgender)
studentgenderdata = [studentgender]
studentgenderdf = pandas.DataFrame(studentgenderdata, index=["quality"])
print(studentgenderdf)

print(Student)
print(studentgender)

studentdf1 = [Student,studentgender]
print(studentdf1)

studentdf2 = pandas.DataFrame(studentdf1,index=["Age","Gender"])
print(studentdf2)





















