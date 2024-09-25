# OAuth2AuthorizeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | 

## Example

```python
from openapi_client.models.o_auth2_authorize_response import OAuth2AuthorizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2AuthorizeResponse from a JSON string
o_auth2_authorize_response_instance = OAuth2AuthorizeResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2AuthorizeResponse.to_json())

# convert the object into a dict
o_auth2_authorize_response_dict = o_auth2_authorize_response_instance.to_dict()
# create an instance of OAuth2AuthorizeResponse from a dict
o_auth2_authorize_response_from_dict = OAuth2AuthorizeResponse.from_dict(o_auth2_authorize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


