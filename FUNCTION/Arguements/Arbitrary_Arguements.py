def function(*vegetable):
    print("The names of vegetable are "+vegetable[2])
    
function('brinjal','cucumber','tomato','curry leaf')

#he *args parameter allows a function to accept any number of positional arguments

#Inside the function, args becomes a tuple containing all the passed argument
