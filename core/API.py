import flask
from flask import request

from core import Config
from core.exceptions import PredictorNotFoundException, CurrencyNotFoundException
from core.predictors import get_all_predictors, Predictor


app = flask.Flask(__name__)
predictors = get_all_predictors()


def get_predictor_by_id(id: str) -> Predictor:

	for predictor in predictors:
		if predictor.config["id"] == id:
			return predictor

	raise PredictorNotFoundException


@app.route("/prediction/", methods=["GET"])
def get_prediction():
	print(f"\n\n[+]Request Recieved")

	base_currency = request.args.get("base_currency")
	quote_currency = request.args.get("quote_currency")
	predictor_id = request.args.get("model_id")
	try:
		predictor = get_predictor_by_id(predictor_id)
	except PredictorNotFoundException:
		flask.abort(404)

	print(f"[+]Base Currency = {base_currency}")
	print(f"[+]Quote Currency = {quote_currency}")
	print(f"[+]Predictor = {predictor.config['name']}(id: {predictor_id})")

	try:
		value = predictor.get_prediction(base_currency, quote_currency)

	except CurrencyNotFoundException:
		flask.abort(404)
		return

	print(f"[+]Value = {value}")

	return flask.jsonify({
		"base_currency": base_currency,
		"quote_currency": quote_currency,
		"value": str(value)
		})

