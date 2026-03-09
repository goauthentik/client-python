# GoogleChromeConnectorRequest

GoogleChromeConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**credentials** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.google_chrome_connector_request import GoogleChromeConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleChromeConnectorRequest from a JSON string
google_chrome_connector_request_instance = GoogleChromeConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleChromeConnectorRequest.to_json())

# convert the object into a dict
google_chrome_connector_request_dict = google_chrome_connector_request_instance.to_dict()
# create an instance of GoogleChromeConnectorRequest from a dict
google_chrome_connector_request_from_dict = GoogleChromeConnectorRequest.from_dict(google_chrome_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


