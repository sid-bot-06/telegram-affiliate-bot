import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load your bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I'm your affiliate bot. Send /help to see what I can do.")


# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start - Start the bot\n/help - List commands")


async def main():
    # Create bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Start polling (keeps bot running)
    print("Bot is running...")
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())




