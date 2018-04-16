# Using frida and capstone to disassembly code on memory region
#
# Run: python read-mem.py
import frida
import sys 
import IPython
import capstone

cs = None
session = None


def on_message(message, data):
    print(message)


def load_script(script_name):
    with open(script_name) as f:
        script = f.read()
    return script 


def setup_capstone():
    cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
    return cs


def disasm(offset, size):
    code = session.read_bytes(offset, size)
    for dis in cs.disasm(code, offset, size):
        print("0x%x:\t%s\t%s" % (dis.address, dis.mnemonic, dis.op_str))


def main():
    # Attach on running process
    global session
    session = frida.attach("target.exe")

    # Create Capstone instance
    global cs
    cs = setup_capstone()

    # Disassemble the codes
    disasm(0x123456, 10)

    IPython.embed()
    session.detach()
    sys.exit(0)


if __name__ == '__main__':
    main()