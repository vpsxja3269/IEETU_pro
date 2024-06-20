from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('제목을 입력해주세요.', validators=[DataRequired()], render_kw={"class": "form-control"})
    content = TextAreaField('내용', validators=[DataRequired()], render_kw={"class": "form-control"})
    author = StringField('작성자', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('제출', render_kw={"class": "btn btn-primary"})
