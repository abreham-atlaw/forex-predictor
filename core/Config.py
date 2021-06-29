import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print(BASE_DIR)

POLYGON_KEY = "1ijeQ0XUYNl1YMHy6Wl_5zEBtGbkipUP"
INFORMATION_COLLECTOR_SLEEP_TIME = 60 #IN SECONDS

BASE_CURRENCY = "USD"

CURRENCIES = sorted([
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

MODEL_PATH = os.path.join(BASE_DIR, "model.h5")
MODEL_LOOK_BACK = 50
