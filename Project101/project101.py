import random
response = 'y'

while response == 'y':
    no = random.randint(1, 6)
    question = str(input("Do you want to roll the dice? Yes or No: "))
    if question == 'Yes' or question == 'yes':
        reponse = 'y'
    else:
        response = 'n'
    if no == 1:
        print('[-----]')
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
        print('[-----]')
    elif no == 2:
        print('[-----]')
        print('[     ]')
        print('[ 0 0 ]')
        print('[     ]')
        print('[-----]')
    elif no == 3:
        print('[-----]')
        print('[     ]')
        print('[0 0 0]')
        print('[     ]')
        print('[-----]')
    elif no == 4:
        print('[-----]')
        print('[ 0 0 ]')
        print('[     ]')
        print('[ 0 0 ]')
        print('[-----]')
    elif no == 5:
        print('[-----]')
        print('[ 0 0 ]')
        print('[  0  ]')
        print('[ 0 0 ]')
        print('[-----]')
    elif no == 6:
        print('[-----]')
        print('[ 0 0 ]')
        print('[ 0 0 ]')
        print('[ 0 0 ]')
        print('[-----]')