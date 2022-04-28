# Forked for Disnake Compatibility
This fork is currently in development and may be not working as of now. Commits are for update purposes to keep track.

This is what you should expect to this fork:

- [x] Support for [disnake](https://pypi.org/project/disnake.py/) (obviously)
- [x] Slight improvements to pagination.
- [x] ~~Music rewording, slight improvements.~~ Please check out [DisnakeWavelink](https://github.com/raianah/DisnakeWavelink).
- [ ] Full usage of buttons instead of reactions (or I can provide both idk)
- [ ] Invite Tracker

# DisnakeUtils
A very useful library made to be used in with [disnake](https://pypi.org/project/disnake/)

# Installation

```
pip install git+https://github.com/raianah/DisnakeUtils
```

Requires disnake and/or disnake[voice] so make sure you have all dependencies of it installed.

# Example code

### DisnakeUtils.Pagination.AutoEmbedPaginator
```python
from disnake import Embed
import DisnakeUtils

@bot.command()
async def paginate(ctx):
    embed1 = Embed(color=ctx.author.color).add_field(name="Example", value="Page 1")
    embed2 = Embed(color=ctx.author.color).add_field(name="Example", value="Page 2")
    embed3 = Embed(color=ctx.author.color).add_field(name="Example", value="Page 3")
    paginator = DisnakeUtils.Pagination.AutoEmbedPaginator(ctx)
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)
```

### DisnakeUtils.Pagination.CustomEmbedPaginator
```python
from disnake import Embed
import DisnakeUtils

@bot.command()
async def paginate(ctx):
    embed1 = Embed(color=ctx.author.color).add_field(name="Example", value="Page 1")
    embed2 = Embed(color=ctx.author.color).add_field(name="Example", value="Page 2")
    embed3 = Embed(color=ctx.author.color).add_field(name="Example", value="Page 3")
    paginator = DisnakeUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔴', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    paginator.add_reaction('🗑️', "delete")
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)
```

### DisnakeUtils.InviteTracker
```python
import disnake
from disnake.ext import commands
import DisnakeUtils

intents = disnake.intents.default()
intents.members = True
bot = commands.AutoShardedBot(command_prefix=">", intents=intents)
tracker = DisnakeUtils.InviteTracker(bot)

@bot.event
async def on_member_join(member):
    inviter = await tracker.fetch_inviter(member) # inviter is the member who invited
```

### DisnakeUtils.Music
```python
import disnake
from disnake.ext import commands
import DisnakeUtils

bot = commands.AutoShardedBot(command_prefix=">")
music = DisnakeUtils.Music()

@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() #Joins author's voice channel
    
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
@bot.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")
        
@bot.command()
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused {song.name}")
    
@bot.command()
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")
    
@bot.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")
    
@bot.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")
    
@bot.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")
    
@bot.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)
    
@bot.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@bot.command()
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume for {song.name} to {volume*100}%")
    
@bot.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")
```

For further information please read the docs

# Links
**[Documentation](https://docs.discordutils.gq)**

**[Github](https://github.discordutils.gq)**

# Support
**__Please make sure that you are on the latest version of [DisnakeUtils](https://github.com/raianah/DisnakeUtils) and [youtube_dl](https://pypi.org/project/youtube_dl) before contacting for support__**

Email me (raianah.twilight@gmail.com) for support.
