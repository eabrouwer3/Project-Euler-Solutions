import re

pattern = "1.2.3.4.5.6.7.8.9.0"
compiled = re.compile(pattern)

i = 1

while not compiled.match("1029384754657483920"):
    i += 1

print i + 1
