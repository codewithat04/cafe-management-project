#define the menu of cafe
menu = {
    'Pizza':250,
    'Cheese burger':100,
    'White sauce pasta':250,
    'Chicken burger':150,
    'Coffee':200,
    'Noodles':120,
    'Latte':250,
    'Virgin mojito':150,
    'Choco waffle':200,
    'Salad':250,


}
#greet
print("welcome to cafe Romiolane")
print("Pizza: Rs250\nCheese burger: Rs100\nWhite sauce pasta: Rs250\nChicken burger: Rs150\nCoffee: Rs200\nNoodles: Rs120\nLatte: Rs250\nVirgin mojito: Rs150\nChoco waffle: Rs200\nSalad: Rs250")
bill_total = 0
#250 +100 =350
dish_1 = input("enter the name of dish you want to order")
if dish_1 in menu:
    bill_total += menu[dish_1] #0+100
    print(f"your dish {dish_1} has been added to your order")
else:
    print(f"ordered dish {dish_1} is not available yet")
another_order = input("do you want to add another dish? (Yes/No)")
if another_order == "Yes":
    dish_2 = input("enter the name of second dish")
    if dish_2 in menu:
        bill_total += menu[dish_2]
        print(f"dish {dish_2} has been added to order")
    else:
        print(f"Ordered dish  {dish_2} is not available!")
    print(f"The total amount of dishes to pasy is {bill_total}")