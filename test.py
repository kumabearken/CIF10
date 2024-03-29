# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(32, 32))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 32, 32, 3)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

# load an image and predict the class
def run_example():
	# load the image
	img = load_image('test6.png')
	# load model
	model = load_model('final_model.h5')
	# predict the class
	result = model.predict_classes(img)
	switcher = {
		0:"airplane",
		1:"automobile",
		2:"bird",
		3:"cat",
		4:"deer",
		5:"dog",
		6:"frog",
		7:"horse",
		8:"ship",
		9:"truck"}
	print(switcher.get(result[0]))

# entry point, run the example
run_example()