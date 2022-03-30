import werobot
from secret import TOKEN,APP_ID,APP_SECRET

robot = werobot.WeRoBot(token=TOKEN)
robot.config["APP_ID"] = APP_ID
robot.config["APP_SECRET"] = APP_SECRET
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
client = robot.client