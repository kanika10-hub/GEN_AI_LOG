# Argument Parsing

## What is Argument Parsing?

Argument parsing allows users to pass values to a Python program from the command line.

Example:

python app.py Kanika

Here:

Kanika = command line argument

---

## Why Use It?

Without argument parsing:

input()

requires user interaction.

With argument parsing:

python app.py --name Kanika

Program runs automatically.

---

## argparse Module

Python provides the argparse module.

Example:

import argparse

parser = argparse.ArgumentParser()

---

## Common Methods

add_argument()

Defines an argument.

parse_args()

Reads user input.

type=

Specifies datatype.

default=

Provides default value.

required=True

Makes argument mandatory.

---

## Benefits

- Professional CLI tools
- Validation
- Help messages
- Automation friendly
