import os

from core import predictors
from training.lib.layers import Delta


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

POLYGON_KEY = "1ijeQ0XUYNl1YMHy6Wl_5zEBtGbkipUP" 
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
			"USD"
		],
		"quote_currencies": [
			"GBP"
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
			"USD"
		],
		"quote_currencies": [
			"GBP"
		]
	},
	{
		"id": "3",
		"name": "Model3",
		"model_path": os.path.join(BASE_DIR, "models/model1.h5"),
		"model_custom_objects": {
			"Delta": Delta
		},
		"look_back": 32,
		"averaging_window": 7,
		"predictor_class": predictors.Predictor3,
		"base_currencies": [
			"USD"
		],
		"quote_currencies": [
			"GBP"
		]
	}

]
