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
def action_test_unique(
        headers,
        params,
        id: "path",
        ptexte: "text [a-zA-Z]{10}",
        htexte: "header",
        pnum: "number .{10}"=1234567890,
        pfile: "file"=None):
    """
    Fonction de test
    @param headers http headers
    @param params all parameters dictionnary
    @param id mandatotory path element
    @param ptexte mandatory text parameter with exactly 10 letters
    @param htexte parameter from header
    @param pnum parameter with 10 carachters with default value 1234567890
    @param pfile optionnal file
    """
return answer(200, body="<html>Hello %s</html>" % ptexte, mime="text/html")
```
