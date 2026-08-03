# GeoIPPolicyCountriesObjInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from authentik_client.models.geo_ip_policy_countries_obj_inner import GeoIPPolicyCountriesObjInner

# TODO update the JSON string below
json = "{}"
# create an instance of GeoIPPolicyCountriesObjInner from a JSON string
geo_ip_policy_countries_obj_inner_instance = GeoIPPolicyCountriesObjInner.from_json(json)
# print the JSON string representation of the object
print(GeoIPPolicyCountriesObjInner.to_json())

# convert the object into a dict
geo_ip_policy_countries_obj_inner_dict = geo_ip_policy_countries_obj_inner_instance.to_dict()
# create an instance of GeoIPPolicyCountriesObjInner from a dict
geo_ip_policy_countries_obj_inner_from_dict = GeoIPPolicyCountriesObjInner.from_dict(geo_ip_policy_countries_obj_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


