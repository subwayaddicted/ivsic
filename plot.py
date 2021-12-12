import matplotlib.pyplot as plt


class Plot:
    def __init__(self, plot_name: str):
        self.fig = None
        self.ax = None
        self.plot_name = plot_name

    def make_fig(self):
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111)

    def add_plot(self, first_arr, second_arr):
        if second_arr is not None:
            self.ax.plot(first_arr, second_arr)
        else:
            self.ax.plot(first_arr)

    def save(self, plot_number: int):
        self.fig.savefig('images/' + self.plot_name + str(plot_number) + '.png')
        print('Picture ' + self.plot_name + str(plot_number) + '.png' + ' has been saved!')

    def clear(self):
        self.fig.clear()
