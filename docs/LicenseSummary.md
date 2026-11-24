# LicenseSummary

Serializer for license status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_users** | **int** |  | 
**external_users** | **int** |  | 
**status** | [**LicenseSummaryStatusEnum**](LicenseSummaryStatusEnum.md) |  | 
**latest_valid** | **datetime** |  | 
**license_flags** | [**List[LicenseFlagsEnum]**](LicenseFlagsEnum.md) |  | 

## Example

```python
from authentik_client.models.license_summary import LicenseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseSummary from a JSON string
license_summary_instance = LicenseSummary.from_json(json)
# print the JSON string representation of the object
print(LicenseSummary.to_json())

# convert the object into a dict
license_summary_dict = license_summary_instance.to_dict()
# create an instance of LicenseSummary from a dict
license_summary_from_dict = LicenseSummary.from_dict(license_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


