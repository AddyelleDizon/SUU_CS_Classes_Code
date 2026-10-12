# -*- coding: utf-8 -*-
"""
Perceptron 

Students implement ONLY:
1) predict(w, b, x)
2) evaluate(w, b, data)
3) train_with_report(train_data, test_data, epochs)

"""

import random
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------
# Fixed true separator for labeling (do not change)
# w_true · x + b_true = 0
# ------------------------------------------------------------
w_true = [1.0, 1.0]
b_true = 0.0

def score_true(x):
    return w_true[0]*x[0] + w_true[1]*x[1] + b_true

def generate_train_balanced(n_each=50, margin=0.5, lo=-5, hi=5):
    """Generate 100 training points: 50 positive + 50 negative, away from boundary."""
    data = []

    while len(data) < n_each:
        x1 = random.uniform(lo, hi)
        x2 = random.uniform(lo, hi)
        if score_true((x1, x2)) >= margin:
            data.append(((x1, x2), 1))

    while len(data) < 2 * n_each:
        x1 = random.uniform(lo, hi)
        x2 = random.uniform(lo, hi)
        if score_true((x1, x2)) <= -margin:
            data.append(((x1, x2), -1))

    random.shuffle(data)
    return data

def generate_test_random(n=200, lo=-5, hi=5):
    """Random test points labeled by the true separator."""
    data = []
    for _ in range(n):
        x1 = random.uniform(lo, hi)
        x2 = random.uniform(lo, hi)
        y = 1 if score_true((x1, x2)) >= 0 else -1
        data.append(((x1, x2), y))
    return data

# ------------------------------------------------------------
# TODO 1 (Students): prediction
# ------------------------------------------------------------
def predict(w, b, x):
    """
    Return +1 or -1.
    w: [w0, w1], b: float, x: (x1, x2)
    """
    # TODO
    value = w[0]*x[0] + w[1]*x[1] + b
    if value >= 0:
        return 1
    else:
        return -1

# ------------------------------------------------------------
# TODO 2 (Students): evaluation
# ------------------------------------------------------------
def evaluate(w, b, data):
    """Return accuracy in [0,1]."""
    # TODO
    accurate = 0
    for x, y in data:
        if predict(w, b, x) == y:
            accurate += 1
    return accurate / len(data)

# ------------------------------------------------------------
# TODO 3 (Students): training with per-epoch report
# ------------------------------------------------------------
def train_with_report(train_data, test_data, epochs=20):
    """
    Train perceptron and print per-epoch train/test accuracy.

    Start: w=[0.0,0.0], b=0.0
    For each epoch:
      - shuffle train_data
      - for each (x,y):
          if predict value != y:
              update w and  b
              ...
      - print epoch, train_acc, test_acc

    Return: (w, b, final_train_acc, final_test_acc)
    """
    # TODO
    w = [0.0, 0.0]
    b = 0.0 

    print("Epoch TrainAcc TestAcc")

    for epoch in range(1, epochs + 1):
        random.shuffle(train_data)

        for x, y in train_data:
            y_pred = predict(w, b, x)

            if y_pred != y:
                w[0] += y * x[0]
                w[1] += y * x[1]
                b += y
        
        train_acc = evaluate(w, b, train_data)
        test_acc = evaluate(w, b, test_data)

        print(f"{epoch:<5} {train_acc:.3f} {test_acc:.3f}")
    
    final_train_acc = evaluate(w, b, train_data)
    final_test_acc = evaluate(w, b, test_data)

    print(f"\nFinal Train Accuracy: {final_train_acc:.3f}")
    print(f"Final Test Accuracy: {final_test_acc:.3f}")

    return w, b, final_train_acc, final_test_acc

# ------------------------------------------------------------
# Plot helpers (given)
# ------------------------------------------------------------
def split_points(data):
    x_pos = [pt[0][0] for pt in data if pt[1] == 1]
    y_pos = [pt[0][1] for pt in data if pt[1] == 1]
    x_neg = [pt[0][0] for pt in data if pt[1] == -1]
    y_neg = [pt[0][1] for pt in data if pt[1] == -1]
    return x_pos, y_pos, x_neg, y_neg

def plot_boundary(w, b, x_vals, label="learned boundary"):
    eps = 1e-12
    if abs(w[1]) < eps:
        x0 = -b / (w[0] if abs(w[0]) > eps else eps)
        plt.axvline(x=x0, label=label)
    else:
        y_vals = -(w[0]*x_vals + b) / w[1]
        plt.plot(x_vals, y_vals, label=label)

def plot_dataset(data, title, w=None, b=None):
    x_pos, y_pos, x_neg, y_neg = split_points(data)
    plt.scatter(x_pos, y_pos, label="+1")
    plt.scatter(x_neg, y_neg, label="-1")

    if w is not None and b is not None:
        x_vals = np.linspace(-5, 5, 200)
        plot_boundary(w, b, x_vals)

    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title(title)
    plt.legend()

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main():
    random.seed(0)

    train_data = generate_train_balanced(n_each=50, margin=0.5)  # 100 points, 50/50
    test_data  = generate_test_random(n=200)

    epochs = 20

    try:
        result = train_with_report(train_data, test_data, epochs=epochs)

        if (result is None) or (not isinstance(result, (tuple, list))) or (len(result) != 4):
            raise RuntimeError("train_with_report must return (w, b, final_train_acc, final_test_acc).")

        w, b, final_train_acc, final_test_acc = result

        plt.figure()
        plot_dataset(train_data, f"Training Data (Accuracy = {final_train_acc:.3f})", w=w, b=b)

        plt.figure()
        plot_dataset(test_data, f"Test Data (Accuracy = {final_test_acc:.3f})", w=w, b=b)

    except Exception:
        print("NOTE: predict / evaluate / train_with_report not implemented yet.")
        print("You should still see the TRAIN and TEST points plotted.")

        plt.figure()
        plot_dataset(train_data, "Training Data (no boundary yet)")

        plt.figure()
        plot_dataset(test_data, "Test Data (no boundary yet)")

    plt.show()

if __name__ == "__main__":
    main()