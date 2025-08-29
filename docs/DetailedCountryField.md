# DetailedCountryField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**CountryCodeEnum**](CountryCodeEnum.md) |  | 
**name** | **str** |  | 

## Example

```python
from authentik_client.models.detailed_country_field import DetailedCountryField

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedCountryField from a JSON string
detailed_country_field_instance = DetailedCountryField.from_json(json)
# print the JSON string representation of the object
print(DetailedCountryField.to_json())

# convert the object into a dict
detailed_country_field_dict = detailed_country_field_instance.to_dict()
# create an instance of DetailedCountryField from a dict
detailed_country_field_from_dict = DetailedCountryField.from_dict(detailed_country_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


