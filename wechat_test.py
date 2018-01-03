import itchat
import os
from PIL import ImageGrab
import datetime


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    # os.system(msg['Text'])
    print(msg.ToUserName)
    if msg.ToUserName == 'filehelper':
        if msg.Text == '截图':
            filename = datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
            filename = "temp/" + filename + '.jpg'
            # im = ImageGrab.grab(bbox = (380, 300, 1350, 1015))
            im = ImageGrab.grab()
            im.save(filename, 'jpeg')
            print('截图')
            itchat.send_image(fileDir=filename, toUserName='filehelper')
        else:
            os.system(msg.text)


itchat.auto_login(hotReload=True)
itchat.run()
