import tensorflow as tf

def write(memory_matrix, write_weighting, erase_vector, write_vector):

    erase_vector = tf.transpose(erase_vector)
    write_vector = tf.transpose(write_vector)
    big_e = tf.ones(tf.shape(memory_matrix).numpy())

    memory_matrix = tf.math.multiply(memory_matrix, tf.math.add(tf.math.subtract(big_e, tf.linalg.matmul(write_weighting, erase_vector)), tf.linalg.matmul(write_weighting, write_vector)))
    return memory_matrix
