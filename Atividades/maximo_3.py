def maximo(num1, num2, num3):
    if num1 > num2 > num3:
        return num1
    elif num1 > num3 > num2:
        return num1
    elif num2 > num1 > num3:
        return num2
    elif num2 > num3 > num1:
        return num2
    elif num3 > num1 > num2:
        return num3
    else:
        if num3 > num2 > num1:
            return num3
        else:
            if num1 == num2 == num3:
                return num1 
