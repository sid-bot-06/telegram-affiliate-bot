import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get the bot token from environment variables (set on Render)
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m alive and running on Python 3.13 🚀")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I can respond to /start, /help, and /test!")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Test successful! ✅")

async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set. Please set it as an environment variable on Render!")

    # Build the application (no Updater used — avoids the bug entirely)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("test", test))

    # Run the bot using polling (no legacy updater involved)
    await app.initialize()
    await app.start()
    print("Bot is running...")
    await app.updater.start_polling()  # modern polling method
    await app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())









