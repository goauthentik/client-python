# CertificateKeyPair

CertificateKeyPair Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**fingerprint_sha256** | **str** | SHA256 fingerprint of the certificate | [readonly] 
**fingerprint_sha1** | **str** | SHA1 fingerprint of the certificate | [readonly] 
**cert_expiry** | **datetime** | Certificate expiry date | [readonly] 
**cert_subject** | **str** | Certificate subject as RFC4514 string | [readonly] 
**private_key_available** | **bool** | Show if this keypair has a private key configured or not | [readonly] 
**key_type** | [**KeyTypeEnum**](KeyTypeEnum.md) | Key algorithm type detected from the certificate&#39;s public key | [readonly] 
**certificate_download_url** | **str** | Get URL to download certificate | [readonly] 
**private_key_download_url** | **str** | Get URL to download private key | [readonly] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [readonly] 

## Example

```python
from authentik_client.models.certificate_key_pair import CertificateKeyPair

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateKeyPair from a JSON string
certificate_key_pair_instance = CertificateKeyPair.from_json(json)
# print the JSON string representation of the object
print(CertificateKeyPair.to_json())

# convert the object into a dict
certificate_key_pair_dict = certificate_key_pair_instance.to_dict()
# create an instance of CertificateKeyPair from a dict
certificate_key_pair_from_dict = CertificateKeyPair.from_dict(certificate_key_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


