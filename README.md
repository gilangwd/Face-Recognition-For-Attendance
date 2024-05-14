# Face Verification and Recognition
  
## Getting Started
This Project contains an answer for Synapsis technical test.

## How to Use
1. Open terminal, change directory to this project.
```sh
    cd ..\Face-Recognition-For-Attendance
```
2. Run python file 'face_verification_facenet.py'.
```sh
    python face_verification_facenet.py
```
3. You must have all the library installed to be able to run the application.
4. There is 4 menu, 1 for training the image and save it to database, 2 for image verification, 3 for image recognition and 4 for exit the application.
5. First we need to train the image and save it to database before trying to do image verification or recognition.
6. Input number 1, and the application will train all image in the dataset folder and name it by its sub-folder name then save it into a database.
7. I gave 5 example image for training, if you wish to add more image, please create a new folder put the image inside the folder and name the folder by the person name. Image extension can be .png, .jpg or .jpeg.
8. After Data Training Success the data is saved into a database and now you can use the application to verify and recognize image.
9. Input number 2 to verify image for attendance.
10. Instead of camera, I will simplify this to verify the image on folder verif_data. Input the image name that you want to verify, you can include image extension or not it doesn't matter. Then input the identity of this image. Press enter to continue.
11. If the image is exist in the verif_data, the application will check if it's on the database or not and then verify it with your input identity. If they are match then the door is open, you can enter the office.
12. Input number 3 to recognize image for checking model accuracy.
13. Input the image name that you want the application to recognize who is it. Then press enter to continue.
14. The application will then check the database, if it can recognize the image, it will give you the image/person identity.
15. But if it not found in the database, the application will return "Not in Database".
16. You can try to register it first, just put the image in the dataset folder. Don't forget to create a sub-folder named by its identity or the application will ignore the image.