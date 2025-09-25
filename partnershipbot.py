# Copyright (c) 2025 - .rotafn (VortexTeam) - All rights reserved.
# Questo codice è protetto dalla Licenza Proprietaria VortexTeam (.rotafn).
# L'uso, la modifica o la distribuzione sono vietati senza autorizzazione scritta.
# La versione completa della licenza è disponibile su richiesta.
# -------------------
import discord
from discord.ext import commands
from discord import app_commands

# === CONFIGURAZIONE  ===
DISCORD_TOKEN = ""  # Token bot
PARTNERSHIP_CHANNEL_ID = 1409569987424948306  # ID canale partnership
EMOJI = "⭐"  # Emoji mezzo
# ===============================

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class PartnershipModal(discord.ui.Modal, title="Invia partnership"):
    def __init__(self, manager: discord.User):
        super().__init__()
        self.manager = manager

        self.msg_input = discord.ui.TextInput(
            label="Messaggio partnership",
            placeholder="Scrivi qui il contenuto della partnership…",
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
            await interaction.response.send_message(
                "⚠️ Canale partnership non trovato o non accessibile.",
                ephemeral=True
            )
            return

        try:
            await channel.send(
                final_message,
                allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True)
            )
            await interaction.response.send_message("✅ Partnership inviata!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ Non ho i permessi per inviare o pingare @everyone.",
                ephemeral=True
            )

class Partnership(commands.Cog):
    def __init__(self, bot_):
        self.bot = bot_

    partnership = app_commands.Group(name="partnership", description="Gestione partnership")

    @partnership.command(name="manager", description="Invia una partnership con manager indicato")
    @app_commands.describe(manager="Utente manager da menzionare")
    async def manager(self, interaction: discord.Interaction, manager: discord.User):
        modal = PartnershipModal(manager=manager)
        await interaction.response.send_modal(modal)

@bot.event
async def on_ready():
    await bot.add_cog(Partnership(bot))
    await bot.tree.sync()
    print(f"Bot connesso come {bot.user}")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)