# ProcessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**user** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.process_request import ProcessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessRequest from a JSON string
process_request_instance = ProcessRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessRequest.to_json())

# convert the object into a dict
process_request_dict = process_request_instance.to_dict()
# create an instance of ProcessRequest from a dict
process_request_from_dict = ProcessRequest.from_dict(process_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


