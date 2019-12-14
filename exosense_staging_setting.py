# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

LOGGER_PRINT = os.getenv("LOGGER_PRINT", "CURL")
TIMEOUT = os.getenv('TIMEOUT','300')

# Application
APPLICATION_ID = os.getenv('APPLICATION_ID','a3i8krqel17k00000')

# Browser
BROWSER_PORT = os.getenv('BROWSER_PORT', None)
DEFAULT_BROWSER = os.getenv('DEFAULT_BROWSER', 'chrome')
WINDOW_HEIGHT = os.getenv('WINDOW_HEIGHT', '1080')
WINDOW_WEIGHT = os.getenv('WINDOW_WEIGHT', '1920')

# ExoSense
HOST = os.getenv('HOST', 'https://rcm-graphql.hosted.exosite.io/graphql')
INVALID_USER_GOOGLE = os.getenv('INVALID_USER_GOOGLE', 'invalidexosense@gmail.com')
INVALID_PASSWORD_GOOGLE = os.getenv('INVALID_PASSWORD_GOOGLE', '1234eszxcv')
URL = os.getenv('URL', 'https://exosense-stg.apps.exosite-staging.io')
EXOSENSE_URL = os.getenv('EXOSENSE_URL', URL + '/#/login')
VALID_ADMIN = os.getenv('VALID_ADMIN', 'testing+admin2@exosite.com')
VALID_MAIL = os.getenv('VALID_MAIL', 'testing@exosite.com')
VALID_MANAGER = os.getenv('VALID_MANAGER', 'testing+manager@exosite.com')
VALID_TESTER = os.getenv('VALID_TESTER', 'testing+tester@exosite.com')
VALID_VIEWER = os.getenv('VALID_VIEWER', 'testing+viewer@exosite.com')
VALID_PASSWORD = os.getenv('VALID_PASSWORD', '8ag1n4rfoBw3eUtbiL5p')
VALID_USER_GOOGLE = os.getenv('VALID_USER_GOOGLE', 'testingexosense@gmail.com')
VALID_PASSWORD_GOOGLE = os.getenv('VALID_PASSWORD_GOOGLE', '1234eszxcv++')
VALID_PASSWORD_EXOSENSE = os.getenv('VALID_PASSWORD_EXOSENSE', '1234eszxcv')

ROOT_GROUP = os.getenv('ROOT_GROUP', 'root')
QA_GROUP = os.getenv('QA_GROUP', 'QA-testing')
QA_GROUP_2 = os.getenv('QA_GROUP_2', 'QA-testing2')
QA_INVITED_API_ADMIN = os.getenv('QA_INVITED_API_ADMIN', 'testing+re-use-api-admin@exosite.com')
QA_INVITED_API_MANAGER = os.getenv('QA_INVITED_API_MANAGER', 'testing+re-use-api-manager@exosite.com')
QA_INVITED_API_TESTER = os.getenv('QA_INVITED_API_TESTER', 'testing+re-use-api-tester@exosite.com')
QA_INVITED_API_VIEWER = os.getenv('QA_INVITED_API_VIEWER', 'testing+re-use-api-viewer@exosite.com')
QA_INVITED_USER_NO_LOGIN = os.getenv('QA_INVITED_USER_NO_LOGIN', 'testing+re-use-no-login@exosite.com')
QA_INVITED_WEB_ADMIN = os.getenv('QA_INVITED_WEB_ADMIN', 'testing+re-use-web-admin@exosite.com')
QA_INVITED_WEB_ADMIN_SUB = os.getenv('QA_INVITED_WEB_ADMIN_SUB', 'testing+re-use-web-admin-sub@exosite.com')

# Login
LOGIN_HOST = os.getenv('LOGIN_HOST','rcm-gql.auth0.com')
VALID_CLIENT_ID = os.getenv('VALID_CLIENT_ID', '7664xeY9wkEPmUwVcjmcpqjDRgGYt1TD')
VALID_CONNECTION = os.getenv('VALID_CONNECTION', 'Username-Password-Authentication')
VALID_TENANT = os.getenv('VALID_TENANT', 'rcm-gql')

# Murano
MURANO_BUSINESS_ID = os.getenv('MURANO_BUSINESS_ID','yumeb2ahd1p')
MURANO_BUSINESS_NAME = os.getenv('MURANO_BUSINESS_NAME','QA-ExoSense-Regression')
MURANO_EMAIL = os.getenv('MURANO_EMAIL','testing+exosense@exosite.com')
MURANO_EXOSENSE_ELEMENT_NAME = os.getenv('MURANO_EXOSENSE_ELEMENT_NAME','ExoSense®'.encode().decode('utf-8'))
MURANO_EXOSENSE_PUMPS_ELEMENT_NAME = os.getenv('MURANO_EXOSENSE_PUMPS_ELEMENT_NAME','ExoSense® Pump Template'.encode().decode('utf-8'))
MURANO_HOST = os.getenv('MURANO_HOST','https://bizapi-staging.hosted.exosite.io/api:1/')
MURANO_PASSWORD = os.getenv('MURANO_PASSWORD','1234eszxcv++')
MURANO_URL = os.getenv('MURANO_URL','https://www.exosite-staging.com')

# Product
# Modify these parameters will also effect MuranoData.py
PRODUCT_HOST = os.getenv('PRODUCT_HOST','m2.exosite.io')
PRODUCT_ID = os.getenv('PRODUCT_ID','b2czzweyo5og00000')
DEVICE_QA001 = os.getenv('DEVICE_QA001','QA001')
DEVICE_QA002 = os.getenv('DEVICE_QA002','QA002')
DEVICE_QA003 = os.getenv('DEVICE_QA003','QA003')
DEVICE_QA004 = os.getenv('DEVICE_QA004','QA004')
DEVICE_JENKINS001 = os.getenv('DEVICE_JENKINS001', 'JENKINS001')
DEVICE_JENKINS001_TOKEN = os.getenv('DEVICE_JENKINS001_TOKEN','jenkins001isareallybeautifulcooldeviceee')
SIGNAL_TEMP = os.getenv('SIGNAL_TEMP','Temperature with celsius')
SIGNAL_PERCENTAGE = os.getenv('SIGNAL_PERCENTAGE','Percentage with 2 precision Channel')
SIGNAL_LOCATION = os.getenv('SIGNAL_LOCATION','Taipei Location')
SIGNAL_ELECTRIC = os.getenv('SIGNAL_ELECTRIC','Electric current')
SIGNAL_POWER = os.getenv('SIGNAL_POWER','Power Channel')
SIGNAL_JSON = os.getenv('SIGNAL_JSON','For JsonPanel data')
SIGNAL_TYPE_TEMPERATURE = os.getenv('SIGNAL_TYPE_TEMPERATURE','TEMPERATURE')
SIGNAL_TYPE_PERCENTAGE = os.getenv('SIGNAL_TYPE_PERCENTAGE','PERCENTAGE')
SIGNAL_TYPE_LOCATION = os.getenv('SIGNAL_TYPE_LOCATION','LOCATION')
SIGNAL_TYPE_ELEC_CURRENT = os.getenv('SIGNAL_TYPE_ELEC_CURRENT','ELEC_CURRENT')
SIGNAL_TYPE_POWER = os.getenv('SIGNAL_TYPE_POWER','POWER')
SIGNAL_TYPE_JSON = os.getenv('SIGNAL_TYPE_JSON','JSON')
SIGNAL_UNITS_CELSIUS = os.getenv('SIGNAL_UNITS_CELSIUS','DEG_CELSIUS')
SIGNAL_UNITS_PERCENT = os.getenv('SIGNAL_UNITS_PERCENT','PERCENT')
SIGNAL_UNITS_LAT_LONG = os.getenv('SIGNAL_UNITS_LAT_LONG','LAT_LONG')
SIGNAL_UNITS_AMPERE = os.getenv('SIGNAL_UNITS_AMPERE','AMPERE')
SIGNAL_UNITS_WATT = os.getenv('SIGNAL_UNITS_WATT','WATT')

# Service
RENDERER_HOST = os.getenv('RENDERER_HOST','https://renderer.h.stg.glass-dev.com')

# Token
ADMIN_TOKEN = os.getenv('ADMIN_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3NDA3Mzk2NjIzNTAuMjg1Njg1Nzk0Mzc0MDg0OSIsInRva2VuIjoiSmJoK3JwT3RoNGgvQUd2MHQvajRvQUhSdnJhWFVMRC8vbkJKSllKK1dFMlRwREpmOCtCdTZUTEJCVW5HUkJOZkg0VGY3VnFOZ0tvRStwcWxFUTNoS09MUVU3QTQ4ZDNrTGNTNDZTTHpTaG9LdlV0cklvcjJvOC9HSkJneTUvcXExcUxHK2JjOXBmSXZycWpPdXcvTDgwNENUbzZRdTllWVY1ejZaNUdxMnY4T1R0ZHRtZ0JUTFF4eUI4NXJZNkxsWHVZMDUzZUh6eTd4ZTUxcEtRMjRvYnBkS0NPbWg3YUJWN3hueGdvQzF4OXJVODk0cGZleXNHeW5yV2Y2eTRCRUlGZnhZdUxrNmZIOTNrdzdRN2ptUTFVQnhRNXlHNlpvUnFzVy9BbGd3U1I5R01NN1BjRUNXa2JVR1Z5NHpxSjZNdlh5S080b1BCRXR6RWFmYjVncW1ndz0ifQ==')
MANAGER_TOKEN = os.getenv('MANAGER_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3NDA3MzczNTU1MjAuMDE1NjU3NjUwNDk5MDc5MDgiLCJ0b2tlbiI6ImZTY0s5OGhzVlMvK0lTNXdlV0tlTWFndllReTdsbzNubDdNd1doOVhTWEMzcUxMRHgvR25LV1Ywa21kMWlOY081WVlFRmNMU3ROekc5ME9BZWJhU2JkVStZaG1JQTFMQ05PeUVKdldJWkl4ODJDb25pZisrMmRCY3MzSGwyYjdrN1dNL1FSQlArSzVRU0pHMHBCT04rV3B0SXE0OVJIbytPb1E0NTJzdFJOMUdRancwdnpsQmFKZmRQa081VHNFM2cxN1hnYVdGa3pudE41RTVJOTVZK1hHYWFnQ2tCUGpQMkN1NDl1NlVTbmJtSU5FUkFTVHdWZUc1YTRtV2pkYnBRTXpFOG83OVVBNHZXeHVNRk4yWU9uSWxGZUR5akRtWHlaNDNHb1BxOHRUaVFSa1dkRklXSjZFVTJyYzJnZHBYeFNnalFVd1dFY3MyTEZTWlp6ZVFEUWc9In0=')
TESTER_TOKEN = os.getenv('TESTER_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3NDA3Mzg1MzU1MjAuMzY2NTQ5ODY3MTUxODQ4OCIsInRva2VuIjoiQmdvaWhJaU5Vd29wYnA1bldTeXFNNXZhVUxqL3hLZHVsTzBobEt5VEdhSFBkWCtyL3RpbDdEbGtkNE9VWXBSTkYxdUZkczlVd2h1U1BLM1ZnMzdoeGNBQjh0ZGloYlJXOGdjQkVMZHY1cDRic2ZtL2UvT1RQckVDMWtiRDMrdTNWT2xWMWxTcWl2ZEtnYXg5SnA3c0p1Qzdub1o5SG1ES3F6ZnNKdm1ib1UxaTV0UmFuRldmTXRDNGc1eGZveGtUVm1PbHdNaTNaTXorWlZkV1pNS2hockNzY1VRY3hocTcxd0FCOHBNaGJpVTFjNDNtbDljaWFDeWhxbGluaG5naW0rc1VlTnk1M3lQYUhySDY1ZisrNUFpREFibmVsMHJLeGFCN0NIOEdPanZocHFzR0gxWGNhR0NTa3QzbFZ2emx2SDNPVHBvaHlkVVBBWnFobWtWdVZ1WT0ifQ==')
VIEWER_TOKEN = os.getenv('VIEWER_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3NDA3MzkxMDEwMTAuMjQzOTQ5MTQ5MTc5MDI3NzciLCJ0b2tlbiI6IndkVTUwbmc1MDExbVQxQ1lpUFliOWUxUU1ZNHF6bmhHMkhYcDh0QmJmZC9IMDdGY3F2c3pNVkQrMlVmMlhRZHdVS2JOOUxQV3VpRmYvVDRLMDdVT2tIcTkzUzlXdzdSTUdHRk1yckI5b245LzlBUmVlMEZvQmx5ekMzaWI3MUU2bkYyNUhCN2Q3ZWx4cVc1RlNNaFpXOGJNREQrQkJPa0g1SzJWNkJPQTdCYko2Kyt6SlRPc1c4SlJRQWRXOHdXdzdZNmF5Sm5vcysxYmpTWHYrZ3ladWl3c0dvQWlFcXZxeHNVNDM5R1JBMTlUbm9jQjRGUzB2czVEeVVMNGpabnVkM1NaQnc0OU85Nk9hUE1xWjduck9jNHZsMU5PbmdtSGErVXVXVkpuY3BmbEY4Rk0vcGc1YkpQNEdZODBmdzJ2Vk53Rk5mRFNjbEZBWjJTWWcvbDBlaEE9In0=')
