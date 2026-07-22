class Pagination:

    DEFAULT_PAGE = 1

    DEFAULT_PAGE_SIZE = 10

    MAX_PAGE_SIZE = 100


class ModelVersion:

    DEFAULT = "v1.0"


class FileUpload:

    MAX_FILE_SIZE = 10 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".docx",
    }