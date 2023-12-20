import binascii

class BaseConversion:
    def __init__(self, text):
        self.text = text

class Text(BaseConversion):
    def text_to_binary(self):
        return bin(int.from_bytes(self.text.encode(), 'big'))[2:]

    def text_to_hex(self):
        return self.text.encode().hex()

    def text_to_decimal(self):
        return [str(ord(char)) for char in self.text]

class Binary(BaseConversion):
    def binary_to_hex(self):
        return hex(int(self.text, 2))[2:]

    def binary_to_text(self):
        n = int(self.text, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

    def binary_to_decimal(self):
        return int(self.text, 2)

class Hex(BaseConversion):
    def hex_to_text(self):
        return bytes.fromhex(self.text).decode('utf-8')

    def hex_to_binary(self):
        return bin(int(self.text, 16))[2:]

    def hex_to_decimal(self):
        return int(self.text, 16)

class Decimal(BaseConversion):
    def decimal_to_text(self):
        return chr(int(self.text))

    def decimal_to_hex(self):
        return hex(int(self.text))

    def decimal_to_binary(self):
        return bin(int(self.text))
