import sys
from manager import man_obj


def main():
    if len(sys.argv) != 2:
        raise KeyError("2 arguments should be passed <file_name> <file_history>")
    for transaction in man_obj.history:
        print(transaction)


if __name__ == '__main__':
    main()