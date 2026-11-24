# LicenseUserCounts

Current active user totals and counts for requested date ranges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_internal_users** | **int** |  | 
**active_external_users** | **int** |  | 
**ranges** | [**List[LicenseUserCountRange]**](LicenseUserCountRange.md) |  | 

## Example

```python
from authentik_client.models.license_user_counts import LicenseUserCounts

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseUserCounts from a JSON string
license_user_counts_instance = LicenseUserCounts.from_json(json)
# print the JSON string representation of the object
print(LicenseUserCounts.to_json())

# convert the object into a dict
license_user_counts_dict = license_user_counts_instance.to_dict()
# create an instance of LicenseUserCounts from a dict
license_user_counts_from_dict = LicenseUserCounts.from_dict(license_user_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


