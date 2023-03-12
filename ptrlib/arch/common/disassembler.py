from logging import getLogger
from typing import Optional, Union
from ptrlib.arch.intel import disassemble_intel, is_arch_intel, bit_by_arch_intel
#from ptrlib.arch.arm   import disassemble_arm, is_arch_arm
from ptrlib.binary.encoding import str2bytes

logger = getLogger(__name__)


def disassemble(code: Union[str, bytes],
                address: int=0,
                bits: Optional[int]=None,
                arch: Optional[str]='intel',
                syntax: Optional[str]='intel',
                returns: Optional[type]=list,
                objdump_path: str=None) -> Union[list, str]:
    if syntax.lower() == 'intel':
        syntax = 'intel' # Intel syntax
    else:
        syntax = 'att' # AT&T syntax

    if isinstance(code, str):
        code = str2bytes(code)

    if is_arch_intel(arch):
        if bits is None:
            bits = bit_by_arch_intel(arch)
            if bits == -1: bits = 64
        l = disassemble_intel(code, bits, address, syntax, objdump_path)

    elif is_arch_arm(arch):
        raise NotImplementedError("Not implemented")

    else:
        raise ValueError("Unknown architecture '{}'".format(arch))

    if returns == str:
        return '\n'.join(map(lambda v: v[1], l))
    else:
        return l

def disasm(code: bytes,
           arch: str='x86',
           mode: str='64',
           endian: str='little',
           address: int=0,
           micro: bool=False,
           mclass: bool=False,
           v8: bool=False,
           v9: bool=False,
           returns: type=list):
    raise NotImplementedError()
