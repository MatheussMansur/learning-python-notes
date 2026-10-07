# Module 5 - Libraries

## math
- `math.pow(2, 5)` -> `32.0` (float!)
- `math.ceil(3.45)` -> 4, `math.floor(5.25)` -> 5
- `math.fabs(-10.33)` -> 10.33
- `math.log(x)` is natural log, `math.log(x, 10)` base 10

## numpy
- `import numpy as np`, `np.array([1, 2, 3])`
- lists don't do vector math: `[1,2,3] * 3` repeats the list, `[1,2,3] + [4,5,6]` concatenates
- arrays do: `u * 3`, `u + v`, `u * v` (element by element)
- `np.dot(u, v)` dot product
- `np.ones((2, 3))`, `.shape`
- all items in an array have the same type

## scipy + matplotlib
- `scipy.optimize.curve_fit(func, x, y)` finds the best parameters for a function
- `plt.plot`, `plt.errorbar`, `plt.title/xlabel/ylabel`
- save with `plt.savefig` BEFORE `plt.show()`

## flask
- `@app.route("/")` maps a url to a function
- `"/<name>"` makes a dynamic page, the name comes as a parameter
- `redirect(url_for("home"))` sends to another route
