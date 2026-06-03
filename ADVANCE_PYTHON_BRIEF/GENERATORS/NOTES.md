# Generators

## What are Generators?

Generators are functions that return values one at a time using the `yield` keyword.

Unlike lists, generators do not store all values in memory.

## Why Use Generators?

- Memory Efficient
- Lazy Evaluation
- Process Large Datasets
- Stream Data

## Return vs Yield

### Return

```python
def numbers():
    return [1, 2, 3]
```

Returns everything at once.

### Yield

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Produces values one at a time.

## How Generators Work

When a generator encounters `yield`:

1. It returns the current value.
2. Pauses execution.
3. Remembers its state.
4. Continues from the same place next time.

## Benefits

- Lower memory usage
- Faster startup
- Better for streaming data

## Key Takeaways

- Uses `yield`
- Returns a generator object
- Implements iterator protocol automatically
- Generates values lazily
