#!/usr/bin/env python3
# Author: Christer Karlsen
# Email: chris@ramosicked.com
# Project: appwrite
# Copyright (c) 2023, Christer Karlsen
# License: MIT License
#
import subprocess
import sys

def start_app():
    subprocess.run(["docker", "run", "-it", "--rm", 
                    "--volume", "/var/run/docker.sock:/var/run/docker.sock", 
                    "--volume", "$(pwd)/appwrite:/usr/src/code/appwrite:rw", 
                    "--entrypoint=install", 
                    "appwrite/appwrite:1.2.0"])

def stop_app():
    subprocess.run(["docker", "stop", "appwrite"])

def reset_app():
    subprocess.run(["rm", "-rf", "$(pwd)/appwrite"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an argument: start, stop, or reset")
    else:
        command = sys.argv[1]
        if command == "start":
            start_app()
        elif command == "stop":
            stop_app()
        elif command == "reset":
            reset_app()
        else:
            print("Invalid argument. Please provide either start, stop, or reset")

