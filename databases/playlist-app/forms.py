from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from models import Song

class SongForm(FlaskForm):
    """Form for creating a new song."""
    title = StringField('Song Title', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    submit = SubmitField('Create Song')
    song = SelectField('Song To Add', coerce=int)

def populate_song_choices(form):
    songs = Song.query.all()
    form.song.choices = [(song.id, song.title) for song in songs]

@app.route('/songs/new', methods=['GET', 'POST'])
def create_song():
    """Create a new song."""
    form = SongForm()
    populate_song_choices(form)
    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data
        song = Song(title=title, artist=artist)
        db.session.add(song)
        db.session.commit()
        return redirect('/songs')
    return render_template('create_song.html', form=form)
