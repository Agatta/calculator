from flask import Flask, request

from calculator import Calculator

app = Flask(__name__)

OPERATIONS = {
    "sum": Calculator.sum,
    "subtract": Calculator.subtract,
    "multiply": Calculator.multiply,
    "divide": Calculator.divide,
}


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/calculate")
def calculate():
    op = request.args.get("op")
    if op not in OPERATIONS:
        return f"Nieznana operacja: {op}. Dostępne: {', '.join(OPERATIONS)}", 400

    try:
        arg1 = float(request.args["arg1"])
        arg2 = float(request.args["arg2"])
    except KeyError as e:
        return f"Brak parametru: {e.args[0]}", 400
    except ValueError:
        return "Parametry arg1 i arg2 muszą być liczbami", 400

    try:
        result = OPERATIONS[op](Calculator(arg1, arg2))
    except ZeroDivisionError as e:
        return str(e), 400

    # 2.0 -> "2", 2.5 -> "2.5"
    if result == int(result):
        result = int(result)
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
