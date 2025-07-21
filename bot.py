import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Make sure this is set in Render environment variables

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! The bot is alive now! 🚀")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a simple affiliate bot. Use /start to begin.")

# Test command
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("The bot is working perfectly!")

async def main():
    # Create the bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("test", test))

    # Run polling (keeps the bot alive)
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())










