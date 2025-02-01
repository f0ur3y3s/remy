from enum import IntEnum, IntFlag


class Opcode(IntEnum):
    STATUS = 0x01
    FILE_IO = 0x02
    EXEC = 0x03
    INTERACTIVE = 0x0F
    LINK = 0x10
    STOP = 0xFF


class Retcode(IntEnum):
    OK = 0x01
    ERROR = 0xFF

# Command codes

class FileIO(IntEnum):
    LIST = 0x01
    PUT = 0x02
    GET = 0x03


class Status(IntEnum):
    GENERAL = 0x01
    UPTIME = 0x02
