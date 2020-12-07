#coding=utf-8
'''
Created on 2019-7-28

@author: LiPing
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

class MailUtils():
	
	@classmethod
	def send_test_report(cls):
		#邮件信息配置. 授权码daL28TenRatvg75c'
		sender = 'liping@91jinrong.com'
		receiver = 'liping@91jinrong.com' 
		auth_code = 'daL28TenRatvg75c'  #设置客户端授权码，不是密码

		'smtp.exmail.qq.com'
		subject = '旺财自动化测试报告'

		#读取文件内容
		f = open("./result.html", 'rb')
		mail_body = f.read()
		f.close()

		#HTML 形式的文件内容
		html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
		html['Subject'] = subject
		html['from'] = sender
		html['to'] = receiver

		# html附件 将测试报告放在附件中发送
		att1 = MIMEText(mail_body, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="TestWangcaiReport.html"'  # 这里的filename可以任意写

		msg = MIMEMultipart()
		msg['Subject'] = subject  # 邮件的标题
		msg.attach(html)  # 将html附加在msg里
		msg.attach(att1)  # 新增一个附件 

		#连接 登录 上smtp服务器
		smtp = smtplib.SMTP() 
		smtp.connect('smtp.exmail.qq.com') 
		smtp.login(sender, auth_code) 

		#发送邮件
		smtp.sendmail(sender, receiver, msg.as_string()) 
		smtp.quit()
