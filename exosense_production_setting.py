# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

LOGGER_PRINT = os.getenv("LOGGER_PRINT", "CURL")
TIMEOUT = os.getenv('TIMEOUT','300')

# Application
APPLICATION_ID = os.getenv('APPLICATION_ID','yfm9l48s1h5k0000')

# Browser
BROWSER_PORT = os.getenv('BROWSER_PORT', None)
DEFAULT_BROWSER = os.getenv('DEFAULT_BROWSER', 'chrome')
WINDOW_HEIGHT = os.getenv('WINDOW_HEIGHT', '1080')
WINDOW_WEIGHT = os.getenv('WINDOW_WEIGHT', '1920')

# ExoSense
HOST = os.getenv('HOST', 'https://exosense-gql-qabot.hosted.exosite.io/graphql')
INVALID_USER_GOOGLE = os.getenv('INVALID_USER_GOOGLE', 'invalidexosense@gmail.com')
INVALID_PASSWORD_GOOGLE = os.getenv('INVALID_PASSWORD_GOOGLE', '1234eszxcv')
URL = os.getenv('URL', 'https://exosense-qabot.apps.exosite.io')
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
MURANO_BUSINESS_ID = os.getenv('MURANO_BUSINESS_ID','by6znzezzcj')
MURANO_BUSINESS_NAME = os.getenv('MURANO_BUSINESS_NAME','QA-Vertical-Project')
MURANO_EMAIL = os.getenv('MURANO_EMAIL','testing+exosense+robot@exosite.com')
MURANO_EXOSENSE_ELEMENT_NAME = os.getenv('MURANO_EXOSENSE_ELEMENT_NAME','ExoSense®'.encode().decode('utf-8'))
MURANO_EXOSENSE_PUMPS_ELEMENT_NAME = os.getenv('MURANO_EXOSENSE_PUMPS_ELEMENT_NAME','ExoSense® Pump Template'.encode().decode('utf-8'))
MURANO_HOST = os.getenv('MURANO_HOST','https://bizapi.hosted.exosite.io/api:1/')
MURANO_PASSWORD = os.getenv('MURANO_PASSWORD','DoQLrd0oBI5DjvpWkadw')
MURANO_URL = os.getenv('MURANO_URL','https://www.exosite.io')

# Product
# Modify these parameters will also effect MuranoData.py
PRODUCT_HOST = os.getenv('PRODUCT_HOST','m2.exosite.io')
PRODUCT_ID = os.getenv('PRODUCT_ID','m1ksokgrdrd4w0000')
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
ADMIN_TOKEN = os.getenv('ADMIN_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3MDE5NzE3NzY5MTAuOTEyMDkxMTkxNDcyODM2OSIsInRva2VuIjoib1dOamRzSTFKL1VTMERHQjdpcmFsSHFzY3hQcDhESW0zdVhSQ0hkQkx5YTltdmViZy9tTVZqMEZRbGYyRHN2djY1Q2RNdTVQV3NBcTlFWDBFUXl4Zlc1NEpZQUFMMFhsc2JzSlplRkdOUnJFY04zVkk0RGlSY1pGcEJnNERaVWxtcVk0cmdJR3dRd0xSVjJDeXd3Q21RcERDZ3pKd1F0QUtwS2xQK1VQZVE0eEFrV1kvRzZnQm43OGhpMk9hMjhjaHk1MVh5RldyU3ZMMTZ4Rkw2clFhNDEwV3U2Z3dmRjRKYVI0em1tUDEwaUJrNzljQnNWVjJDWG0waHQwL2l6cFBRb0haaW9nNDR6ZFZza09JVHN4TGdqSnI1UzFWWWt4N3NaUlI0SW82aHZBUVQ3ekVSVGQvTC92ZXZJRmlncTdkbFVQUXQ0bHY5MFIwN2Frc3lIQk1rND0ifQ==')
MANAGER_TOKEN = os.getenv('MANAGER_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3MDE5NzE5OTEyNzAuMDc4NjYzNzMwMjY4MjQ5OCIsInRva2VuIjoiejczNGo3WlZVRXdMRnNvQWZ2MFppUklSSzE0Z094R3dIclFmKzVldGJXVFBNbzlaUU0rTWZkclBMNEI5Y3d2VG1OaGFQaG42NTY2WmliQzNiWmNxL0xSQ050aDV2d1dFM2x4OTZVU0VuYkE1MSthS01WdXN4b29CeUgzeTR4eE1RK3pvT3VLZFhmUEtrOERRbW5lSDZLV2laSmVkTHNOOHc1bkJFbFhQcEhqQ2pNcENyOU9qZXgwVlZNZW5ETWpBR3FHRUg2TmpUQlVRTVAxK0R0NDkvMCtsc2NGYjNWNFJ5dDk4ZVdBVmJuSER6Y1FHazMrVzBrSkIyd1RYcXl4bTZ4UjVrdkdoNWZRTGVoT2NTKzNtdFZ3Y2FzYkVXVjJCcXBzRVpJUHRMWWhTRFc5QTU3NjgxRVE0ZURCTWpMeHYyZ29PMXZ2NWM5VTNJeHFCRDR6UG96UT0ifQ==')
TESTER_TOKEN = os.getenv('TESTER_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3MDE5NzIyMjc3MzAuMjc0MjYyMDMwNTE3Nzc2MSIsInRva2VuIjoiNUZyVE4wR3oxNEI4L0lYaUZUTmdncUErV3U4S09vZmQ4d2tsdTgweHI2eVphQjc5VjZuZ3RBOFIvT3BUdFp6RmI4RGs3bkFpbEV3aWhobjl1WlJUVU85alBrSzNvWjI5RytQb3dRZ3ZSczRUKzlxMTN4YnNucHNpOFlodVVwbzM3OXAvZDd1ZUttL3dML0JISkFNWnc0eWRDOFdabGVITUxJMkQzdkk4WDBGd2k1UlJ2dnZxK3FheWtGNStnWWxIZHJ2VHFRMEM0TUgxSEJ0NTJQakJXUUZORXYvc1pXYmowRFNnOUtUaHRFbHB4RVFHQW1kcktPZ2ZvTU1oRlJWZFJZbk5VQm44elRmd2dvR3JvanFVeGdldC9zMDdJUnlDTGlnTEpsNXlwZ0ZXaHNaMVhpeENROEpoUTBud3NzRU5JcVo5MXhZQ3ZhTWF2V2dCaS9YeEVIdz0ifQ==')
VIEWER_TOKEN = os.getenv('VIEWER_TOKEN','eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3MDE5NzI0NzYxNTAuODA4NzI1NDAzODIzMjMwNSIsInRva2VuIjoiM2ZrV1gzbzRBditVUi95aHhiYStid1EvcFpvMC85NVYwTzNic3BBNDJFTTRYemJnUWxrc0JwYXhCcXVDb3pycFNIUWRrU3BMWFdMektXUmVsT0pQd0JJaDNMUUM4bEk2ZUpWSm1uOEhZVFI2eEVoZmRHcVgydlVrTWh6RGN6cDVzdGlQbzdzK3ZrenRqUEl5ZDE5QU1SV1BxblVSd3lqOW1mOXBRSGE1SFhOOWFYcWlLUzVXeDlEc3NjUm5yOGtZMzM4VFk5USt4MkpEZndLMzFudEV1TTFPTS9CbStvY2pISityRmREQWJtL1VFOHEwMU1Ic3dZemt0UDh5czAya1ltb09XZW94VEJZVmY5bXpxaDFlRExreEZBMXBZTURxRUJLZC9hc0NPM0JIL0YwNTIyaU5TT25UN2xSRU9XR2NHaXp4UVhnZDc4THZOMEZEVE9ueFhVRT0ifQ==')
 