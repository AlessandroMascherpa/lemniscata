#! python3
# -*- coding: utf-8 -*-


import sys
import matplotlib.pyplot as plt
import numpy as np



def show_help( name, parameters ):
    args = [ name ]
    for item in parameters:
        args.append( item )

    for item in args:
        print( item, end=' ' )


def render_chart( lower, upper, count, y, name="" ):
    x = np.linspace( lower, upper, num=count )

    # https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html
    fig, ax = plt.subplots()
    ax.plot( x, y )
    ax.set( xlabel='x', ylabel='y', title='Gaussian ' + name )
    ax.grid()

    name = chart_name( name )

    fig.savefig( name )
    plt.show()
    plt.close( fig )
    del ax
    del fig


from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def render_chart3d( x, y, z, name="" ):

    x, y = np.meshgrid( x, y )

    z = np.array( z )


    fig = plt.figure()
    ax = Axes3D( fig )
    ax.plot_surface( x, y, np.transpose( z ), cmap=cm.viridis )

    name = chart_name( name )

    fig.savefig( name )
    plt.show()
    plt.close( fig )
    del ax
    del fig


def  contour( lower, upper, count, z, name="" ):

    name = chart_name( name )

    x = np.linspace( lower, upper, num= count )
    y = np.linspace( lower, upper, num= count )
    x, y = np.meshgrid( x, y )

    fig = plt.figure()
    plt.contour( x, y, z )
    fig.savefig( name )
    plt.show()
    plt.close( fig )


def  chart_name( name ):
    if name != "": name = 'chart.' + name + '.png'
    else: name = 'chart.png'

    return name
