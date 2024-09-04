"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import json
import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import *

logger = get_logger('lumu')


class LUMU:
    def __init__(self, config):
        self.server_url = config.get('server_url')
        if not (self.server_url.startswith('https://') or self.server_url.startswith('http://')):
            self.server_url = 'https://' + self.server_url
        self.server_url = self.server_url.strip('/')
        self.verify_ssl = config.get('verify_ssl')

    def make_request(self, endpoint, method='GET', data=None, params=None, files=None):
        try:
            url = self.server_url + endpoint
            logger.info('Executing url {}'.format(url))
            headers = {'Content-Type': 'application/json'}

            # CURL UTILS CODE
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, endpoint, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.error(f"Error in curl utils: {str(err)}")

            response = requests.request(method, url, params=params, files=files, data=data, headers=headers,
                                        verify=self.verify_ssl)
            if response.ok:
                logger.info('Successfully got response for url {}'.format(url))
                if method.upper() == 'DELETE':
                    return response
                else:
                    return response.json()
            elif response.status_code == 400:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 401:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 404:
                error_response = response.json()
                raise ConnectorError(error_response)
            else:
                logger.error(response.json())
        except requests.exceptions.SSLError:
            logger.error('SSL certificate validation failed')
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            logger.error('The request timed out while trying to connect to the server')
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            logger.error('The server did not send any data in the allotted amount of time')
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            logger.error('Invalid endpoint or credentials')
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(str(err))
            raise ConnectorError(str(err))
        raise ConnectorError(response.text)


def get_incidents(config: dict, params: dict):
    try:
        lu = LUMU(config)
        params = _build_payload(params, get_incidents_dict)
        params_dict = {"key": config.get('company_key'), "page": params.pop("page", 1),
                       "items": params.pop("items", 50)}
        endpoint = '/api/incidents/all'
        return lu.make_request(endpoint=endpoint, method='POST', params=params_dict, data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_incident_by_uuid(config: dict, params: dict):
    try:
        lu = LUMU(config)
        params = _build_payload(params)
        params_dict = {"key": config.get('company_key')}
        endpoint = f"/api/incidents/{params.pop('incident_uuid')}/details"
        return lu.make_request(endpoint=endpoint, method='GET', params=params_dict)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_incident_context(config: dict, params: dict):
    try:
        lu = LUMU(config)
        params = _build_payload(params)
        endpoint = f"/api/incidents/{params.pop('incident_uuid')}/context"
        params.update({"key": config.get('company_key')})
        return lu.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_incident_endpoints(config: dict, params: dict):
    try:
        lu = LUMU(config)
        params = _build_payload(params)
        endpoint = f"/api/incidents/{params.pop('incident_uuid')}/endpoints-contacts"
        params_dict = {"key": config.get('company_key'), "page": params.pop("page", 1),
                       "items": params.pop("items", 50)}
        return lu.make_request(endpoint=endpoint, method='POST', params=params_dict, data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def close_incident(config: dict, params: dict):
    try:
        lu = LUMU(config)
        params = _build_payload(params)
        endpoint = f"/api/incidents/{params.pop('incident_uuid')}/close"
        params_dict = {"key": config.get('company_key')}
        return lu.make_request(endpoint=endpoint, method='POST', params=params_dict, data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def _check_health(config):
    try:
        lu = LUMU(config)
        endpoint = '/api/incidents/all'
        response = lu.make_request(endpoint=endpoint, params={"key": config.get('company_key')})
        if response:
            logger.info("Lumu Connector Available")
            return True
        else:
            return False
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def _build_payload(params: dict, options_dict: dict = {}) -> dict:
    if params.get('other_fields'):
        params.update(params.pop('other_fields'))

    for csv_field in csv_fields:
        if params.get(csv_field) is not None:
            field = params.get(csv_field)
            if isinstance(field, str):
                trimmed_list = [item.strip() for item in field.split(',')]
                params.update({csv_field: trimmed_list})

    return {key: options_dict.get(val, val) if isinstance(val, str) else val for key, val in params.items() if
            isinstance(val, (bool, int)) or val}


operations = {
    "get_incidents": get_incidents,
    "get_incident_by_uuid": get_incident_by_uuid,
    "get_incident_context": get_incident_context,
    "get_incident_endpoints": get_incident_endpoints,
    "close_incident": close_incident
}