import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
# Read input image
file_path = filedialog.askopenfilename()
img = cv2.imread(file_path)

# Define default values for filter size and order

s =int(input("Filter size (odd number):"))
k =float(input("Highboost filter order:"))
root = tk.Tk()
root.config(bg="grey")
# Define function to update filter and display output image
fig1 = Figure(figsize=(6, 4), dpi=100,facecolor="grey")
ax1 = fig1.add_subplot(111)
fig2 = Figure(figsize=(6, 4), dpi=100,facecolor="grey")
ax2 = fig2.add_subplot(111)
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas2 = FigureCanvasTkAgg(fig2, master=root)
def update_filter():
    global s, k, img
    # Define filter h
    h = np.zeros((s,s))
    h[int((s-1)/2), int((s-1)/2)] = (k+1)
    for i in range(s):
        for j in range(s):
            if not(i==int((s-1)/2) and j==int((s-1)/2)):
                h[i,j] = (-k)/(s*s-1)
    output = cv2.filter2D(img, -1, h)
    # Display input and output images side by side

    ax1.imshow(img, cmap='gray')
    ax1.axis('off')
    ax2.imshow(output, cmap='gray')
    ax2.axis('off')

    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)


# Define function to increase filter size
def increase_s():
    global s
    s += 2
    update_filter()
    changelabel()

# Define function to decrease filter size
def decrease_s():
    global s
    if s > 3:
        s -= 2
    else :
        s-=2
        update_filter()
        changelabel()

# Define function to increase filter order
def increase_k():
    global k
    k += 0.5
    update_filter()
    changelabel()

# Define function to decrease filter order
def decrease_k():
    global k
    if k > 0.5:
        k -= 0.5
    else:
        k -= 0.5
        update_filter()
        changelabel()

def select_image():
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    update_filter()

# Create tkinter window


# Create buttons to adjust filter size and order
s_frame = tk.Frame(root)
s_frame.pack(side=tk.TOP)
s_frame.config(background="grey")
s_label = tk.Label(s_frame, text="Filter size (odd number):"+str(s),fg="white",bg="black")
s_label.pack()
s_plus_button = tk.Button(s_frame, text="+", command=increase_s, fg="red", bg="black", width=7,font="Verdana 15")
s_plus_button.pack(side=tk.RIGHT)
s_minus_button = tk.Button(s_frame, text="-", command=decrease_s, fg="blue", bg="black", width=7,font="Verdana 15")
s_minus_button.pack(side=tk.LEFT)

k_frame = tk.Frame(root)
k_frame.pack(side=tk.BOTTOM)
k_frame.config(background="grey")
k_label = tk.Label(k_frame, text="Highboost filter order:"+str(k),fg="white",bg="black")
k_label.pack()
k_plus_button = tk.Button(k_frame, text="+", command=increase_k, fg="red", bg="black", width=7,font="Verdana 15")
k_plus_button.pack(side=tk.RIGHT)
k_minus_button = tk.Button(k_frame, text="-", command=decrease_k, fg="blue", bg="black", width=7,font="Verdana 15")
k_minus_button.pack(side=tk.LEFT)
def changelabel():
    s_label.config(text="Filter size (odd number):"+str(s))
    k_label.config(text="Highboost filter order:"+str(k))
# Display initial output image
update_filter()

# Start tkinter main loop
root.mainloop()