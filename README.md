# pyweb
Framework for Python HTTP server


## Example

### Decorator

```python
@core.http("GET", "/root/{id}/{action}.do")
def action_1 (headers, parameters, id: "path", action: "path"):
  return answer(200, hs={}, body="Hello world")
```
