import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    X=np.array(x)
    ReLU=np.maximum(0,X)
    relu=np.array(ReLU)
    return relu
    