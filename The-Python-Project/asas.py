# Code source: Óscar Nájera
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt


def main():
    x = [1650, 1750, 1850, 1925, 1956, 1966, 1970, 1974, 1976, 1980, 1991, 2000, 2004, 2010, 2015, 2020]
    y = [500000000, 700000000, 1000000000, 2000000000, 2500000000, 3300000000, 3600000000, 3900000000, 4000000000, 4400000000, 5500000000, 6000000000,6400000000,6900000000,7300000000,7700000000]

    plt.figure()
    plt.plot(x, y)
    plt.xlabel('$x$')
    plt.ylabel('$\exp(x)$')

    plt.figure()
    plt.plot(x, -np.exp(-x))
    plt.xlabel('$x$')
    plt.ylabel('$-\exp(-x)$')

    plt.show()

if __name__ == '__main__':
    main()