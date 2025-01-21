from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-item/<item_name>")
def get_orders(item_name):
    order_data = {
        "item_name": item_name,
        "username": "yo_yo",
        "price": "10p"
    }

    extra = request.args.get("extra")
    if extra:
        order_data["extra"] = extra

        return jsonify(order_data), 200



if __name__ == "__main__":
    app.run(debug=True)