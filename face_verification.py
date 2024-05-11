from PIL import Image
import io
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

def processImage(image_path):
    try:
        # Open the image file
        with open(image_path, 'rb') as file:
            img = Image.open(io.BytesIO(file.read()))
            imageVerification(img)
            # print("Image processing complete!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

def imageVerification(image):
    # Load the model
    model = load_model('best_model_pooling.h5')
    
    verif_datagen_augmented = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = verif_datagen_augmented.flow(image, batch_size = 1)

    prediction = model.predict(image)
    # print("Prediction : ", prediction)
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    # print("Class Index : ", predicted_class_index)
    classes = ['Chris Evans', 'Chris Hemsworth', 'Mark Ruffalo', 'Robert Downey Jr', 'Scarlett Johansson']
    predicted_class_name = classes[predicted_class_index]
    print("Predicted Face ======= ", predicted_class_name)

def menuInterface():
    isExit = False
    print("Welcome to Image Verification Apps!\n")
    while not isExit:
        print("Menu:")
        print("1. Image Verification")
        print("2. Exit")
        inputMenu = input("Input : ")

        if inputMenu == "1":
            imagePath = input("Enter the image file name on verif_data directory : ")
            processImage('verif_data/' + imagePath)
        elif inputMenu == "2":
            isExit = True
        else:
            print("Please input the right number.")
        print("")
    else:
        print("Thank You!")

if __name__ == "__main__":
    menuInterface()