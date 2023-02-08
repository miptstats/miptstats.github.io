import matplotlib.pyplot as plt
import numpy as np


def plot_batman():
    """
    Функция, которая отрисовывает эмблему Бэтмена.
    Реализация честно позаимствована с поста на Медиуме и приведена в читаемый вид: 
    https://medium.com/@subarnopal/plotting-the-batman-equation-in-python-using-numpy-and-matplotlib-b209b02aed68
    """
    Y = np.arange(-4,4,.005)
    X = np.abs(Y / 2) - 0.09137 * Y**2 + np.sqrt(1 - (np.abs(np.abs(Y) - 2)- 1 )**2) - 3

    Y1 = np.append(np.arange(-7,-3,.01), np.arange(3,7,.01))
    X1 = 3 * np.sqrt(-(Y1 / 7)**2 + 1)
        
    X = np.append(X, X1)
    Y = np.append(Y, Y1)
    
    Y1 = np.append(np.arange(-7.,-4,.01), np.arange(4,7.01,.01))
    X1 = -3 * np.sqrt(-(Y1 / 7)**2 + 1)
        
    X = np.append(X, X1)
    Y = np.append(Y, Y1)
    
    Y1 = np.append(np.arange(-1,-.8,.01), np.arange(.8, 1,.01))
    X1 = 9 - 8 * np.abs(Y1)
        
    X = np.append(X, X1)
    Y = np.append(Y, Y1)
    
    Y1 = np.arange(-.5,.5,.05)
    X1 = np.full_like(Y1, 2)
        
    X = np.append(X, X1)
    Y = np.append(Y, Y1)
    
    Y1 = np.append(np.arange(-2.9, -1, .01), np.arange(1, 2.9,.01))
    X1 = 1.5 - .5 * np.abs(Y1) - 1.89736 * (np.sqrt(3 - Y1**2 + 2 * np.abs(Y1)) - 2)
        
    X = np.append(X, X1)
    Y = np.append(Y, Y1)
    
    Y1 = np.append(np.arange(-.7,-.45,.01), np.arange(.45, .7,.01))
    X1 = 3 * np.abs(Y1) + .75
    
    X = np.append(X,X1)
    Y = np.append(Y,Y1)
   
    ax = plt.gca()
    ax.set_facecolor((0, 0, 0))
    ax.plot(Y, X, 'yo')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
