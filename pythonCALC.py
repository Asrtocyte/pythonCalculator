#my simple calculator
num1=int(input("Enter first nuber: "))
num2=int(input("Enter second number: "))
choose=str(input("choose oparator eg -(subtraction),+(add),/(division) or x(multiplication) "))
addition1 = num1+num2
subtraction2 = num1-num2
multiplication3 = num1*num2
division4 = num1/num2
if choose == "subtraction" or choose == "-":
  print(subtraction2)
elif choose == "add" or choose == "+":
  print(addition1)
elif choose == "multiplication" or choose == "x":
  print(multiplication3)
elif choose == "division" or choose == "/":
  print(division4)