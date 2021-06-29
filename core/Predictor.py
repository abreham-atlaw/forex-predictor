from tensorflow import keras
import numpy as np

import Config
from InformationCollector import InformationCollector

class Predictor:

	def __init__(self, model_path=Config.MODEL_PATH):
		self.model: keras.Sequential = keras.models.load_model(model_path)
		self.information_collector = InformationCollector()

	#TODO IMPLEMENT DYNAMIC BASE CURRENCY
	def get_prediction(self, quote_currency) -> float:
		if quote_currency not in Config.CURRENCIES:
			raise Exception(f"Invalid Currency {quote_currency}")

		margins = self.information_collector.get_exchange_margins(
			time_units=Config.MODEL_LOOK_BACK,
			base_currency=Config.BASE_CURRENCY,
			quote_currency=quote_currency
		)

		country_encoding = [0]*len(Config.CURRENCIES)
		country_encoding[Config.CURRENCIES.index(quote_currency)] = 1
		
		features = np.array(list(margins)+list(country_encoding)).reshape((1, 67))

		return self.model.predict(features).reshape(1)[0]



