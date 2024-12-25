import resource_data

milk = 200
coffee = 100
water = 300
money = 0
stop_machine = False

while not stop_machine:
    choose = input("What would you like? espresso/latte/cappuccino ")
    if choose == "off":
        stop_machine = True
    if choose == "report":
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Water: {water}ml")
        print(
            f"Money: ${resource_data.total_balance(resource_data.transactionProcess(inp_quarter,
            inp_dim,
            inp_cent,
            inp_penny), money)}"
        )
    else:
        print("Please enter coin? ")
        inp_quarter = int(input("How money quarter? "))
        inp_dim = int(input("How money dim? "))
        inp_cent = int(input("How money cent? "))
        inp_penny = int(input("How money penny? "))
        resource_data.orderProcess(
            choose,
            inp_quarter,
            inp_dim,
            inp_cent,
            inp_penny,
            water,
            milk,
            coffee,
            money,
        )
