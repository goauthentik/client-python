# GoogleChromeConnector

GoogleChromeConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**credentials** | **Dict[str, object]** |  | 
**chrome_url** | **str** | Full URL to be used in Google Workspace configuration | [readonly] 

## Example

```python
from authentik_client.models.google_chrome_connector import GoogleChromeConnector

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleChromeConnector from a JSON string
google_chrome_connector_instance = GoogleChromeConnector.from_json(json)
# print the JSON string representation of the object
print(GoogleChromeConnector.to_json())

# convert the object into a dict
google_chrome_connector_dict = google_chrome_connector_instance.to_dict()
# create an instance of GoogleChromeConnector from a dict
google_chrome_connector_from_dict = GoogleChromeConnector.from_dict(google_chrome_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


