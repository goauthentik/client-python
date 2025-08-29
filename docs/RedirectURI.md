# RedirectURI

A single allowed redirect URI entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_mode** | [**MatchingModeEnum**](MatchingModeEnum.md) |  | 
**url** | **str** |  | 

## Example

```python
from authentik_client.models.redirect_uri import RedirectURI

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectURI from a JSON string
redirect_uri_instance = RedirectURI.from_json(json)
# print the JSON string representation of the object
print(RedirectURI.to_json())

# convert the object into a dict
redirect_uri_dict = redirect_uri_instance.to_dict()
# create an instance of RedirectURI from a dict
redirect_uri_from_dict = RedirectURI.from_dict(redirect_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


