# GrantRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [readonly] 
**created_by** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**requester_data** | **Dict[str, object]** |  | [optional] 
**fulfiller_data** | **Dict[str, object]** |  | [optional] 
**revoked_by** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**agent_owner** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**is_active** | **bool** |  | [readonly] 
**expires** | **datetime** |  | [optional] 
**status** | [**RequestStatus**](RequestStatus.md) |  | [readonly] 
**targets** | **List[UUID]** |  | [readonly] 
**target_objs** | [**List[RequestableTarget]**](RequestableTarget.md) |  | [readonly] 
**uuid** | **UUID** |  | [optional] 

## Example

```python
from authentik_client.models.grant_request import GrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantRequest from a JSON string
grant_request_instance = GrantRequest.from_json(json)
# print the JSON string representation of the object
print(GrantRequest.to_json())

# convert the object into a dict
grant_request_dict = grant_request_instance.to_dict()
# create an instance of GrantRequest from a dict
grant_request_from_dict = GrantRequest.from_dict(grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


