import os

def addition():
    os.system('cls' if os.name=='nt' else 'clear')
    print('Addition')

    continue_calc='y'
    num_1=float(input('Enter a number:'))
    num_2=float(input('Enter another number'))
    ans=num_1+num_2
    print(f'Current result: {ans}')

    while continue_calc.lower()=='y':
        continue_calc=(input('enter more (y/n):'))
        while continue_calc.lower() not in ['y','n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc=(input('Enter more(y/n): '))
            if continue_calc.lower()=='n':
                break
    num=float(input('Enter another number:'))
    answ +=num
    print(f'Current result: {ans}')
    values_entered +=1
    return[ans,values_entered]

def subtraction():
    os.system('cls' if os.name=='nt' else 'clear')
    print('Subtraction')

    continue_calc='y'
    num_1=float(input('Enter a number:'))
    num_2=float(input('Enter another number'))
    ans=num_1-num_2
    print(f'Current result: {ans}')

    while continue_calc.lower()=='y':
        continue_calc=(input('enter more (y/n):'))
        while continue_calc.lower() not in ['y','n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc=(input('Enter more(y/n): '))
            if continue_calc.lower()=='n':
                break
    
     cnum=float(input('Enter another number:'))
    answ +=num
    print(f'Current result: {ans}')
    values_entered +=1
    return[ans,values_entered]

def multiplication():
    os.system('cls' if os.name=='nt' else 'clear')
    print('Mutliplication')

    continue_calc='y'
    num_1=float(input('Enter a number:'))
    num_2=float(input('Enter another number'))
    ans=num_1*num_2
    print(f'Current result: {ans}')

    while continue_calc.lower()=='y':
        continue_calc=(input('enter more (y/n):'))
        while continue_calc.lower() not in ['y','n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc=(input('Enter more(y/n): '))
            if continue_calc.lower()=='n':
                break
    
    num=float(input('Enter another number:'))
    answ +=num
    print(f'Current result: {ans}')
    values_entered +=1
    return[ans,values_entered]

def division():
    os.system('cls' if os.name=='nt' else 'clear')
    print('Division')

    continue_calc='y'
    num_1=float(input('Enter a number:'))
    num_2=float(input('Enter another number'))
    ans=num_1/num_2
    print(f'Current result: {ans}')

    while continue_calc.lower()=='y':
        continue_calc=(input('enter more (y/n):'))
        while continue_calc.lower() not in ['y','n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc=(input('Enter more(y/n): '))
            if continue_calc.lower()=='n':
                break
    
    num=float(input('Enter another number:'))
    answ +=num
    print(f'Current result: {ans}')
    values_entered +=1
    return[ans,values_entered] 

def calculator():
    quit=False
    while not quit:
        results = []
        print ('Simple calculator')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for subtraction')
        print('Enter \'m\' for Multiplication')
        print('Enter \'d\' for Division')
        print('Enter \'q\' for Quit')

        choice=input('Selection')

        if choice=='q':
            quit=True
            continue
        if choice=='a':
            results=addition()
            print('Ans=',results[0],'total inputs',results[0])



        else:
            print('Not a valid argument')

if __name__=='__main__':
    calculator()
 



        
