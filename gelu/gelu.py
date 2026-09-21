import math
import numpy as np
from scipy.special import erf
def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    X=np.array(x)
    GELU= np.array(0.5*X*(1+erf(X/np.sqrt(2))))
    return GELU
    pass