#coding=utf-8
__author__ = 'lixiaojian'

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from orm.response import Rsp
from orm.marshal import quick_marshal

import logging
import json
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/spider'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
db_session=db.session

# after db init
from orm.model import *


@app.route('/')
def index():
    return 'flask'

@app.route('/scrapy/run', methods=['POST'])
def scrapy_run():
    spider_name = "youku"
    subprocess.check_output(['scrapy', 'crawl', spider_name])
    return json.dumps({'code': '0', 'msg': 'success'})

@app.route('/scrapy/task', methods=['POST'])
def scrapy_task_create():

    rsp = Rsp()
    try:
        task = request.get_json()
        app.logger.info("receive scrapy task -> %s", task)
        t = ScrapyTask(**task)

        if t.id:
            ScrapyTask.query.filter(ScrapyTask.id == t.id).update(dict(task))
        else:
            db_session.add(t)
        db_session.commit()
        rsp.ok(t.id)

    except Exception as e:
        app.logger.error("scrapy_task_create error", e)
        rsp.fail(msg='connect db error')

    app.logger.info("scrapy task rsp: %s", rsp.content)

    return json.dumps(rsp.content)

@app.route('/scrapy/task', methods=['GET'])
def scrapy_task_query():
    id = request.args.get('id', type=int)
    page_no = request.args.get('page_no', type=int, default=1)
    page_size = request.args.get('page_size', type=int, default=10)

    rsp = Rsp()
    query = ScrapyTask.query

    if id:
        query = query.filter(ScrapyTask.id == id)
    if page_no and page_size:
        query = query.paginate(page=page_no, per_page=page_size)

    rsp.ok(quick_marshal(ScrapyTask)(query.items))
    rsp.content['total'] = query.total

    app.logger.info("scrapy task query rsp: %s", rsp.content)

    return json.dumps(rsp.content)


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s %(levelname)s [%(threadName)s] - %(filename)s:%(lineno)s[%(funcName)s]: %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)

    app.run()