# DetailedCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**CountryCodeEnum**](CountryCodeEnum.md) |  | 
**name** | **str** |  | 

## Example

```python
from authentik_client.models.detailed_country import DetailedCountry

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedCountry from a JSON string
detailed_country_instance = DetailedCountry.from_json(json)
# print the JSON string representation of the object
print(DetailedCountry.to_json())

# convert the object into a dict
detailed_country_dict = detailed_country_instance.to_dict()
# create an instance of DetailedCountry from a dict
detailed_country_from_dict = DetailedCountry.from_dict(detailed_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


