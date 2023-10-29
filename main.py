import discord, utils

config = utils.Config.from_env(".env")
print("Logging in...")

bot = utils.DiscordBot(
    config=config, command_prefix=config.discord_prefix,
    prefix=config.discord_prefix, command_attrs=dict(hidden=True),
    help_command=utils.HelpFormat(),
    allowed_mentions=discord.AllowedMentions(
        everyone=False, roles=False, users=True
    ),
    intents=discord.Intents(
        # kwargs found at https://docs.pycord.dev/en/master/api.html?highlight=discord%20intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True,
        presences=True, message_content=True,
    )
)

try:
    bot.run(config.discord_token)
except Exception as e:
    print(f"Error when logging in: {e}")

utils.Alive()