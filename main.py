import re

from loguru import logger
from RSS import my_trigger as tr
from RSS.rss_class import Rss
from RSS.bot import robot

@robot.filter("1")
def hello_world():
    return '喵喵喵🐱'

@robot.filter(re.compile("订阅 (.*)"))
def add(message,session,match):
    logger.info("进入处理逻辑")
    user=message.source
    name=match.group(1)
    if name not in ["教务通知"]:
        return "暂不支持该订阅！"

    rss = Rss()
    
    def add_user(_rss:Rss,_openid):
        _rss.add_user_or_group(user=_openid)
        tr.add_job(_rss)
        logger.info("添加成功")

    rss_tmp = rss.find_name(name=name)
    if rss_tmp is not None:
        add_user(rss_tmp, user)
    else:
        # 当前名称、url都不存在
        rss.name = name
        url = "/bilibili/user/dynamic/353703267"
        rss.url = url
        add_user(rss, user)

    return "订阅成功！"

@robot.templatesendjobfinish_event
def _(message):
    logger.info(message)
    return None

#robot.run()

import tornado.ioloop
import tornado.web
from werobot.contrib.tornado import make_handler
application = tornado.web.Application([
    (r"/", make_handler(robot)),
])

application.listen(80)
tornado.ioloop.IOLoop.instance().start()