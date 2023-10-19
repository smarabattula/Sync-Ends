import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def post_data_to_email(data):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Use the appropriate SMTP port
    sender_email = 'gudhe_varun@srmap.edu.in'
    sender_password = 'tjiv cxxw iyzs nuho'
    receiver_email = 'smaraba@ncsu.edu'
    subject = 'Postman API Changes'
    
    for x in data:
        if x is not None and len(x) > 0:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            message = x
            msg.attach(MIMEText(message, 'plain'))
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()  # Enable TLS encryption
                server.login(sender_email, sender_password)

                # Send the email
                server.sendmail(sender_email, receiver_email, msg.as_string())

                print('Email sent successfully')
            except Exception as e:
                print('Error sending email:', str(e))
            finally:
                server.quit()  
data=['''1)  EndPoint Name: Create mock purchase
URL: {{baseUrl}}/post
Request Method: POST''',
'''2)  EndPoint Name: Create mock blog post
URL: {{baseUrl}}/post
Request Method: POST''',
'''3)  EndPoint Name: sasank_tried_this
URL: https://api.getpostman.com/mocks?test key=test value
Request Method: GET''']
post_data_to_email(data)                
# # Email configuration
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587  # Use the appropriate SMTP port
# sender_email = 'gudhe_varun@srmap.edu.in'
# sender_password = 'tjiv cxxw iyzs nuho'
# receiver_email = 'varundeepakchowdary@gmail.com'
# subject = 'Postman API Changes'
# message = 'Body of your email'

# # Create a MIMEText object
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg['Subject'] = subject

# # Attach the message to the email
# msg.attach(MIMEText(message, 'plain'))

# # Create an SMTP connection
# try:
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()  # Enable TLS encryption
#     server.login(sender_email, sender_password)

#     # Send the email
#     server.sendmail(sender_email, receiver_email, msg.as_string())

#     print('Email sent successfully')
# except Exception as e:
#     print('Error sending email:', str(e))
# finally:
#     server.quit()  # Close the SMTP server connection



#     # def post_data_to_slack(self, data):

#     #     try:
#     #         slack_web_client = WebClient(
#     #             # Add the slack access token here
#     #             token=self.slack_token
#     #         )

#     #         response_true_cnt = 0
#     #         for x in data:
#     #             if x is not None and len(x) > 0:
#     #                 message = {
#     #                     "channel": self.slack_channel,
#     #                     "blocks": [
#     #                         {
#     #                             "type": "section",
#     #                             "text": {"type": "plain_text", "text": x},
#     #                         }
#     #                     ],
#     #                 }
#     #                 response = slack_web_client.chat_postMessage(**message)

#     #                 if response:
#     #                     response_true_cnt += 1
#     #     except SlackApiError as e:
#     #         return e

#     #     return response_true_cnt