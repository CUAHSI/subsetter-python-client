# ExtractMetadataRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** |  | 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.extract_metadata_request_body import ExtractMetadataRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractMetadataRequestBody from a JSON string
extract_metadata_request_body_instance = ExtractMetadataRequestBody.from_json(json)
# print the JSON string representation of the object
print(ExtractMetadataRequestBody.to_json())

# convert the object into a dict
extract_metadata_request_body_dict = extract_metadata_request_body_instance.to_dict()
# create an instance of ExtractMetadataRequestBody from a dict
extract_metadata_request_body_from_dict = ExtractMetadataRequestBody.from_dict(extract_metadata_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


