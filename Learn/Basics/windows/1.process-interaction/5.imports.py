# Archive of Reversing.ID
# Frida Compendium - Windows Basic
#
# Enumerate imported symbol of application
#
# Run: python enum-imports.py
#
import frida
import sys

TARGET_APP = "dllfunc32.exe"
LIB_NAME   = "library32.dll"

def on_message(message, data):
    print(message)


def read_script(script_name):
    with open(script_name) as f:
        script = f.read() 
    return script 
        

def main():
    # Attach on running process
    session = frida.attach(TARGET_APP)

    # Instrumentation script 
    # Using Interceptor to attach to a function
    # Here we are inside a function
    jscode = read_script("imports.js"); 
    script = session.create_script(jscode % (TARGET_APP))

    # Set a callback, when frida is sending a string, we print it out
    script.on('message', on_message)

    # Load the script
    script.load()

    # Delay
    # Execution is happened on other process so we need to make our script 
    # running all the way to the end
    input("[!] Press <Enter> at any time to detach from instrumented program.\n\n")
    session.detach()


if __name__ == '__main__':
    main()