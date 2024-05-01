from header import *
from keras.models import save_model
import numpy as np

with open("dataset.txt","r") as file:
    readlines = [x.replace("\n","") for x in file.readlines()]
    #print(readlines)


# The types in data are string. Not a number. I have to extract numbers
data = np.array(readlines)

# Extracting inputs
inputs = []
for i in range(4):
    inputs.append([int(data[i][0]),int(data[i][2])])
inputs = np.array(inputs)
print("Inputs\n", inputs)

# Extracting output
output = []
for i in range(4):
    output.append(int(data[i][4]))
output = np.array(output)
output = np.reshape(output,(4,1))
print("Output\n", output)

# Creating the model
model = create_new_model(lr=0.01)
model.fit(inputs,output,batch_size=1,epochs=60,validation_data=(inputs,output))
print(model.evaluate)
save_model(model,"model.h5")