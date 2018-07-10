from bases import BaseCommand
from errors import EmptyCoordinatesError

class Match(BaseCommand): 
    def __init__(self, client):
        super(Match, self).__init__(client)

    def get(self):
        raise NotImplementedError
    
class Nearest(BaseCommand):
    def __init__(self, client):
        super(Nearest, self).__init__(client)

    def get(self):
        raise NotImplementedError

class Route(BaseCommand):
    def __init__(self, client):
        super(Route, self).__init__(client)

    def get(self):
        raise NotImplementedError

class Table(BaseCommand):
    def __init__(self, client):
        super(Table, self).__init__(client)
    
    def get(self, profile='v1', sources=[],
            destinations=[], distance=True, duration=True):

        coordinates = sources + destinations
        if not coordinates:
            raise EmptyCoordinatesError

        # index for sources [first_idx:second_idx]
        # index for destinations [second_idx:third_idx]
        first_idx = 0
        second_idx = len(sources)
        third_idx = second_idx + len(destinations)

        sources_idx = list(range(first_idx, second_idx))
        destinations_idx = list(range(second_idx, third_idx))

        params = {}

        if sources:
            params['sources'] = ';'.join(map(str, sources_idx))

        if destinations:
            params['destinations'] = ';'.join(map(str, destinations_idx))

        annotations = []
        if duration:
            annotations.append('duration')
        if distance:
            annotations.append('distance')
        
        if annotations:
            params['annotations'] = ','.join(annotations)


        return super(Table, self).request(
            service='table', coordinates=coordinates,
            params=params)


class Tile(BaseCommand):
    def __init__(self, client):
        super(Tile, self).__init__(client)

    def get(self):
        raise NotImplementedError

class Trip(BaseCommand):
    def __init__(self, client):
        super(Trip, self).__init__(client)

    def get(self):
        raise NotImplementedError
