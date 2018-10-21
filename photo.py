from PIL import Image, ImageDraw, ImageFont

grey = '#5C5D5C'
white = '#FFFFFF'
black = '#000000'
green = '#A2F057'

serif = ImageFont.truetype("serif.ttf", 50)
sans = ImageFont.truetype("sans.ttf", 50)
small_serif = ImageFont.truetype("serif.ttf", 20)

post_text = "Are we done here?"
response_text = "Ouija says: GOOD BYE"
post_link = 'ryanalvaro.com'
sizes = []
sizes.append(serif.getsize(post_text)[0])
sizes.append(sans.getsize(response_text)[0])
sizes.append(small_serif.getsize(post_link)[0])
img = Image.new('RGB', (max(sizes) + 100, 240), color=black)
d = ImageDraw.Draw(img)
d.text((50, 50), post_text, fill=white, font=serif)
d.text((50, 110), response_text, fill=green, font=sans)
d.text((50, 170), post_link, fill=grey, font=small_serif)

img.save('hi.png')
