import time
timesteamp = time.strftime('%H:%M:%S')
print(timesteamp)
timesteamp = int(time.strftime('%H'))
print(timesteamp)
timesteamp = time.strftime('%M')
print(timesteamp)
timesteamp = time.strftime('%S')
print(timesteamp)
# Good Morning Sir 
n = input("Enter your name: ")
h = int(time.strftime('%H'))
if(5<=h<12):
    print("Good Morning",n)
# Good Afternoon sir
elif(12<h<=17):
    print("Good Afternoon",n)
# Good evening sir
elif(17<h<=20):
    print("Good evening",n)
#Good night sir
else:
    print("Good night",n)
