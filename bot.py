import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading

# Load your bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I'm your affiliate bot. Send /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start - Start the bot\n/help - List commands")

# Keep-alive Flask server (prevents Render from shutting down the bot)
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app_web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Start Telegram bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    # Run Flask server in a separate thread
    threading.Thread(target=run_flask).start()

    # Run the Telegram bot
    asyncio.run(main())







