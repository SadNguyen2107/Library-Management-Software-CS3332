from flask import Flask

import smtplib
from email import encoders
from email.mime.text import MIMEText # The Text going to use
from email.mime.base import MIMEBase # To Use for the Attachment
from email.mime.multipart import MIMEMultipart


class Mail:
    def init_app(self, app: Flask):
        self.user = app.config['USER']
        self.password = app.config['PASSWORD']

    def send_mail_to(self,
        mail_from: str,
        mail_to: str, 
        mail_subject: str,
        plain_message: str,
        html_message: str,
        image_directory: str
    ):
        #? Use SMTP to send mails

        #* 1st Step: Write Python Script to Log into existing email account
        #* 2nd Step: Use SMTP + Python Script -> Send mail from that account

        stmp_server = 'smtp.office365.com'      # or smtp.gmail.com
        stmp_port = 587  # Use TLS
        server = smtplib.SMTP(stmp_server, stmp_port)
        server.starttls()    # Enable TLS
        
        # Log into the account
        server.login(user=self.user, password=self.password)

        #* 1st Step: Create a message
        #? A Mail consisting of multiple parts of attachment of message  
        msg = MIMEMultipart()

        # Define the header
        msg['From'] = mail_from
        msg['To'] = mail_to
        msg['Subject'] = mail_subject

        
        # If has plain_message
        if plain_message:
            # Not adding the txt file to the mail
            #? Are Adding the text      
            msg.attach(MIMEText(plain_message, 'html'))      # plain or html

        # If has html_message
        if html_message:
            msg.attach(MIMEText(html_message, 'html'))

        # If has image file
        if image_directory:
            #? Image has to be open in Binary Mode
            with open(image_directory, 'rb') as attachment:
                # Create a payload object
                payload = MIMEBase('application', 'octet-stream')   # octet-stream: Stream to process Image

                #Set the payload of this payload to attachment to the filestream
                payload.set_payload(attachment.read())

                # Encode the image data that we just read and that we set as a payload
                encoders.encode_base64(payload)
                payload.add_header('Content-Disposition', f'attachment; filename="{image_directory}"')

                # Payload has to attach to the message
                msg.attach(payload)


        # Get the whole thing as a string
        # Then this string is going to be sent by the server
        text = msg.as_string()
        server.sendmail(mail_from, mail_to, text)

        # Quit the server
        server.quit()
        