# GrantRequestCreateRequest

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pbms** | **List[UUID]** |  | 
**expiry** | **str** | Optional override for how long the grant should last once approved. Clamped to the granting rule binding(s)&#39; expiry_granted_max. | [optional] 

## Example

```python
from authentik_client.models.grant_request_create_request import GrantRequestCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantRequestCreateRequest from a JSON string
grant_request_create_request_instance = GrantRequestCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GrantRequestCreateRequest.to_json())

# convert the object into a dict
grant_request_create_request_dict = grant_request_create_request_instance.to_dict()
# create an instance of GrantRequestCreateRequest from a dict
grant_request_create_request_from_dict = GrantRequestCreateRequest.from_dict(grant_request_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


