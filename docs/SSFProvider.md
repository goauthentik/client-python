# SSFProvider

SSFProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**signing_key** | **UUID** | Key used to sign the SSF Events. | 
**token_obj** | [**Token**](Token.md) |  | [readonly] 
**oidc_auth_providers** | **List[int]** |  | [optional] 
**ssf_url** | **str** |  | [readonly] 
**event_retention** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.ssf_provider import SSFProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SSFProvider from a JSON string
ssf_provider_instance = SSFProvider.from_json(json)
# print the JSON string representation of the object
print(SSFProvider.to_json())

# convert the object into a dict
ssf_provider_dict = ssf_provider_instance.to_dict()
# create an instance of SSFProvider from a dict
ssf_provider_from_dict = SSFProvider.from_dict(ssf_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


