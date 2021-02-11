# rest_api

# Instructions

## Requirements
* Python 3*
* virtualenv
* pip

## Install

`cd` into the `/rest_api` DIR

Using virtualenv:

Install an environment using python 3
`virtualenv -p /usr/bin/python3 ~/rest_api_venv`

activate your `rest_api_venv`
`source ~/rest_api_venv/bin/activate`

Install environment requirements
`pip install -r requirements.txt`


## Run server

`python server.py`

## Run unittest
`python test.py`


## Example run

```
python  server.py
2021-02-10 22:47:53,486 asyncio selector_events.py:59 - DEBUG - Using selector: EpollSelector
^B^[[B2021-02-10 22:48:16,066 handler server.py:56 - INFO - Saved patient_id 1
2021-02-10 22:48:16,066 tornado.access web.py:2239 - INFO - 200 PUT /patients (127.0.0.1) 0.88ms
2021-02-10 22:48:16,069 handler server.py:44 - INFO - Found patient_id 1
2021-02-10 22:48:16,070 tornado.access web.py:2239 - INFO - 200 GET /patients/1 (127.0.0.1) 0.72ms
2021-02-10 22:48:16,073 handler server.py:56 - INFO - Saved patient_id 2
2021-02-10 22:48:16,073 tornado.access web.py:2239 - INFO - 200 PUT /patients (127.0.0.1) 0.55ms
2021-02-10 22:48:16,076 handler server.py:44 - INFO - Found patient_id 1
2021-02-10 22:48:16,077 tornado.access web.py:2239 - INFO - 200 GET /patients/1 (127.0.0.1) 0.69ms
2021-02-10 22:48:16,080 handler server.py:44 - INFO - Found patient_id 2
2021-02-10 22:48:16,080 tornado.access web.py:2239 - INFO - 200 GET /patients/2 (127.0.0.1) 0.55ms
```

```
python test.py
2021-02-10 22:48:16,062 API-client test.py:34 - INFO - PUT:http://localhost:8888/patients
2021-02-10 22:48:16,067 API-client test.py:38 - INFO - Found {'first_name': 'first_name_1', 'last_name': 'last_name', 'date_of_birth': 'date_of_birth', 'phone_number': 'phone_number', 'id': '1'} object
2021-02-10 22:48:16,067 API-client test.py:23 - INFO - GET:http://localhost:8888/patients/1
2021-02-10 22:48:16,070 API-client test.py:27 - INFO - Found {'first_name': 'first_name_1', 'last_name': 'last_name', 'date_of_birth': 'date_of_birth', 'phone_number': 'phone_number', 'id': '1'} object
.2021-02-10 22:48:16,070 API-client test.py:34 - INFO - PUT:http://localhost:8888/patients
2021-02-10 22:48:16,074 API-client test.py:38 - INFO - Found {'first_name': 'first_name_2', 'last_name': 'last_name', 'date_of_birth': 'date_of_birth', 'phone_number': 'phone_number', 'id': '2'} object
2021-02-10 22:48:16,074 API-client test.py:23 - INFO - GET:http://localhost:8888/patients/1
2021-02-10 22:48:16,077 API-client test.py:27 - INFO - Found {'first_name': 'first_name_1', 'last_name': 'last_name', 'date_of_birth': 'date_of_birth', 'phone_number': 'phone_number', 'id': '1'} object
2021-02-10 22:48:16,077 API-client test.py:23 - INFO - GET:http://localhost:8888/patients/2
2021-02-10 22:48:16,081 API-client test.py:27 - INFO - Found {'first_name': 'first_name_2', 'last_name': 'last_name', 'date_of_birth': 'date_of_birth', 'phone_number': 'phone_number', 'id': '2'} object
.
----------------------------------------------------------------------
Ran 2 tests in 0.019s

OK

```