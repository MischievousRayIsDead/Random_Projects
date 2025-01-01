class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 500,
            "money": 50.00 #to give change during some of the first orders
        }
        self.menu = { #i don't know the actual recipe of any of these
            "espresso": {"ingredients": {"water": 100, "milk": 0, "coffee": 50}, "price": 1.50},
            "latte": {"ingredients": {"water": 100, "milk": 200, "coffee": 50}, "price": 3.00},
            "cappuccino": {"ingredients": {"water": 100, "milk": 150, "coffee": 50}, "price": 2.50}
        }

    def report(self): #generating report
        for item, amount in self.resources.items():
            unit = "ml" if item in ["water", "milk"] else "g" if item == "coffee" else "$"
            print(f"{item.capitalize()}: {amount}{unit}")

    def is_sufficient(self, ingredients): #to check whether there is enough resource to make the order or not
        for item, amount in ingredients.items():
            if self.resources[item] < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self, price): #To handle the coin input...YEAH IT IS A COIN ONLY MACHINE...SO WHAT HUHH...I AM A RETROPHIL, DON"T GIVE ME A HARD TIME!!!
        print("Please insert coins.")
        try:
            quarters = int(input("Number of quarters: ")) * 0.25
            dimes = int(input("Number of dimes: ")) * 0.10
            nickles = int(input("Number of nickles: ")) * 0.05
            pennies = int(input("Number of pennies: ")) * 0.01
        except ValueError:
            print("Invalid input. Transaction canceled.") #in case the user gives something else as an input for the price
            return False, 0

        total = round(quarters + dimes + nickles + pennies, 2)
        if total < price:
            print("Sorry that's not enough money. Money refunded.")
            return False, 0
        change = round(total - price, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True, total

    def make_coffee(self, choice): #as the name suggests, it will make coffee
        drink = self.menu[choice]
        if self.is_sufficient(drink["ingredients"]):
            success, payment = self.process_coins(drink["price"])
            if success:
                for item, amount in drink["ingredients"].items():
                    self.resources[item] -= amount
                self.resources["money"] += drink["price"]
                print(f"Here is your {choice}. Enjoy!")

    def run(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
            if choice == "off": #off is a secret keyword that the normal buyer won't see
                print("Turning off the machine. Goodbye!")
                break
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                self.make_coffee(choice)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()
