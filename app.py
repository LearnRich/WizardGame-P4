import random
import copy

def print_store_list(list):
    for counter in range(0, len(list)):
        print(counter+1, ")", list[counter]['item_name'])
    print("X) Exit store department")
    choice = input("Please enter item number you wish to purchase: ")
    return choice

running = True

character = {
    "name": "unknown",
    "lvl": 1,
    "xp": 0,
    "hp": 50,
    "mp": 50,
    "atk": 10,
    "spell": {
            "name": "Lightning",
            "dmg": 25,
            "mp_cost": 20,
            "lvl": 1
        },
    "cash": 20,
    "items": [
        {
            "item_name": "Small Health Pot",
            "item_effect": "hp",
            "effect:value": 25
        }
    ]
}

monster_dict = []
monster_dict.append({
    "name": "George",
    "lvl": 1,
    "hp": 15,
    "xp": 5,
    "atk": 1,
    "reward": 1
})
monster_dict.append({
    "name": "Norman",
    "lvl": 1,
    "hp": 12,
    "xp": 5,
    "atk": 2,
    "reward": 2
})
monster_dict.append({
    "name": "Toad",
    "lvl": 2,
    "hp": 25,
    "xp": 7,
    "atk": 2,
    "reward": 5
})

wizmart_potions = [
    {
        "item_name": "Small Health Pot",
        "item_effect": "hp",
        "effect:value": 25,
        "cost": 20
    },
    {
        "item_name": "Small Mana Pot",
        "item_effect": "mp",
        "effect:value": 20,
        "cost": 20
    },
    {
        "item_name": "Medium Health Pot",
        "item_effect": "hp",
        "effect:value": 50,
        "cost": 40
    },
    {
        "item_name": "Medium Mana Pot",
        "item_effect": "mp",
        "effect:value": 40,
        "cost": 40
    },
    {
        "item_name": "Large Health Pot",
        "item_effect": "hp",
        "effect:value": 100,
        "cost": 60
    },
    {
        "item_name": "Large Mana Pot",
        "item_effect": "mp",
        "effect:value": 80,
        "cost": 60
    }

]

wizmart_weapons = [
    {
        "item_name": "Lightsaber",
        "item_effect": "weapon",
        "effect:value": 200,
        "cost": 60
    },
    {
        "item_name": "N00b Wand",
        "item_effect": "weapon",
        "effect:value": 80,
        "cost": 60
    },
    {
        "item_name": "A Rock",
        "item_effect": "weapon",
        "effect:value": 1,
        "cost": 60
    }
]
wizmart_food = []
wizmart_spells = [
    {
        "item_name": "Fireball",
        "item_effect": "spell",
        "effect:value": 160,
        "cost": 140
    },
    {
        "item_name": "Ice Bolt",
        "item_effect": "spell",
        "effect:value": 80,
        "cost": 100
    }
]

while running:

    # Printing the main menu
    print(" Super Wizard Battle Network")
    print("-----------------------------")
    print("A) New Game")
    print("B) Load Game")
    print("X) Exit Game")
    #get user choice
    choice = input("Please Enter Choice: ").lower()

    #decide what to run based on choice
    if choice == "x":
        running = False
    elif choice == "a":
        # Create the character
        character["name"] = input("Please enter your name: ")

        print("Welcome", character["name"],
              "to the Wizard Battle Network")

        game_running = True
        while game_running:
            print("Wizard Menu")
            print("-----------")
            print("A) Train against Monsters")
            print("B) Battle other Wizard")
            print("C) Visit Store")
            print("D) Character Profile")
            print("S) Save")
            print("X) Exit to Main Menu")
            choice = input("Please Enter Choice: ").lower()

            if choice == "x":
                game_running = False
            elif choice == "a":
                monster = monster_dict[random.randrange(0, len(monster_dict))].copy()
                battle = True
                #
                print("You are about to battle:")

                while battle:
                    print("Monster:", monster['name'])
                    print("Health Points:", monster['hp'])
                    # Display to user option for attacking
                    print("1: Physical Attack")
                    print("2: Cast Spell")
                    option = input("Please select attack: ")
                    if option == "1":
                        print("You wacked", monster["name"], "for", character["atk"])
                        monster["hp"] -= character["atk"]
                    elif option == "2":
                        print("Your", character["spell"]["name"], "damages",
                              monster["name"], "for", character["spell"]["dmg"] )
                        monster["hp"] -= character["spell"]["dmg"]
                    else:
                        print("Not a valid option")
                        print("INVALID OPTION: M HP", monster['hp'])

                    if monster["hp"] > 0:
                        print(monster["name"], "damages you for", monster["atk"])
                        character["hp"] -= monster["atk"]

                    if monster["hp"] <= 0:
                        character['xp'] += monster['xp']
                        character['cash'] += monster['reward']
                        print("Congratulations! You are the winner!")
                        print("You gained", monster['xp'], "experience")
                        print("You collected ", monster['reward'], "coin")
                        battle = False
                    if character["hp"] <= 0:
                        print("You are unable to battle......")
                        battle = False

            elif choice == "b":
                print("Battle")
            elif choice == "c":
                store_menu = True
                while store_menu:
                    print("WizMart TM")
                    print("-----------------")
                    print("A) Potions")
                    print("B) Weapons")
                    print("C) Food Court")
                    print("D) Spells")
                    print("X) Exit Store")
                    print("You currently have", character['cash'], " WizDollars")
                    choice = input("Please choose a store department: ").lower()

                    # YOU ADD THE IF-STATEMENT!!
                    if choice == "x":
                        store_menu = False
                    elif choice == 'a':
                        potions_menu = True
                        while potions_menu:
                            print("Potions List")
                            choice = print_store_list(wizmart_potions).lower()
                            if choice == "x":
                                potions_menu = False
                    elif choice == "b":
                        weapos_menu = True
                        while weapons_menu:
                            print("Weapons List")
                            choice = print_store_list(wizmart_weapons).lower()
                            if choice == "x":
                                weapons_menu = False
                    elif choice == "c":
                        potions_menu = True
                        while potions_menu:
                            print("Food Court Items List")
                            choice = print_store_list(wizmart_food).lower()
                            if choice == "x":
                                potions_menu = False
                    elif choice == "d":
                        potions_menu = True
                        while potions_menu:
                            print("Spells List")
                            choice = print_store_list(wizmart_spells).lower()
                            if choice == "x":
                                potions_menu = False



            elif choice == "d":
                profile_menu = True
                while profile_menu:
                    print("Profile Menu")
                    print("A) Display Profile")
                    print("B) Update Profile")
                    print("X) Back")
                    choice = input("Please Enter Choice: ").lower()

                    if choice == "x":
                        profile_menu = False
                    elif choice == 'a':
                        print("Name:", character['name'])
                        print("Level:", character['lvl'])
                        print("Items:")
                        for item in character['items']:
                            print(item)

                print("Profile")
            elif choice == "s":
                print("save")
            else:
                print("Please enter a valid choice")


    elif choice == "b":
        print("Load game code here")
    else:
        print("Please enter a valid choice")