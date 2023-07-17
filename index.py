num1 = Element("num1")
num2 = Element("num2")
oper = Element("opera")
screen = Element("ans")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b

def clear():
    num1.clear()
    num2.clear()
    oper.clear()

def answer(*a,**ab):
    result = f"Num1={num1.value} Num2={num2.vlaue} Oper={oper.value}"
    screen.write(result)
 
    
    # if oper.value == "+":
    #     result = add(int(num1.value),int(num2.value))
    #     screen.write(result)
    # elif oper.value =="-":
    #     result = sub(int(num1.value),int(num2.value))
    #     screen.write(result)

    # elif oper.value =="x" or oper.value =="*":
    #     result = mul(int(num1.value),int(num2.value))
    #     screen.write(result)
    # elif oper.value =="/":
    #      result = div(int(num1.value),int(num2.value))
    #      screen.write(result)
    # else:
    #     screen.write(0)
    #     clear()

    