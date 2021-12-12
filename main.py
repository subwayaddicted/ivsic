from arguments import Arguments
from signals import Signals

arguments = Arguments([3, 2, 5, 4])
second_arguments = Arguments([2, 2, 1, 2])

signals = Signals(arguments, second_arguments)
signals.harmonic()
signals.noise()
signals.fourier_noise()