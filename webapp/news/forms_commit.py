from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.news.models import News


class CommentForm(FlaskForm):
	news_id = HiddenField('ID news', validators=[DataRequired()])
	comment_text = StringField('Text comment', validators=[DataRequired()], render_kw={"class": "large-textarea"})
	submit = SubmitField('Send comment!', render_kw={"class": "btn_primary"})

	def validate_news_id(self, news_id):
		if not News.query.get(news_id.data):
			raise ValidationError('News for this id is not!!!')