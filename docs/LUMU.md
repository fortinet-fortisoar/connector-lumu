## About the connector
LUMU provides Real-time detection, analysis, and response to network threats.
<p>This document provides information about the LUMU Connector, which facilitates automated interactions, with a LUMU server using FortiSOAR&trade; playbooks. Add the LUMU Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with LUMU.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-lumu</pre>

## Prerequisites to configuring the connector
- You must have the credentials of LUMU server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the LUMU server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>LUMU</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>IP address or hostname of the LUMU server to which you will connect and perform automated operations.
</td>
</tr><tr><td>Company Key</td><td>Specify the API Key that you will use to access the LUMU REST API.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Incidents</td><td>Retrieves a paginated list of incidents for the company. The items are listed by the most recent.</td><td>get_incidents <br/>Investigation</td></tr>
<tr><td>Get Incident by UUID</td><td>Retrieves a details of a specific Incident. The response for this operation may include extra data ( DNSPacketExtraInfo for example) in its parameters which may vary according to the data collection source</td><td>get_incident_by_uuid <br/>Investigation</td></tr>
<tr><td>Get Incident Context</td><td>Retrieves details of the context information from a specific Incident</td><td>get_incident_context <br/>Investigation</td></tr>
<tr><td>Get Incident Endpoints</td><td>Retrieves a paginated summary of the endpoints affected by a specified incident</td><td>get_incident_endpoints <br/>Investigation</td></tr>
<tr><td>Close Incident</td><td>Closes a LUMU Incident according to Incident UUID and comment provided</td><td>close_incident <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Incidents
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>From Date</td><td>Specify the Search start date. The default value is 7 days before the current date. Example: 2024-04-01T14:40:14.939Z
</td></tr><tr><td>To Date</td><td>Specify the Search end date. The default value is the current date. Example: 2021-04-07T14:40:14.939Z
</td></tr><tr><td>Incident Status</td><td>Select one or more incident statuses from the following options to filter incidents: Open, Muted, or Closed. If not specified, all objects are returned.
</td></tr><tr><td>Adversary Type</td><td>Select one or more adversary types from the following options to filter incidents: C2C, Malware, DGA, Mining, Spam, or Phishing. If not specified, all objects are returned.
</td></tr><tr><td>Labels</td><td>Specify the Label IDs in Comma separated Format. You may previously use the label API call to retrieve label IDs and names. If not specified, all objects are returned. Example: 2, 3, 5
</td></tr><tr><td>Page</td><td>Specify the Page number of the result set.Default value is : 1
</td></tr><tr><td>Limit</td><td>Limit the number of results per page. Default value is : 50, Max value can be : 100
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "items": [
        {
            "id": "",
            "timestamp": "",
            "statusTimestamp": "",
            "status": "",
            "contacts": "",
            "adversaries": [],
            "adversaryTypes": [],
            "labelDistribution": {
                "17": ""
            },
            "totalEndpoints": "",
            "lastContact": "",
            "unread": ""
        }
    ],
    "paginationInfo": {
        "page": "",
        "items": ""
    }
}</pre>

### operation: Get Incident by UUID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident UUID</td><td>Specify the Incident UUID whose details you want to Fetch
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "timestamp": "",
    "isUnread": "",
    "contacts": "",
    "adversaryId": "",
    "adversaries": [],
    "adversaryTypes": [],
    "description": "",
    "labelDistribution": {
        "144": ""
    },
    "totalEndpoints": "",
    "lastContact": "",
    "actions": [
        {
            "datetime": "",
            "userId": "",
            "action": "",
            "comment": ""
        }
    ],
    "status": "",
    "statusTimestamp": "",
    "firstContactDetails": {
        "uuid": "",
        "datetime": "",
        "host": "",
        "types": [],
        "details": [],
        "endpointIp": "",
        "endpointName": "",
        "label": "",
        "sourceType": "",
        "sourceId": "",
        "sourceData": {
            "DNSPacketExtraInfo": {
                "question": {
                    "type": "",
                    "name": "",
                    "class": ""
                },
                "responseCode": "",
                "flags": {
                    "authoritative": "",
                    "recursion_available": "",
                    "truncated_response": "",
                    "checking_disabled": "",
                    "recursion_desired": "",
                    "authentic_data": ""
                },
                "answers": [
                    {
                        "name": "",
                        "type": "",
                        "class": "",
                        "ttl": "",
                        "data": ""
                    }
                ],
                "opCode": ""
            }
        },
        "isPlayback": ""
    },
    "lastContactDetails": {
        "uuid": "",
        "datetime": "",
        "host": "",
        "types": [],
        "details": [],
        "endpointIp": "",
        "endpointName": "",
        "label": "",
        "sourceType": "",
        "sourceId": "",
        "sourceData": {
            "DNSPacketExtraInfo": {
                "question": {
                    "type": "",
                    "name": "",
                    "class": ""
                },
                "responseCode": "",
                "flags": {
                    "authoritative": "",
                    "recursion_available": "",
                    "truncated_response": "",
                    "checking_disabled": "",
                    "recursion_desired": "",
                    "authentic_data": ""
                },
                "answers": [
                    {
                        "name": "",
                        "type": "",
                        "class": "",
                        "ttl": "",
                        "data": ""
                    }
                ],
                "opCode": ""
            }
        },
        "isPlayback": ""
    }
}</pre>

### operation: Get Incident Context
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident UUID</td><td>Specify the Incident UUID whose context details you want to Fetch
</td></tr><tr><td>Hash Type</td><td>Specify the Message-digest algorithm (Cryptographic Hash Function) you are requesting, can correspond to SHA256, SHA1 or MD5. If a hash type isn't requested, this will return a SHA256 hash by default. This parameter isn't case sensitive
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "adversary_id": "",
    "currently_active": "",
    "deactivated_on": "",
    "mitre": {
        "details": [
            {
                "tactic": "",
                "techniques": []
            }
        ],
        "matrix": "",
        "version": ""
    },
    "related_files": [],
    "threat_details": [],
    "threat_triggers": [],
    "playbooks": [],
    "external_resources": [],
    "timestamp": ""
}</pre>

### operation: Get Incident Endpoints
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident UUID</td><td>Specify the Incident UUID whose Endpoints details you want to Fetch
</td></tr><tr><td>Endpoint IDs</td><td>Specify the List of ID of contacting endpoints. If not specified, all objects are returned. Example: 182.168.100.29, DESK-9867
</td></tr><tr><td>Labels</td><td>Specify the Label IDs in Comma separated Format. You may previously use the label API call to retrieve label IDs and names. If not specified, all objects are returned. Example: 2, 3, 5
</td></tr><tr><td>Page</td><td>Specify the Page number of the result set.Default value is : 1
</td></tr><tr><td>Limit</td><td>Limit the number of results per page. Default value is : 50, Max value can be : 100
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "items": [
        {
            "label": "",
            "endpoint": "",
            "total": "",
            "first": "",
            "last": ""
        }
    ],
    "paginationInfo": {
        "page": "",
        "items": ""
    }
}</pre>

### operation: Close Incident
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident UUID</td><td>Specify the Incident UUID which you want to close
</td></tr><tr><td>Comment</td><td>Specify the Comment to be added in the Incident log. Example: Internal penetration tests
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - lumu - 1.0.0` playbook collection comes bundled with the LUMU connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the LUMU connector.

- Close Incident
- Get Incident Context
- Get Incident Endpoints
- Get Incident by UUID
- Get Incidents
- LUMU > Fetch and Create
- LUMU > Ingest

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
## Data Ingestion Support
Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling events/alerts/incidents, based on the requirement.

**TODO:** provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.