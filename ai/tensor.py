import tensorflow as tf
import numpy as np
import sys
# Ensure UTF-8 encoding is used
sys.stdout.reconfigure(encoding='utf-8')

# Generate some synthetic data for regression (Fibonacci sequence)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]], dtype=np.float32)
y = np.array([[0], [1], [1], [2], [3], [5], [8], [13]], dtype=np.float32)

# Build a simple feedforward neural network
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(units=8, activation='relu', input_shape=[1]),  # Hidden layer with 8 neurons
    tf.keras.layers.Dense(units=1)  # Output layer with 1 neuron (linear activation by default)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=500, verbose=0)

# Values for which to make predictions
values = np.array([[9], [10], [11], [12], [13], [14], [15], [16]], dtype=np.float32)

# Make predictions
predictions = model.predict(values)

# Print the predictions
for i, prediction in enumerate(predictions):
    print(f"Input: {values[i][0]} - Predicted: {prediction[0]:.4f}")