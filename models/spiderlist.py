from databases.ext import db
from sqlalchemy.dialects.mssql import TINYINT


class SpiderList(db.Model):
    sid = db.Column(db.BigInteger, primary_key=True)
    uk = db.Column(db.BigInteger)
    file_fetched = db.Column(db.INTEGER, default=0)
    follow_fetched = db.Column(db.INTEGER, default=0)
    follow_done = db.Column(TINYINT, default=0)
    file_done = db.Column(TINYINT, default=0)
    weight = db.Column(TINYINT, default=5)
    uid = db.Column(db.BigInteger, default=0)

    def __init__(self, sid, uk, file_fetched, follow_fetched, follow_done, file_done, weight, uid):
        self.sid = sid
        self.uk = uk
        self.file_fetched = file_fetched
        self.follow_fetched = follow_fetched
        self.follow_done = follow_done
        self.file_done = file_done
        self.weight = weight
        self.uid = uid
