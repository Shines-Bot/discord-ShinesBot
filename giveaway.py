# A command for a giveaway system.

giveaways = []

@bot.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, duration: int, *, prize: str):
    """Let's you create a giveaway. !giveaway 'Duration' 'Prize'
    
    Example:
    !giveaway 10 test prize
    """
    embed = discord.Embed(
        title="🎉 Giveaway",
        description=f"Prize: {prize}\nDuration: {duration} seconds",
        color=discord.Color.brand_green()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction("🎉")

    giveaway = {
        "message_id": message.id,
        "channel_id": message.channel.id,
        "duration": duration,
        "prize": prize,
        "participants": []
    }

    giveaways.append(giveaway)

    await asyncio.sleep(duration)
    giveaway = next((g for g in giveaways if g["message_id"] == message.id), None)
    if giveaway is None:
        return

    new_message = await ctx.fetch_message(giveaway["message_id"])
    reaction = discord.utils.get(new_message.reactions, emoji="🎉")

    if reaction is None:
        return

    users = []
    async for user in reaction.users():
        if not user.bot:
            users.append(user)

    if len(users) > 0:
        winner = random.choice(users)
        if winner is not None:
            await ctx.send(f"Congratulations {winner.mention}! You won the {giveaway['prize']}!")
    else:
        await ctx.send(f"No participants joined the giveaway for the {giveaway['prize']}.")

    giveaways.remove(giveaway)

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    for giveaway in giveaways:
        if reaction.message.id == giveaway["message_id"]:
            if user.id not in giveaway["participants"]:
                giveaway["participants"].append(user.id)
            return
