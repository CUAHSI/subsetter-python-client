# DatasetMetadataRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** |  | 
**metadata** | [**HydroShareMetadata**](HydroShareMetadata.md) |  | 

## Example

```python
from openapi_client.models.dataset_metadata_request_model import DatasetMetadataRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMetadataRequestModel from a JSON string
dataset_metadata_request_model_instance = DatasetMetadataRequestModel.from_json(json)
# print the JSON string representation of the object
print(DatasetMetadataRequestModel.to_json())

# convert the object into a dict
dataset_metadata_request_model_dict = dataset_metadata_request_model_instance.to_dict()
# create an instance of DatasetMetadataRequestModel from a dict
dataset_metadata_request_model_from_dict = DatasetMetadataRequestModel.from_dict(dataset_metadata_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


