# LEGB rule
# local

def report():
    # Local assignment
    x = 'local'
    print(x)

# Enclosing

x = 'Global level'

def enclosing():
    x = 'enclosing level'
    
    def inside():
        x = 'local level'
        print(x)
    
    inside() 

# Global

x ='outside'

def report():
    # Local assignment
    global x
    # reassign global
    x = 'local'
    return x
    
# Built-in