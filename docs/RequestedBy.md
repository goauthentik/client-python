# RequestedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 

## Example

```python
from authentik_client.models.requested_by import RequestedBy

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedBy from a JSON string
requested_by_instance = RequestedBy.from_json(json)
# print the JSON string representation of the object
print(RequestedBy.to_json())

# convert the object into a dict
requested_by_dict = requested_by_instance.to_dict()
# create an instance of RequestedBy from a dict
requested_by_from_dict = RequestedBy.from_dict(requested_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


