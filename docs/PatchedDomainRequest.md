# PatchedDomainRequest

Domain Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**is_primary** | **bool** |  | [optional] 
**tenant** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_domain_request import PatchedDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDomainRequest from a JSON string
patched_domain_request_instance = PatchedDomainRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDomainRequest.to_json())

# convert the object into a dict
patched_domain_request_dict = patched_domain_request_instance.to_dict()
# create an instance of PatchedDomainRequest from a dict
patched_domain_request_from_dict = PatchedDomainRequest.from_dict(patched_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


