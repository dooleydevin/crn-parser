This repository includes a parser for Chemical Reaction Networks (CRNs), allowing users to define a CRN and simulate it in an intuitive way.

# Installation
This project was written in Python3, and outside of the packages included standard with [Python3 installations](https://www.python.org/downloads/), the [Python Lex-Yacc (PLY)](http://www.dabeaz.com/ply/) and [Matplotlib](http://matplotlib.org/) libraries were used.
 
# Syntax

## Parameters
A CRN file requires a total volume and a time-frame to be defined in order to simulate the given CRN. The volume and time-frame are set by setting the `VOLUME` and `TIME` variables to some integer values, respectively. An example is given below.

Volume is measured in molecules. Time measures the number of calculations made (i.e. the granularity is 1 unit).

```
VOLUME = 50000
TIME = 10000
```

The software also supports some optional parameters. To use a deterministic rather than stochastic model, supply the keyword `DETERMINISTIC` by itself on a line:

```
DETERMINISTIC
```

## Species
A species is defined as a string of characters of any form, excluding the use of `-`, `+`, `#`, `<` and `>` characters. Species must be set to some initial value prior to any reactions containing them. An example is given below:

```
ALPHA = 500
BETA = 200
ALPHA_2 = 700
```

## Reactions
Reactions are of a standard form, with species separated by `+` symbols on either side of an arrow, denoted `->`:

```
ALPHA + BETA -> ALPHA_2
```

Reactions with zero or more reactants and products are accepted. To change the rate of a reaction, include an integer or floating point value for the rate in-between the `-` and `>` characters. All rates default to the value 1. If we wanted to take the above example and change the rate of the reaction to 20, it would be done like so:

```
ALPHA + BETA -20> ALPHA_2
```

## Comments
Single-line comments are supported, and are denoted by a `#` character.

```
# This is a comment.
```

# Simulating a CRN
The crnlex.py file supports command line arguments. If all the proper packages are installed, and "python3" is the keyword associated with your python3 interpreter, you simply need to run 

```
python3 crnlex.py filename
```

to output the results of your file at the location "filename".  

# Examples
Example CRNs are provided in the "examples" directory. 
