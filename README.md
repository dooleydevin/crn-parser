This repository includes a parser for Chemical Reaction Networks (CRNs), allowing users to define a CRN and simulate it in an intuitive way.

# Syntax

## Parameters 
A .crn file requires a total volume and a time-frame to be defined in order to simulate the given CRN. The volume and time-frame are set by setting the VOLUME and TIME variables to some integer values, respectively. An example is given below.

VOLUME = 50000
TIME = 10000

## Species
A species is defined as a string of characters of any form, excluding the use of '-', '+', '#', '<' and '>' characters. Species must be set to some initial value prior to any reactions containing them. An example is given below.

ALPHA = 500
BETA = 200
ALPHA_2 = 700

## Reactions
Reactions are of a standard form, with species separated by '+' symbols on either side of an arrow, denoted '->'. Reactions with zero or more reactants and products are accepted. An example of a simple reaction is given below.

ALPHA + BETA -> ALPHA_2

To change the rate of a reaction, include an integer for the rate in between the '-' and '>' characters. All rates default to the value 1. If we wanted to take the above example and change the rate of the reaction to 20, it would be done like so:

ALPHA + BETA -20> ALPHA_2

## Simulating a CRN


## Examples
Example CRNs are provided in the 'examples' file. 
