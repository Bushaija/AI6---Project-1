import torch
import numpy as np
from torchSummaryX import summary
import torchaudio.transforms as tat
import sklearn
import gc
import zipfile
import pandas as pd
from tqdm import tqdm
import os
import datatime
import wandb
import yaml

"""
    1. torch:

            Purpose: Provides functions and classes for building
            and training deep learning models.

            Function: Core library for tensor computations and neural
            network operations in PyTorch.

    2. numpy:

            Purpose: Supports large, multi-dimensional arrays and matrices,
            along with a collection of mathematical functions to operate on these arrays.

            Function: Used for numerical computations and manipulating arrays.

    3. torchSummaryX:

            Purpose: Provides a summary of the model architecture,
            similar to Keras' summary.

            Function: Generates a detailed summary of a PyTorch model,
            including layer types, output shapes, and the number of parameters.

    4. torchaudio.transforms (as tat):

            Purpose: Provides common audio processing transforms.

            Function: Used for applying various audio preprocessing operations,
            like spectrogram, MFCC, and others.


    5. sklearn:

            Purpose: Offers simple and efficient tools for data mining and data analysis.

            Function: Provides a range of tools for machine learning and statistical
            modeling, including classification, regression, clustering, and
            dimensionality reduction.
    6. gc:

            Purpose: Provides an interface to the garbage collection facility.

            Function: Used to manually trigger garbage collection and free up
            memory by removing unreferenced objects.

    7. zipfile:

            Purpose: Allows for the creation, reading, writing, and extraction of ZIP files.

            Function: Used for working with ZIP archives, which can be useful for
            compressing and decompressing datasets.

    8. pandas (as pd):

            Purpose: Provides data structures and data analysis tools.

            Function: Used for data manipulation and analysis, especially
            with tabular data in DataFrame objects.

    9. tqdm:

            Purpose: Provides a fast, extensible progress bar.

            Function: Used to display progress bars for loops and other iterative
            processes to track progress visually.

    10. os:

            Purpose: Provides functions for interacting with the operating system.

            Function: Used for various OS-related tasks, such as file and directory operations, environment variables, and executing system commands.

    11. datetime (corrected from datatime):

            Purpose: Supplies classes for manipulating dates and times.

            Function: Used for date and time operations, such as creating, formatting, and manipulating dates and times.

    12. wandb:

            Purpose: Provides a platform for experiment tracking and model management.

            Function: Used for tracking machine learning experiments, logging metrics, and visualizing results.

    13. yaml:

            Purpose: Provides support for parsing and emitting YAML.

            Function: Used for reading and writing YAML files, which are often used for configuration
            files due to their human-readable format.
"""
