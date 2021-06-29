from polygon import RESTClient
from requests import HTTPError

import Config

import datetime
import time


class InformationCollector:
	class TimeSpan:
		MINUTE = "minute"
		HOUR = "hour"
		DAY = "day"

	def __init__(self):
		self.client = RESTClient(Config.POLYGON_KEY)
		self.kwargs_converter = {"day": "days", "hour": "hours", "minute": "minutes"}

	#TODO: FIND A BETTER OF IMPLEMENTING THIS LIKE USING DECORATORS
	def network_call(self, call_function, *args, **kwargs):
		try:
			return call_function(*args, **kwargs)
		except HTTPError:
			print("Error Sleeping ...")
			time.sleep(Config.INFORMATION_COLLECTOR_SLEEP_TIME)
			return self.network_call(call_function, *args, **kwargs)


	def get_exchanges(self, time_units, base_currency, quote_currency, time_span: str = TimeSpan.DAY) -> list:
		if time_span not in list(self.kwargs_converter.keys()):
			raise Exception(f"Invalid timespan {time_span}")

		print(f"Getting Aggregates")
		response = self.network_call(
			self.client.forex_currencies_aggregates,
			ticker=f"C:{base_currency}{quote_currency}",
			multiplier=1,
			timespan=time_span,
			from_=datetime.date.today() - datetime.timedelta(**{self.kwargs_converter[time_span]: time_units}),
			to=datetime.date.today()
		)
		"""response = self.client.forex_currencies_aggregates(
			ticker=f"C:{base_currency}{quote_currency}",
			multiplier=1,
			timespan=time_span,
			from_=datetime.date.today() - datetime.timedelta(**{self.kwargs_converter[time_span]: time_units}),
			to=datetime.date.today()
		)
		"""

		original_time_units = time_units

		while(len(response.results) < original_time_units):
			time_units += original_time_units - len(response.results)
			print("Getting Aggregates")

			response = self.network_call(
				self.client.forex_currencies_aggregates,
				ticker=f"C:{base_currency}{quote_currency}",
				multiplier=1,
				timespan=time_span,
				from_=datetime.date.today() - datetime.timedelta(**{self.kwargs_converter[time_span]: time_units}),
				to=datetime.date.today()
			)

			"""response = self.client.forex_currencies_aggregates(
				ticker=f"C:{base_currency}{quote_currency}",
				multiplier=1,
				timespan=time_span,
				from_=datetime.date.today() - datetime.timedelta(**{self.kwargs_converter[time_span]: time_units}),
				to=datetime.date.today()
			)"""

		return [bar["c"] for bar in response.results]

	def get_exchange_margins(self, time_units, base_currency, quote_currency, time_span: str = TimeSpan.DAY) -> list:
		rates = self.get_exchanges(time_units+1, base_currency, quote_currency, time_span=time_span)

		return [
			(rates[i+1] - rates[i])/rates[i]
			for i in range(len(rates)-1)
		]

