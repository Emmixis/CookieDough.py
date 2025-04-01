import logging
import discord
from discord.ext import commands
import random

log = logging.getLogger("cogs.misc")

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def faq(self, ctx):
        """FAQ/Copypasta list"""
        await ctx.send('''
## Gay Baby Jail - Frequently Asked Questions
Below is a list of commands you can use to either learn more about the server or quickly educate others
* Roles & Economy: `.economy`, `.allroles`, `.diapertraining`, `.verify`, `.verify-example`, `.vetted`
* Bots: `.pluralkit`, `.modmail`, `.help`, `pk;help`
* Other: `.feedback`, `.roleplay`, `.textrules`, `.lights`, `.discussion`, `.mediaguide`
''')
    @commands.hybrid_command(aliases=["verified"])
    async def verify(self,ctx):
        """copypasta command explaining our verification process"""
        await ctx.send('''
# 18+ Verification
Hi! Thank you for showing interest in becoming a verified member. Remember, this is not the same as becoming vetted, but it is part of the overall process. Need an example? Type `.verify_example`
## How-To
1. On a piece of paper, write “GBJ”, today\'s date, and your Discord username.
2. Take a photo of your ID laying on the previously written on paper.
3. Take a photo of you holding up your ID next to your face.
4. Use editing software to blur out all information on your ID aside from your birthdate, and your image.
5. Open a ticket in <#1172337920431104053> with your images. Wait for staff to review.
### What types of ID are accepted?
Anything that has your picture on it, so we can compare it against your face.
Typically, any government issued photo-ID is accepted. A birth certificate would not.
### What if I would rather not show my face?
You can wear a mask to cover the lower half of your face, but we must be able to tell it's you from your ID. If you choose to cover the bottom half, ensure the top half of your face is clear in both images.
                       ''')

    @commands.hybrid_command(aliases=["verifyexample"])
    async def verify_example(self,ctx):
        await ctx.send('''
# Example verification post
if your username is .girl-kisser and its January 28th, 2024, your verification would look like this.
Failure to follow this format will result in your verification request being denied. 
[Step 1 & 2](https://files.catbox.moe/rztcpp.jpg) | [Step 3](https://files.catbox.moe/xo542q.jpg)
                       ''')

    @commands.hybrid_command()
    async def economy(self, ctx):
        """copypasta command explaining all the ways to earn cookies in the economy"""
        await ctx.send('''
# Learn how to succeed in the GBJ economy
## Earning Cookies
### Commands
- All users can use `/work` in <#395837746083528704> every eight hours to earn 75–125 :cookie:
- Server boosters can user `/collect` in <#395837746083528704> once per month to earn 1000 :cookie:
### Posting Content
- In <#466529435861123072> and <#395817140181008394>, users can react to your posts with a :cookie:. Each reaction is worth 35 :cookie:.
- In <#395817177904840705>, <#396186429467656192>, <#928419082523541574>, <#468644623578038282>, or <#468644693669052417> users can react to your posts with a :pushpin:. If you get 16, your post will be sent to the #📌pinboard. Each post will earn you 150 :cookie:.
Redemption for these is manual. To claim your cookies, <#1172337920431104053>. In your ticket, post the link to your content. If you're claiming :cookie: reactions, be sure to include how many reactions you received next to each post.
### Community Engagement
- In <#1066605514466799616>, you can compete with other users in activities for each others :cookie:. A list of tasks can be found in the pinned messages if you need ideas.
- Use `!pay @username {amount}` to pay someone cookies. 
## Spending Cookies
- In <#395837746083528704>, you can browse the `/item store`. To buy an item, type `/item buy`.
## Useful Information
- To check your :cookie: balance, type `/bal` in <#395837746083528704>. To check someone else's balance, type `/bal @username`.
- To see all the roles you can purchase, type `.allroles`.
''')

    @commands.hybrid_command(aliases=["diaperserver"])
    async def discussion(self, ctx):
        """copypasta command explaining why we allow and encourage serious or adult conversations"""
        await ctx.send(
            '''Gay Baby Jail is not _just_ a diaper server. Its mostly a hangout server where diapers are normalized. \
We don't allow roleplay or baby-talk in the generals, and we're all adults. While serious topics aren't always being \
discussed, they are very much welcome in our server. Our goal is to create a kink-positive space; not a kink-only space.
Attempting to derail or discourage conversations by spamming GIFs, bringing up random topics, or exclaiming something \
to the effect of "this is a diaper server, why are we talking about this?" will result in a warning and/or a timeout.
If the current topic makes you uncomfortable, we have other channels, and there's plenty of other servers you can \
visit in the meantime as well. Thank you for your understanding.
''')

    @commands.hybrid_command()
    async def modmail(self, ctx):
        """copypasta command explaining modmail"""
        await ctx.send('''\
# How do I contact the GBJ staff?
Head to <#1172337920431104053>, and click `Open a ticket!`. This will put you in a channel with staff only, where you can express your concerns.
## Why can't I just send a PM to staff members?
Staff members are users of the server, first and foremost. We don't want to be a looming authority over the masses, we want to enjoy the server in the same way you do. This allows us to keep our PMs clear of formalities, and fosters friendships, rather than a power dynamic. 
## What if I have a complaint against another staff member?
If you need to submit a formal complaint against another moderator, we still urge you to use the ticket system. Each ticket has a robust logging system, allowing everyone to see the transcript of a ticket's message history. We use this to keep each staff member accountable. 
If you believe it's urgent, and the server is in danger, you may message any of the available babysitters individually. Abusing this may result in a warning.
''')

    @commands.hybrid_command(aliases=["mediaguide", "media", "mediaguidelines"])
    async def mediaguideline(self, ctx):
        """copypasta command explaining what kind of images are allowed in media channels"""
        await ctx.send('''\
Images which have the intention of being (abdl-)memes rather than "abdl-media" should be posted in \
<#639395194898219011>, and should not be posted in media channels. Posts in media channels must somehow pass as art, \
porn, photosets, erotica, fantasy, or something thereof, and must seem to have an intent to illicit either an erotic \
or aesthetic response in greater or equal proportion to memetic value. Bonus points for original art assets. You "know \
it when you see it".
[**Here's a few examples of what and what not to post in media channels (img-link)**](https://files.catbox.moe/e3vxwj.png)''')

    @commands.hybrid_command(aliases=["pk"])
    async def pluralkit(self, ctx):
        """copypasta command explaining what pluralkit is"""
        await ctx.send('''
## ____Why Are There Bots Talking?____
<@!466378653216014359> is a bot designed for plural systems that use Discord. It allows you to register systems, \
maintain system information, set up alters, set up message proxying, log headmate switching, and more.
Basically, the bot detects messages from an account and then is able to replace that message under a "proxy" \
account using webhooks. This is useful for multiple people sharing one body (systems), people who wish to \
roleplay as different characters without having several accounts, or anyone else who may want to post messages as a \
different person from one account. TL;DR, they're not bots, but regular chatters proxying their messages through \
a bot. You can react to a PK proxied message with ❓ to get info about the account that posted it, and 🔔 to ping the \
account.

You can learn more about the bot on [PluralKit's website](<https://pluralkit.me/>) \
or by using `pk;help in <#395837746083528704>`
You can learn more about plurality on [MoreThanOne.info](<https://morethanone.info/>)''')

    @commands.hybrid_command(aliases=["listroles", "roleslist", "rolelist"])
    async def allroles(self, ctx):
        """copypasta command that lists all available roles"""
        await ctx.send('''\
## All Custom Roles
We had to move the list to [this google sheet](<https://bit.ly/3Bd1Zbq>), it doesn't fit in discord anymore!
## Special Roles
* **<:PottyBanned:779149826154823691> Diaper Training** is a challenge role that diaperchecks you. Use \
`.diapertraining` in <#395837746083528704> for more info.\
''')

    @commands.hybrid_command()
    async def diapertraining(self, ctx):
        """copypasta explaining the diapertraining role"""
        embed = discord.Embed(title="<:PottyBanned:779149826154823691> .DiaperTraining",
                      description="\"<:K3llyQuestion:779208283197014026> What is this?\" Well basically, when <@&1134156024962617344> is pinged, trainers must post a padded selfie. The role was made to encourage and enforce wearing diapers 24/7.\n**24/7 and .verified? Join now!** You can buy access in <#395837746083528704> for 3000🍪!",
                      colour=0xc254ea)
        embed.add_field(name="📜 Rules:",
                value="1. Once pinged, trainers have **3 hours** to follow tasks expected of them\n2. Trainers **must** prove they're padded by posting a photo of themselves wearing to <#395817140181008394> or <#1207845981580697650>, then they will be immune for **8 hours**\n-# (However, we encourage them to continue participating)\n2. Trainers **must** react to any ping with a verification checkmark after posting their photo. They're also encouraged (but not required) to react with the diaper check emoji set\n-# (see reaction key for details)",
                inline=True)
        embed.add_field(name="<:Spank:633476981174042634> Punishments:",
                value="Trainers that fail to follow the rules will be fined a 1000🍪 penalty.\n\nFined cookies go to <@1335736614705430729>, so send your cookies to her to pay the fine\n-# `!pay <@1335736614705430729> 1000` \n\nAlternatively, trainers can ping an enforcer to leave diaper-training and have their role removed\n\n**If a trainer is caught lying or reusing an old photo, they will be banned from the server for 14 days and removed from the role.**",
                inline=True)
        embed.add_field(name="<:Noted:1173546484264874064> Reaction Key:",
                value="When <@&1134156024962617344> is pinged, a random reaction from each category will be added to the message which trainers are encouraged to fill out\nHere's what the reactions mean:\n\n**Required**:\nPhoto posted:\n<:GlowDiaperCheck:1356492857237569556>✅\n\n  **Optional Diaper Checks**:\nDry:\n<:PaddedPat:635092900769693716><:IsaButt:583184713611477012><:DrinkYourWater:753894051429744650><:RyderDiaperDab:1176023678698401802><:SammyButt:639496751593685022>\nWet:\n<:PeePee:582451994321747969><:DiaperSquish:644754120426651663><:DesperateHolding:690463676158705694>\nMess:\n<:PicartoMess:779886752357154846><:WoonessMess:639520828505194527><:RyhnMess:419732539951939594>\nSticky:\n<:Cummies:399457276056043520><:BooShy:656529920469630987><:AyinBlush:779202966708027392>",
                inline=True)
        embed.add_field(name="Rule Clarifications/Notes",
                value="- If a trainer is asleep, they will be required to post their photo right when they wake up.\n- Trainers may provide preemptive photos if they'll be awake and unable to check Discord for ≥3 hours. When they return, they must provide another picture.\n -# A good reason and a detailed explanation must be provided to be granted amnesty. Mundane reasons won't be accepted.",
                inline=False)
        embed.add_field(name="<:BridApplause:1356492855849385984> Users:",
                value="<:MeruPolice:935948597063716874> **Enforcers**:\n<@178965982528798720>\n<:PaddedPat:635092900769693716> **Diaper Trainers**:\n<@210817997269499904> <@221774651012022273> <@289078554837123073> <@114922027869143042> <@235482330335019008> <@281903443893813250> <@336555319134257155> <@184482129063837696>",
                inline=False)
        embed.set_footer(text="This post was brought to you by Anti Big Toilet")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        """diapertraining ping. add reactions and run the diapertraining hybrid command to paste the info copypasta"""
        if message.author.id == self.bot.user.id:
            return
        if len(message.role_mentions) > 0:
            for role_mention in message.role_mentions:
                if role_mention.id == 634353285498667008:
                    ctx = await self.bot.get_context(message)
                    command = self.bot.get_command("diapertraining")
                    await ctx.invoke(command)
                    verification = random.choice(['✅', '<:GlowDiaperCheck:1356492857237569556>'])
                    dry = random.choice(['<:PaddedPat:635092900769693716>', '<:IsaButt:583184713611477012>', '<:DrinkYourWater:753894051429744650>', '<:RyderDiaperDab:1176023678698401802>', '<:SammyButt:639496751593685022>'])
                    wet = random.choice(['<:PeePee:582451994321747969>', '<:DiaperSquish:644754120426651663>', '<:DesperateHolding:690463676158705694>'])
                    mess = random.choice(['<:PicartoMess:779886752357154846>', '<:WoonessMess:639520828505194527>', '<:RyhnMess:419732539951939594>'])
                    sticky = random.choice(['<:Cummies:399457276056043520>', '<:BooShy:656529920469630987>', '<:AyinBlush:779202966708027392>'])
                    await message.add_reaction(f'{verification}')
                    await message.add_reaction(f'{dry}')
                    await message.add_reaction(f'{wet}')
                    await message.add_reaction(f'{mess}')
                    await message.add_reaction(f'{sticky}')


    @commands.hybrid_command(aliases=["rule2", "rp"])
    async def roleplay(self, ctx):
        """copypasta explaining our roleplay rule"""
        await ctx.send('''\
## Rule 2: No Roleplay (or baby-talk)
We understand this is a very divisive rule which many don't understand. In short, we haven't curated GBJ to be a \
space for roleplay, and we feel it often comes into conflict with our desire to make the server a casual hang-out spot \
to have conversation in. There is a community owned opt-in channel <#855947209560162355> where you're free to roleplay \
and use baby-talk to your heart's content. You can opt-in at <#858253598944526337>. We also allow roleplay in \
<#1006312425487867944> threads which explicitly allow it in the OP.
\
## How does GBJ define roleplay (and baby-talk)?
We define **roleplay** in a number of ways. One of which includes any type of "action message". Examples include: \
_hugs_, [hugs], hugs you, etc.
Of course, roleplay can also involve any type of behavior which is fictional in nature and meant to act out a fantasy. \
one could roleplay a conversation with fictional circumstances. For example, talking as if you're in a nursery and are \
getting changed by the person you're talking to (or vice versa.)
Just because it isn't listed as an example doesn't mean we may not consider it roleplay. We'll use our best judgement \
when we're determining if a message is RP or not. However, emoji in almost all contexts are fine. Maybe use those as a\
substitute!
**Baby-talk** is a bit more complicated, but it's sort of a "know it when you see it" situation. Purposefully incorrect \
grammar, spelling, etc.
\
## How can I express myself?
As stated earlier, we have a range of emoji that you can use to express yourself, many of which are available without \
Nitro. If there's an emote we're missing, you can use `.economy` to learn how to buy it and add it to the server. You \
can also use `.stamps` to get a list of stamps provided by me, <@!641788291225747487>! They're a bit like stickers, but \
completely free. Albeit they only work in servers I'm a part of.
''')

    @commands.hybrid_command(aliases=["rules"])
    async def textrules(self, ctx):
        """copypasta linking our rules on gdocs"""
        await ctx.send('''\
[Here's a link to our current rules in plain text]\
(https://docs.google.com/document/d/13pxzthxFImkSLBOit4u4J6QXi2_5cbVq41qcwcnBYFE). \
You can make a copy by clicking `File > Make a copy` if you need to make it more readable. 
''')

    @commands.hybrid_command()
    async def lights(self, ctx):
        """copypasta for lights"""
        await ctx.send('''\
## Consent Indicators (aka lights)
* <:LightGreen:749514803822854224>: All clear, everything is going well. I consent.
* <:LightYellow:749514808335925288>: No to that, but lets keep going. Or, pause and check in. Something's not working.
* <:LightRed:749514808331731034>: Stop immediately and begin aftercare.
Failure to follow or heed to people's lights will result in an immediate ban. We take consent very seriously here.
''')

async def setup(bot):
    await bot.add_cog(Misc(bot))
