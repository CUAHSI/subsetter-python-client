# GeoJsonFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | **object** |  | 

## Example

```python
from openapi_client.models.geo_json_feature import GeoJsonFeature

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonFeature from a JSON string
geo_json_feature_instance = GeoJsonFeature.from_json(json)
# print the JSON string representation of the object
print(GeoJsonFeature.to_json())

# convert the object into a dict
geo_json_feature_dict = geo_json_feature_instance.to_dict()
# create an instance of GeoJsonFeature from a dict
geo_json_feature_from_dict = GeoJsonFeature.from_dict(geo_json_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


