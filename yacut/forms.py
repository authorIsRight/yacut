from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Это не ссылка')],
    )

    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 16),
                    Optional(),
                    Regexp(regex=r'^[a-zA-Z\d]{1,16}$',
                           message='Только латиница и цифры')
                    ]

    )
    submit = SubmitField('Создать')
