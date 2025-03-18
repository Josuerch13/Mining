# import django
# import pandas as pd
# import matplotlib
# import numpy as np
# import chart_studio
# import plotly
# import keras
# import tensorflow as tf
# import pkg_resources

# print("Django version:", django.get_version())
# print("Pandas version:", pd.__version__)
# print("Matplotlib version:", matplotlib.__version__)
# print("NumPy version:", np.__version__)
# # print("Chart Studio version:", chart_studio.__version__)
# print("Chart Studio version:", pkg_resources.get_distribution("chart-studio").version)
# print("Plotly version:", plotly.__version__)
# print("Keras version:", keras.__version__)
# print("TensorFlow version:", tf.__version__)

import django
import pandas as pd
import matplotlib
import numpy as np
import chart_studio
import plotly
import keras
import tensorflow as tf
import sklearn
import pkg_resources
import google.protobuf
import sys

print("Django version:", django.get_version())
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("NumPy version:", np.__version__)
print("Chart Studio version:", pkg_resources.get_distribution("chart-studio").version)
print("Plotly version:", plotly.__version__)
print("Keras version:", keras.__version__)
print("TensorFlow version:", tf.__version__)
print("Scikit-learn version:", sklearn.__version__)
print("Protobuf version:", google.protobuf.__version__)
print("Statsmodels version:", pkg_resources.get_distribution("statsmodels").version)
print("Python version:", sys.version)