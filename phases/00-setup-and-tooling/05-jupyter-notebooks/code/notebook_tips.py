import time
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def timing_comparison():
    print("=== Timing: List vs NumPy ===\n")

    size = 1_000_000

    start = time.perf_counter()
    python_list = [x ** 2 for x in range(size)]
    list_time = time.perf_counter() - start
    print(f"List comprehension: {list_time:.4f}s")

    start = time.perf_counter()
    numpy_array = np.arange(size) ** 2
    numpy_time = time.perf_counter() - start
    print(f"NumPy:              {numpy_time:.4f}s")
    print(f"Speedup:            {list_time / numpy_time:.1f}x")


def inline_plotting():
    print("\n=== Inline Plotting ===\n")

    np.random.seed(42)
    x = np.linspace(0, 10, 200)
    y_sin = np.sin(x)
    y_noisy = y_sin + np.random.normal(0, 0.2, 200)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].plot(x, y_sin, label="sin(x)")
    axes[0].plot(x, y_noisy, alpha=0.5, label="noisy")
    axes[0].set_title("Signal vs Noise")
    axes[0].legend()

    axes[1].hist(y_noisy - y_sin, bins=30, edgecolor="black")
    axes[1].set_title("Noise Distribution")

    plt.tight_layout()
    plt.savefig("notebook_plot.png", dpi=100)
    print("Saved plot to notebook_plot.png")
    print("In a notebook, plt.show() displays this inline.")




def memory_check():
    print("\n=== Memory Usage ===\n")

    small = np.random.randn(1000)
    medium = np.random.randn(100_000)
    large = np.random.randn(10_000_000)

    for name, arr in [("1K", small), ("100K", medium), ("10M", large)]:
        size_mb = arr.nbytes / 1e6
        print(f"Array {name:>4s} elements: {size_mb:>8.2f} MB")

    print(f"\nPython process memory: ~{sys.getsizeof(large) / 1e6:.1f} MB for the large array")
    print("In notebooks, memory accumulates across cells. Restart the kernel to free it.")


def magic_command_equivalents():
    print("\n=== Magic Command Equivalents ===\n")
    print("In a notebook, you would use magic commands:")
    print("  %timeit np.random.randn(10000)    -> micro-benchmark")
    print("  %%time long_operation()            -> wall clock time")
    print("  %matplotlib inline                 -> show plots in cells")
    print("  !pip install package               -> install from notebook")
    print("  %env VAR                           -> check env variable")
    print()

    iterations = 1000
    start = time.perf_counter()
    for _ in range(iterations):
        np.random.randn(10000)
    elapsed = time.perf_counter() - start
    per_call = elapsed / iterations * 1e6

    print(f"Manual timing (like %%timeit): np.random.randn(10000)")
    print(f"  {per_call:.1f} us per call ({iterations} iterations)")


if __name__ == "__main__":
    print("Notebook Tips - Key Patterns\n")
    print("Run these in a Jupyter notebook to see rich output.\n")

    timing_comparison()
    inline_plotting()
    dataframe_display()
    memory_check()
    magic_command_equivalents()
