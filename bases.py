import json

class BaseCommand(object):
    def __init__(self, client):
        self.client = client

    def request(
            self, service=None, version='v1', profile='driving',
            coordinates=[], params={}, output_type='text'):

    	# set generate_hints default to false
    	params['generate_hints'] = 'false'
    	
        response = self.client.send_request(
            service, version, profile, 
            coordinates, params, output_type)

        return json.loads(response)
