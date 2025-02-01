from repy.modules.opcodes import *
from ctypes import c_uint


class Protocol:
    opcode: Opcode
    commcode: FileIO | Status | bytes
    packet_len: c_uint
    data: bytes
