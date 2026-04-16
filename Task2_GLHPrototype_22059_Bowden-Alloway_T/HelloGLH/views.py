from datetime import datetime
from flask import render_template, request
from HelloGLH import app


@app.route('/')
@app.route('/home')
@app.route('/home/<name>')
def home(name=None):
    """Render home page. If a name is provided (path or query param `name`),
    greet the user with that name.
    Examples:
      /home
      /home?name=Alice
      /home/Alice
    """
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Prefer path parameter, fallback to query string
    if not name:
        name = request.args.get('name')

    if name:
        message = f"Hello, {name}"
    else:
        message = "Hello, customer!"

    return render_template(
        "index.html",
        title="Hello, GLH",
        message=message,
        content=" on " + formatted_now,
    )
