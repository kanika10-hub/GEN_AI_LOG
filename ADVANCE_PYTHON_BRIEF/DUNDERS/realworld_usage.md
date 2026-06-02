# Real World Usage of Dunder Methods

## Dataclasses

Python dataclasses automatically generate:

- __init__
- __repr__
- __eq__

## Django

Django models often implement:

__str__

for admin panel display.

## LangChain

Many internal classes use:

- __call__
- __iter__
- __repr__

to create clean APIs.

## PyTorch

Neural network modules use:

__call__

which internally invokes:

forward()

Example:

model(x)

instead of

model.forward(x)

## Pandas

DataFrames use:

- __getitem__
- __len__
- __iter__

allowing:

df["name"]
len(df)
