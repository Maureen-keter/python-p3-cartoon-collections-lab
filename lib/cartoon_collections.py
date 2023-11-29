def roll_call_dwarves(dwarfs):
    index=0
    for dwarf in dwarfs:
        print(f"{index +1}. {dwarf}")
        index+=1

def summon_captain_planet(planeteers):
    capitalized_planeteers=[planet.capitalize() + "!" for planet in planeteers]
    return capitalized_planeteers


def long_planeteer_calls(calls):
        for call in calls:
             if len(call)>4:
                  return True
        else:
             return False          
                           
def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]

    for ingredient in ingredients:
         if any(cheese in ingredient for cheese in cheeses):
            return ingredient
         
    return None


         


