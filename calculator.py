def main():
    num1=recive_numb()
    num2=recive_numb()
    print('Sum=', num1+num2)

def recive_numb():
    '''filtr input. recive only number.return float'''
    while True:
        num = input()
        try:
            num=float(num)
            break
        except:
            pass 
    return num

def add(a,b):
    '''sum two numbers'''
    return a+b

if __name__ == "__main__":
    TRASHE STRING 
    main()
