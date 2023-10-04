#CS175
#Sashank Vaddiparty
#Assignment 3 Restaurant


#Making a List for all restaurant's menu and its options
print("Welcome to Restaurant Program, where your dietary needs are meet")

repeatProgram = "yes"
while repeatProgram== "yes":


    JoesGourmetBurgers = []
    MainStreetPizzaCompany  = ["Vegetarian", "Gluten-Free"]
    CornerCafe = ["Vegetarian", "Vegan", "Gluten-Free"]                           
    MamasFineItalian = ["Vegetarian"]             
    TheChefsKitchen  = ["Vegetarian", "Vegan", "Gluten-Free"]              

#Making a dict to contain the restaurants so it can be connected back to the Menu options above
    restaurants = {
    'Joes Gourmet Burgers': JoesGourmetBurgers,
    'Main Street Pizza Company': MainStreetPizzaCompany,
    'Corner Cafe': CornerCafe,
    'Mamas Fine Italian': MamasFineItalian,
    'The Chefs Kitchen': TheChefsKitchen
}


#Getting the User input of their dietary req.
    QVegetarian = input("Is anyone in your party Veg?  ").lower() == 'yes'
    QVegan = input("Is anyone in your party Vegan?  ").lower() == 'yes'
    QGluten_free = input("Is anyone in your party Gluten-free?  ").lower() == 'yes'

#Making a empty list that will hold the suitable restaurants based on user input
    suitable_restaurants = []

#Using item.() for name and options
# Name will name of restuarants
#Options will be the name of options: Veg, Vegan, Gluten.
    for name, options in restaurants.items(): #Runs a for loop for each restaurant 
        if QVegetarian  and "Vegetarian" not in options:# If the question and option is not in the options continues the code to nextline
            continue
        if QVegan and "Vegan" not in options:
            continue
        if QGluten_free and "Gluten-Free" not in options:
            continue
        suitable_restaurants.append(name)#If the user input meets req, then it will append the name of the restaurants from using item()

#Printing what we appended to the new Iist and printing that list
    print("Here are your restaurants choices:  ")
    for restaurants in suitable_restaurants:
        print(restaurants)

    repeatProgram = input("Would you like to change your mind about the menu?")

Print("The Program is quit")
