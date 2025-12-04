#db.py
#set file name into a variable
filename="money.txt"
def read_money():
    # read  data from file
    try:

        with open(filename, 'r') as file:
            money = file.readlines()
        return money
    except FileNotFoundError:
        print("File not found")


def write_money(money, filename):
   # write data to file
   try:
        with open(filename, 'w') as file:
            for line in money:
                file.write(line)
   except FileNotFoundError:
       print("File not found")

