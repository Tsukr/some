def main():
    num1=recive_numb()
    print(num1)

def recive_numb():
    '''filtr input. recive only number'''
    while True:
        num = input()
        if num.isdigit():
            break
    return num

def add(a,b):
    ...

if __name__ == "__main__":
    main()
