# Discord Spin Bot

Welcome to the Discord Spin Bot repository! This bot allows users to engage in a thrilling spinning experience where they receive random names from predefined lists. With features tailored for administrators, you can effortlessly manage and customize the spinning experience for your Discord server.

## Setup Instructions

Follow these steps to set up the Discord Spin Bot on your local machine:

1. Clone the Repository: Start by cloning the repository to your local machine using the following command:
   git clone https://github.com/yourusername/discord-spin-bot.git

2. Install Dependencies: Use pip to install the required dependencies by running:
   pip install -r requirements.txt

3. Create Discord Application and Bot: Visit the Discord Developer Portal to create a new Discord application and bot. Obtain your bot token from the Bot section of your application on the Developer Portal.

4. Configure Bot Token: Create a `config.json` file in the root directory of the project and add your Discord bot token in the following format:
   {
     "token": "YOUR_DISCORD_BOT_TOKEN"
   }

5. Define Spin Lists: Create a `names.json` file in the root directory of the project to define spin lists. Customize the names and quantities according to your preferences.

6. Run the Bot: Execute the bot using the following command:
   python bot.py

## Usage

Here's how you can utilize the Discord Spin Bot in your server:

- To spin the wheel for list 1: /spin [times]
- To spin the wheel for list 2: /spin [times] 2
- To add names to a list (admin only): /addlist [list_num] [name1 qty1, name2 qty2, ...]
- To reload spin configuration (admin only): /reload

Replace [times], [list_num], [name1 qty1, name2 qty2, ...] with the appropriate values.

## Note

This project is currently in its early stages, and thorough testing is pending. It was developed for personal use within a Discord community. Contributions and feedback are welcome!
