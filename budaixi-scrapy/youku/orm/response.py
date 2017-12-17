#coding=utf-8
__author__ = 'lixiaojian'


rsp = {
    'code':'0',
    'msg':'success',
    'data':None
}


class Rsp(object):

    content = {
        'code':'0',
        'msg':'success',
        'data':None
    }

    def __init__(self):
        pass

    def ok(self, data):
        self.content = rsp
        self.content['data'] = data
        return self.content

    def fail(self, code='-1', msg=None):
        self.content = rsp
        self.content['code'] = code
        self.content['msg'] = msg
        return self.content
