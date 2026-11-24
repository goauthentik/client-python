# PaginatedEmailDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[EmailDevice]**](EmailDevice.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_email_device_list import PaginatedEmailDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEmailDeviceList from a JSON string
paginated_email_device_list_instance = PaginatedEmailDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEmailDeviceList.to_json())

# convert the object into a dict
paginated_email_device_list_dict = paginated_email_device_list_instance.to_dict()
# create an instance of PaginatedEmailDeviceList from a dict
paginated_email_device_list_from_dict = PaginatedEmailDeviceList.from_dict(paginated_email_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


