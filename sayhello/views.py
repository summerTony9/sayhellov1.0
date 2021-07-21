from flask import flash, redirect, url_for, render_template
from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('index'))
    messages = Message.query.all()
    return render_template('index.html', form=form, messages=list(reversed(messages)))
