import random
import sys
import time

def main():
    if  len(sys.argv) == 1:
        roll()
    elif len(sys.argv) == 2:
        if int(sys.argv[1]) < 3:
            print("Max number should be minimum 3")
        else:
            custom_roll(int(sys.argv[1]))
    else:
        print("Wrong argument count: you can use this scrips as:\n'python roll.py'\n'python roll.py <max number>'")

def custom_roll(number):
    random.seed(time.process_time())
    print("Rolling...\n...\n")
    time.sleep(2)
    print(random.randint(1,number))

def roll():
    random.seed(time.process_time())
    print("Rolling...\n...\n")
    time.sleep(2)
    print(random.randint(1,6))

if __name__=="__main__":
    main()