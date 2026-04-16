from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    document.getElementById('output').innerHTML = " "

    boxes =  np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    sold_boxes = np.array([7, 7, 2, 5, 3, 0, 0])
    sample_graph = plt.plot(boxes, sold_boxes)
    plt.show(sample_graph)

    plt.title("Library Books Checked Out")
    plt.xlabel('Days')
    plt.ylabel('Number of Books')

#pip3 install numpy
#pip install numpy


