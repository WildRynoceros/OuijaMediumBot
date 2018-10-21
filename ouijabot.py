from PIL import Image, ImageDraw, ImageFont
import pyimgur
import praw
import config

im = pyimgur.Imgur(config.IMGUR_ID)

bot = praw.Reddit(user_agent='OuijaMediumBot v0.1',
                  client_id=config.REDDIT_ID,
                  client_secret=config.REDDIT_SECRET,
                  username=config.REDDIT_USER,
                  password=config.REDDIT_PASS)

grey = '#5C5D5C'
white = '#FFFFFF'
black = '#000000'
green = '#A2F057'

serif = ImageFont.truetype("serif.ttf", 50)
sans = ImageFont.truetype("sans.ttf", 50)
small_serif = ImageFont.truetype("serif.ttf", 20)

subreddit = bot.subreddit('test')

for comment in subreddit.stream.comments():
    if 'u/ouijamediumbot' in comment.body.lower():
        submission = comment.submission
        post_text = bot.submission(id=submission).title
        response_text = bot.submission(id=submission).link_flair_text
        post_link = 'www.reddit.com/r/AskOuija/comments/{}'.format(submission)
        img = Image.new('RGB', (serif.getsize(post_text)[0] + 100, 240), color=black)
        d = ImageDraw.Draw(img)
        d.text((50, 50), post_text, fill=white, font=serif)
        d.text((50, 110), response_text, fill=green, font=sans)
        d.text((50, 170), post_link, fill=grey, font=small_serif)

        img.save('hi.png')

        title = 'TEST - AskOuija {}'.format(submission)
        uploaded_image = im.upload_image('hi.png', title=title, description=post_link)

        print(uploaded_image.link)
        comment.reply('[I have conjured the spirits for you]({})'.format(link))
        print("Completed\n")
