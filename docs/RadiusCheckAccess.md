# RadiusCheckAccess

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **str** |  | [optional] 
**access** | [**PolicyTestResult**](PolicyTestResult.md) |  | 

## Example

```python
from authentik_client.models.radius_check_access import RadiusCheckAccess

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusCheckAccess from a JSON string
radius_check_access_instance = RadiusCheckAccess.from_json(json)
# print the JSON string representation of the object
print(RadiusCheckAccess.to_json())

# convert the object into a dict
radius_check_access_dict = radius_check_access_instance.to_dict()
# create an instance of RadiusCheckAccess from a dict
radius_check_access_from_dict = RadiusCheckAccess.from_dict(radius_check_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


