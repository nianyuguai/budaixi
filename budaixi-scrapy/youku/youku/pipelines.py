# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class YoukuPipeline(object):
    def process_item(self, item, spider):
        db_config = spider.settings.get('DB_CONFIG')
        con = pymysql.connect(**db_config)
        # con.set_character_set('utf8')

        cur = con.cursor()
        # cur.execute('SET NAMES utf8;')
        # cur.execute('SET CHARACTER SET utf8;')
        # cur.execute('SET CHARACTER_SET_CONNECTION=utf8;')
        sql = ("replace into t_video (id, album_id, title, url, img_url) "
               "VALUES (%s, %s, %s, %s, %s)")

        list = (
            item['id'],
            item['album_id'],
            item['title'],
            item['url'],
            item['img_url']
        )


        try:
            cur.execute(sql, list)
            con.commit()
        except Exception as e:
            con.rollback()
        finally:
            cur.close()
            con.close()

        return item

