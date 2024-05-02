from keras.models import Sequential, load_model
from os import system
from time import sleep
from numpy import array

appropriate_inputs = [
    [[0,0]],
    [[0,1]],
    [[1,0]],
    [[1,1]]
]

model : Sequential
model = load_model("model.h5")
while True:
    system("cls")
    print("Put the inputs like shown below: \nnumber number\n0 0")
    try:
        # Getting the inputs
        x = input("Inputs: ")

        # Normalizing the input
        x_list = x.split(" ")
        x = [list(map(int,x_list))]
        
        # Checking if the input is appropriate
        if x not in appropriate_inputs:
            raise ValueError
        
        # Converting input to numpy array
        x = array(x)
        print("Input array: ", x)
        
        # Predicting
        y = model.predict(x)
        print("Prediction: \n", round(y[0][0]))

    except ValueError:
        print("Inappropriate inputs!")
    except:
        print("Error!")
    finally:
        sleep(1)