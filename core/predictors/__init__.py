from .predictors import Predictor, Predictor0, Predictor1, Predictor2, Predictor3
from core import Config


def get_all_predictors() -> list:
	print("[+]Creating Predictors")
	return [
		config["predictor_class"](config) for config in Config.PREDICTORS_CONFIGS
	]
