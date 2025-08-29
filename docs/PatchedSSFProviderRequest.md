# PatchedSSFProviderRequest

SSFProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**signing_key** | **str** | Key used to sign the SSF Events. | [optional] 
**oidc_auth_providers** | **List[int]** |  | [optional] 
**event_retention** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_ssf_provider_request import PatchedSSFProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSSFProviderRequest from a JSON string
patched_ssf_provider_request_instance = PatchedSSFProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSSFProviderRequest.to_json())

# convert the object into a dict
patched_ssf_provider_request_dict = patched_ssf_provider_request_instance.to_dict()
# create an instance of PatchedSSFProviderRequest from a dict
patched_ssf_provider_request_from_dict = PatchedSSFProviderRequest.from_dict(patched_ssf_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


