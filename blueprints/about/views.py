from flask import render_template, Blueprint

about = Blueprint(
    'about', __name__, template_folder='templates'
)


@about.route('/')
def index():
    return render_template('about.html')
