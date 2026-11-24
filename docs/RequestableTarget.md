# RequestableTarget

Generic representation of a single request target: whatever was actually requested (an Application, an Application Entitlement, ...), always paired with the parent it belongs to, so the UI/audit trail has that context even when the request itself was scoped narrower than the whole app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**pbm_uuid** | **str** |  | [readonly] 
**label** | **str** |  | [readonly] 
**parent** | [**Application**](Application.md) |  | [readonly] 

## Example

```python
from authentik_client.models.requestable_target import RequestableTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RequestableTarget from a JSON string
requestable_target_instance = RequestableTarget.from_json(json)
# print the JSON string representation of the object
print(RequestableTarget.to_json())

# convert the object into a dict
requestable_target_dict = requestable_target_instance.to_dict()
# create an instance of RequestableTarget from a dict
requestable_target_from_dict = RequestableTarget.from_dict(requestable_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


