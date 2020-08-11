import json
import logging

import requests

from app.shared.helpers import Helpers, MyEncoder
from app.shared.variables import Variables


class ApiService(object):

    api_key = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ApiService, cls).__new__(cls)
            cls.instance.on_init()
        return cls.instance

    def on_init(self):
        from app.shared.storage_service import StorageService

        self.api_key = StorageService().get_value('api_key')
        pass

    def reply_finished(self):

        pass

    def request(self, url, query, on_success, on_error):

        request_url = Variables().url_api + url
        body = json.dumps(query, cls=MyEncoder)

        logging.debug(request_url)
        logging.debug(body)

        headers = {'User-Agent': 'TarderSync 0.1', 'Content-Type': 'application/json'}

        if self.api_key:
            headers = {'User-Agent': 'TarderSync 0.1', 'Content-Type': 'application/json', 'apikey': self.api_key}

        response = requests.put(request_url, data=body, headers=headers)

        response_data = response.text

        logging.debug(response_data)

        if response.status_code == requests.codes.ok:
            logging.debug('Success')
            if len(response_data) > 0 and (response_data.startswith('{') or response_data.startswith('[')):
                result = json.loads(response_data)
                result = Helpers.to_obj(result)
            else:
                result = None
            on_success(result)
        else:
            if len(response_data) > 0 and (response_data.startswith('{') or response_data.startswith('[')):
                error_text = json.loads(response_data)
                error_text = Helpers.to_obj(error_text)
                if error_text.error:
                    error_text = error_text.error.message
                else:
                    error_text = reply.errorString()
            else:
                error_text = reply.errorString()
            logging.error(error_text)
            on_error(error_text)

        pass

    def get_key(self, query, on_success, on_error):
        self.request('sync/getApiKey', query, on_success, on_error)

    def login(self, query, on_success, on_error):
        self.request('sync/login', query, on_success, on_error)

    def get_companies(self, query, on_success, on_error):
        self.request('sync/getCompanies', query, on_success, on_error)

    def get_items(self, query, on_success, on_error):
        self.request('sync/getItems', query, on_success, on_error)

    def get_points(self, query, on_success, on_error):
        self.request('sync/getPoints', query, on_success, on_error)

    def upload_amounts(self, query, on_success, on_error):
        self.request('sync/updateAmounts', query, on_success, on_error)