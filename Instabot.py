from instabot import bot
bot=bot()
bot.login(username="your_insta_id",password="password")

#bot.follow('the account that you gonna follow')

#bot.upload_photo("file path" ,caption= new photo ")

#bot.unfollow("the account you want to unfollow")

#bot.send_message("hii",[ "account id that you want to send message","account id that you want to send message"])

followers=bot.get_user_followers("the account that you gonna know their followers")
for follwer in follower:
    print(bot.get_user_info(follower))
