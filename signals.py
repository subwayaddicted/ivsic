from math import sin
from numpy import pi, arange, sin as nsin
from numpy.random import rand
from scipy.fft import fft
from plot import Plot
from arguments import Arguments
import os


class Signals:
    def __init__(self, arguments: Arguments):
        self.formula = None
        self.arguments = arguments
        if not os.path.exists('images'):
            os.makedirs('images')

    # Actually looks like: 2*sin(3*pi*t) + 3*sin(4*pi*t)
    def calculate_signal(self, t):
        return (self.arguments.before_first_sin * sin(self.arguments.inside_first_sin * pi * t)) + (
                self.arguments.before_second_sin * sin(self.arguments.inside_second_sin * pi * t))

    def harmonic(self):
        t_array = arange(0, 10, 0.1)
        y_array = []

        for t in t_array:
            a = self.calculate_signal(t)
            y_array.append(a)

        fourie_y = fft(y_array)
        y = abs(fourie_y)

        plain_x = arange(0, 10, 0.1)
        plain_y = nsin(plain_x)

        plot = Plot('harmonic')

        plot.make_fig()
        plot.add_plot(t_array, y_array)
        plot.add_plot(plain_x, plain_y)
        plot.save(1)
        plot.clear()

        plot.make_fig()
        plot.add_plot(t_array, y)
        plot.save(2)
        plot.clear()

    def noise(self):
        t_array = arange(0, 1000, 1)
        y_array = rand(1000)

        plot = Plot('noise')

        plot.make_fig()
        plot.add_plot(t_array, y_array)
        plot.save(1)
        plot.clear()

    def fourie_noise(self):
        t_array = arange(0, 10, 0.01)
        y_array = []

        for t in t_array:
            a = self.calculate_signal(t)
            s = a + rand()
            y_array.append(s)

        fourie_y = fft(y_array)
        y = abs(fourie_y)

        plot = Plot('fourie_noise')

        plot.make_fig()
        plot.add_plot(t_array, y)
        plot.save(1)
        plot.clear()
