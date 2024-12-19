#You have a business of many bicycles that
# people can rent. We assume that:
 #Somebody  rents a bicycle no more than 
 #24 hours within the same day.
#The rate per hour depends on the time 
#of the day as follows:
# 0 - 7         and 21-24  the rate 
#is RWF 500 per hour#
# 7-  10     and      19-21 the rate
 #is  RWF 1000 per hour
#10- 19 the rate is 1500 per hour 
#Write a python program that takes as 
#input the starting time and the ending time 
#and  does the following:
#(a) If the starting is greater than the
 #ending time or the sarting time or ending
  #time is out of the range 0-24, 
  #then display invalid input
#(#b) Print the total amount to be paid 
#by the renter.





 
def calculate_rental_cost(start_time, end_time):
    if start_time < 0 or end_time < 0 or start_time >= 24 or end_time >= 24:
        return "Invalid input: Time must be in the range 0-24."
    if start_time >= end_time:
        return "Invalid input: Starting time must be less than ending time."
    
    total_cost = 0
    current_time = start_time

    while current_time < end_time:
        if (0 <= current_time < 7) or (21 <= current_time < 24):
            total_cost += 500  # RWF 500 per hour
        elif (7 <= current_time < 10) or (19 <= current_time < 21):
            total_cost += 1000  # RWF 1000 per hour
        elif (10 <= current_time < 19):
            total_cost += 1500  # RWF 1500 per hour

        current_time += 1  # Move to the next hour

    return total_cost

# Input from the user
try:
    start_time = float(input("Enter the starting time (0-24): "))
    end_time = float(input("Enter the ending time (0-24): "))

    cost = calculate_rental_cost(start_time, end_time)
    if isinstance(cost, str):  # If the return is a string, it's an error message
        print(cost)
    else:
        print(f"Total amount to be paid: RWF {cost}")

except ValueError:
    print("Invalid input: Please enter numeric values for time.")





#We have six types of mushrooms : 
#Agaric jaunissant
#Cepe de bordeaux
#3
#Amanite tue-mouche
#Coprin chevelu
#Girolle
#Pied Bleu
#•The cepe bordeaux is the only 
#one to have pores, the other mushrooms
# having gills.
# •Both coprin chevelu and agaric jaunissant 
# grow In meadows, other mushrooms grow 
# in forests
 #•The only mushrooms to have a convex cup 
 #are agaric jaunissant,amanite tue-mouches,
#  and pied bleu.
  #•The only mushrooms to have a ring are 
  #agaric jaunissant,amanite tue-mouches,
  #and coprin chevelu.
 # The User thinks of a mushroom (one of the six).
#The program asks at most three of the  
#following four questions.
#The User answers truthfully by yes or no
#Based on the user’s answers, the program 
#determines the mushroom.
#The questions: 
#Does your mushroom have gills ?
#Does your mushroom grow in a forest ?
#Does your mushroom have a ring?
#Does your mushroom have a convex cup?



def determine_mushroom():
    print("Think of a mushroom from the following list:")
    print("1. Agaric jaunissant")
    print("2. Cepe de bordeaux")
    print("3. Amanite tue-mouche")
    print("4. Coprin chevelu")
    print("5. Girolle")
    print("6. Pied Bleu")
    print("Answer the following questions with 'yes' or 'no':")
    
    # Questions and their implications
    has_gills = input("Does your mushroom have gills? ").strip().lower() == "yes"
    if has_gills:
        # If it has gills, check further
        grows_in_forest = input("Does your mushroom grow in a forest? ").strip().lower() == "yes"
        if grows_in_forest:
            has_ring = input("Does your mushroom have a ring? ").strip().lower() == "yes"
            if has_ring:
                # Amanite tue-mouche
                print("Your mushroom is Amanite tue-mouche.")
            else:
                # Girolle
                print("Your mushroom is Girolle.")
        else:
            # Check for Coprin chevelu or Agaric jaunissant
            has_convex_cup = input("Does your mushroom have a convex cup? ").strip().lower() == "yes"
            if has_convex_cup:
                # Agaric jaunissant
                print("Your mushroom is Agaric jaunissant.")
            else:
                # Coprin chevelu
                print("Your mushroom is Coprin chevelu.")
    else:
        # If it doesn't have gills, it must be Cepe de bordeaux or Pied Bleu
        grows_in_forest = input("Does your mushroom grow in a forest? ").strip().lower() == "yes"
        if grows_in_forest:
            has_convex_cup = input("Does your mushroom have a convex cup? ").strip().lower() == "yes"
            if has_convex_cup:
                # Pied Bleu
                print("Your mushroom is Pied Bleu.")
            else:
                # This is ambiguous as the user may have chosen Girolle
                print("Your mushroom is Cepe de bordeaux.")
        else:
            # If it grows in meadows, it must be Girolle
            print("Your mushroom is Girolle.")

# Run the function
determine_mushroom()
