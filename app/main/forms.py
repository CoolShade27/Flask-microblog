from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import User
from flask_babel import _, lazy_gettext as _l
from flask import request

class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=256)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Username already taken!'))

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    post = TextAreaField(
        _l('Write something...'),
        validators=[DataRequired(), Length(min=1, max=256)]
    )
    submit = SubmitField(_l('Submit'))

class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)