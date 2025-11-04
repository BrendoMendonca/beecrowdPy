import struct
import sys

#função para simular a precisão simples de float 32-bit
def to_float32(n):
    return struct.unpack('f', struct.pack('f', n))[0]

s = input()
s1_in, s2_in = map(float, s.split())
s1 = to_float32(s1_in)
s2 = to_float32(s2_in)

f = input()
f1, f2 = map(float, f.split())

print(f"A = {s1:.6f}, B = {s2:.6f}")
print(f"C = {f1:.6f}, D = {f2:.6f}")

print(f"A = {s1:.1f}, B = {s2:.1f}")
print(f"C = {f1:.1f}, D = {f2:.1f}")

print(f"A = {s1:.2f}, B = {s2:.2f}")
print(f"C = {f1:.2f}, D = {f2:.2f}")

print(f"A = {s1:.3f}, B = {s2:.3f}")
print(f"C = {f1:.3f}, D = {f2:.3f}")

print(f"A = {s1:.3E}, B = {s2:.3E}")
print(f"C = {f1:.3E}, D = {f2:.3E}")

print(f"A = {s1:.0f}, B = {s2:.0f}")
print(f"C = {f1:.0f}, D = {f2:.0f}")