import struct, zlib

w, h = 1000, 600
with open("board.raw", "rb") as f:
    raw = f.read()
data = b"".join(b"\x00" + raw[i * w * 3 : (i + 1) * w * 3] for i in range(h))
def chunk(t, c):
    return struct.pack(">I", len(c)) + t + c + struct.pack(">I", zlib.crc32(t + c))
png = b"\x89PNG\r\n\x1a\n"
png += chunk(b"IHDR", struct.pack(">2I5B", w, h, 8, 2, 0, 0, 0))
png += chunk(b"IDAT", zlib.compress(data))
png += chunk(b"IEND", b"")
with open("board.png", "wb") as f:
    f.write(png)
