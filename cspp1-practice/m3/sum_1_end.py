'''
@author : Rohithmarktricks
This program prints the sum of n variable from 1
'''
SUM_ = 0
END = int(input("Enter the end variable :"))
i = 1
while i <= END:
    SUM_ += i
    i += 1
print(SUM_)
#Using For loop:
END = int(input("Enter the end integer value :"))
SUM_ = 0
for i in range(1, END+1, 1):
    SUM_ += i
print(SUM_)
