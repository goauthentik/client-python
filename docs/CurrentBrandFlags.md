# CurrentBrandFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flows_continuous_login** | **bool** | Upon successful authentication, re-start authentication in other open tabs. | 
**flows_refresh_others** | **bool** | Refresh other tabs after successful authentication. | 

## Example

```python
from authentik_client.models.current_brand_flags import CurrentBrandFlags

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentBrandFlags from a JSON string
current_brand_flags_instance = CurrentBrandFlags.from_json(json)
# print the JSON string representation of the object
print(CurrentBrandFlags.to_json())

# convert the object into a dict
current_brand_flags_dict = current_brand_flags_instance.to_dict()
# create an instance of CurrentBrandFlags from a dict
current_brand_flags_from_dict = CurrentBrandFlags.from_dict(current_brand_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


