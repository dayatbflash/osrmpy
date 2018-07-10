import requests

from commands import Match, Nearest, Route, Table, Tile, Trip

try: # Python 3
    from urllib.parse import urlencode
except ImportError: # Python 2
    from urllib import urlencode

class Client(object):
    def __init__(self, host, port=''):
        self.host = host
        self.port = port

        # OSRM Services
        self.table = Table(self)
        self.route = Route(self)
        self.nearest = Nearest(self)
        self.match = Match(self)
        self.trip = Trip(self)
        self.tile = Tile(self)

    def send_request(
            self, service, version, profile,
            coordinates, params, output_type, with_ssl=False):

        # check host is start with http or not
        url_prefix = ''
        if not self.host.startswith('http'):
            if with_ssl:
                url_prefix = 'https://'
            else:
                url_prefix = 'http://'

        coordinates_str = ';'.join(
            '{},{}'.format(b, a) for (a,b) in coordinates)

        url = '{}{}:{}/{}/{}/{}/{}?{}'.format(
            url_prefix, self.host, self.port, service, version, profile, coordinates_str, 
            urlencode(params))

        r = requests.get(url)

        return {
            'json': r.json,
            'text': r.text,
        }.get(output_type, r.raw)
