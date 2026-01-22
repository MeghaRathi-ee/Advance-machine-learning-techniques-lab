# task2.py
from data import generate_overlapping_data
from visual import plot_data, show

def main():
    X, y = generate_overlapping_data()
    plot_data(X, y, title="Overlapping Data")
    show()

if __name__ == "__main__":
    main()
