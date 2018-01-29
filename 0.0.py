import requests
import itchat

KEY = '9e44ff190110468eb88d7de0446f14a5'

def get_response(msg):
  apiUrl = 'http://www.tuling123.com/openapi/api'
  data = {
    'key'  : KEY,
    'info'  : msg,
    'userid' : 'lucius_521356@163.com',
  }
  try:
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
  except:
    return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
  print(msg['Text'])
  defaultReply = 'I received: ' + msg['Text']
  reply = get_response(msg['Text'])+'[来自莫斯科的老司机自动回复]'
  return reply or defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()
