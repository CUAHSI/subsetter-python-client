# openapi_client.HydroshareApi

All URIs are relative to *https://subsetter-api-jbzfw6l52q-uc.a.run.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_dataset_metadata_post**](HydroshareApi.md#create_metadata_dataset_metadata_post) | **POST** /dataset/metadata | Create Metadata
[**update_metadata_dataset_metadata_put**](HydroshareApi.md#update_metadata_dataset_metadata_put) | **PUT** /dataset/metadata | Update Metadata


# **create_metadata_dataset_metadata_post**
> object create_metadata_dataset_metadata_post(dataset_metadata_request_model)

Create Metadata

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.dataset_metadata_request_model import DatasetMetadataRequestModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subsetter-api-jbzfw6l52q-uc.a.run.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subsetter-api-jbzfw6l52q-uc.a.run.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.HydroshareApi(api_client)
    dataset_metadata_request_model = openapi_client.DatasetMetadataRequestModel() # DatasetMetadataRequestModel | 

    try:
        # Create Metadata
        api_response = api_instance.create_metadata_dataset_metadata_post(dataset_metadata_request_model)
        print("The response of HydroshareApi->create_metadata_dataset_metadata_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HydroshareApi->create_metadata_dataset_metadata_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_metadata_request_model** | [**DatasetMetadataRequestModel**](DatasetMetadataRequestModel.md)|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_dataset_metadata_put**
> object update_metadata_dataset_metadata_put(dataset_metadata_request_model)

Update Metadata

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.dataset_metadata_request_model import DatasetMetadataRequestModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subsetter-api-jbzfw6l52q-uc.a.run.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subsetter-api-jbzfw6l52q-uc.a.run.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.HydroshareApi(api_client)
    dataset_metadata_request_model = openapi_client.DatasetMetadataRequestModel() # DatasetMetadataRequestModel | 

    try:
        # Update Metadata
        api_response = api_instance.update_metadata_dataset_metadata_put(dataset_metadata_request_model)
        print("The response of HydroshareApi->update_metadata_dataset_metadata_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HydroshareApi->update_metadata_dataset_metadata_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_metadata_request_model** | [**DatasetMetadataRequestModel**](DatasetMetadataRequestModel.md)|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

