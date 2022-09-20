from flask import Flask, render_template, request, redirect
from konto import main as konto_main
from magazyn import main as magazyn_main
from saldo import main as saldo_main
from zakup import main as zakup_main
from sprzedaz import main as sprzedaz_main
from przeglad import main as przeglad_main


app = Flask(__name__)

file = "history.txt"


@app.route("/")
def home():
    return render_template("home.html", account=konto_main(file), stock=magazyn_main(file))


@app.route("/action", methods=["GET", "POST"])
def check():
    if request.form.get("method") == "saldo":
        action = request.form.get("method")
        change = request.form.get("change")
        change = int(change)
        comment = request.form.get("comment")
        result = saldo_main(action=action, change=change, comment=comment, file=file)
        if result:
            return render_template("error.html", msg=result)
        return redirect("/")
    elif request.form.get("method") == "zakup":
        action = request.form.get("method")
        product_id = request.form.get("product_id")
        buy_price = request.form.get("buy_price")
        buy_qty = request.form.get("buy_qty")
        buy_price, buy_qty = int(buy_price), int(buy_qty)
        result = zakup_main(action=action, product_id=product_id, buy_price=buy_price, buy_qty=buy_qty, file=file)
        if result:
            return render_template("error.html", msg=result)
        return redirect("/")
    elif request.form.get("method") == "sprzedaz":
        action = request.form.get("method")
        product_id = request.form.get("product_id")
        sell_price = request.form.get("sell_price")
        sell_qty = request.form.get("sell_qty")
        sell_price, sell_qty = int(sell_price), int(sell_qty)
        result = sprzedaz_main(action=action, product_id=product_id, sell_price=sell_price, sell_qty=sell_qty, file=file)
        if result:
            return render_template("error.html", msg=result)
        return redirect("/")
    return render_template("error.html", msg="check function error")


def get_history(history, start=None, finish=None):
    history_list = []
    for action in history:
        for details in action:
            history_list.append(details)
    history_list.append("stop")
    if not start or not finish:
        return history_list
    final_list = history_list[start:finish]
    return final_list


@app.route("/history/<start>/<finish>")
def history_start_finish(start=0, finish=0):
    start, finish = int(start), int(finish)
    if start and finish:
        history_list_index = get_history(przeglad_main(file), start=start, finish=finish)
        return render_template("history.html", history=history_list_index)


@app.route("/history/")
def history():
    return render_template("history.html", history=get_history(przeglad_main(file)))
