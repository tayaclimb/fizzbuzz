Questions = { 
    'strong' : 'Do you like a strong drink?',
    'rocks' : 'Do you like your drink watered down and or cold?',
    'sweet' : 'Do you want a bit of sugar with your drink?',
    'salty' : 'Do you want your drink to taste of the ocean?',
    'fresh' : 'Do you want a hint of the fresh air?'
    }
    
Ingredients = {
    'strong': ['Rum', 'Vodka', 'Black tea and Rum'],
    'rocks': ['crushed ice', 'blended ice', 'just ice'],
    'sweet': ['Splash of syrup', 'hint of sugar', 'handful of rockcandy'],
    'salty': ['Classic salted rim', 'scoop of ocean water', 'hint of sand'],
    'fresh': ['crushed mint', 'sprig of cilantro', 'twist of citrus']
    }
import random
def ask_the_customer():
    Answers = dict()
    for key in Questions:
        preference = raw_input(Questions[key] + ' ')
        preference = str(preference)
        #print preference
        if preference == 'yes':
            Answers[key] = True
            #print Answers
        else:
            Answers[key] = False
           # print Answers
            
    #print Answers
    return Answers

your_drink = list()

#ask_the_customer()
def make_the_drink():
    Answers = ask_the_customer()
    for key in Answers:
        if Answers[key] == True:
            i_like = random.choice(Ingredients[key])
            #print i_like
            your_drink.append(i_like)
        else:
            continue
    print('Your drink includes:'), your_drink
make_the_drink()    

    
    
    
    
    


