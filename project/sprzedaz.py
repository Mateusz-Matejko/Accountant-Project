import sys
from manager import man_obj


def main(action, product_id, sell_price, sell_qty, file):
    # if len(sys.argv) != 5:
    #     raise KeyError("5 arguments should be passed <file_name> <file_history> <product_id> <price> <qty>")
    # action = "sprzedaz"
    # file = sys.argv[1]
    # product_id = sys.argv[2]
    # sell_price = int(sys.argv[3])
    # sell_qty = int(sys.argv[4])
    man_obj.get_history(file)
    man_obj.execute(action=action, product_id=product_id, sell_price=sell_price, sell_qty=sell_qty)
    man_obj.write_history(file=file)
    # return f"{sell_qty}pcs of \"{product_id}\" successfully sold. Current stock:"


if __name__ == '__main__':
    main()