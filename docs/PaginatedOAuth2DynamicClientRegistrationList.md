# PaginatedOAuth2DynamicClientRegistrationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[OAuth2DynamicClientRegistration]**](OAuth2DynamicClientRegistration.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_o_auth2_dynamic_client_registration_list import PaginatedOAuth2DynamicClientRegistrationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOAuth2DynamicClientRegistrationList from a JSON string
paginated_o_auth2_dynamic_client_registration_list_instance = PaginatedOAuth2DynamicClientRegistrationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOAuth2DynamicClientRegistrationList.to_json())

# convert the object into a dict
paginated_o_auth2_dynamic_client_registration_list_dict = paginated_o_auth2_dynamic_client_registration_list_instance.to_dict()
# create an instance of PaginatedOAuth2DynamicClientRegistrationList from a dict
paginated_o_auth2_dynamic_client_registration_list_from_dict = PaginatedOAuth2DynamicClientRegistrationList.from_dict(paginated_o_auth2_dynamic_client_registration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


