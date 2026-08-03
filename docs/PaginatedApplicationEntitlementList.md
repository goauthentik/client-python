# PaginatedApplicationEntitlementList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ApplicationEntitlement]**](ApplicationEntitlement.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_application_entitlement_list import PaginatedApplicationEntitlementList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedApplicationEntitlementList from a JSON string
paginated_application_entitlement_list_instance = PaginatedApplicationEntitlementList.from_json(json)
# print the JSON string representation of the object
print(PaginatedApplicationEntitlementList.to_json())

# convert the object into a dict
paginated_application_entitlement_list_dict = paginated_application_entitlement_list_instance.to_dict()
# create an instance of PaginatedApplicationEntitlementList from a dict
paginated_application_entitlement_list_from_dict = PaginatedApplicationEntitlementList.from_dict(paginated_application_entitlement_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


