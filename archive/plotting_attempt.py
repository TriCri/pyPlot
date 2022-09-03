import os
from turtle import clear
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Layout settings for plot
backgroundcolor_graph = 'lightgrey'
backgroundcolor_figure = 'white'

plot_image_name = "plot" # filename of generated image of the plot
image_resultion = 600 # resolution of generated image of the plot [dpi]


# Define Titel & Labels
title_center = "Geschwindigkeitsverlauf"
title_left = "Testreihe 1"
title_right = "Test Nr. 1"
x_label = "t [s]"
y_label = "v [m/s]"

# Data input
# Import data from file

# Data as function
x = np.arange(0, 4, 0.05) # from range, to range, resolution
y = np.sin(x*np.pi) # function

# Data in arrays
# x = [1, 2, 3, 4]
# y = [1, 4, 2, 3]

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.

fig, ax = plt.subplots()
ax.plot(x, y, linestyle = 'dashed', label = 'periodic' )
ax.plot(x, x, linestyle = 'dotted', label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, linestyle = 'dashdot', label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, linestyle = 'solid', label='cubic')  # ... and some more.

ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_title(title_center)
ax.set_title(title_left, loc='left')
ax.set_title(title_right, loc='right')
ax.set_facecolor(backgroundcolor_graph) # set background color
fig.set_facecolor(backgroundcolor_figure) # set background color
ax.legend();  # Add a legend.

# Show plot
plt.show()

# Save results
# Create folder for results if not existing
script_dir = os.path.dirname(__file__)
script_dirCut =  os.path.split(script_dir)
cut = str(script_dirCut[1])
results_dir = script_dir.replace(cut, 'results/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

# save results
fig.savefig(results_dir + plot_image_name, dpi = image_resultion)