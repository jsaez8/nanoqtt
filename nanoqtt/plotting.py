# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:56:28 2021

@author: jsaezmol
"""
import matplotlib.pyplot as plt
from qcodes.plots.qcmatplotlib import MatPlot
from qcodes.data.data_set import DataSet

def plot_dataset(dataset: DataSet, scanjob, save=True) -> None:
    """ Plot a dataset to matplotlib figure window

    Args:
        dataset: DataSet to be plotted
        scanjob: scanjob of the measurement
        save: Select if you want to save the plots

    """
    
    parameter_names = [name for name in dataset.arrays.keys() if not dataset.arrays[name].is_setpoint]
    default_array = dataset.default_parameter_array()
    
    # Path for saving
    base_loc = dataset.default_io.base_location
    folder = '\\' + dataset.location + '\\'
    label = str(scanjob.get('dataset_label'))
    path = base_loc + folder + label
    
    # 2D plots
    if len(default_array.shape) >= 2:
        for idx, parameter_name in enumerate(parameter_names):
                plot_handle = MatPlot(dataset.arrays[parameter_name], num=idx)
                plot_handle.rescale_axis()
                if save==True:
                    plt.savefig(path + str(idx) + '.png')

    # 1D plots        
    else:
        for idx, parameter_name in enumerate(parameter_names):
            plot_handle = MatPlot(dataset.arrays[parameter_name], num=idx)
            plot_handle.rescale_axis()
            if save==True:
                plt.savefig(path + str(idx) + '.png')