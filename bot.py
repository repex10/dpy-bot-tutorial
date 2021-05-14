import discord

bot = commands.Bot(command_prefix='d!') # 프리픽스(접두사)을 설정입니다

@bot.event
async def on_ready():
  print(f'{bot.user.name}bot is online\n{bot.user.name} 봇이 온라인 되었습니다.')
  
@bot.command()
async def 핑(ctx):
  await ctx.send(f'{bot.latcner*1000}ms')

bot.run('토큰')
