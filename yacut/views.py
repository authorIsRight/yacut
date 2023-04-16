from flask import flash, redirect, render_template

from yacut import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id, is_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_id()
    elif not is_unique_short_id(custom_id):
        flash(f'Имя {custom_id} уже занято!', 'not_unique_error')
        return render_template('index.html', form=form)
    new_url = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    db.session.add(new_url)
    db.session.commit()
    return render_template('index.html', url=new_url, form=form)


@app.route('/<short_id>')
def redirect_from_short(short_id):

    obj = URLMap.query.filter(URLMap.short == short_id).first_or_404()
    original_link = obj.original
    return redirect(original_link)


@app.route('/easteregg')
def index():
    return redirect('https://youtu.be/dQw4w9WgXcQ')