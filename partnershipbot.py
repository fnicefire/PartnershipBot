# Copyright (c) 2025 - .rotafn (VortexTeam) - All rights reserved.
# This code is protected by the VortexTeam (.rotafn) Proprietary License.
# Use, modification, or distribution is prohibited without written permission.
# The full version of the license is available upon request.
# -------------------
import discord
from discord.ext import commands
from discord import app_commands

# === CONFIGS  ===
DISCORD_TOKEN = ""  # Bot Token
PARTNERSHIP_CHANNEL_ID = 1409569987424948306  # Channed ID
EMOJI = "⭐"  # Emoji 
# ===============================

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class PartnershipModal(discord.ui.Modal, title="Invia partnership"):
    def __init__(self, manager: discord.User):
        super().__init__()
        self.manager = manager

        self.msg_input = discord.ui.TextInput(
            label="Partnership message",
            placeholder="Write the content of the partnership here…"
            style=discord.TextStyle.long,
            max_length=1900,
            required=True
        )
        self.add_item(self.msg_input)

    async def on_submit(self, interaction: discord.Interaction):
        content = str(self.msg_input.value).strip()
        guild_name = interaction.guild.name if interaction.guild else "N/A"

        final_message = (
            f"{content}\n"
            f"⬩ ⬩ ⬩ ⬩ ⬩✦ {EMOJI} ✦⬩ ⬩ ⬩ ⬩ ⬩ \n"
            f"🧑‍💻 **Author:** {interaction.user.mention}\n"
            f"🏰 **Server:** {guild_name}\n"
            f"👑 **Manager:** {self.manager.mention}\n"
            f"📢 **Ping:** @everyone @here"
        )

        channel = interaction.client.get_channel(PARTNERSHIP_CHANNEL_ID)
        if not channel:
            await interaction.response.send_message("⚠️ Partnership channel not found or not accessible.", ephemeral=True)
            return

        try:
            await channel.send(final_message, allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True))
            await interaction.response.send_message("✅ Partnership successfully sent!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ I don’t have permission to send messages or mention", ephemeral=True)

class Partnership(commands.Cog):
    def __init__(self, bot_):
        self.bot = bot_

    partnership = app_commands.Group(name="partnership", description="Partnership management")

    @partnership.command(name="manager", description="Send a partnership with the specified manager")
    @app_commands.describe(manager="Manager user to mention")
    async def manager(self, interaction: discord.Interaction, manager: discord.User):
        modal = PartnershipModal(manager=manager)
        await interaction.response.send_modal(modal)

@bot.event
async def on_ready():
    await bot.add_cog(Partnership(bot))
    await bot.tree.sync()
    print(f"Bot connected as {bot.user}")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
