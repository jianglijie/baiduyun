from databases.ext import db
from sqlalchemy.dialects.mssql import TINYINT


class ShareUser(db.Model):
    uid = db.Column(db.BigInteger, primary_key=True)
    user_name = db.Column(db.String(50))
    uk = db.Column(db.BigInteger, unique=True)
    avatar_url = db.Column(db.String(200))
    intro = db.Column(db.TEXT)
    follow_count = db.Column(db.INTEGER)
    fans_count = db.Column(db.INTEGER)
    pubshare_count = db.Column(db.INTEGER)
    album_count = db.Column(db.INTEGER)
    last_visited = db.Column(db.INTEGER)
    weight = db.Column(TINYINT)
    create_time = db.Column(db.INTEGER)
    visited_count = db.Column(db.INTEGER, default=0)

    def __init__(self, uid, user_name, uk, avatar_url, intro, follow_count, fans_count, pubshare_count, album_count,
                 last_visited, weight, create_time,visited_count):
        self.uid = uid
        self.user_name = user_name
        self.uk = uk
        self.avatar_url = avatar_url
        self.intro = intro
        self.follow_count = follow_count
        self.fans_count = fans_count
        self.pubshare_count = pubshare_count
        self.album_count = album_count
        self.last_visited = last_visited
        self.weight = weight
        self.create_time = create_time
        self.visited_count = visited_count
