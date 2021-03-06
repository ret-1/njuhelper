import re

from loguru import logger
from RSS import my_trigger as tr
from RSS.rss_class import Rss
from RSS.bot import robot

@robot.filter("1")
def hello_world():
    return 'åµåµåµð±'

@robot.filter(re.compile("è®¢é (.*)"))
def add(message,session,match):
    logger.info("è¿å¥å¤çé»è¾")
    user=message.source
    name=match.group(1)
    if name not in ["æå¡éç¥"]:
        return "æä¸æ¯æè¯¥è®¢éï¼"

    rss = Rss()
    
    def add_user(_rss:Rss,_openid):
        _rss.add_user_or_group(user=_openid)
        tr.add_job(_rss)
        logger.info("æ·»å æå")

    rss_tmp = rss.find_name(name=name)
    if rss_tmp is not None:
        add_user(rss_tmp, user)
    else:
        # å½ååç§°ãurlé½ä¸å­å¨
        rss.name = name
        url = "/bilibili/user/dynamic/353703267"
        rss.url = url
        add_user(rss, user)

    return "è®¢éæåï¼"

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