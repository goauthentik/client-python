# ImpersonationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 

## Example

```python
from authentik_client.models.impersonation_request import ImpersonationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImpersonationRequest from a JSON string
impersonation_request_instance = ImpersonationRequest.from_json(json)
# print the JSON string representation of the object
print(ImpersonationRequest.to_json())

# convert the object into a dict
impersonation_request_dict = impersonation_request_instance.to_dict()
# create an instance of ImpersonationRequest from a dict
impersonation_request_from_dict = ImpersonationRequest.from_dict(impersonation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


