from dotenv import load_dotenv

load_dotenv()

import discord
from os import environ

image_exts = [
    "jpg",
    "jpeg",
    "png",
    "webp",
    "gif",
    "tiff",
    "tif",
    "bmp",
    "heif",
    "heic",
    "svg",
]


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message: discord.message.Message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.channel.id == 330061439685492736:
            has_direct_image = len(message.attachments) > 0
            has_image_url = "http" in message.content and any(
                ext in message.content for ext in image_exts
            )

            if not has_direct_image and not has_image_url:
                # no images in this message!
                await message.delete()
            else:
                nick = message.author.nick
                name = nick if nick is not None else message.author.name
                thread_name = f"{name}'s Leekz!"

                content = message.content

                if has_image_url:
                    # strip out the url
                    content = content.split(" ")
                    new_content = []
                    for i in content:
                        if "http" not in i:
                            new_content.append(i)
                    content = " ".join(new_content)

                if content.strip() != "":
                    thread_name = content

                await message.create_thread(name=thread_name)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


token = environ.get("LEEKZ_TOKEN")
client.run(token)
