Python Client for Open Source Routing Machine Services
======================================================

## Description
This library brings the OSRM API web service to your python application with following OSRM APIs:

- [Match](https://github.com/dayatbflash/osrmpy/blob/master/commands.py#L4)
- [Nearest](https://github.com/dayatbflash/osrmpy/blob/master/commands.py#L11)
- [Route](https://github.com/dayatbflash/osrmpy/blob/master/commands.py#L18)
- [Table](https://github.com/dayatbflash/osrmpy/blob/master/commands.py#L25)
- [Tile](https://github.com/dayatbflash/osrmpy/blob/master/commands.py#L68)
- [Trip](https://github.com/dayatbflash/osrmpy/blob/master/commands.py#L75)


## How to Use
1. open terminal
2. go to your project directory
`cd {PROJECT_DIRECTORY}`
3. clone osrmpy
`git clone https://github.com/dayatbflash/osrmpy.git`
4. and its done, you can import it from your `{PROJECT_DIRECTORY}/osrmpy`

#### Usage Example 
`{PROJECT_DIRECTORY}/test.py`
```python
from osrmpy import osrm

client = osrm.Client('https://router.project-osrm.org')
table_response = client.table.get(sources=[(-6.5962986, 106.7972421)], destinations=[(-6.17126, 106.64404)])

print table_response
````
and if it prints:
```python
{u'sources': [{u'name': u'', u'location': [106.797017, -6.595779]}], u'durations': [[3285.1]], u'code': u'Ok', u'distances': [[67952.4]], u'destinations': [{u'name': u'', u'location': [106.64404, -6.171251]}]}
```
you are doing fine :)

some concerns for the demo server:
- dont worry about the distance(s) or duration(s) differs from yours because it can be updated anytime.
- demo server oftenly returns message `Too many requests`, dont worry its not your fault. just keep trying or just run your own server on local to avoid this matter. you can follow [this guide](https://github.com/Project-OSRM/osrm-backend#using-docker) (use docker)

## Features
As starting point, this library can only request Table. you can see the whole API Documentation [here](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md)

## Requirements
- Python 2.7 or higher

## Contribute
Please feel free to contribute to this repo, it would be appreciated.

