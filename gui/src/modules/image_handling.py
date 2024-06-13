from PIL import Image

def resize_image(image_path: str, output_image: str, size) -> None:
  with Image.open(image_path) as image:
    resized_image = image.resize(size)
    resized_image.save(output_image)

