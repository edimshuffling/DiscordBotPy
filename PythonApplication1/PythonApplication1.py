import asyncio
import discord
from discord.ext import commands

class Commands:
    @commands.command(pass_context=True, no_pm=True)
    async def delete(self, ctx, numb : int):
        deleted = 0
        try:
            deleted = await bot.purge_from(ctx.message.channel, limit=numb)
            msg = await bot.send_message(ctx.message.channel, "Deleted {} messages.".format(len(deleted)))
            print("s")
        except:

            async for i in bot.logs_from(ctx.message.channel, limit=numb):
                await bot.delete_message(i)
                deleted+=1
            msg = await bot.send_message(ctx.message.channel, "Deleted {} messages.".format(str(deleted)))
            print("a")
        await asyncio.sleep(5)
        print("d")
        await bot.delete_message(msg)

    @commands.command(pass_context=True, no_pm=True)
    async def deleteall(self, ctx):
        deleted = 0
        async for i in bot.logs_from(ctx.message.channel):
            await bot.delete_message(i)
            deleted += 1
        msg = await bot.send_message(ctx.message.channel, "Deleted {} message(s).".format(str(deleted)))
        await asyncio.sleep(2)
        await bot.delete_message(msg)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('|'), description='A playlist example for discord.py')
bot.add_cog(Commands())

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run("") #Token in quotation marks
