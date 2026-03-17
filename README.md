#### https://SenatorovAI.com

# Gradient Descent & SGD Solver — Course Implementation

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Website](https://img.shields.io/badge/website-live-blue.svg)](https://senatorovai.github.io/gradient-descent-sgd-solver-course/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18818738.svg)](https://doi.org/10.5281/zenodo.18820824)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)]()
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)]()

> 🚀 Professional educational project for understanding and implementing **Gradient Descent and Stochastic Gradient Descent (SGD)** from scratch in Python.

---

## 🔥 Project Overview

This repository demonstrates the mathematical foundation and practical implementation of:

- Gradient Descent (GD)
- Stochastic Gradient Descent (SGD)
- Mini-Batch Gradient Descent
- Convergence analysis
- Optimization visualization

---

## Keywords

```

gradient descent
stochastic gradient descent
sgd solver python
optimization algorithm
machine learning optimization
gradient descent from scratch
mini batch gradient descent
convex optimization
loss function minimization
python optimization implementation

```


---

## 📚 Mathematical Foundation

### Gradient Descent Update Rule

For parameters:

$$
\theta
$$

Update rule:

$$
\theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)
$$

Where:

- $$\eta$$ — learning rate  
- $$J(\theta)$$ — loss function  
- $$\nabla J(\theta)$$ — gradient  

---

### Stochastic Gradient Descent

Instead of full dataset gradient:

$$
\theta_{t+1} = \theta_t - \eta \nabla J_i(\theta_t)
$$

Where:

- Gradient computed on a single sample
- Faster but noisier updates

---

### Mini-Batch Version

$$
\theta_{t+1} = \theta_t - \eta \frac{1}{B} \sum_{i \in B} \nabla J_i(\theta_t)
$$

Balances:

- Stability
- Speed
- Computational efficiency

---

## 🧠 Why This Project Matters

Gradient-based optimization is used in:

- Neural networks
- Linear regression
- Logistic regression
- Deep learning
- Large-scale optimization

This project explains the algorithm at a mathematical and implementation level.

---

## 🏗 Project Structure

```

gradient-descent-sgd-solver/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── src/
│   ├── gradient_descent.py
│   ├── sgd.py
│   ├── loss_functions.py
│   ├── optimizer.py
│
├── examples/
│   └── demo.py
│
├── docs/
│   └── theory.md
│
├── images/
│   └── convergence_plot.png
│
└── index.html


``` 

Clean structure improves:

✔ Discoverability  
✔ Professional appearance  
✔ Portfolio quality  

---

## 🐍 Example Implementation — Gradient Descent

```python
import numpy as np

def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)

    for _ in range(epochs):
        predictions = X @ theta
        error = predictions - y
        gradient = (1/m) * X.T @ error
        theta -= lr * gradient

    return theta
````

---

## 🚀 Installation

```bash id="install1"
pip install -r requirements.txt
```

Run example:

```bash id="run1"
python examples/demo.py
```

---

## 📊 Visualization (Recommended)

Add:

* Loss curve plot
* Parameter convergence graph
* 3D loss surface

Example:

```python
import matplotlib.pyplot as plt

plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Convergence")
plt.show()
```


