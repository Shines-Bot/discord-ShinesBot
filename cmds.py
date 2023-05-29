
# The socials command.

@bot.command()
async def socials(ctx):
    """Visit some of the largest Social Media/Sites on your internett browser!"""
    view = ButtonView()
    await ctx.send('**__Click the buttons for any Socials to either visit or enter!__**', view=view)

 
# The Chances minigame and Guide.

 @bot.command()
 async def chance(ctx):
    """Let's you play a game of chances with 8 other users!"""
    messages = [
        '|CHANCE| You reversed, {}!',
        '|CHANCE| You added 1 extra round, {}!',
        '|CHANCE| You lost, {}!',
        '|CHANCE| You got away, {}!'
    ]
    response = random.choice(messages).format(ctx.author.name)

    embed = discord.Embed(title="Chance Result", description=response, color=discord.Color.brand_green())
    embed.set_author(name=ctx.author.name)

    await ctx.send(embed=embed)
