'''
Password Strength checker
----------------------------------------#
'''

import string
import getpass

def check_password_strength():
    
    strength=0
    remarks=''
    lower_count=upper_count=num_count=wspace_count=special_count=0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count +=1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count +=1
        elif char ==' ':
            wspace_count +=1
        else:
            special_count +=1

        if lower_count >=1:
            strength +=1
        if upper_count >=1:
            strength +=1
        if num_count >=1:
            strength +=1
        if wspace_count >=1:
            strength +=1
        if special_count >=1:
            strength +=1

        if strength==1:
            remarks=('That\'s a very weak password')
        if strength==2:
            remarks=('That\'s a  weak password')
        if strength==3:
            remarks=('That\'s a an okay password')
        if strength==4:
            remarks=('That\'s a good password')
        if strength==5:
            remarks=('That\'s a Strong password')

        print('Your password has:-')
        print(f'Password score:{strength / 5}')
        print(f'Remarks: {remarks}')
'''
def check_pwd(another_pw=False):
        valid=False
        if another_pw:
            choice=input('Do you want to cHeck another password? (Y/N')
        else:
            choice=input('Do you want to cHeck Your password? (Y/N')

        while not valid:
            if choice.lower()=='y':
                return True
            elif choice.lower()=='n':
                print('Exiting....')
                return False
            else:
                print('Invalid input')

            '''    
if __name__ == '__main__':
        print('welcome to password strength checker')
        password=getpass.getpass('ENTER THE PASSWORD')
        check_password_strength()
        
        
