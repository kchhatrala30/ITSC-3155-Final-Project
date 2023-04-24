from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rating(db.Model):
    __tablename__ = 'rating'

    rating_id = db.Column(db.Integer, primary_key=True)
    restroom_name = db.Column(db.String(255))
    rating_body = db.Column(db.Text)
    cleanliness = db.Column(db.Numeric(2,1))
    accessibility = db.Column(db.String(255))
    functionality = db.Column(db.Boolean)
    overall = db.Column(db.Numeric(2,1))
    map_tag = db.Column(db.String(255))
    votes = db.Column(db.Integer)
    rater_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    rater = db.relationship('Users', backref='rating_user')

    def __init__(self, restroom_name, cleanliness, overall, rating_body=None, accessibility=None, functionality=None, map_tag=None, votes=None, rater_id=None):
        self.restroom_name = restroom_name
        self.rating_body = rating_body
        self.cleanliness = cleanliness
        self.accessibility = accessibility
        self.functionality = functionality
        self.overall = overall
        self.map_tag = map_tag
        self.votes = votes
        self.rater_id = rater_id


class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    favorite = db.Column(db.String(255))
    picture = db.Column(db.String(255))

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class Comments(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    comment_body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    user = db.relationship('Users', backref='user_comment')
    rating_id = db.Column(db.Integer, db.ForeignKey('rating.rating_id'), nullable=True)
    rating = db.relationship('Rating', backref='rating_comment')
    total_votes = db.Column(db.Integer)

    def __init__(self, comment_body, user_id, rating_id, total_votes):
        self.comment_body = comment_body
        self.user_id = user_id
        self.rating_id = rating_id
        self.total_votes = total_votes


class Rating_votes(db.Model):
    __tablename__ = 'rating_votes'

    id = db.Column(db.Integer, primary_key=True)  # New primary key
    rating_id = db.Column(db.Integer)  # Remove primary_key=True
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    user = db.relationship('Users', backref='user_rating_votes')
    rating_id_vote = db.Column(db.Integer, db.ForeignKey('rating.rating_id'), nullable=True)
    rating = db.relationship('Rating', backref='rating_votes')

    def __init__(self,id, rating_id, upvotes, downvotes, user_id, rating_id_vote):
        self.id = id
        self.rating_id = rating_id
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.user_id = user_id
        self.rating_id_vote = rating_id_vote


class Comment_votes(db.Model):
    __tablename__ = 'comment_votes'

    comment_id = db.Column(db.Integer, primary_key=True)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    user = db.relationship('Users', backref='user_comment_votes')
    comment_id_vote = db.Column(db.Integer, db.ForeignKey('comments.comment_id'), nullable=True)
    comment = db.relationship('Comments', backref='comment_votes')

    def __init__(self, comment_id, upvotes, downvotes, user_id, comment_id_vote):
        self.comment_id = comment_id
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.user_id = user_id
        self.comment_id_vote = comment_id_vote
