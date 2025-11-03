import numpy as np

class RegresiLinear:
    def __init__(self, X, y):
        # Pastikan semua data dalam bentuk numpy array bertipe float
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float).reshape(-1, 1)

        # Tambahkan kolom 1 di depan untuk intercept (bias term)
        self.X = np.c_[np.ones((X.shape[0], 1)), X]
        self.y = y
        self.theta = None

    def train(self):
        # Rumus Normal Equation: θ = (XᵀX)⁻¹ Xᵀy
        X_T = self.X.T
        theta = np.linalg.inv(X_T @ self.X) @ X_T @ self.y
        self.theta = theta
        return theta.flatten()

    def predict(self, X_new):
        # Konversi data baru ke float dan tambahkan kolom 1
        X_new = np.array(X_new, dtype=float)
        X_new = np.c_[np.ones((X_new.shape[0], 1)), X_new]
        return X_new @ self.theta

