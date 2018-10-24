def cheese_and_chrackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} crackers!")
    print("Man that's enough for a party.")
    print("Get a blanket.\n")

print("We can just give the function numbers directly!")
cheese_and_chrackers(20,30)

print("OR,we can use variables from mour scirpt:")
amount_of_cheese = 20
boxes_of_crackers = 50

cheese_and_chrackers(amount_of_cheese,boxes_of_crackers)


print("We can even do math inside too:")
cheese_and_chrackers(10 + 20, 5 + 6)

print("And we can combin the tow,variables and math:")
cheese_and_chrackers(amount_of_cheese+100,boxes_of_crackers + 200)
