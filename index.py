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
    if oper.value == "+":
        result = add(int(num1.value),int(num2.value))
        ans =f"{num1.value} {oper.value} {num2.value} = {result}"
        screen.write(ans)
        clear()
    elif oper.value =="-":
        result = sub(int(num1.value),int(num2.value))
        ans =f"{num1.value} {oper.value} {num2.value} = {result}"
        screen.write(ans)
        clear()

    elif oper.value =="x" or oper.value =="*":
        result = mul(int(num1.value),int(num2.value))
        ans =f"{num1.value} {oper.value} {num2.value} = {result}"
        screen.write(ans)
        clear()
    elif oper.value =="/":
         result = div(int(num1.value),int(num2.value))
         ans =f"{num1.value} {oper.value} {num2.value} = {result}"
         screen.write(ans)
         clear()
    else:
        screen.write("Math Error")
        clear()

    