from enum import Enum

SUPPORTED_FILE_EXTENSIONS = {'.csv', '.json'}

class DataReadingErrorMessages(Enum):
    INVALID_CLAIM_ID = "Invalid claim ID provided."
    CLAIM_NOT_FOUND = "Claim not found in the system."
    INVALID_CLAIM_STATUS = "The provided claim status is invalid."
    UNAUTHORIZED_ACCESS = "You do not have permission to access this claim."
    DATABASE_ERROR = "An error occurred while accessing the database."
    INVALID_INPUT = "The input provided is not valid."
    CLAIM_ALREADY_EXISTS = "A claim with this ID already exists."
    PROCESSING_ERROR = "An error occurred while processing the claim."
    TIMEOUT_ERROR = "The request timed out. Please try again later."
    UNKNOWN_ERROR = "An unknown error has occurred. Please contact support."
    INVALID_FILE_PATH = "The provided file path is invalid."
    FILE_NOT_FOUND = "The specified file could not be found."
    INVALID_FILE_PATH_TYPE = "The file path must be a string or Path object."
    DATA_FORMAT_ERROR = "The data format is incorrect or unsupported."
    EXT_NOT_SUPPORTED = "The file extension '{ext}' is not supported. Supported extensions are: {supported_extensions}."
    EMPTY_DATA = "The data file is empty or contains no valid records."