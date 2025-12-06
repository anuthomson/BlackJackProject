#db.py
import csv
#set file name into a variable
filename="money.txt"
def read_money(filename="money.txt"):
    # read  data from file
    try:

        with open(filename, 'r',newline="") as file:
            reader = csv.reader(file)
            raw=next(reader)
            return float(raw[0])
    except FileNotFoundError:
        #create a default file with 100.0 starting money
        write_money(100.0,filename="money.txt")
        return 100.0
    except Exception:
        print("\nError reading money file Resetting balance to 100.0")
        write_money(100.0,filename="money.txt")
        return 100.0

def write_money(money, filename="money.txt"):
   # write data to file
   try:
        with open(filename, 'w',newline="") as file:
            writer = csv.writer(file)
            writer.writerow([round(money,2)])

   except FileNotFoundError:
       print("File not found")

