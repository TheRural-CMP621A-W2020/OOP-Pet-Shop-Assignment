 
 
from pet import Pet
 
pets = list()  #an empty list that will store all the pets in the shops

#initialize and describe Spot the Dog.
spot = Pet('Spot')
spot.set_animal('dog')
spot.set_description('Short legged, white fur with a single black spot')
''' spot.set_noise('Woof!') '''
pets.append(spot)

#initialize and describe Shadow the Cat.
shadow = Pet('Shadow')
shadow.set_animal('cat')
shadow.set_description('Shy, with all dark fur. She likes to hide behind furniture.')
''' shadow.set_noise('Meow!')  '''
pets.append(shadow)

''' Add your own pet(s) here '''



#Customer Interaction with the Pets
print('Welcome to My Pet Shop!')

current_pet = pets[0]

while True:
    print('\n')
    print('Choose the pet that you would like to meet.')
    
    for index, pet_name in enumerate(pets):     #prints a list of pets 
        print(index, pet_name.get_name())
        
    choice = input(' >')
    try:  
        i = int(choice)             #get user choice
        current_pet = pets[i]       #set the current_pet as the one chosen by customer
    
    except:     #ERROR if the customer does not choose a NUMBER from the options
        print('!!! You will need to choose a number from the pet options !!!')
        continue
    
    current_pet.describe()  
    
    print('What would you like to say to this pet?')
    greeting = input(' >')
    
    ''' current_pet.pet_talk(greeting) '''
    
    

