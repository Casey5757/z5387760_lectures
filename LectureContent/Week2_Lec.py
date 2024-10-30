tic = "qan.ax"
print(tic)

# Exercise 1
str_1 = '''John said: "Let's learn Python together." '''
print(str_1)

#Exercise 2
length = 56
width = 33
height = 30.5
volume = length * width * height
print(volume)
print("The volume is " + str(volume) + "cm^3")

#Exercise 3
line = "From firstname.surname@unsw.edu.au Wed Sep 09:18:13"
words = line.split()
email = words[1]
domain = email.split("@")[1]
print("The domain name is :", domain)

a = 5*2
b = 5**2
print(a,b)
print(a)
print(b)

f = 0.2+0.2+0.2
print(f)
print(f == 0.6) # false

i = 1
test = i == 1
print(test) # true

import math
f = 0.2+0.2+0.2
print(math.isclose(f,0.6)) # true

