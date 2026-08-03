# InvitationSendEmailRequest

Serializer for sending invitation emails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_addresses** | **List[object]** |  | 
**cc_addresses** | **List[object]** |  | [optional] 
**bcc_addresses** | **List[object]** |  | [optional] 
**template** | **str** |  | [optional] [default to 'invitation']

## Example

```python
from authentik_client.models.invitation_send_email_request import InvitationSendEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationSendEmailRequest from a JSON string
invitation_send_email_request_instance = InvitationSendEmailRequest.from_json(json)
# print the JSON string representation of the object
print(InvitationSendEmailRequest.to_json())

# convert the object into a dict
invitation_send_email_request_dict = invitation_send_email_request_instance.to_dict()
# create an instance of InvitationSendEmailRequest from a dict
invitation_send_email_request_from_dict = InvitationSendEmailRequest.from_dict(invitation_send_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


