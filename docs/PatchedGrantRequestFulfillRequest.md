# PatchedGrantRequestFulfillRequest

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**status** | [**RequestStatus**](RequestStatus.md) |  | [optional] 

## Example

```python
from authentik_client.models.patched_grant_request_fulfill_request import PatchedGrantRequestFulfillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGrantRequestFulfillRequest from a JSON string
patched_grant_request_fulfill_request_instance = PatchedGrantRequestFulfillRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGrantRequestFulfillRequest.to_json())

# convert the object into a dict
patched_grant_request_fulfill_request_dict = patched_grant_request_fulfill_request_instance.to_dict()
# create an instance of PatchedGrantRequestFulfillRequest from a dict
patched_grant_request_fulfill_request_from_dict = PatchedGrantRequestFulfillRequest.from_dict(patched_grant_request_fulfill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


