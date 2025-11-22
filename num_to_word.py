num_words = {0:'zero',1:'one',2:'two',3:'three'}
user_inp = input('Enter valid number : ')
if not user_inp.isdigit():
    print('Enter valid input')
else:
    user_inp = int(user_inp)
    print(f'{user_inp}')