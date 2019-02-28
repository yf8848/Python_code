#!/bin/env python3

import tensorflow as tf

hello=tf.constant("Hell, Tensorflow.")
sess=tf.Session()
print(sess.run(hello))