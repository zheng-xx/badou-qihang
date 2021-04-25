import numpy as np


def forward(x):
    if x.ndim != 2:
        raise Exception("The dim of input only support 2D!")
    else:
        centered = x - np.mean(x, axis=0)
        normalized = centered / np.std(centered, axis=0)
        return normalized
