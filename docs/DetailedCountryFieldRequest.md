# DetailedCountryFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**CountryCodeEnum**](CountryCodeEnum.md) |  | 
**name** | **str** |  | 

## Example

```python
from authentik_client.models.detailed_country_field_request import DetailedCountryFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedCountryFieldRequest from a JSON string
detailed_country_field_request_instance = DetailedCountryFieldRequest.from_json(json)
# print the JSON string representation of the object
print(DetailedCountryFieldRequest.to_json())

# convert the object into a dict
detailed_country_field_request_dict = detailed_country_field_request_instance.to_dict()
# create an instance of DetailedCountryFieldRequest from a dict
detailed_country_field_request_from_dict = DetailedCountryFieldRequest.from_dict(detailed_country_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


