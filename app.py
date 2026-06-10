from flask import Flask, render_template, request

app = Flask(__name__)

balance = 0
account = ""

@app.route("/", methods=["GET", "POST"])
def home():
    global balance,account

    if request.method == "POST":
        account = request.form["account"]
        amount = float(request.form["amount"])

        if request.form["action"] == "credit":
            balance += amount

        elif request.form["action"] == "debit":
            balance -= amount

    return render_template("index.html", balance=balance,account = account)

# app.run(debug=True)
app.run(host="0.0.0.0",port=5000,debug=True)