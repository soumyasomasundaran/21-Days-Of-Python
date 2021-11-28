import re
try:
    re.compile(input())
    is_valid = True
except re.error as e:
    is_valid = False
finally:
    print(is_valid)