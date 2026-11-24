# MicrosoftIntuneConnectorRequest

MicrosoftIntuneConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**tenant_id** | **str** |  | 
**certificate_authorities** | **List[UUID]** | Certificate authorities which issue device certificates via Intune (Cloud PKI, SCEP or PKCS profiles), used by the endpoint stage to validate certificates. This option has a higher priority than the &#x60;client_certificate&#x60; option on &#x60;Brand&#x60;. | [optional] 

## Example

```python
from authentik_client.models.microsoft_intune_connector_request import MicrosoftIntuneConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftIntuneConnectorRequest from a JSON string
microsoft_intune_connector_request_instance = MicrosoftIntuneConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(MicrosoftIntuneConnectorRequest.to_json())

# convert the object into a dict
microsoft_intune_connector_request_dict = microsoft_intune_connector_request_instance.to_dict()
# create an instance of MicrosoftIntuneConnectorRequest from a dict
microsoft_intune_connector_request_from_dict = MicrosoftIntuneConnectorRequest.from_dict(microsoft_intune_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


