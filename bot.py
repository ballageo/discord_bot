import discord, random
from discord.ext import commands
from settings import settings

client = commands.Bot("!")

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f"{member} has left the building!")

@client.command()
async def profile(ctx):
    await ctx.send(f"twitch.tv/sir_saltimus client is - {client.latency}")

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = [
        'Is gon b gud',
        'Try again later',
        'Sucks to suck, loser',
        'Git gud, scrub',
    ]
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear_all(ctx):
    await ctx.channel.purge()

client.run(settings.get('token'))