import random
import sys
import time

def main():
    if  len(sys.argv) == 1:
        toss()
    else:
        print("Wrong argument count: you can use this scrips as:\n'python toss.py'\n")
def toss():
    random.seed(time.process_time())
    print("Tossing...\n...\n")
    time.sleep(2)
    coin = ["Heads","Tails"]
    print(random.choice(coin))

if __name__=="__main__":
    main()