import os
from flask import Flask, request, render_template
import datetime
import random

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) #获取目录地址
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF']) #确保上传的均为图片类型


#生成唯一的图片的名称字符串，防止图片显示时的重名问题
class Pic_str:
    def create_uuid(self):
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
        randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum);
        uniqueNum = str(nowTime) + str(randomNum);
        return uniqueNum;

# 上传照片
@app.route('/up_photo/', methods=["GET","POST"])
def up_photo():
    img = request.files.get("photo")

    if img:
        if str(img.filename.rsplit('.',1)[1]) in ALLOWED_EXTENSIONS: # 判断文件是否为图片类型
            path = basedir + "/static/photo/"
            filename = Pic_str.create_uuid("123") # 随机生成的图片名称
            img_type = "." + img.filename.rsplit('.',1)[1] # 图片类型
            file_path = path + filename + img_type
            img.save(file_path)
            print("图片存储路径为：" + str(file_path))
            print("图片类型为：" + img_type)
            return render_template('success.html')
        else:
            return render_template('fail.html')

    return render_template('hello.html')


if __name__ == '__main__':
    app.run()