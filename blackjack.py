from db import read_money,write_money

suits=["Hearts","Diamonds","Clubs","Spades"]
ranks= ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
values = [2,3,4,5,6,7,8,9,10,11]

#
def buy_money(money):
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
    return money









def main():
    #display title
    print(" BlackJACK!")
    print("Blackjack payout is 3:2")

    #read data from file
    money=read_money()
    #money=3
    while True:
        print(f"\nMoney:  {money}")
        #handle  insufficient funds
        if money < 5:
            money=buy_money(money)
        print(f"\nMoney:  {money}")
        if money < 5:
            print("Sorry, you don't have enough money  to continue. Good buy :")
            break







if __name__ == '__main__':
    main()