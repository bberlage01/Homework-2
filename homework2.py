#Bethany Berlage Homework 2
#Problem 1
def print_name(name):
    print("The name is", name)
print_name("Bethany")

#Problem 2
def ninety(a,b,c):
    d=90*4-a-b-c
    return d
print(ninety (2,3,4))

#Problem 3
def miles_per_hour(miles,hours,minutes,seconds):
    a=miles
    b=hours
    c=minutes/60
    d=seconds/3600
    speed=a/(b+c+d)
    return speed
print(miles_per_hour(20,2,21,16))

#Problem 4
def greeting(name):
    if name=="Chris":
        print("Hello Chris")
    else:
        print("Goodbye", name)
greeting("Chris")
greeting("Bethany")

#Problem 5
def convert_temperature(temp,units):
    if units=="celcius":
        value=temp*1.8+32
        return value
    elif units=="farenheit":
        value=5/9*(temp-32)
        return value
print(convert_temperature(39,"celcius"))
print(convert_temperature(41,"farenheit"))

#Problem 6
def calculate_grade(score):
    if 90<=score:
        return "A"
    elif 80<=score<90:
        return "B"
    elif 70<=score<80:
        return "C"
    elif 60<=score<70:
        return "D"
    elif score<60:
        return "F"
print(calculate_grade(98))
print(calculate_grade(84))
print(calculate_grade(76))
print(calculate_grade(65))
print(calculate_grade(41))
