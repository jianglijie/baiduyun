from databases.ext import db
from sqlalchemy.dialects.mysql import TINYINT


class ShareFile(db.Model):
    fid = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(100))
    uk = db.Column(db.BigInteger)
    short_url = db.Column(db.String(15))
    is_dir = db.Column(TINYINT, index=True)
    size = db.Column(db.BigInteger)
    md5 = db.Column(db.String(32))
    share_id = db.Column(db.String(20))
    deleted = db.Column(TINYINT, default=0)
    d_cnt = db.Column(db.INTEGER, default=0)
    ext = db.Column(db.String(10))
    create_time = db.Column(db.INTEGER)
    file_type = db.Column(TINYINT, index=True, doc='0:video;1:image;2:document;3:music;4:package;5:software')
    uid = db.Column(db.BigInteger, index=True)
    feed_type = db.Column(db.String(10), default='share', index=True)
    feed_time = db.Column(db.INTEGER)
    indexed = db.Column(TINYINT, default=0, index=True)

    def __init__(self, fid, title, uk, short_url, is_dir, size, md5, share_id, deleted, d_cnt, ext, create_time,
                 file_type, uid, feed_type, feed_time, indexed):
        self.fid = fid
        self.title = title
        self.uk = uk
        self.short_url = short_url
        self.is_dir = is_dir
        self.size = size
        self.md5 = md5
        self.share_id = share_id
        self.deleted = deleted
        self.d_cnt = d_cnt
        self.ext = ext
        self.create_time = create_time
        self.file_type = file_type
        self.uid = uid
        self.feed_type = feed_type
        self.feed_time = feed_time
        self.indexed = indexed
