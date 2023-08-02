gamelist=[0,1,2]

def diplaygame(gamelist):
     
     print(gamelist)

print(diplaygame(gamelist)) 

def positionchoice():

    choice='word'

    while choice not in ['0','1','2']:


        choice=input('choose a number between (0,1,2):')

        if choice not in ['0','1','2']:

            print('soory, input is invailid!!')
        

    return int(choice)

print(positionchoice())

def replaceposition(gamelist,position):

    placementposition=input('write a word which you want to replace with:')

    gamelist[position]=placementposition

    return gamelist

print(replaceposition([0,1,2],1))


def gameon():

    choice ='word'

    while choice not in ['Y','N']:

        choice=input('dou you wana play more??')

        if choice not in ['Y','N']:

            print('invailid input')

    if choice=='Y':
        return True
    if choice=='N':
            return False
 
print(gameon())  

gameonagain=True

gamelist=[0,1,2]

while gameon:
    diplaygame(gamelist)

    position=positionchoice()

    gamelist=replaceposition(gamelist,position)

    diplaygame(gamelist)

    gameonagain=gameon()


   




