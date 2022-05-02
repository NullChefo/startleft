from enum import Enum

from startleft.messages import messages


class ErrorCode(Enum):
    IAC_TO_OTM_EXIT_UNEXPECTED = (1, "IacToOtmUnexpectedError")
    IAC_TO_OTM_EXIT_VALIDATION_FAILED = (2, "IacToOtmValidationError")
    OTM_TO_IR_EXIT_UNEXPECTED = (3, "OtmToIrUnexpectedError")
    OTM_TO_IR_EXIT_VALIDATION_FAILED = (4, "OtmToIrValidationError")
    MAPPING_FILE_EXIT_VALIDATION_FAILED = (5, "MalformedMappingFile")

    def __init__(self, system_exit_status, error_type):
        self.system_exit_status = system_exit_status
        self.error_type = error_type

    def __str__(self):
        return f'{self.exit_value}'


class CommonError(Exception):
    message: str
    http_status_code: int
    error_code: ErrorCode


class IriusUnauthorizedError(CommonError):
    message = messages.UNAUTHORIZED_EXCEPTION
    http_status_code = 401
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED


class IriusTokenNotSetError(CommonError):
    message = messages.UNAUTHORIZED_EXCEPTION
    http_status_code = 401
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED


class IriusForbiddenError(CommonError):
    message = messages.FORBIDDEN_OPERATION
    http_status_code = 403
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED


class IriusProjectNotFoundError(CommonError):
    message = messages.PROJECT_NOT_FOUND
    http_status_code = 404
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED


class IriusServerNotSetError(CommonError):
    message = messages.IRIUS_SERVER_NOT_SET
    http_status_code = 500
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED


class IriusServerUnreachableError(CommonError):
    message = messages.IRIUS_SERVER_UNREACHABLE
    http_status_code = 500
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED


class IriusCommonApiError(CommonError):
    message = messages.UNEXPECTED_API_ERROR
    http_status_code = 500
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED

    def __init__(self, http_status_code: int, message: str):
        self.http_status_code = http_status_code
        self.message = message


class IriusInvalidResponseError(CommonError):
    message = messages.IRIUS_INVALID_RESPONSE
    http_status_code = 500
    error_code = ErrorCode.OTM_TO_IR_EXIT_VALIDATION_FAILED


class OTMInconsistentIdsError(CommonError):
    message = messages.INCONSISTENT_IDS
    http_status_code = 500
    error_code = ErrorCode.OTM_TO_IR_EXIT_VALIDATION_FAILED


class OTMSchemaNotValidError(CommonError):
    message = messages.OTM_SCHEMA_IS_NOT_VALID
    http_status_code = 500
    error_code = ErrorCode.OTM_TO_IR_EXIT_VALIDATION_FAILED


class OTMFileNotFoundError(CommonError):
    message = messages.OTM_FILE_NOT_FOUND
    http_status_code = 500
    error_code = ErrorCode.OTM_TO_IR_EXIT_UNEXPECTED


class MappingFileNotFoundError(CommonError):
    message = messages.MAPPING_FILE_NOT_FOUND
    http_status_code = 500
    error_code = ErrorCode.IAC_TO_OTM_EXIT_UNEXPECTED


class MappingFileSchemaNotValidError(CommonError):
    message = messages.MAPPING_FILE_SCHEMA_NOT_VALID
    http_status_code = 400
    error_code = ErrorCode.MAPPING_FILE_EXIT_VALIDATION_FAILED

    def __init__(self, message: str):
        self.message = f"{self.message}. {message}"


class WriteThreatModelError(CommonError):
    message = messages.ERROR_WRITING_THREAT_MODEL
    http_status_code = 500
    error_code = ErrorCode.IAC_TO_OTM_EXIT_UNEXPECTED
