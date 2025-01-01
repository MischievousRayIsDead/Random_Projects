import sys

#default storage of resources during the starting of the machine
milk = 1000
water = 1000
coffee = 500
money = 50.00 #to give change for some of the first orders

def report():
    global milk
    global water
    global coffee
    global money
    print(f"water: {water}")
    print(f"milk: {milk}")
    print(f"coffee: {coffee}")
    print(f"money: ${money}")

def process_coins(price):
    global money
    quarter=int(input("Number of quartes: "))
    dime=int(input("Number of dimes: "))
    nickle=int(input("Number of nickles: "))
    penny=int(input("Number of pennies: "))
    total = 0.25*quarter + 0.10*dime + 0.05*nickle + 0.01*penny
    if price > total:
        print("Sorry that's not enough money. Money refunded.")
        status = 0
    if price == total:
        money = money + total
        status = 1
    if price < total:
        money = money + total
        change = round(total - price ,2)
        money = money - change
        print(f"Here is ${change} dollars in change.")
        status = 1
    return status

def resources(m,w,c):
    global milk
    global water
    global coffee
    avail = 1
    if milk<m:
        print("Sorry there is not enough milk")
        avail = 0
    if water<w:
        print("Sorry there is not enough water")
        avail = 0
    if coffee<c:
        print("Sorry there is not enough coffee")
        avail = 0
    if avail == 1:
        milk=milk-m
        water=water-w
        coffee=coffee-c
        return 1
    if avail == 0:
        print("Sorry there's not enough resources. Money refunded.")
        return 0

def espresso(): #let say espresso needs 0 ml milk, 100ml water, 50g coffee and the price is $1.50
    price = 1.50
    status=process_coins(price)
    if status==1:
        avail=resources(0,100,50)
        if avail==1:
            print("Here is your espresso. Enjoy!")

def cappuccino(): #let say cappuccino needs 150 ml milk, 100ml water, 50g coffee and the price is $2.50
    price = 2.50
    status=process_coins(price)
    if status==1:
        avail=resources(150,100,50)
        if avail==1:
            print("Here is your cappuccino. Enjoy!")

def latte(): #let say latte needs 200 ml milk, 100ml water, 50g coffee and the price is $3.00
    price = 3.00
    status=process_coins(price)
    if status==1:
        avail=resources(200,100,50)
        if avail==1:
            print("Here is your latte. Enjoy!")

def prompt():
    prompt = input("What would you like ? (espresso, latte, cappuccino): ")
    match prompt:
        case 'report':
            report()
            pass
        case 'espresso':
            espresso()
            pass
        case 'latte':
            latte()
            pass
        case 'cappuccino':
            cappuccino()
            pass
        case 'off':
            print("The machine is turned off now.")
            sys.exit(0)

def main():
    while 1:
        prompt()

if __name__=="__main__":
    main()
