# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.phase_enum import PhaseEnum
from typing import Optional, Set
from typing_extensions import Self

class SubmissionResponseModel(BaseModel):
    """
    SubmissionResponseModel
    """ # noqa: E501
    workflow_id: StrictStr
    workflow_name: StrictStr
    phase: Optional[PhaseEnum] = None
    started_at: Optional[StrictStr] = Field(default=None, alias="startedAt")
    finished_at: Optional[StrictStr] = Field(default=None, alias="finishedAt")
    estimated_duration: Optional[StrictInt] = Field(default=None, alias="estimatedDuration")
    __properties: ClassVar[List[str]] = ["workflow_id", "workflow_name", "phase", "startedAt", "finishedAt", "estimatedDuration"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SubmissionResponseModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if phase (nullable) is None
        # and model_fields_set contains the field
        if self.phase is None and "phase" in self.model_fields_set:
            _dict['phase'] = None

        # set to None if started_at (nullable) is None
        # and model_fields_set contains the field
        if self.started_at is None and "started_at" in self.model_fields_set:
            _dict['startedAt'] = None

        # set to None if finished_at (nullable) is None
        # and model_fields_set contains the field
        if self.finished_at is None and "finished_at" in self.model_fields_set:
            _dict['finishedAt'] = None

        # set to None if estimated_duration (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_duration is None and "estimated_duration" in self.model_fields_set:
            _dict['estimatedDuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubmissionResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workflow_id": obj.get("workflow_id"),
            "workflow_name": obj.get("workflow_name"),
            "phase": obj.get("phase"),
            "startedAt": obj.get("startedAt"),
            "finishedAt": obj.get("finishedAt"),
            "estimatedDuration": obj.get("estimatedDuration")
        })
        return _obj


