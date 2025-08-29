# GeoIPPolicy

GeoIP Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**bound_to** | **int** | Return objects policy is bound to | [readonly] 
**asns** | **List[int]** |  | [optional] 
**countries** | [**List[CountryCodeEnum]**](CountryCodeEnum.md) |  | 
**countries_obj** | [**List[DetailedCountryField]**](DetailedCountryField.md) |  | [readonly] 
**check_history_distance** | **bool** |  | [optional] 
**history_max_distance_km** | **int** |  | [optional] 
**distance_tolerance_km** | **int** |  | [optional] 
**history_login_count** | **int** |  | [optional] 
**check_impossible_travel** | **bool** |  | [optional] 
**impossible_tolerance_km** | **int** |  | [optional] 

## Example

```python
from authentik_client.models.geo_ip_policy import GeoIPPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of GeoIPPolicy from a JSON string
geo_ip_policy_instance = GeoIPPolicy.from_json(json)
# print the JSON string representation of the object
print(GeoIPPolicy.to_json())

# convert the object into a dict
geo_ip_policy_dict = geo_ip_policy_instance.to_dict()
# create an instance of GeoIPPolicy from a dict
geo_ip_policy_from_dict = GeoIPPolicy.from_dict(geo_ip_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


