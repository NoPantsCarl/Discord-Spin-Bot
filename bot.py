import discord
from discord.ext import commands
import asyncio
import random
import json

# Define the bot's prefix
bot = commands.Bot(command_prefix='/')

# Function to load spin configuration from JSON file
def load_spin_config():
    try:
        with open('names.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save spin configuration to JSON file
def save_spin_config(spin_config):
    with open('names.json', 'w') as file:
        json.dump(spin_config, file)

# Function to get a random name from the spin list
def get_random_name(spin_list):
    name, qty = random.choice(list(spin_list.items()))
    if qty == 1:
        spin_list.pop(name)
    else:
        spin_list[name] -= 1
    return name

# Load spin configuration when bot starts
spin_config = load_spin_config()

# Command to spin the wheel
@bot.command()
async def spin(ctx, times: int, list_num: int = 1):
    spin_list = spin_config.get("spin_lists", {}).get(str(list_num), {}).get("Names", {})
    if spin_list:
        names = [get_random_name(spin_list) for _ in range(times)]
        await ctx.send(f"Spinning the wheel for list {list_num}... 🌀\n{' '.join(names)}")
    else:
        await ctx.send(f"Spin list {list_num} not configured.")

# Command to add names to the spin list
@bot.command()
async def addlist(ctx, list_num: int, *, names_and_qty: str):
    if ctx.author.guild_permissions.administrator:
        spin_config.setdefault("spin_lists", {}).setdefault(str(list_num), {}).setdefault("Names", {})
        names_qty = names_and_qty.split(",")
        for name_qty in names_qty:
            name, qty = name_qty.strip().split(" ")
            spin_config["spin_lists"][str(list_num)]["Names"][name] = int(qty)
        save_spin_config(spin_config)
        await ctx.send(f"Names added to spin list {list_num}.")
    else:
        await ctx.send("You don't have permission to add names to the spin list.")

# Command to reload spin configuration (admin only)
@bot.command()
async def reload(ctx):
    if ctx.author.guild_permissions.administrator:
        spin_config.clear()
        spin_config.update(load_spin_config())
        await ctx.send("Spin configuration reloaded.")
    else:
        await ctx.send("You don't have permission to reload the spin configuration.")

# Start the bot
bot.run("YOUR_DISCORD_TOKEN")
