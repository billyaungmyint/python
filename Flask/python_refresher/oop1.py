class Dog():
    
    #CLASS OBJECT ATTRIBUTES
    species = "mamal"
    
    def __init__(self , input_breed , name):
        self.breed = input_breed
        self.name = name
        
x = Dog('Huskie' , 'Sammy')

print(x.breed)
print(x.name)
print(x.species)