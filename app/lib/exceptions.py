# app/lib/exceptions.py

from dataclasses import dataclass


class BaseAPIException(Exception):
    pass


@dataclass
class EnvFileUnavailableError(BaseAPIException):
    error_code: int = 1
    pass


@dataclass
class UnavailableEnvironVariablesError(BaseAPIException):
    error_code: int = 2
    pass


@dataclass
class UnableToLoginToAPIError(BaseAPIException):
    error_code: int = 3
    pass


@dataclass
class InvalidRUTError(BaseAPIException):
    error_code: int = 4
    pass


@dataclass
class UnableToFindJSONFileError(BaseAPIException):
    error_code: int = 5
    pass


@dataclass
class InvalidAPILoginCredentialsError(BaseAPIException):
    error_code: int = 6
    pass


@dataclass
class InvalidExecutionFolderError(BaseAPIException):
    error_code: int = 7
    pass


@dataclass
class InvalidRUTLengthError(BaseAPIException):
    error_code: int = 8
    pass
