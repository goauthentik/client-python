# LogoutURL

Data for a single logout URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**provider_name** | **str** |  | [optional] 
**binding** | **str** |  | [optional] 
**saml_request** | **str** |  | [optional] 
**saml_response** | **str** |  | [optional] 
**saml_relay_state** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.logout_url import LogoutURL

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutURL from a JSON string
logout_url_instance = LogoutURL.from_json(json)
# print the JSON string representation of the object
print(LogoutURL.to_json())

# convert the object into a dict
logout_url_dict = logout_url_instance.to_dict()
# create an instance of LogoutURL from a dict
logout_url_from_dict = LogoutURL.from_dict(logout_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


