import math
#calculate test scores


test1=input ("enter first test score")
test2=input("enter second test score")
test3=input("enter third test score")
test4=input("enter fourth test score")
test5=input("enter fifth test score")
test6=input("enter sixth test score")
test7=input("enter seventh test score")
test8=input("enter eigth test score")
test9=input("enter ninth test score")
test10=input("enter tenth test score")
num5=input("enter maximum amount of points")
grade="F"
num3= int(test1) + int(test2) + int(test2) + int(test3) + int(test4) + int(test5) + int(test6) + int(test7) + int(test8) + int(test9) + int(test10)
num4= int(num3) / int(num5)

if num4 >= .90:
    grade="A" 

elif num4 >= .80:
    grade="B"

elif num4 >= .70:
    grade="C"
 
elif num4 >= .60:
    grade="D"

else:
    grade="F"

print (num4,grade)

