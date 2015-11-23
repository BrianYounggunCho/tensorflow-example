

import tensorflow as tf
import numpy as np
import ImageFlow as img_fl
from PIL import Image
#import PIL





#file_dir = tf.train.string_input_producer(['/home/yg/yg-data/Dataset/rgbd-dataset/rgbd1/liv1/'])
file_dir = '/home/yg/yg-data/Dataset/rgbd-dataset/rgbd1/temp/'
image_list = img_fl.read_images(file_dir)

#Image.show(tf.image.encode_jpeg(Image.fromarray (image_list[0])))


