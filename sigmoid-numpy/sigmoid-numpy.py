import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    X=np.array(x)
    sigmoid=1/(1+np.exp(-X))
    return sigmoid
