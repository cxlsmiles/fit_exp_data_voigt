import numpy as np

pi_inv = 1.0/np.pi

sqrt_pi = np.sqrt(np.pi)
sqrt_pi_inv = 1.0/sqrt_pi

class voigt:
    def __init__  (self, gamma, alpha, x0):
        self.gamma = gamma
        self.alpha = alpha
        self.x0 = x0

    def at (self, x):
        x_ = np.array(x)
        return np.array(np.sqrt(self.alpha) * sqrt_pi_inv * np.exp(- self.alpha * (x_ - self.x0)**2) + pi_inv * self.gamma * 0.5 / ((x_ - self.x0)**2 + self.gamma**2))