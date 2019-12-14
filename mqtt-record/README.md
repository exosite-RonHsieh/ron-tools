# MQTT RECORD README

In this guide, you will enable MQTT for your product. You will then activate your device and connect your activated device with the Murano MQTT endpoint.

# Requirements

## Software Setup

To complete this guide, you must first download and install the following:

  * Python version 3.5.0 ([Python website](https://www.python.org/) or you can use [pipenv](https://github.com/pypa/pipenv)).
  * Install a patched version of the Eclipse Paho™ MQTT Python Client via the following command:

  ```
  pip install git+https://github.com/exosite/paho.mqtt.python.git@openssl_sni_support
  ```

## Overview

This script is extended from [dqa-mqtt](https://github.com/exosite/dqa-mqtt), so if you encounter a problem that cannot be resolved smoothly, you can get some information from this repository.

The main purpose of the script is to simulate the record of a Sinko customer through MQTT batch publish.

## Getting Started

### trusted.crt

Save the following certificate into a file called "trusted.crt"
```
-----BEGIN CERTIFICATE-----
MIIDVDCCAjygAwIBAgIDAjRWMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT
MRYwFAYDVQQKEw1HZW9UcnVzdCBJbmMuMRswGQYDVQQDExJHZW9UcnVzdCBHbG9i
YWwgQ0EwHhcNMDIwNTIxMDQwMDAwWhcNMjIwNTIxMDQwMDAwWjBCMQswCQYDVQQG
EwJVUzEWMBQGA1UEChMNR2VvVHJ1c3QgSW5jLjEbMBkGA1UEAxMSR2VvVHJ1c3Qg
R2xvYmFsIENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2swYYzD9
9BcjGlZ+W988bDjkcbd4kdS8odhM+KhDtgPpTSEHCIjaWC9mOSm9BXiLnTjoBbdq
fnGk5sRgprDvgOSJKA+eJdbtg/OtppHHmMlCGDUUna2YRpIuT8rxh0PBFpVXLVDv
iS2Aelet8u5fa9IAjbkU+BQVNdnARqN7csiRv8lVK83Qlz6cJmTM386DGXHKTubU
1XupGc1V3sjs0l44U+VcT4wt/lAjNvxm5suOpDkZALeVAjmRCw7+OC7RHQWa9k0+
bw8HHa8sHo9gOeL6NlMTOdReJivbPagUvTLrGAMoUgRx5aszPeE4uwc2hGKceeoW
MPRfwCvocWvk+QIDAQABo1MwUTAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTA
ephojYn7qwVkDBF9qn1luMrMTjAfBgNVHSMEGDAWgBTAephojYn7qwVkDBF9qn1l
uMrMTjANBgkqhkiG9w0BAQUFAAOCAQEANeMpauUvXVSOKVCUn5kaFOSPeCpilKIn
Z57QzxpeR+nBsqTP3UEaBU6bS+5Kb1VSsyShNwrrZHYqLizz/Tt1kL/6cdjHPTfS
tQWVYrmm3ok9Nns4d0iXrKYgjy6myQzCsplFAMfOEVEiIuCl6rYVSAlk6l5PdPcF
PseKUgzbFbS9bZvlxrFUaKnjaZC2mqUPuLk/IH2uSrW4nOQdtqvmlKXBx4Ot2/Un
hw4EbNX/3aBd7YdStysVAq45pmp06drE57xNNB6pXE0zX5IJL4hmXXeXxx12E6nV
5fEWCRE11azbJHFwLJhWC9kXtNHjUStedejV0NxPNO3CBWaAocvmMw==
-----END CERTIFICATE-----
```

### batch_publish.py
Setup the device information into a file called "batch_publish.py"

    * product_id (Update your mqtt product id)
    * device_token (Update your mqtt device token)
    * timestamp (timestamp default is the current time, you can change this value if you want)
    * config_io (config_io default data is Sinko custom config_io)
    * data_in (because custom data is too large, so split into two-part "data_in_1" and "data_in_1")

### schedule.py
"schedule.py" will record data via MQTT batch per 10 minutes, if you want to update report rate of batch_pbulish you can set rate in the main function (unit is second).
If you only want to send values ​​once, you can use batch_publish.py directly
