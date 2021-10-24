# apple pos

print("--------------------")
print("\tApples")
print("--------------------")

savings = float(input("Amount of your money: "))
apple = float(input("How much apple will you buy:: "))

money_change = savings - apple
print(f"You can buy {int(apple)} apples and" + 
f"your change is {money_change} pesos.")

