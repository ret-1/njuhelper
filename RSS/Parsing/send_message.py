from typing import Any, Dict
from loguru import logger
from ..rss_class import Rss
from ..bot import client
from ..secret import template

async def send_msg(rss: Rss, msg: Dict[str, Any], item: Dict[str, Any]) -> bool:
    data={
        "first": {
            "value": "订阅已更新"
        },
        "keyword1": {
            "value": msg["title"]
        },
        "keyword2": {
            "value": "订阅"
        },
        "keyword3": {
            "value": msg["date"]
        },
        "keyword4": {
            "value": "南哪小助手"
        },
        "keyword5": {
            "value": msg["title"]
        },
        "remark": {
            "value": "测试模板消息"
        },
    }
    for user in rss.user_id:
        logger.info("开始发送")
        ret = client.send_template_message(user,template,data,url=msg['link'])
        if ret["errcode"] != 0:
            logger.error(ret)