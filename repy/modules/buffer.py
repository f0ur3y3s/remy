"""
This module contains the buffer class and datatype classes for packing and
unpacking data.

Example:
```
    buffer = Buffer()
    buffer.write_packed(DataType.UINT8, 255)
    buffer.write(b"Hello, World!")
    print(buffer.unpack(DataType.UINT8))
    # Output: 255
    print(buffer.data)
    # Output: b'Hello, World!'
```

"""

from enum import Enum
from struct import calcsize, pack, unpack, error as struct_error


class DataType(Enum):
    """Enum for uint data types for packing and unpacking"""

    UINT8 = ">B"
    UINT16 = ">H"
    UINT32 = ">I"


class DataTypeMax(Enum):
    """Enum for uint data types for packing and unpacking"""

    UINT8 = 0xFF
    UINT16 = 0xFFFF
    UINT32 = 0xFFFFFFFF


class Buffer:
    """Buffer for packing and unpacking data"""

    def __init__(self):
        self.buffer = bytearray()

    def write_packed(self, fmt: DataType, *args):
        """Write packed data to the buffer

        Args:
            fmt (DataType): DataType enum to use for packing
            *args: Data to pack
        """
        self.buffer.extend(pack(fmt.value, *args))

    def write(self, data: bytes = b""):
        """Write data to the buffer

        Args:
            data (bytes, optional): Data to write to the buffer.
            Defaults to b"".
        """
        self.buffer.extend(data)

    def unpack(self, fmt: DataType) -> tuple:
        """Unpack data from the buffer. This function is destructive and will
        remove the unpacked data from the buffer.

        Args:
            fmt (DataType): DataType enum to use for unpacking

        Returns:
            tuple: Unpacked data

        Raises:
            struct.error: If the buffer is too small to unpack the data
        """
        size = calcsize(fmt.value)

        try:
            data = unpack(fmt.value, self.buffer[:size])[0]
        except struct_error:
            raise

        self.buffer = self.buffer[size:]

        return data

    @property
    def data(self) -> bytes:
        """Get the buffer data

        Returns:
            bytes: Buffer data
        """
        return self.buffer
