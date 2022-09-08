import os
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
y_label_left = r'v(t) [$\frac{m}{s}$]'
y_label_right = r'a(t) [$\frac{m}{s^2}$]'
# Data as function
# x = np.arange(0, 4, 0.05) # from range, to range, resolution
# y = np.sin(x*np.pi) # function

x = np.arange(0, 2, 0.01) # from range, to range, resolution
y = x**2 # function

# Data in arrays
# x = [1, 2, 3, 4]
# y = [1, 4, 2, 3]

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.

fig, ax = plt.subplots(constrained_layout = True)
ax.plot(x, y, linestyle = 'solid', label = 'Geschwindigkeit ' + y_label_left)
ax.plot(x, (y/x), linestyle = 'dashed', label = 'Beschleunigung ' + y_label_right)


# #define functions for seoundary y-axis
# def val1(y):
#     return y
 
# def val2(y):
#     return y
 
# secax = ax.secondary_yaxis('right', functions =(val1, val2))

ax.set_xlabel(x_label)
# ax.set_ylabel(ylabel = y_label_left)
# secax.set_ylabel(y_label_right)
ax.set_title(title_center)
ax.set_title(title_left, loc='left')
ax.set_title(title_right, loc='right')
ax.set_facecolor(backgroundcolor_graph) # set background color
fig.set_facecolor(backgroundcolor_figure) # set background color
ax.legend();  # add a legend

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