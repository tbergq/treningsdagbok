import smtplib
import email
from Account.models import SystemSettings



class MailService():
	def send_mail(self, reciever, message):
		msg = email.message_from_string(message)
		msg['From'] = SystemSettings.objects.get(key='sender-email').value
		msg['To'] = reciever
		msg['Subject'] = 'Password reset'

		smtpObj = smtplib.SMTP(SystemSettings.objects.get(key='smtp-address').value, '587')
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.ehlo()
		smtpObj.login(msg['From'], SystemSettings.objects.get(key='email-password').value)
		
		smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
		smtpObj.quit()

	def test(self, message):
		print "test: %s" % message