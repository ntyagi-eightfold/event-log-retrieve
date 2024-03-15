# Salesforce Event Monitoring Log Retrieval

Python command line utility that fetches Salesforce Log Files.

## Requirements

* Salesforce Event Monitoring
* Python v3.0 or greater
* User with Salesforce API access

## Setup

To Run & test simple_salesforce auth based connection 

* ### Run Simple_Salesforce Version Locally

```sh
$ python3 eventFile.py
```

* ### Run Non-Simple_Salesforce Version Locally

Retrieve logs for a given environment

```sh
$ python3 retrieveLogs.py {orgname}
>>Fetching logs from, eightfold.my.salesforce.com
```
