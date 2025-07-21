import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Hello! Your affiliate bot is now running!")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # Start polling in async mode
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())



