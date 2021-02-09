<!-- -*- coding: utf-8 -*- -->
# Activity 07: Modules and Classes
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)


Solve the following problems.

See https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2021/02/09/04_Python_4/ for help.

(*Note that the last activity on class inheritance is optional* — you
don't need the final 10 points to get 100% on this activity even
though GitHub autograding will still show the tests as failing. Don't
worry about that: if you have 47 points you have 100%)

## Modules

### constants module

1. Create a module `constants.py` with values for the mathematical
   constant [π](https://mathworld.wolfram.com/Pi.html) (named `pi`,
   see also OEIS [A000796](http://oeis.org/A000796)) and the physical
   constants `c` for the [speed of light in
   vaccuum](https://physics.nist.gov/cgi-bin/cuu/Value?c) (in ms/s)
   and [Planck's
   constant](https://physics.nist.gov/cgi-bin/cuu/Value?h) `h` (in J
   s).

2. In a file `problem1.py`, import your *constants* module and compute
   the reduced Planck's constant ħ = h/2π and store it in variable
   `hbar`. Print it to all 9 significant figures in scientific notation with
   ```python
   print("hbar = {hbar:.9e}".format(hbar))
   ```
   
### myfuncs module

Use your *myfuncs* module from the last lesson in a file `problem2.py` and

1. Compute *Heaviside(n)* for the integers -10 ≤ n ≤ 10, assign the
   list to a variable `y`, and print it with
   ```python
   print(f"Heaviside: {y}")
   ```
   (this `print` uses an
   [f-string](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals),
   available since Python 3.6 as an improvement over [format
   representations](https://docs.python.org/3/library/functions.html#format);
   both use the [Format Specification
   Mini-Language](https://docs.python.org/3/library/string.html#formatspec))

2. Compute the temperature of the boiling point of water under
   standard conditions in degrees Celsius from the value in Kelvin,
   *T*<sub>boil</sub> = 373.15 K. Assign it to a variable `t_boil` and
   print it with
   ```python
   print(f"Water boils at {t_boil:.2f} C")
   ```

### Standard library

Import the *[math](https://docs.python.org/3/library/math.html)*
module and the *[os](https://docs.python.org/3/library/os.html)*
module from the [Python Standard
Library](https://docs.python.org/3/library/index.html) in a file
`problem3.py`. Look in these modules for functions and attributes to
solve the following problems:

1. Compute `y_full_circle =
   sin(`[`tau`](https://docs.python.org/3/library/math.html#math.tau)`)`. (Optionally,
   you can also print the value.)

2. Define the [cumulative distribution
   function](https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function)
   of the normal distribution with mean µ and standard deviation σ

        Phi(x, µ, σ) = 1/2 [1 + erf( (x-µ)/(σ sqrt(2)) )]

   as a Python function `Phi(x, mu=0., sigma=1.0)`.
   
   For a random variable X that is normally distributed with mean
   µ=88.6 and standard deviation σ=6.3 compute the probability
   *P(X>95)* to observe a value of X > 95, using

        P(X > x) = 1 - Phi(x, µ, σ)

   Assign your result to a variable `P_aplus` and print it with
   ```python
   print(f"P(X > 95) = {100 * P_aplus:.1f}%")
   ```


3. Get the current working directory as a string and assign to the
   variable `cwd` and print it with
   ```python
   print(f"cwd = '{cwd}'")
   ```   

## Objects and Classes

### String methods

Given the sentence `sentence = "MAY THE FORCE BE WITH YOU!"` in file `problem4.py`

1. test if it is lower case (assign the boolean value to a variable `all_lower`)
2. make it lower case (store in `l_sentence`)

### Creating your own classes

#### `Sphere` class definition
Create a file `bodies.py` that contains the class `Sphere`.

* A `Sphere` instance is initialized with its *position* (Cartesian
  coordinates a list or tuple with three floating point numbers) and
  optionally its *radius*; the default for *radius* is 1.0.
* Store the position in an attribute `pos` and the radius in attribute `radius`.
* The class has a method `volume()` that returns the volume of the sphere.
* The class has a method `translate(t)`, that changes the position of
  the sphere by adding the translation vector `t` (tuple with three
  floats) to the current position.

#### Instantiation: A ball is a sphere

Create a file `balls.py` in which you

1. create an object representing a ball by instantiating a `Sphere` at
   position `(0, 0, 10)` with radius 2 and assigning it to variable
   `ball`
2. change the position of the ball to `(-5, 0, 0)`,
3. assign the volume of the ball to a variable `volume` and print it to 3 decimals,
4. translate the ball by `(5, 0, 0)`

After each step, print the position of the ball.

#### Independence: A balloon is not a ball

Create a file `ball_oons.py` in which you

1. create a ball (as a `Sphere`) at position `(0, 0, 10)` with radius
   2 (variable `ball`),
2. create a balloon (as a `Sphere`) at position `(0, 0, 10)` with radius
   6 (variable `balloon`),
3. change the ball's position to `(-1, -1, 0)`
4. compare the balloon's and the ball's position by printing
   ```python
   print(f"ball at {ball.pos} != balloon at {balloon.pos}")
   ```
#### Inheritance: Earth is a Sphere (OPTIONAL)

In file `astronomy.py`, define a class `Planet` that is derived from
`Sphere` and is instantiated as `Planet(name, pos, mass, radius)`.

`Planet` must have a method `Planet.density()` that returns the
density of the planet, mass/volume.

Use your class to represent Earth (quantities from <http://www.wolframalpha.com>)
```python
# lengths in m and mass in kg
earth = Planet("Earth", (1.4959802296e11 , 0, 0), 5.9721986e24, 6371e3)
print(earth.density())
```
and print the density.
