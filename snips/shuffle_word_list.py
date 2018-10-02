import argparse
from random import randint
from time import sleep

# Setup our arguments
parser = argparse.ArgumentParser()
parser.add_argument("--word", "-w", help="Word to shuffle",
                    type=str, required=True)
args = parser.parse_args()


def shuffle(word):
    shuffled = []
    mylist = [c for c in word]
    while len(mylist) > 0:
        myindex = randint(0, len(mylist) - 1)
        shuffled.append(mylist[myindex])
        del mylist[myindex]

    return "".join(shuffled)


while True:
    print(shuffle(args.word))
    sleep(1)
