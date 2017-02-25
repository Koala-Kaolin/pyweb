# pyweb
Framework for Python HTTP server

## Titorial

## Getting started

### URL parameters

```python
@core.http("GET", "/root/{id}/{action}.do")
def action_1 (headers, parameters, id: "path", action: "path"):
  return answer(200, hs={}, body="Hello world")
```

### Pattern

```python
@core.http("GET|POST", "/test/unique/{id}")
@echo("pfile")
def action_test_unique(
        headers,
        params,
        id: "path",
        ptexte: "text [a-zA-Z]{10}",
        htexte: "header",
        pnum: "number .{10}"=10,
        pfile: "file"=None):
    """
    Fonction de test
    @param headers entetes
    @param params disctionnaire des paramètres
    @param ptexte test
    @param htexte test
    @param pnum test
    @param pfile test
    """
return answer(200, body="<html>Hello %s</html>" % ptexte, mime="text/html")
```
