from arguments import Arguments
from signals import Signals

arguments = Arguments([3, 2, 5, 4])
signals = Signals(arguments)
signals.harmonic()
signals.noise()
signals.fourie_noise()