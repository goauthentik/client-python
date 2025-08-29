# RedirectURIRequest

A single allowed redirect URI entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_mode** | [**MatchingModeEnum**](MatchingModeEnum.md) |  | 
**url** | **str** |  | 

## Example

```python
from authentik_client.models.redirect_uri_request import RedirectURIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectURIRequest from a JSON string
redirect_uri_request_instance = RedirectURIRequest.from_json(json)
# print the JSON string representation of the object
print(RedirectURIRequest.to_json())

# convert the object into a dict
redirect_uri_request_dict = redirect_uri_request_instance.to_dict()
# create an instance of RedirectURIRequest from a dict
redirect_uri_request_from_dict = RedirectURIRequest.from_dict(redirect_uri_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


