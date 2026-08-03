# LifecycleIterationRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | [**ContentTypeEnum**](ContentTypeEnum.md) |  | 

## Example

```python
from authentik_client.models.lifecycle_iteration_request import LifecycleIterationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleIterationRequest from a JSON string
lifecycle_iteration_request_instance = LifecycleIterationRequest.from_json(json)
# print the JSON string representation of the object
print(LifecycleIterationRequest.to_json())

# convert the object into a dict
lifecycle_iteration_request_dict = lifecycle_iteration_request_instance.to_dict()
# create an instance of LifecycleIterationRequest from a dict
lifecycle_iteration_request_from_dict = LifecycleIterationRequest.from_dict(lifecycle_iteration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


