import flask
from flask import request

from core.Predictor import Predictor
from core import Config

app = flask.Flask(__name__)
predictor = Predictor()

@app.route("/prediction/", methods=["GET"])
def get_prediction():
	base_currency = request.args.get("base_currency")
	quote_currency = request.args.get("quote_currency")

	if(base_currency != Config.BASE_CURRENCY):
		flask.abort(404)#TODO: NOT IMPLEMENTED YET

	if quote_currency not in Config.CURRENCIES:
		flask.abort(404)

	value = predictor.get_prediction(quote_currency)

	print(f"[+]Request Recieved")
	print(f"[+]Base Currency = {base_currency}")
	print(f"[+]Quote Currency = {quote_currency}")
	print(f"[+]Value = {value}")

	return flask.jsonify({
		"base_currency": base_currency,
		"quote_currency": quote_currency,
		"value": str(value)
		})

