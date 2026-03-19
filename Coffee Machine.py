from art import logo
def report_coffee(curr_water,curr_milk,curr_coffee,curr_money):
    print(f'Water: {curr_water}ml')
    print(f'Milk: {curr_milk}ml')
    print(f'Coffee: {curr_coffee}g')
    print(f'Money: ${curr_money}')

def process_coffee(ch_coff,curr_water,curr_milk,curr_coffee,curr_money):
    if ch_coff == 'espresso':
        price_coffee = 2.50
        needed_water = 100
        needed_milk = 50
        needed_coffee = 20
    elif ch_coff == 'latte':
        price_coffee = 3.25
        needed_water = 75
        needed_milk = 60
        needed_coffee = 30
    else:
        price_coffee = 3.75
        needed_water = 60
        needed_milk = 90
        needed_coffee = 35
    #print(f'Please pay ${price_coffee} for your {ch_coff}')
    if curr_water > needed_water and curr_milk > needed_milk and curr_coffee > needed_coffee:
        print(f'Please pay ${price_coffee} for your {ch_coff}')
        needed_money_quarters = int(input('Insert number of quarters: '))
        needed_money_dimes = int(input('Insert number of dimes: '))
        needed_money_nickels = int(input('Insert number of nickles: '))
        needed_money_pennies = int(input('Insert number of pennies: '))
        taken_money_count = (needed_money_quarters * 0.25 + needed_money_dimes * 0.10 + needed_money_nickels * 0.05 + needed_money_pennies * 0.01)
        print(f'You have paid ${taken_money_count}.')
        if taken_money_count > price_coffee:
            coffee_refund = taken_money_count - price_coffee
            print(f'Here is your ${coffee_refund} change')
            curr_water = curr_water - needed_water
            curr_milk = curr_milk - needed_milk
            curr_coffee = curr_coffee - needed_coffee
            curr_money = curr_money + price_coffee
            print('Transaction Successful')
            print(f'Here is your {ch_coff}. Enjoy!')
            return curr_water,curr_milk,curr_coffee,curr_money
        elif taken_money_count == price_coffee:
            curr_water = curr_water - needed_water
            curr_milk = curr_milk - needed_milk
            curr_coffee = curr_coffee - needed_coffee
            curr_money = curr_money + price_coffee
            print('Transaction Successful')
            print(f'Here is your {ch_coff}. Enjoy!')
            return curr_water,curr_milk,curr_coffee,curr_money
        else:
            print(f"Sorry, that's not enough money. ${taken_money_count} refunded.")
            return curr_water,curr_milk,curr_coffee,curr_money
    else:
        if needed_water > curr_water:
            resource_less = 'water'
        elif needed_milk > curr_milk:
            resource_less = 'milk'
        elif needed_coffee > curr_coffee:
            resource_less = 'coffee'
        print(f'Sorry, there is not enough {resource_less}')
        print(f'Refilling the {resource_less}')
        if resource_less == 'water':
            curr_water = 150
        elif resource_less == 'milk':
            curr_milk = 500
        elif resource_less == 'coffee':
            curr_coffee = 500
        return curr_water,curr_milk,curr_coffee,curr_money
        

print(logo)
coffee_machine_status = 'on'
quant_water = 1000
quant_milk = 500
quant_coffee = 500
quant_money = 0
while coffee_machine_status == 'on':
    choice_coffee = input('What would you like? (espresso/latte/cappuccino)').lower()
    if choice_coffee == 'report':
        report_coffee(quant_water,quant_milk,quant_coffee,quant_money)
    elif choice_coffee == 'off':
        coffee_machine_status = 'off'
    elif choice_coffee == 'latte' or choice_coffee == 'espresso' or choice_coffee == 'cappuccino':
        quant_water,quant_milk,quant_coffee,quant_money = process_coffee(choice_coffee,quant_water,quant_milk,quant_coffee,quant_money)
    else:
        print('Invalid Selection!!!')
    
        
    
