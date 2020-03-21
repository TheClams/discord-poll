import discord, re
from discord.ext import commands

token = ''
pollers = []

# Read configuration : token, pollers, ...
with open('config.yaml', "r") as f:
    section = ''
    for l in f.readlines() :
        if len(l.strip()) == 0:
            continue
        if section == '' :
            m = re.match(r'(\w+)\s+:\s*(.*)',l)
            if m :
                if m.group(1) == 'token' : token = m.group(2);
                else : section = m.group(1);
            else :
                print('Unkown config line {}'.format(l))
        elif section == 'pollers':
            m = re.match(r'\s+-(.*)',l)
            if m :
                pollers.append(m.group(1).strip())
        else :
            section = ''

# print('token = {}'.format(token))
print('Pollers role are {}'.format(pollers))

bot = discord.Client()

@bot.event
async def on_ready():
    print('ViralVote online !')

# Message handler:
# Accept two format of messages:
#  - !poll This is my poll
#  - !poll {This is my question} [Choice 1] [Choice 2] [Choice 3] [Choice 4] ...
@bot.event
async def on_message(message):

    if message.author.bot or not isinstance(message.author,discord.Member):
        return

    if not message.content.startswith("!poll") :
        return;

    roles = [r.name for r in message.author.roles]
    l = list(set(roles) & set(pollers))
    if len(l) == 0:
        print('{} has roles {} -> Not a poller'.format(message.author.name, roles))
        return

    msg = message.clean_content
    m = re.search(r'\{(.*?)\}',msg)
    if not m:
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')
    else:
        title = m.group(1)

        options = re.findall(r'\[(.*?)\]',msg)
        if len(options) > 25:
            await message.channel.send("Maximum of 25 options")
            return

        emojis = []
        txt = ""
        for i,option in enumerate(options):
            if len(option)==0:
                continue
            hex_str = hex(224 + (6 + i))[2:]
            reaction = b'\\U0001f1a'.replace(b'a', bytes(hex_str, "utf-8")).decode("unicode-escape")
            emojis.append(reaction)
            if i != 0:
                txt+= '\n\n'
            txt += '{} {}'.format(reaction,option)

        vote_embed = discord.Embed(title=title,description=txt)
        vote_embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)

        poll_msg = await message.channel.send(embed=vote_embed)

        for emoji in emojis:
            await poll_msg.add_reaction(emoji)

# Start bot
bot.run(token)