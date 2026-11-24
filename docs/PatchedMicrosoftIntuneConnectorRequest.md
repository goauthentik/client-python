# PatchedMicrosoftIntuneConnectorRequest

MicrosoftIntuneConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**certificate_authorities** | **List[UUID]** | Certificate authorities which issue device certificates via Intune (Cloud PKI, SCEP or PKCS profiles), used by the endpoint stage to validate certificates. This option has a higher priority than the &#x60;client_certificate&#x60; option on &#x60;Brand&#x60;. | [optional] 

## Example

```python
from authentik_client.models.patched_microsoft_intune_connector_request import PatchedMicrosoftIntuneConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMicrosoftIntuneConnectorRequest from a JSON string
patched_microsoft_intune_connector_request_instance = PatchedMicrosoftIntuneConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedMicrosoftIntuneConnectorRequest.to_json())

# convert the object into a dict
patched_microsoft_intune_connector_request_dict = patched_microsoft_intune_connector_request_instance.to_dict()
# create an instance of PatchedMicrosoftIntuneConnectorRequest from a dict
patched_microsoft_intune_connector_request_from_dict = PatchedMicrosoftIntuneConnectorRequest.from_dict(patched_microsoft_intune_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


