from PIL import Image, ImageDraw, ImageFont
import pyimgur
import config

im = pyimgur.Imgur(config.IMGUR_ID)

grey = '#5C5D5C'
white = '#FFFFFF'
black = '#000000'
green = '#A2F057'

serif = ImageFont.truetype("serif.ttf", 50)
sans = ImageFont.truetype("sans.ttf", 50)
small_serif = ImageFont.truetype("serif.ttf", 20)
post_text = "Where will this image end up?"
response_text = "Ouija says: RIGHTHERE"
post_link = 'there would be a link here, but hey, this is only a demonstration'
img = Image.new('RGB', (serif.getsize(post_text)[0] + 100, 240), color=black)
d = ImageDraw.Draw(img)
d.text((50, 50), post_text, fill=white, font=serif)
d.text((50, 110), response_text, fill=green, font=sans)
d.text((50, 170), post_link, fill=grey, font=small_serif)

img.save('hi.png')

title = 'API TEST {}'.format(post_text)
uploaded_image = im.upload_image('hi.png', title=title, description=post_link)

print(uploaded_image.link)
