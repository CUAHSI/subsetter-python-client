# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.argo_api import ArgoApi


class TestArgoApi(unittest.TestCase):
    """ArgoApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ArgoApi()

    def tearDown(self) -> None:
        pass

    def test_argo_metadata_argo_workflow_id_get(self) -> None:
        """Test case for argo_metadata_argo_workflow_id_get

        Argo Metadata
        """
        pass

    def test_extract_metadata_extract_metadata_post(self) -> None:
        """Test case for extract_metadata_extract_metadata_post

        Extract Metadata
        """
        pass

    def test_logs_logs_workflow_id_get(self) -> None:
        """Test case for logs_logs_workflow_id_get

        Logs
        """
        pass

    def test_refresh_workflow_refresh_get(self) -> None:
        """Test case for refresh_workflow_refresh_get

        Refresh Workflow
        """
        pass

    def test_refresh_workflow_refresh_workflow_id_get(self) -> None:
        """Test case for refresh_workflow_refresh_workflow_id_get

        Refresh Workflow
        """
        pass

    def test_submissions_submissions_get(self) -> None:
        """Test case for submissions_submissions_get

        Submissions
        """
        pass

    def test_submit_nwm1_submit_nwm1_post(self) -> None:
        """Test case for submit_nwm1_submit_nwm1_post

        Submit Nwm1
        """
        pass

    def test_submit_nwm2_submit_nwm2_post(self) -> None:
        """Test case for submit_nwm2_submit_nwm2_post

        Submit Nwm2
        """
        pass

    def test_submit_nwm_submit_nwm_post(self) -> None:
        """Test case for submit_nwm_submit_nwm_post

        Submit Nwm
        """
        pass

    def test_submit_parflow_submit_parflow_post(self) -> None:
        """Test case for submit_parflow_submit_parflow_post

        Submit Parflow
        """
        pass


if __name__ == '__main__':
    unittest.main()
