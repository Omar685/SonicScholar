class BRT:
  def encrypt(text: str, password: int = 90):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
          ascii_offset = ord("a") if char.islower() else ord("A")
          encrypted_char = chr((ord(char) - ascii_offset + password) % 26 + ascii_offset)
          encrypted_text += encrypted_char
        else:
          encrypted_text += char
    return encrypted_text

  def decrypt(encrypt_text, password: int):
    return BRT.encrypt(encrypt_text, -password)