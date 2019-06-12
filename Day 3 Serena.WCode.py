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
# {} use to define the pair data 
Chocolate1 = {"Cadburymilk":5} # (milk,5)
Chocolate2 = {"Cadburydark":8} # (dark,8)
Chocolate3 = {"Cadburywhite":3} # (white,3)

print(Chocolate1, Chocolate2, Chocolate3)
Chocolate = {"Cadburymilk":5,"Cadburydark":8,"Cadburywhite":3}
print(Chocolate)

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

# pandas practice
chocolatecol = pandas.Series(Chocolate)
print(Chocolate)
studentgendercol = pandas.Series(studentgender)
print(studentgender)

























