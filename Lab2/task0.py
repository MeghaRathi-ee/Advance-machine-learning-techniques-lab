# task0.py
from data import generate_linear_data
from visual import plot_data, show

def main():
    X, y = generate_linear_data()
    plot_data(X, y, "Linearly Separable Data")
    show()

if __name__ == "__main__":
    main()
