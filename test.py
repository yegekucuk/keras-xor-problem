from keras.models import Sequential, load_model
from os import system
from time import sleep
from numpy import array

model : Sequential
model = load_model("model.h5")
while True:
    system("cls")
    print("Put the inputs like shown below: \nnumber number\n0 0")
    try:
        x = input("Inputs: ")
        # Normalizing the input
        x = [[int(x[0]),int(x[2])]]
        x = array(x)
        print(x)
        # Predicting
        y = model.predict(x)
        print("Prediction: \n", round(y[0][0]))
    except:
        print("Error! Try again!")
    finally:
        sleep(1)