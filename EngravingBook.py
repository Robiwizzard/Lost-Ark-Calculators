import math

def calc():
    print("Input number of players:")
    players = float(input())
    print("Input engraving book price:")
    price = float(input()) * 0.95
    bid =  (price - (price - ((players - 1) * (price / players)))) / 1.1
    print(
    "Bid for maximum profit: " +
    str(math.ceil(bid))
    )
    print(
    "Bid for equal profit: " +
    str(math.ceil(price - (price - ((players - 1) * (price / players)))))
    )
    
calc()