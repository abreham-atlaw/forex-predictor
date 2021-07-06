from tensorflow import keras
import numpy as np

from abc import ABC, abstractmethod

from core.InformationCollector import InformationCollector
from core.exceptions import CurrencyNotFoundException


class Predictor(ABC):

	def __init__(self, config):
		self.config = config
		self.information_collector = InformationCollector()

	def get_prediction(self, base_currency, quote_currency) -> float:
		if quote_currency not in self.config["quote_currencies"]:
			raise CurrencyNotFoundException(f"Invalid Currency {quote_currency}")
		if base_currency not in self.config["base_currencies"]:
			raise CurrencyNotFoundException(f"Invalid Currency {base_currency}")

		return self.predict(base_currency, quote_currency)

	@abstractmethod
	def predict(self, base_currency, quote_currency) -> float:
		pass


class Predictor0(Predictor):

	def __init__(self, config):
		super(Predictor0, self).__init__(config)
		self.model: keras.Model = keras.models.load_model(config["model_path"], custom_objects=config["model_custom_objects"])

	def predict(self, base_currency, quote_currency) -> float:
		margins = self.information_collector.get_exchange_margins(
			time_units=self.config["look_back"],
			base_currency=base_currency,
			quote_currency=quote_currency
		)

		country_encoding = [0] * len(self.config["quote_currencies"])
		country_encoding[self.config["quote_currencies"].index(quote_currency)] = 1

		features = np.array(list(margins) + list(country_encoding)).reshape((1, 67))

		return self.model.predict(features).reshape((1,))[0]


class Predictor1(Predictor):

	def __init__(self, config):
		super(Predictor1, self).__init__(config)
		self.model = keras.models.load_model(config["model_path"], custom_objects=config["model_custom_objects"])

	def predict(self, base_currency, quote_currency) -> float:
		exchanges = self.information_collector.get_exchanges(
			time_units=self.config["look_back"] + 1,
			base_currency=base_currency,
			quote_currency=quote_currency
		).reshape((-1, 1))

		return (self.model.predict(exchanges[:-1].reshape((1, -1, 1))) - self.model.predict(exchanges[1:].reshape((1, -1, 1)))).reshape((1,))[0]


class Predictor2(Predictor):

	def __init__(self, config):
		super(Predictor2, self).__init__(config)
		self.model = keras.models.load_model(config["model_path"], custom_objects=config["model_custom_objects"])

	def predict(self, base_currency, quote_currency) -> float:
		exchanges = self.information_collector.get_exchanges(
			time_units=self.config["look_back"],
			base_currency=base_currency,
			quote_currency=quote_currency
		).reshape((-1, 1))

		return self.model.predict(exchanges.reshape((1, -1, 1))).reshape((1,))[0] - exchanges.reshape((-1,))[-1]
