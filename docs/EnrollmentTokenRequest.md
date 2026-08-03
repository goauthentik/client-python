# EnrollmentTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_group** | **UUID** |  | [optional] 
**connector** | **UUID** |  | 
**name** | **str** |  | 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from authentik_client.models.enrollment_token_request import EnrollmentTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentTokenRequest from a JSON string
enrollment_token_request_instance = EnrollmentTokenRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollmentTokenRequest.to_json())

# convert the object into a dict
enrollment_token_request_dict = enrollment_token_request_instance.to_dict()
# create an instance of EnrollmentTokenRequest from a dict
enrollment_token_request_from_dict = EnrollmentTokenRequest.from_dict(enrollment_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


