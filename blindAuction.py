#blind auction

from ascii_art import gravel, trophy
from os import system

ask_again = True
bidders = {}

def find_winner():
    winner_bid = 0
    winner_name = ""
    for name1 in bidders:
        bid1 = bidders[name1]
        if bid1 >= winner_bid:
            winner_bid = bid1
            winner_name = name1

    print(trophy)
    print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
    
while(ask_again):
    print(gravel)
    name = input("Bidder's name: ")
    bid = int(input("Bidder's bid: $"))
    bidders[name] = bid

    other_bidders = input("Any other bidders?(y/n):\n").lower()
    system('clear')
    if other_bidders == "n":
        ask_again = False
find_winner()



