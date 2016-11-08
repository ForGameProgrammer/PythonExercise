from struct import *

# Convert To Byte
converted = pack("iif", 25, 13, 28.2)

"""
pack(format,*data)
Format :
i -> Integer
f -> Float
d -> Double
l -> Long
s -> char[] -> String
"""

print(converted)

resolved = unpack("iif", converted)

print(resolved)
