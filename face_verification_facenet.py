import os
import numpy as np
from numpy import genfromtxt
import tensorflow as tf

database = {}
model = tf.keras.models.load_model('model')
FRmodel = model

def img_to_encoding(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0) # add a dimension of 1 as first dimension
    embedding = model.predict_on_batch(x_train)
    return embedding / np.linalg.norm(embedding, ord=2)

def trainImages():
    data_path = 'dataset'
    for person_folder in os.listdir(data_path):
        person_folder_path = os.path.join(data_path, person_folder)

        if os.path.isdir(person_folder_path):
            for photo in os.listdir(person_folder_path):
                photo_path = os.path.join(person_folder_path, photo)
                
                # Save Database
                database[person_folder] = img_to_encoding(photo_path, FRmodel)
    print("Image Training Success, Data has been added to database!")

def imageVerification(image_path, identity):
    encoding = img_to_encoding(image_path, model)
    dist = np.linalg.norm(tf.subtract(database[identity], encoding))
    if dist < 0.8:
        print("It's " + str(identity) + ", welcome in!")
        door_open = True
    else:
        print("It's not " + str(identity) + ", please go away")
        door_open = False
    return dist, door_open

def imageReccognition(image_path):
    encoding =  img_to_encoding(image_path, model)
    min_dist = 100
    for (name, db_enc) in database.items():
        dist = np.linalg.norm(tf.subtract(db_enc, encoding))
        if dist < min_dist:
            min_dist = dist
            identity = name
    if min_dist > 0.8:
        print("Not in the database.")
    else:
        print ("it's " + str(identity) + ", the distance is " + str(min_dist))
    return min_dist, identity

def findImageFile(fileName):
    basePath = 'verif_data'
    fileName = os.path.join(basePath, fileName)
    # Check if Have extension
    if os.path.splitext(fileName)[1]:
        # Check if file exist
        if os.path.isfile(fileName):
            return True, fileName
        else:
            return False, fileName
    else:
        extensions = ['.png', '.jpg', '.jpeg']
        for ext in extensions:
            fileNameExtension = fileName + ext
            if os.path.isfile(fileNameExtension):
                return True, fileNameExtension
            else:
                return False, fileNameExtension

def menuInterface():
    isExit = False
    print("Welcome to Image Verification Apps!\n")
    while not isExit:
        print("Menu:")
        print("1. Train Image and Save to Database")
        print("2. Image Verification")
        print("3. Image Recognition")
        print("4. Exit")
        inputMenu = input("Input : ")

        if inputMenu == "1":
            trainImages()
        elif inputMenu == "2":
            if not database:
                print('Please Train Image first')
            else:
                imageFile = input("Enter the image file name on verif_data directory : ")
                identity = input("Enter the image identity : ")
                imageCheck = findImageFile(imageFile)
                if (imageCheck[0]):
                    imageVerification(imageCheck[1], identity)
                else:
                    print("Image not found")
        elif inputMenu == "3":
            if not database:
                print('Please Train Image first')
            else:
                imageFile = input("Enter the image file name on verif_data directory : ")
                imageCheck = findImageFile(imageFile)
                if (imageCheck[0]):
                    imageReccognition(imageCheck[1])
                else:
                    print("Image not found")
        elif inputMenu == "4":
            isExit = True
        else:
            print("Please input the right number.")
        print("")
    else:
        print("Thank You!")

if __name__ == "__main__":
    menuInterface()