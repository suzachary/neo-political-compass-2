from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired
from neopolcomp.quiz.questions import questions, default_choices

class QuizForm(FlaskForm):
    question1 = RadioField(questions[0], choices=default_choices, validators=[DataRequired()])
    question2 = RadioField(questions[1], choices=default_choices, validators=[DataRequired()])
    question3 = RadioField(questions[2], choices=default_choices, validators=[DataRequired()])
    question4 = RadioField(questions[3], choices=default_choices, validators=[DataRequired()])
    question5 = RadioField(questions[4], choices=default_choices, validators=[DataRequired()])
    question6 = RadioField(questions[5], choices=default_choices, validators=[DataRequired()])
    question7 = RadioField(questions[6], choices=default_choices, validators=[DataRequired()])
    question8 = RadioField(questions[7], choices=default_choices, validators=[DataRequired()])
    question9 = RadioField(questions[8], choices=default_choices, validators=[DataRequired()])
    question10 = RadioField(questions[9], choices=default_choices, validators=[DataRequired()])
    question11 = RadioField(questions[10], choices=default_choices, validators=[DataRequired()])
    question12 = RadioField(questions[11], choices=default_choices, validators=[DataRequired()])
    question13 = RadioField(questions[12], choices=default_choices, validators=[DataRequired()])
    question14 = RadioField(questions[13], choices=default_choices, validators=[DataRequired()])
    question15 = RadioField(questions[14], choices=default_choices, validators=[DataRequired()])
    question16 = RadioField(questions[15], choices=default_choices, validators=[DataRequired()])
    question17 = RadioField(questions[16], choices=default_choices, validators=[DataRequired()])
    question18 = RadioField(questions[17], choices=default_choices, validators=[DataRequired()])
    question19 = RadioField(questions[18], choices=default_choices, validators=[DataRequired()])
    question20 = RadioField(questions[19], choices=default_choices, validators=[DataRequired()])
    question21 = RadioField(questions[20], choices=default_choices, validators=[DataRequired()])
    question22 = RadioField(questions[21], choices=default_choices, validators=[DataRequired()])
    question23 = RadioField(questions[22], choices=default_choices, validators=[DataRequired()])
    question24 = RadioField(questions[23], choices=default_choices, validators=[DataRequired()])
    question25 = RadioField(questions[24], choices=default_choices, validators=[DataRequired()])
    question26 = RadioField(questions[25], choices=default_choices, validators=[DataRequired()])
    question27 = RadioField(questions[26], choices=default_choices, validators=[DataRequired()])
    question28 = RadioField(questions[27], choices=default_choices, validators=[DataRequired()])
    question29 = RadioField(questions[28], choices=default_choices, validators=[DataRequired()])
    question30 = RadioField(questions[29], choices=default_choices, validators=[DataRequired()])
    submit = SubmitField('Submit Answers')
