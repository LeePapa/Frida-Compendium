# Archive of Reversing.ID
# Frida Compendium - Windows Basic
#
# Create and RPC endpoint which can be used in host and executed by the frida
#
# Run: python rpc.py 
import frida
import sys

# Use this script to inject following JS file to target

# Target: id.reversing.classop
#   - rpc.js

TARGET_APP = "id.reversing.classop"

def load_script(script_name):
    with open(script_name) as f:
        script = f.read()
    return script 


def main():
    # Attach on running process
    session = frida.get_usb_device().attach(TARGET_APP)

    # Instrumentation script 
    jscode = load_script("rpc.js")
    script = session.create_script(jscode)

    # Load the script
    script.load()

    # Use exported RPC
    api    = script.exports
    # Call function hello()
    api.hello("Xathrya", "World")


    # Delay
    # Execution is happened on other process so we need to make our script 
    # running all the way to the end
    input("[!] Press <Enter> at any time to detach from instrumented program.\n\n")
    session.detach()


if __name__ == '__main__':
    main()

    