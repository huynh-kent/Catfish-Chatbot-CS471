import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

yml_configs = {}
media_urls = {}
with open('config.yml', 'r') as yml_file, open('media.yml') as media_file:
    yml_configs = yaml.safe_load(yml_file)
    media_urls = yaml.safe_load(media_file)


def send_message(user, body):
    message = g.sms_client.messages.create(
                     body = body,
                     from_ = yml_configs['twillio']['phone_number'],
                     to = user,
                 )
    return json_response(sid = message.sid)

def send_picture(user, picture_name):
    message = g.sms_client.messages.create(
                    from_ = yml_configs['twillio']['phone_number'],
                    media_url = media_urls['images'][f'{picture_name}'],
                    to = user,
    )
    return json_response(sid = message.sid)


