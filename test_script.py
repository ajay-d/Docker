# -*- coding: utf-8 -*-

from os import path, getcwd, chdir
import pandas as pd
import tensorflow as tf

def print_my_path():
    print('cwd:     {}'.format(getcwd()))
    print('__file__:{}'.format(__file__))
    print('abspath: {}'.format(path.abspath(__file__)))
	
    print('tensorflow: {}'.format(tf.__version__))
    print('pandas: {}'.format(pd.__version__))

print_my_path()

