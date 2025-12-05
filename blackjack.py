import random

from db import read_money,write_money
# card creation using list of lists
suits=["Hearts","Diamonds","Clubs","Spades"]
ranks= ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
values = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def create_deck():
    # create and return shuffled  52 -card deck
    deck=[]
    for suit in suits:
        for i,rank in enumerate(ranks):
            value = values[i]
            deck.append((suit,rank,value))

    random.shuffle(deck)
    return deck

def calculate_hand_values(hand):
    # return  value of a hand
    total=sum(card[2] for card in hand)

    ace= sum(1 for card in hand if card[1] =="Ace")


    while total >21 and ace>0:
        total-=10
        ace-=1


    return total

def print_hand( title,hand):
    print(title)

    for card in hand:
        print(f"{card[1]} of {card[0]}")



#
"""def buy_money(money):
    # ask user if they want to buy more money to play the game
    print(f"your money is below the minimum bet ($5) .")
    choice=input("Do you want to buy  more money? (y/n)")
    if choice.lower()=="y":
        while True:
            try:
                amount=int(input("How much money would you like to buy ($): "))
                if amount <=0:
                    print("Sorry, you don't have enough money enter a positive amount :")
                    continue
                return money + amount
            except ValueError:
                print("enter a valid number :")
    return money"""









def main():
    #display title
    print(" BlackJACK!")
    print("Blackjack payout is 3:2")

    #read data from file
    #  money=read_money()
    #money=3
    """  while True:
        print(f"\nMoney:  {money}")
        #handle  insufficient funds
        if money < 5:
            money=buy_money(money)
        print(f"\nMoney:  {money}")
        if money < 5:
            print("Sorry, you don't have enough money  to continue. Good buy :")
            break

     # handle insufficient funds
     while True:
       try:
            bet=float(input("Bet amount (5-1000): "))
            if bet <= 5:
                print("minimum bet is 5.")
            elif bet > 1000:
                print("maximum bet is 1000 .")
            elif bet > money:
                print("you cannot bet more than you have")
            else:
                break
       except ValueError:
           print("enter a valid numeric bet:")"""

    deck = create_deck()
    #print(deck)

    #draw two cards
    player=[deck.pop(), deck.pop()]
    dealer=[deck.pop(), deck.pop()]
   # print(player)
   # print(dealer)

    total=calculate_hand_values(player)
   # print(f"\n player Hand value:{total}")
    print()
    total = calculate_hand_values(dealer)
    #print(f"\n dealer Hand value:{total}")

    print("\nDEALER' SHOW CARD :")
    print(f"{dealer[0][1]} of {dealer[0][0]}\n ")

    print_hand("YOUR CARDS :",player)











if __name__ == '__main__':
    main()