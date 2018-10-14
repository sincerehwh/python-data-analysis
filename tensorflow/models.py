
import tensorflow as tf 


# Y = W*x + b
def regression(x):
	W = tf.Varible(tf.zero([784,10]), name="W")
	b = tf.Varible(tf.zeros([10], name='b'))
	y = tf.softmax(tf.matmul(x,W) + b)

	return y, [W,b]



