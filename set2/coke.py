#prompts the user to insert a coin, one at a time, each time informing the user of the amount due

amount = 50
while (amount > 0):
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount -= coin
print("Change Owed:", -amount)
