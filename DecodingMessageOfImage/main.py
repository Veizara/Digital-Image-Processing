from PIL import Image
class DecodeClass:
    def FindingMessage(self):

        image = "23.tif"
        sentinel = "&"
        img = Image.open(image)
        pixels = list(img.getdata())
        width, height = img.size

        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        lsb_plane = [[pixel & 1 for pixel in row] for row in pixels]
        bits = [lsb_plane[j][i] for i in range(width) for j in range(height)]

        message = ""
        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            byte_str = "".join(str(bit) for bit in byte)
            byte_ascii = int(byte_str, 2)
            char = chr(byte_ascii)
            message += char
            if char == sentinel:
                break
        print(message[:-1])

message = DecodeClass()
message.FindingMessage()