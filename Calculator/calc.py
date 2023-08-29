def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        raise ValueError('Cannot divide by zero\n')
    return x/y


while True:
    try:

        option = int(input('Choose option:\n' '1:Add\n' '2:Subtract\n' '3: Multiply\n' '4:Divide\n'))

        if option not in (1,2,3,4):
            print('Please enter a valid number')
            continue

        num1 = float(input('Enter first number:\n'))
        num2 = float(input('Enter second number:\n'))

        match option:

            case 1: 
                print('Result: ', add(num1, num2))
            case 2: 
                print('Result: ', subtract(num1, num2))
            case 3: 
                print('Result: ', multiply(num1, num2))
            case 4:
                print('Result: ', divide(num1, num2))
        try:
            while True:
                value = int(input('Do you want to perform another calculation?\n 1: Yes\n 2: No\n'))
                if value not in (1,2):
                    print('Please enter a valid number')
                    continue
                else:
                    break

            if (value == 2):
                break
        except ValueError:
            print('Invalid input. Please enter valid numbers')
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")    
