# PaginatedGeoIPPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GeoIPPolicy]**](GeoIPPolicy.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_geo_ip_policy_list import PaginatedGeoIPPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGeoIPPolicyList from a JSON string
paginated_geo_ip_policy_list_instance = PaginatedGeoIPPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGeoIPPolicyList.to_json())

# convert the object into a dict
paginated_geo_ip_policy_list_dict = paginated_geo_ip_policy_list_instance.to_dict()
# create an instance of PaginatedGeoIPPolicyList from a dict
paginated_geo_ip_policy_list_from_dict = PaginatedGeoIPPolicyList.from_dict(paginated_geo_ip_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


