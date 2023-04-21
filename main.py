#!/usr/bin/env python3
import sys
import re
import importlib


def to_camel_case(s):
    return re.sub(r'(?:^|_)(\w)', lambda m: m.group(1).upper(), s)


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['-plan', '-p']:
        print("Usage: python main.py -plan <plan_name>")
        return

    plan_name = to_camel_case(sys.argv[2])
    module_name = f"plan.{plan_name}Plan"
    print(module_name)

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print("Invalid plan!")
        return

    if not hasattr(module, "execute"):
        print(f"{module_name}.execute method not found!")
        return

    module.execute()


if __name__ == '__main__':
    main()
