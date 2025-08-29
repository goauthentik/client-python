# PatchedGeoIPPolicyRequest

GeoIP Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**asns** | **List[int]** |  | [optional] 
**countries** | [**List[CountryCodeEnum]**](CountryCodeEnum.md) |  | [optional] 

## Example

```python
from authentik_client.models.patched_geo_ip_policy_request import PatchedGeoIPPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGeoIPPolicyRequest from a JSON string
patched_geo_ip_policy_request_instance = PatchedGeoIPPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGeoIPPolicyRequest.to_json())

# convert the object into a dict
patched_geo_ip_policy_request_dict = patched_geo_ip_policy_request_instance.to_dict()
# create an instance of PatchedGeoIPPolicyRequest from a dict
patched_geo_ip_policy_request_from_dict = PatchedGeoIPPolicyRequest.from_dict(patched_geo_ip_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


