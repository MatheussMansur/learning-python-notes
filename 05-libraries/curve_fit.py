# electromagnet example from the module: fit a line to I x B and save the chart

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

current = np.array([4.0, 3.5, 3.0, 2.5, 2.0])
field = np.array([1.31, 1.14, 0.97, 0.81, 0.76])
current_error = [0.2] * 5
field_error = [0.03, 0.02, 0.04, 0.02, 0.05]


def line(x, m, b):
    return m * x + b


params, cov = opt.curve_fit(line, current, field)
print("m and b:", params.round(3))

plt.errorbar(current, field, xerr=current_error, yerr=field_error, fmt="o", ms=3)
plt.plot(current, line(current, *params), linestyle="dashed", label="Fit")
plt.title("I vs. B of the electromagnet")
plt.xlabel("Current I (A)")
plt.ylabel("Magnetic field B (T)")
plt.legend()
plt.savefig("05-libraries/i_vs_b.png")
print("chart saved")
