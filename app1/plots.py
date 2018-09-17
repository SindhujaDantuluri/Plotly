import datetime
import glob
import logging
import os

import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

logger = logging.getLogger(__name__)


def plot1d():
    x_data = np.arange(0, 120, 0.1)
    trace1 = go.Scatter(
        x=x_data,
        y=np.sin(x_data)
    )

    data = [trace1]
    layout = go.Layout(
        # autosize=False,
        # width=900,
        # height=500,

        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    logger.info("Plotting number of points {}.".format(len(x_data)))
    return plot_div




def plot1d_multiple(n):
    '''
    n = number of plots. It is a random number coming from JS.
    This basically tests the speed of PlotLy for multiple plots.
    '''
    x_array = []
    y_array = []
    n_points = 100
    x = np.arange(0.001, 1, 1/n_points)
    for i in range(n):
        x_array.append(x)
        y_array.append(np.sin(x*np.pi*(i+2)))
    data = []
    for x, y in zip(x_array, y_array):
        trace = go.Scatter(x=x, y=y)
        data.append(trace)

    layout = go.Layout(
        height=600,
        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


