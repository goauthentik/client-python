# LicenseUserCountRange

Counts of active users added within a date range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**interval** | **str** |  | 
**internal_users_added** | **int** |  | 
**external_users_added** | **int** |  | 

## Example

```python
from authentik_client.models.license_user_count_range import LicenseUserCountRange

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseUserCountRange from a JSON string
license_user_count_range_instance = LicenseUserCountRange.from_json(json)
# print the JSON string representation of the object
print(LicenseUserCountRange.to_json())

# convert the object into a dict
license_user_count_range_dict = license_user_count_range_instance.to_dict()
# create an instance of LicenseUserCountRange from a dict
license_user_count_range_from_dict = LicenseUserCountRange.from_dict(license_user_count_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


