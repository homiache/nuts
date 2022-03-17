# coding=utf-8


# This script shows charts for three variants of reverse number functions to make a decision on what variant for float
# numbers is better.


from bokeh.plotting import figure, show
from ntl.task_02_reverse_number.reverse_number import natural_number_reverse


# 12.345 -> 21.543
def point_is_point(number):
    inte, frac = str(number).split(".")
    inte = inte[::-1]
    frac = frac[::-1]
    return float("{}.{}".format(inte, frac))


# 12.345 -> 543.21
def mirror(number):
    return float(str(number)[::-1])


# Create a new plot with a title and axis labels.
p = figure(title="natural_number_reverse", x_axis_label='x', y_axis_label='y', plot_width=1600, plot_height=900)

# Create coordinate lists
x_natural = []
y_natural = []
x_point = []
y_point = []
x_mirror = []
y_mirror = []

# Fit coordinate lists
for each in range(10000):
    x_natural.append(each)
    y_natural.append(natural_number_reverse(each))
    each = each/10
    x_point.append(each)
    y_point.append(point_is_point(each))
    x_mirror.append(each)
    y_mirror.append(mirror(each))

# Add lines to the plot.
p.line(x_natural, y_natural, line_width=2, color="lightblue", legend_label="132 -> 321")
p.line(x_point, y_point, line_width=2, color="purple", legend_label="12.345 -> 21.543")
p.line(x_mirror, y_mirror, line_width=2, color="red", legend_label="12.345 -> 543.21")

# Show the result.
show(p)
