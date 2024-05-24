import typing

import os

from django.core.mail import EmailMessage


class MailClient:

	def __init__(self, source: str, template_dir: str, fail_silently: bool = False):
		self.__source = source
		self.__fail_silently = fail_silently
		self.__template_dir = template_dir

	def __render(self, template: str, context: typing.Dict[str, typing.Any]) -> str:
		with open(os.path.join(self.__template_dir, template), 'r') as f:
			email_html = f.read()

		for key, value in context.items():
			email_html = email_html.replace('{{ ' + key + ' }}', str(value))
		return email_html

	def send_mail(
			self,
			subject: str,
			recipient_list: typing.List[str],
			template: str,
			context: typing.Dict[str, typing.Any]
	):
		content = self.__render(template, context)

		email = EmailMessage(
			subject,
			content,
			self.__source,
			recipient_list,
		)
		email.content_subtype = 'html'
		email.send()

	def send_invitation_mail(
			self,
			to: str,
			link: str,
			organisation: str,
	):
		self.send_mail(
			subject=f"Invitation to join {organisation}",
			recipient_list=[to],
			template="invitation.html",
			context={
				"signup_link": link,
				"organization_name": organisation
			}
		)

	def send_reset_password_mail(
			self,
			to: str,
			link: str
	):

		self.send_mail(
			subject=f"Reset Password",
			recipient_list=[to],
			template="reset_password.html",
			context={
				"reset_link": link
			}
		)
