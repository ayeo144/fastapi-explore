Part 1: Writing the Application Code
------------------------------------

**The Start**

I chose a ToDo app as the API service as it's quite a basic concept, and I wanted to
focus on methods of deploying such a service more than creating an advanced and 
complicated application.

I chose to use `FastAPI` for this. I already had some experience with `Flask`, but for such
a simple application `FastAPI` seemed like a good choice and gave me an excuse to learn a 
new package.

I also discovered the [`pydantic`](https://pydantic-docs.helpmanual.io/) package through 
reading the `FastAPI` docs, which is a really cool package for helping parse input data 
and enforce strict typing via the standard library `typing` module, and other Python types.

**Object-Oriented Approach**

Previously when working with `Flask` I had used the `flask_restful` package which applied a
class-based approach to grouping API endpoints. To replicate this with `FastAPI` I used the
`fastapi-utils` package and it's Class Based Views (`fastapi_utils.cbv`) feature to create
'resources' which helped bundle together the HTTP requests for a specific endpoint.

This was, for me at least, a preferred way of structuring the code. Although a little more
complex for this first simple example, it would allow for a more organised codebase when/if
it was scaled up to create a more complex API service.

**Testing**

After organising the first few endpoints into classes, I wanted to get to grips with testing
in `FastAPI` before I went any further. This was quite simple to set-up following the `FastAPI`
docs and tutorials, and using the `TestClient` and some configuration code ([`test\utils.py`](../tests/utils.py))
it was quite easy to create a test database, send a request to the API and validate the response.