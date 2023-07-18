
from PIL import Image, ImageDraw

# Create a blank image
image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)

# Draw a line
draw.line((50, 50, 350, 50), fill="black", width=3)

# Draw a circle
draw.ellipse((50, 100, 150, 200), outline="black", width=3)

# Draw an arc
draw.arc((200, 100, 300, 200), start=45, end=180, fill="blue", width=3)

# Draw an ellipse
draw.ellipse((50, 250, 200, 350), outline="red", width=3)

# Draw a rectangle
draw.rectangle((250, 250, 350, 350), outline="green", width=3)

# Save the image
image.save("graphics_constructions.png", "PNG")
