import tensorflow as tf
from keras.layers import Layer


class FloatEmbedding(Layer):

	def __init__(self, units, **kwargs):
		self.units = units
		super(FloatEmbedding, self).__init__(**kwargs)

	def build(self, input_shape):
		if len(input_shape) != 3:
			raise Exception(f"Expected rank 3 but got input_shape={input_shape}")
		self.w = self.add_weight(
			shape=(input_shape[2], self.units),
			initializer="random_normal",
			trainable=True
		)
		self.b = self.add_weight(
			shape=(self.units,),
			initializer="random_normal",
			trainable=True
		)

	def call(self, inputs, **kwargs):
		return tf.matmul(inputs, self.w) + self.b


class PositionalEncoding(Layer):

	def __init__(self, **kwargs):
		super(PositionalEncoding, self).__init__(**kwargs)

	def call(self, inputs, **kwargs):
		# inputs.shape[1] must be an even number
		r = tf.cast(tf.reshape(tf.range(inputs.shape[1]), (-1, 1)), tf.float64) / (
				10000 ** (2 * tf.reshape(tf.range(inputs.shape[2]), (1, -1)) / inputs.shape[2]))
		return tf.cast(inputs, tf.float64) + tf.reshape(tf.concat([tf.sin(r[::2]), tf.cos(r[1::2])], axis=1), (inputs.shape[1], inputs.shape[2]))

