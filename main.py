import tkinter as tk
from keras.models import Sequential, load_model
from numpy import array

def calculate_xor():
    global input1
    global input2
    global model
    global appropriate_inputs

    try:
        # Get inputs
        x1 = int(input1.get())
        x2 = int(input2.get())
        x = [[x1,x2]]

        # Checking if the input is appropriate
        if x not in appropriate_inputs:
            raise ValueError
        
        # Converting input to numpy array
        x = array(x)
        
        # Get predict
        y = model.predict(x)
        pred = round(y[0][0])

        # Display result
        result_label.config(text="Result: %s" %(str(pred)))

    except ValueError:
        # Display error
        result_label.config(text="Result: Inappropriate inputs!")
    except:
        # Display error
        result_label.config(text="Result: Error!")

appropriate_inputs = [
    [[0,0]],
    [[0,1]],
    [[1,0]],
    [[1,1]]
]

# Load the model
model : Sequential
model = load_model("model.h5")

# Create the main window
root = tk.Tk()
root.title("Keras XOR Problem")

# Set the window resolution
root.geometry('400x200')

# Create a header label
header_label = tk.Label(root, text="Keras XOR Problem", font=('Helvetica', 16))
header_label.pack(pady=10)

# Create frame for inputs and button
frame = tk.Frame(root)
frame.pack(pady=10)

# Number input 1
input1 = tk.Entry(frame, width=10)
input1.pack(side=tk.LEFT, padx=5)

# Number input 2
input2 = tk.Entry(frame, width=10)
input2.pack(side=tk.LEFT, padx=5)

# Calculate button
calculate_btn = tk.Button(frame, text="Calculate", command=calculate_xor)
calculate_btn.pack(side=tk.LEFT, padx=10)

# Result label
result_label = tk.Label(root, text="Enter values and press calculate.")
result_label.pack(pady=20)

# Start the GUI
root.mainloop()