# EnrollmentToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_uuid** | **UUID** |  | [readonly] 
**device_group** | **UUID** |  | [optional] 
**device_group_obj** | [**DeviceAccessGroup**](DeviceAccessGroup.md) |  | [readonly] 
**connector** | **UUID** |  | 
**name** | **str** |  | 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from authentik_client.models.enrollment_token import EnrollmentToken

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentToken from a JSON string
enrollment_token_instance = EnrollmentToken.from_json(json)
# print the JSON string representation of the object
print(EnrollmentToken.to_json())

# convert the object into a dict
enrollment_token_dict = enrollment_token_instance.to_dict()
# create an instance of EnrollmentToken from a dict
enrollment_token_from_dict = EnrollmentToken.from_dict(enrollment_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


