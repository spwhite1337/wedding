import os
import numpy as np
import matplotlib.pyplot as plt

from wedding.utils.prices import prices

from config import Config


def calc_costs():
    plt.figure(figsize=(8, 8))
    guests = np.linspace(50, 200, 150)
    for label, cost_per_guest in prices.items():
        plt.plot(guests, [cost_per_guest(guest) for guest in guests], label=label)
    plt.xlabel('Num Guests')
    plt.ylabel('Cost')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(Config.ROOT_DIR, 'costs.png'))
