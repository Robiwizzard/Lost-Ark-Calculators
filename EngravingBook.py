import math

def calc():
    print("Input number of players:")
    players = float(input())
    print("Input engraving book price:")
    price = float(input())
    bid = (price * 0.95 - (price / players)) / 1.1
    print(
    "Bid for maximum profit: " +
    str(math.ceil(bid))
    )
    print(
    "Bid for equal profit: " +
    str(math.ceil((price * 0.95 - (price / players))))
    )
    
calc()