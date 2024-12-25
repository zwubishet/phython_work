import math


def transactionProcess(quarter, dime, cent, penny):
    return (quarter * 0.25) + (dime * 0.1) + (cent * 0.05) + (penny * 0.01)


def total_balance(pay, money):
    return pay + money


def orderProcess(order, quarter, dime, cent, penny, water, milk, coffee, money):

    es_water = 150
    es_coffee = 18
    la_water = 200
    la_coffee = 24
    la_milk = 150
    ca_water = 250
    ca_coffee = 24
    ca_milk = 100

    if order == "espresso":
        amount = 2.25
        if es_water <= water & es_coffee <= coffee:
            water -= es_water
            coffee -= es_coffee
            user_amount = round(transactionProcess(quarter, dime, cent, penny), 2)
            if user_amount > amount:
                print(f"Here is your change: {amount-user_amount}")
                money += amount
                print("Here is your Espresso ☕.")
            elif user_amount < amount:
                print("Sorry, That is not enough Money.")
            else:
                print("Here is your Espresso ☕.")
        elif es_water > water:
            print("Sorry, there is no enough water.")
        else:
            print("Sorry, there is no enough coffee.")
    elif order == "latte":
        amount = 0.5
        if la_water <= water and la_coffee <= coffee and la_milk <= milk:
            water -= la_water
            coffee -= la_coffee
            milk -= la_milk
            user_amount = round(transactionProcess(quarter, dime, cent, penny), 2)
            if user_amount > amount:
                print(f"Here is your change: ${user_amount-amount}")
                money += amount
                print("Here is your Latte ☕.")
            elif user_amount < amount:
                print("Sorry, That is not enough Money.")
            else:
                print("Here is your Latte ☕.")
        elif la_water > water:
            print("Sorry, there is no enough water.")
        elif la_milk > milk:
            print("Sorry, there is no enough milk.")
        else:
            print("Sorry, there is no enough coffee.")
    elif order == "cappuccino":
        amount = 2.75
        if ca_water <= water & ca_coffee <= coffee & ca_milk <= milk:
            water -= ca_water
            coffee -= ca_coffee
            milk -= ca_milk
            user_amount = round(transactionProcess(quarter, dime, cent, penny), 2)
            if user_amount > amount:
                print(f"Here is your change: {amount-user_amount}")
                money += amount
                print("Here is your cappuccino ☕.")
            elif user_amount < amount:
                print("Sorry, That is not enough Money.")
            else:
                print("Here is your cappuccino ☕.")
        elif ca_water > water:
            print("Sorry, there is no enough water.")
        elif ca_milk > milk:
            print("Sorry, there is no enough milk.")
        else:
            print("Sorry, there is no enough coffee.")
