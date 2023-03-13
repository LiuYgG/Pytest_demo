# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 03 月 13 日
  将测试报告发送到邮箱
'''

import smtplib
import os
import email
# 负责构造文本
from datetime import date
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Mail():

    def send_email(self):
        # SMTP 服务器
        mail_host = "Smtp.qq.com"
        # 发件人邮箱
        mail_sender = "952904268@qq.com"
        # 邮箱授权码
        mail_license = "udppllrpezgrbcfc"
        # 邮箱收件人,可以设置多个收件人
        mail_receives = ["952904268@qq.com"]

        # 构建 MIMEMultipart对象代表邮件本身，可以往里面添加文本、图片、附件等
        mm = MIMEMultipart('related')

        # 设置邮件头部内容
        # 邮件主题
        subjcet_content = """ 测试报告 """
        # 设置发送者，注意严格遵守格式，里面邮箱为发件人邮箱
        mm["From"] = "sender_name<952904268@qq.com>"
        # 设置接受者，注意严格遵守格式，里面邮箱为接受者邮箱
        mm["To"] = "receiver_1_name<952904268@qq.com>"
        # 设置邮件主题
        mm["Subject"] = Header(subjcet_content, 'utf-8')

        # 邮件正文内容
        body_content="""您好，测试报告请注意查收"""
        # 构造附件
        atta = MIMEText(open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"reports", "result.html")
                             , 'rb').read(), 'base64', 'utf-8')
        # 设置附件信息
        atta["Content-Disposition"] = 'attachment; filename ="result.html"'
        # 添加附件到邮件信息中去
        mm.attach(atta)

        # 发送邮件
        # 创建 SMTP 对象
        stp = smtplib.SMTP()
        # 设置发件人邮箱的域名和端口
        stp.connect(mail_host, 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        stp.set_debuglevel(1)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        stp.login(mail_sender,mail_license)
        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        stp.sendmail(mail_sender, mail_receives, mm.as_string())
        print("邮件发送成功")
        # 关闭SMTP对象
        stp.quit()

if __name__ == '__main__':
    s = Mail()
    s.send_email()