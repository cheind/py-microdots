class CodecError(ValueError):
    """A base class for exceptions related to encoding/decoding issues."""

    pass


class DecodingError(CodecError):
    """Exceptions related to decoding."""

    pass
