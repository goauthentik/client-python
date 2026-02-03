# SSFProviderRequest

SSFProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**signing_key** | **UUID** | Key used to sign the SSF Events. | 
**oidc_auth_providers** | **List[int]** |  | [optional] 
**event_retention** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.ssf_provider_request import SSFProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SSFProviderRequest from a JSON string
ssf_provider_request_instance = SSFProviderRequest.from_json(json)
# print the JSON string representation of the object
print(SSFProviderRequest.to_json())

# convert the object into a dict
ssf_provider_request_dict = ssf_provider_request_instance.to_dict()
# create an instance of SSFProviderRequest from a dict
ssf_provider_request_from_dict = SSFProviderRequest.from_dict(ssf_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


