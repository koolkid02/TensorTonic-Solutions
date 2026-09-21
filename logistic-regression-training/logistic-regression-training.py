import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    n_samples, n_features = X.shape
    print(X.shape)
    # Initialize parameters
    w = np.zeros(n_features)
    b = 0.0

    for _ in range(steps):

        # 1. Forward pass
        z = X @ w + b
        p = _sigmoid(z)

        # 2. Gradients
        dw = (X.T @ (p - y)) / n_samples
        db = np.mean(p - y)

        # 3. Update parameters
        w -= lr * dw
        b -= lr * db

    return w, b