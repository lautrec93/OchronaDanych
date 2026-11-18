"""Sejf sekretow i kalkulator - celowo podatna aplikacja do laboratorium 7.

Uruchamiaj wylacznie lokalnie, w kontenerze z pakietu. Dane sa fikcyjne.
"""
import operator
import re
import sqlite3

from flask import Flask, abort, render_template, request

app = Flask(__name__)
BAZA = "file:/dane/sekrety.db?mode=ro"

WZOR_KALK = re.compile(r"\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*")
DZIALANIA = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sekret")
def sekret():
    klucz = request.args.get("klucz", "")
    zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"
    wiersze, blad = [], None
    try:
        with sqlite3.connect(BAZA, uri=True) as db:
            wiersze = db.execute(zapytanie, (klucz,)).fetchall()
    except sqlite3.Error:
        app.logger.exception("Blad zapytania do bazy sekretow")
        blad = "Wystapil blad podczas realizacji zapytania."
    return render_template("sekret.html", klucz=klucz, zapytanie=zapytanie, wiersze=wiersze, blad=blad)


@app.route("/kalkulator")
def kalkulator():
    if "wyrazenie" not in request.args:
        return render_template("kalkulator.html", wyrazenie="", wynik=None)
    wyrazenie = request.args.get("wyrazenie", "")
    if len(wyrazenie) > 100:
        abort(400, "Bledne wyrazenie.")
    dopasowanie = WZOR_KALK.fullmatch(wyrazenie)
    if not dopasowanie:
        abort(400, "Bledne wyrazenie.")
    a, op, b = float(dopasowanie.group(1)), dopasowanie.group(2), float(dopasowanie.group(3))
    if op == "/" and b == 0:
        abort(400, "Dzielenie przez zero.")
    wynik = DZIALANIA[op](a, b)
    if wynik == int(wynik):
        wynik = int(wynik)
    return render_template("kalkulator.html", wyrazenie=wyrazenie, wynik=wynik)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
