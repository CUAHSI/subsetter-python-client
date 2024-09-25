# openapi_client.UtilitiesApi

All URIs are relative to *https://subsetter-api-jbzfw6l52q-uc.a.run.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_nwm_bbox_nwm_compute_bbox_post**](UtilitiesApi.md#compute_nwm_bbox_nwm_compute_bbox_post) | **POST** /nwm/compute_bbox | Compute Nwm Bbox


# **compute_nwm_bbox_nwm_compute_bbox_post**
> object compute_nwm_bbox_nwm_compute_bbox_post(geo_json_feature_collection)

Compute Nwm Bbox

Computes the bounding box of geometries provided in the WGS 1984 coordinate reference system (CRS) in the CRS used by the National Water Model (NWM).  Arguments: ========== geojson: str - a GeoJSON string representing the geometries for which to compute the bounding box.  Returns: ======== dict - a dictionary containing the bounding box in the CRS used by the NWM.

### Example


```python
import openapi_client
from openapi_client.models.geo_json_feature_collection import GeoJsonFeatureCollection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subsetter-api-jbzfw6l52q-uc.a.run.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subsetter-api-jbzfw6l52q-uc.a.run.app"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UtilitiesApi(api_client)
    geo_json_feature_collection = openapi_client.GeoJsonFeatureCollection() # GeoJsonFeatureCollection | 

    try:
        # Compute Nwm Bbox
        api_response = api_instance.compute_nwm_bbox_nwm_compute_bbox_post(geo_json_feature_collection)
        print("The response of UtilitiesApi->compute_nwm_bbox_nwm_compute_bbox_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesApi->compute_nwm_bbox_nwm_compute_bbox_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geo_json_feature_collection** | [**GeoJsonFeatureCollection**](GeoJsonFeatureCollection.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

