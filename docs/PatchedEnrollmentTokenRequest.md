# PatchedEnrollmentTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_group** | **UUID** |  | [optional] 
**connector** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from authentik_client.models.patched_enrollment_token_request import PatchedEnrollmentTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEnrollmentTokenRequest from a JSON string
patched_enrollment_token_request_instance = PatchedEnrollmentTokenRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEnrollmentTokenRequest.to_json())

# convert the object into a dict
patched_enrollment_token_request_dict = patched_enrollment_token_request_instance.to_dict()
# create an instance of PatchedEnrollmentTokenRequest from a dict
patched_enrollment_token_request_from_dict = PatchedEnrollmentTokenRequest.from_dict(patched_enrollment_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


