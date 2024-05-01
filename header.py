from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.optimizers import Adam

def create_new_model(lr : float):
    opt = Adam(lr)
    model = Sequential()
    model.add(Dense(8,input_dim=2,activation="relu"))
    model.add(Dense(1,activation="sigmoid"))
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    return model

if __name__ == "__main__":
    print("This file is compiled without any errors")