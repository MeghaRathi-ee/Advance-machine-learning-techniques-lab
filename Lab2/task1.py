# task1.py
import numpy as np
from sklearn.svm import SVC

from data import generate_linear_data
from visual import plot_svm_margin, show

def main():
    # Step 1: Generate linearly separable data
    X, y = generate_linear_data()

    # Step 2: Train hard-margin linear SVM
    svm_hard = SVC(kernel='linear', C=1e6)
    svm_hard.fit(X, y)

    # Step 3: Extract model parameters
    w = svm_hard.coef_[0]
    b = svm_hard.intercept_[0]

    # Step 4: Compute margin
    margin = 2 / np.linalg.norm(w)

    print("Weight vector (w):", w)
    print("Bias (b):", b)
    print("Margin:", margin)
    print("Number of support vectors:", len(svm_hard.support_vectors_))

    # Step 5: Visualize decision boundary and margins
    plot_svm_margin(X, y, w, b)
    show()

if __name__ == "__main__":
    main()
