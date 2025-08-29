# PaginatedAuthenticatorEmailStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorEmailStage]**](AuthenticatorEmailStage.md) |  | 

## Example

```python
from authentik_client.models.paginated_authenticator_email_stage_list import PaginatedAuthenticatorEmailStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorEmailStageList from a JSON string
paginated_authenticator_email_stage_list_instance = PaginatedAuthenticatorEmailStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorEmailStageList.to_json())

# convert the object into a dict
paginated_authenticator_email_stage_list_dict = paginated_authenticator_email_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorEmailStageList from a dict
paginated_authenticator_email_stage_list_from_dict = PaginatedAuthenticatorEmailStageList.from_dict(paginated_authenticator_email_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


