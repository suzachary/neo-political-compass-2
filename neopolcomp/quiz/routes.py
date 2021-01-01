from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from neopolcomp import db
from neopolcomp.models import QuizResult
from neopolcomp.quiz.forms import QuizForm

quiz = Blueprint('quiz', __name__)

@login_required
@quiz.route("/quiz", methods=['GET', 'POST'])
def quiz_questions():
    if not current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = QuizForm()
    if form.validate_on_submit():
        # calculate scores
        econ = 0
        econ -= int(form.question1.data)
        econ += int(form.question2.data)
        econ -= int(form.question3.data)
        econ -= int(form.question4.data)
        econ += int(form.question5.data)
        econ += int(form.question6.data)
        econ -= int(form.question7.data)
        econ -= int(form.question8.data)
        econ += int(form.question9.data)
        econ += int(form.question10.data)

        social = 0
        social -= int(form.question11.data)
        social -= int(form.question12.data)
        social -= int(form.question13.data)
        social += int(form.question14.data)
        social -= int(form.question15.data)
        social += int(form.question16.data)
        social -= int(form.question17.data)
        social += int(form.question18.data)
        social += int(form.question19.data)
        social += int(form.question20.data)

        ethics = 0
        ethics -= int(form.question21.data)
        ethics += int(form.question22.data)
        ethics += int(form.question23.data)
        ethics -= int(form.question24.data)
        ethics -= int(form.question25.data)
        ethics += int(form.question26.data)
        ethics -= int(form.question27.data)
        ethics += int(form.question28.data)
        ethics += int(form.question29.data)
        ethics += int(form.question30.data)

        print("scores: " + str(econ + social + ethics))

        # store new result
        result = QuizResult(econ_score=econ, social_score=social, ethics_score=ethics, author=current_user)
        db.session.add(result)
        db.session.commit()

        # flash message and redirect home
        flash('Your quiz has been submitted.', 'success')
        return redirect(url_for('main.home'))
    return render_template('quiz.html', title='Quiz', form=form, legend='Quiz')

