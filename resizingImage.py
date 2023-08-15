from PIL import Image

image = Image.open("C:\\Users\\marvi\\Downloads\\istockphoto-1172427455-612x612.jpg")
print(f"Original size : {image.size}")

sunset_resized = image.resize((400, 400))
sunset_resized.save('sunset_400.jpg')