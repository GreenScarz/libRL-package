'''
this example file demonstrates how to use the included
functions available through the libRL library. Users are encouraged
to call/read the docstrings for descriptions and full context on the
*args and **kwargs available, or read the documentation available the following
websites:

Overview:
https://1mikegrn.github.io/libRL/

examples:
https://1mikegrn.github.io/libRL/#examples
'''

import libRL
import pandas as pd
import numpy as np
from os import path

def main():
    """

this example script is designed to run a demonstration of each of the
available functions in libRL. Data is imported directly from the GitHub
repository for convenience. Results are simply printed.

    :return: nothing

    """

    here = path.dirname(path.abspath(__file__))
    data_string = path.join(here, 'test', 'test_data.csv')
    
    reflection_loss = libRL.reflection_loss(
        data=data_string,
        f_set=(1,18,0.25),
        d_set=(0,20,0.25),
        interp='cubic',
        multiprocessing=True,
        multicolumn=True,
        as_dataframe=True
    ) 

    print(reflection_loss)

    # characterization = libRL.characterization(
    #     data=data_string,
    #     f_set=(1,18,0.25),
    #     params='all',
    #     as_dataframe=True
    # )

    # print(characterization)

    # band_analysis = libRL.band_analysis(
    #     data=data_string,
    #     f_set=(1,18,0.1),
    #     d_set=(1,5,0.1),
    #     m_set=[1,2,3,4,5],
    #     thrs=-10,
    #     as_dataframe=True,
    # )

    # print(band_analysis)

if __name__ == "__main__":
    main()