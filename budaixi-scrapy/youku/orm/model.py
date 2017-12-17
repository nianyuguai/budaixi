#coding=utf-8
__author__ = 'lixiaojian'

# from orm.dbbase import db

from server import db

####################
# 模型
####################


# scrapy task
class ScrapyTask(db.Model):
    # set table name
    __tablename__ = 't_scrapy_task'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    domain = db.Column(db.String(128))
    start_urls = db.Column(db.String(255))
    url = db.Column(db.String(255))
    album_id = db.Column(db.String(128))
    rule_id = db.Column(db.String(128))
    create_time = db.Column(db.TIMESTAMP())
    update_time = db.Column(db.TIMESTAMP())

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self):
        """Define the string format for instance of ScrapyTask."""
        return "<Model ScrapyTask `{}`>".format(self.id)
