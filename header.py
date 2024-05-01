from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.optimizers import Adam

def create_new_model(lr : float):
    opt = Adam(lr)
    model = Sequential()
    model.add(Flatten(input_shape=(2,1)))
    model.add(Dense(2,activation="sigmoid"))
    model.add(Dense(3,activation="sigmoid"))
    model.add(Dense(1,activation="sigmoid"))
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    return model

if __name__ == "__main__":
    print("This file is compiled without any errors")