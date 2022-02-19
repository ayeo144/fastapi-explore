Part 1: Writing the Application Code
------------------------------------

I chose a ToDo app as the API service as it's quite a basic concept, and I wanted to
focus on methods of deploying such a service more than creating an advanced and 
complicated application.

I chose to use `FastAPI` for this. I already had some experience with `Flask`, but for such
a simple application `FastAPI` seemed like a good choice and gave me an excuse to learn a 
new package.

I also discovered the [`pydantic`](https://pydantic-docs.helpmanual.io/) package through 
reading the `FastAPI` docs, which is a really cool package for helping parse input data 
and enforce strict typing via the standard library `typing` module.