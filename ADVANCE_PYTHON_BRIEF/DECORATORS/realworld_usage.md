# Real World Usage of Decorators

## Flask

Routes are implemented using decorators.

```python
@app.route("/")
def home():
    pass
```

Decorators register functions as endpoints.

---

## FastAPI

API methods use decorators.

```python
@app.get("/users")
```

---

## Django

Authentication uses decorators.

```python
@login_required
```

Users must be authenticated before accessing a view.

---

## Logging Systems

Decorators automatically log function calls.

```python
@logger
```

---

## Performance Monitoring

Measure execution time.

```python
@timer
```

---

## Caching

Python provides:

```python
@lru_cache
```

to cache expensive computations.

---

## AI Applications

Decorators are used for:

* LLM Call Monitoring
* Token Usage Tracking
* Cost Tracking
* Retry Logic
* API Rate Limiting

Example:

```python
@track_tokens
def generate():
    pass
```

---

## Testing Frameworks

Pytest uses decorators heavily.

```python
@pytest.mark.slow
```

---

## Security

Authentication and authorization checks are commonly implemented using decorators.
