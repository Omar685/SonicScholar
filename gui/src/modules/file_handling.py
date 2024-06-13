def read_css(filename: str) -> str:
  with open(filename, "r") as style_file:
    code = style_file.read()
  return code

def readFile(filename: str):
  with open(filename, "r") as file:
    code = file.read()
  return code

