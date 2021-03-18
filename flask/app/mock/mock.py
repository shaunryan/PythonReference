import json
import time
from flask import request, Blueprint, current_app

bp = Blueprint('mock',__name__)

@bp.route('/process', methods=['POST'])
def process():

    input = json.loads(request.get_data())

    with open(input['_id'], 'w') as file:
        file.write(input['text'])
    time.sleep(5.0)

    response = {'id' : input['_id']}    
    
    return response 


@bp.route('/_/health', methods=['GET'])
def health():

    return ('ok', 204)


@bp.route('/_/ready', methods=['POST'])
def ready():

    return ({}, 200)

