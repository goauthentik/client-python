# PatchedGoogleChromeConnectorRequest

GoogleChromeConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**credentials** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.patched_google_chrome_connector_request import PatchedGoogleChromeConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGoogleChromeConnectorRequest from a JSON string
patched_google_chrome_connector_request_instance = PatchedGoogleChromeConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGoogleChromeConnectorRequest.to_json())

# convert the object into a dict
patched_google_chrome_connector_request_dict = patched_google_chrome_connector_request_instance.to_dict()
# create an instance of PatchedGoogleChromeConnectorRequest from a dict
patched_google_chrome_connector_request_from_dict = PatchedGoogleChromeConnectorRequest.from_dict(patched_google_chrome_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


