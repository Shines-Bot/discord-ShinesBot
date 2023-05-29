# Here we create a reaction roles sytem for our bot.

@bot.command()
@commands.has_permissions(manage_roles=True)
async def crr(ctx):
    """Creates a reaction roles system with predefined roles."""
    guild = ctx.guild

    # Create the roles if they don't exist
    role_names = ["Giveaways Ping", "Notifications", "Event Ping"]
    for role_name in role_names:
        role = discord.utils.get(guild.roles, name=role_name)
        if role is None:
            role = await guild.create_role(name=role_name)

    # Create the embed message
    embed = discord.Embed(title='Reaction Roles',
                          description='React with any of the emojis below to this message to get a role.',
                          color=discord.Color.brand_green())

    embed.add_field(name='🎁', value='Giveaways Ping')
    embed.add_field(name='📆', value='Event Ping')
    embed.add_field(name='🔔', value='Notifications')

    message = await ctx.send(embed=embed)

    reactions = ['🎁', '📆', '🔔']
    for reaction in reactions:
        await message.add_reaction(reaction)


@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    emoji_role_mapping = {
        '🎁': 'Giveaways Ping',
        '📆': 'Event Ping',
        '🔔': 'Notifications'
    }

    role_name = emoji_role_mapping.get(str(payload.emoji))
    if role_name:
        role = discord.utils.get(guild.roles, name=role_name)
        await member.add_roles(role)
        await member.send(f"You have been given {role.name}!")


@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    emoji_role_mapping = {
        '🎁': 'Giveaways Ping',
        '📆': 'Event Ping',
        '🔔': 'Notifications'
    }

    role_name = emoji_role_mapping.get(str(payload.emoji))
    if role_name:
        role = discord.utils.get(guild.roles, name=role_name)
        await member.remove_roles(role)
        await member.send(f"You have been removed from {role.name}!")
