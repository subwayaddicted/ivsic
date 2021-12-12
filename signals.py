from math import sin
from numpy import pi, arange, sin as nsin
from numpy.random import rand
from scipy.fft import fft
from plot import Plot
from arguments import Arguments
import os


class Signals:
    def __init__(self, arguments: Arguments, second_arguments: Arguments):
        self.formula = None
        self.arguments = arguments
        self.second_arguments = second_arguments
        if not os.path.exists('images'):
            os.makedirs('images')

    # Actually looks like: 2*sin(3*pi*t) + 3*sin(4*pi*t)
    def calculate_signal(self, t):
        return (self.arguments.before_first_sin * sin(self.arguments.inside_first_sin * pi * t)) + (
                self.arguments.before_second_sin * sin(self.arguments.inside_second_sin * pi * t))

    def calculate_second_signal(self, t):
        return (self.second_arguments.before_first_sin * sin(self.second_arguments.inside_first_sin * pi * t)) + (
                self.second_arguments.before_second_sin * sin(self.second_arguments.inside_second_sin * pi * t))

    def populate_harmonic_y_array(self, t_array: list, y_array: list, first: bool):
        if y_array:
            raise Exception('y_array is not empty, clear it')

        for t in t_array:
            a = self.calculate_signal(t) if first else self.calculate_second_signal(t)
            s = a + rand()
            y_array.append(s)

    def populate_fourier_noise_y_array(self, t_array: list, y_array: list, first: bool):
        if y_array:
            raise Exception('y_array is not empty, clear it')

        for t in t_array:
            a = self.calculate_signal(t) if first else self.calculate_second_signal(t)
            y_array.append(a)

    def apply_fourier_transformation(self, y_array):
        fourie_y = fft(y_array)
        return abs(fourie_y)

    def harmonic(self):
        t_array = arange(0, 10, 0.1)
        first_y_array = []

        self.populate_harmonic_y_array(t_array, first_y_array, True)
        y = self.apply_fourier_transformation(first_y_array)

        second_y_array = []
        self.populate_harmonic_y_array(t_array, second_y_array, False)
        second_y = self.apply_fourier_transformation(second_y_array)

        plot = Plot('harmonic')

        plot.make_fig()
        plot.add_plot(t_array, first_y_array)
        plot.add_plot(t_array, second_y_array)
        plot.save(1)
        plot.clear()

        plot.make_fig()
        plot.add_plot(t_array, y)
        plot.add_plot(t_array, second_y)
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

    def fourier_noise(self):
        t_array = arange(0, 10, 0.01)
        first_y_array = []

        self.populate_fourier_noise_y_array(t_array, first_y_array, True)
        y = self.apply_fourier_transformation(first_y_array)

        second_y_array = []
        self.populate_fourier_noise_y_array(t_array, second_y_array, False)
        second_y = self.apply_fourier_transformation(second_y_array)

        plot = Plot('fourier_noise')

        plot.make_fig()
        plot.add_plot(t_array, y)
        plot.add_plot(t_array, second_y)
        plot.save(1)
        plot.clear()
