import numpy as np

# Let's say these come from your GUI:
layer_sizes = [4, 5, 3]  # Example: 4 inputs, 5 hidden, 3 outputs
has_bias = True         # True or False from GUI

# 1. Initialize empty lists for weights and biases
weights = []
biases = []

# 2. Loop through the layers to create matrices
for i in range(len(layer_sizes) - 1):
    rows = layer_sizes[i + 1]  # Number of nodes in NEXT layer
    cols = layer_sizes[i]      # Number of nodes in CURRENT layer
    
    # Create a 2D matrix of shape (rows, cols)
    weight_matrix = np.random.randn(rows, cols)
    weights.append(weight_matrix)
    
    # Create bias vector of shape (rows, 1) if enabled
    if has_bias:
        b = np.zeros((rows, 1))
        biases.append(b)

print("Weights initialized:", len(weights))
print("Biases initialized:", len(biases) if has_bias else "No bias used")