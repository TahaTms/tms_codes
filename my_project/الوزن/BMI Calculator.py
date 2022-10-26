w =int(input("inter the Weight: "))
h = float(input ("inter the Height"))
bmi = (w/(h**2))

while bmi<18.5:
     print("Underweight")
     break 
while  bmi>=18.5 and bmi<25.0:
     print ("Normal")
     break
while bmi>=25.0 and bmi<30.0:
     print ("Overweight")
     break
while  bmi>30.0:
     print ("Obesity")
     break