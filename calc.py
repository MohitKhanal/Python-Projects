import math
choice=input("Do you want to work with one or with two values?(O/T)")
match choice:
    case "O":
        onenum=float(input("Enter any number:"))
        operation=int(input('''Choosee:\n
                        1.Factorial
                        2.Trignometric
                        3.Exponential
                        4.logarithmic
                        5.Absolute
                        6.Roundoff
                        \n'''))
        match operation:
            case 1:
                print(f"The factoial of {onenum} is",math.factorial(int(onenum)))
            case 2:
                trig=int(input('''Here is a list of trignometric functions choose any one of them.Give the index that you want to use!! 
                           1.sin(x)
                           2.cos(x)
                           3.tan(x)
                           4.arc sin(x)
                           5.arc cos(x)
                           6.arc tan(x)
                           7.sinh(x)
                           8.cosh(x)
                           9.tanh(x)
                            '''))
                match trig:
                    case 1:
                        print(math.sin(onenum))
                    
                    case 2:
                        print(math.cos(onenum))
                    
                    case 3:
                        print(math.tan(onenum))
                    
                    case 4:
                        print(math.asin(onenum))
                    
                    case 5:
                        print(math.acos(onenum))
                    
                    case 6:
                        print(math.atan(onenum))
                    
                    case 7:
                        print(math.sinh(onenum))
                    
                    case 8:
                        print(math.cosh(onenum))
                    
                    case 9:
                        print(math.tanh(onenum))
            case 3:
                power=int(input("enter the power you want to raise your number to"))
                print(math.pow(onenum,power))
            case 4:
                bs=int(input("Base of log:"))
                print(math.log(onenum)/(math.log(bs)))
            case 5:
                print(f"The absolute value of {onenum} is",math.fabs(onenum))
            case 6:
                print(f"{onenum} has been rounded off to",round(onenum,2))
    case "T":
        num1=float(input("First number:"))
        num2=float(input("Second number:"))
        operation=int(input('''
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division                    
        '''))
        match operation:
            case 1:
                print(num1+num2)
            case 2:
                print(num1-num2)
            case 1:
                print(num1*num2)
            case 1:
                print(num1/num2)
        
        






        
          