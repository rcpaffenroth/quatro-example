import matplotlib.pyplot as plt
import numpy as np

# Generate simple scatter plot data
x = np.random.randn(100)
y = x + np.random.randn(100)

plt.scatter(x, y, alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sample Scatter Plot')
plt.show()
