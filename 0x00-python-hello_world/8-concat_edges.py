#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str + str[39:67] + str[107:111] + str[6] + str[:6]
str = str[129:]
print(str)
