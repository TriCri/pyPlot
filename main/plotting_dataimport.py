import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Define import file

name_importfile = r'C:\Users\chris\Repos\pyPlot\main\data.txt'
delimiter_sign = '\t'

# Layout settings for plot
backgroundcolor_graph = 'lightgrey'
backgroundcolor_figure = 'white'
plot_image_name = "plot" # filename of generated image of the plot
image_resultion = 600 # resolution of generated image of the plot [dpi]


# Define Titel & Labels
title_center = "Pathplot Druckbehälter"
title_left = ""
title_right = ""
x_label = r'Arc Length [$mm$]'
y_label_left = r'Equivalent Von Mises Stress [$\frac{N}{mm^2}$]'
y_label_right = r'a(t) [$\frac{m}{s^2}$]'

# Data as function
# x = np.arange(0, 4, 0.05) # from range, to range, resolution
# y = np.sin(x*np.pi) # function

# x = np.arange(0, 2, 0.05) # from range, to range, resolution
# y = x**2 # function

# Data in arrays
# x = [1, 2, 3, 4]
# y = [1, 4, 2, 3]

# # Import data from file
# array1 = []
# array2 = []

# with open(name_importfile, 'r') as f:
#     for line in f.readlines():
#         l = line.strip().split(delimiter_sign)
#         array1 = l[0]
#         array2 = l[1]
my_data = np.loadtxt(name_importfile, delimiter="\t", skiprows = 2, unpack=True)
list1, list2, list3, list4, list5 = my_data[::] #unpack your array
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.

fig, ax = plt.subplots(constrained_layout = False)
ax.plot(list2, list3, linestyle = 'solid', label = 'Top Layer')
ax.plot(list2, list4, linestyle = 'solid', label = 'Middle Layer')
ax.plot(list2, list5, linestyle = 'solid', label = 'Bottom Layer')
# ax.plot(x, y, linestyle = 'solid', label = 'Geschwindigkeit ' + y_label_left)
# ax.plot(x, (y/x), linestyle = 'dashed', label = 'Beschleunigung ' + y_label_right)


# #define functions for seoundary y-axis
# def val1(y):
#     return y
 
# def val2(y):
#     return y
 
# secax = ax.secondary_yaxis('right', functions =(val1, val2))

ax.set_xlabel(x_label)
ax.set_ylabel(y_label_left)
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