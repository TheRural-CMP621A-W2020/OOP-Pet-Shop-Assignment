
class Pet():
    def __init__(self, pet_name):
        self.name = pet_name
        self.animal = None
        self.description = None
        ''' Add an attribute called noise '''
    
    #Getter Methods
    def get_name(self):
        return self.name
    
    def get_animal(self):
        return self.animal
    
    def get_description(self):
        return self.description
    
    ''' def get_noise(self):
    add a getter method that returns the noise attribute '''
    
    
    #Setter Methods
    def set_name(self, new_name):
        self.name = new_name
    
    def set_animal(self, animal_type):
        self.animal = animal_type
    
    def set_description(self, pet_description):
        self.description = pet_description
        
    ''' def set_noise(self, pet_noise):
        add a setter method that sets the noise attribute.   '''
    
    #Other Methods
    
    #Describe the pet
    def describe(self):
        print(self.name)
        ''' add code so that the pet is described to the customer
        1) A sentence with the pet name and animal type
        2) The description of the animal.   '''
    
    #Speak with the pet
    def pet_talk(self, greeting):
        ''' The animal should make noise for every word in the greeting
            For Example:  "Here kitty kitty!"  Would result in 'Meow!Meow!Meow!  
            and Exampel:  "Roll over!"         Would result in 'Woof!Woof!'   
        '''
        
    