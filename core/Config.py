import os

from core import predictors
from training.lib.layers import Delta


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

POLYGON_KEY = "123456789098765432" 
INFORMATION_COLLECTOR_SLEEP_TIME = 60 #IN SECONDS

PREDICTORS_CONFIGS = [
	{
		"id": "0",
		"name": "Model0",
		"model_path": os.path.join(BASE_DIR, "models/model0.h5"),
		"model_custom_objects": {},
		"look_back": 50,
		"predictor_class": predictors.Predictor0,
		"base_currencies": [
			"USD",
		],
		"quote_currencies": sorted([
			"AUD",  # Australia
			"BRL",  # Brazil
			"CAD",  # Canada
			"CNH",  # Chine
			"DKK",  # Denmark
			"EUR",  # Euro
			"HKD",  # Hong Kong
			"JPY",  # Japan
			"NZD",  # New Zealand
			"NOK",  # Norway
			"SGD",  # Singapore
			"ZAR",  # South Africa
			"KRW",  # South Korea
			"SEK",  # Sweden
			"CHF",  # Switzerland
			"TWD",  # Taiwan
			"GBP"   # United Kingdom
		])
	},
	{
		"id": "1",
		"name": "Model1",
		"model_path": os.path.join(BASE_DIR, "models/model1.h5"),
		"model_custom_objects": {
			"Delta": Delta
		},
		"look_back": 32,
		"predictor_class": predictors.Predictor1,
		"base_currencies": [
			"GBP"
		],
		"quote_currencies": [
			"USD"
		]
	},
	{
		"id": "2",
		"name": "Model2",
		"model_path": os.path.join(BASE_DIR, "models/model1.h5"),
		"model_custom_objects": {
			"Delta": Delta
		},
		"look_back": 32,
		"predictor_class": predictors.Predictor2,
		"base_currencies": [
			"GBP"
		],
		"quote_currencies": [
			"USD"
		]
	},

]
