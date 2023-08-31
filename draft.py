import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from utils import get_resume_name, get_resume_path

SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]


class Draft:
    sender = "erictao04@gmail.com"

    def __init__(self, company, custom_resume) -> None:
        self.company = company
        self.custom_resume = custom_resume

    def authenticate(self):
        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file(
                'token.json', scopes=SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', scopes=SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return creds

    def set_fields(self, recipient, subject, body, mimeMessage):
        mimeMessage['to'] = recipient
        mimeMessage['From'] = self.sender
        mimeMessage['subject'] = subject
        mimeMessage.attach(MIMEText(body, 'html'))

    def attach_file(self, mimeMessage: MIMEMultipart):
        with open(get_resume_path(self.company, self.custom_resume), 'rb') as content_file:
            myFile = MIMEBase("application", 'pdf')
            myFile.set_payload(content_file.read())
            myFile.add_header('Content-Disposition',
                              'attachment', filename=get_resume_name(self.company, self.custom_resume))
            encoders.encode_base64(myFile)
            mimeMessage.attach(myFile)

    def upload_draft(self, mimeMessage: MIMEMultipart):
        creds = self.authenticate()

        service = build('gmail', 'v1', credentials=creds)

        encoded_string = base64.urlsafe_b64encode(
            mimeMessage.as_bytes()).decode()

        create_message = {
            'message': {
                'raw': encoded_string
            }
        }

        service.users().drafts().create(userId="me",
                                        body=create_message).execute()

    def create_draft(self, recipient, subject, body):
        try:
            mimeMessage = MIMEMultipart()

            self.set_fields(recipient, subject, body, mimeMessage)
            self.attach_file(mimeMessage)
            self.upload_draft(mimeMessage)

            print(f'Successfully created draft for {recipient}')
        except HttpError as error:
            print(f'An error occurred while creating draft for {recipient}')
