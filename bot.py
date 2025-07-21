import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")

# --- Simple health check server for Render ---
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def start_server():
    server = HTTPServer(('0.0.0.0', 10000), HealthHandler)
    server.serve_forever()

# --- Bot Commands ---
async def start(update, context):
    await update.message.reply_text("Hey! Your bot is alive and running!")

async def help_command(update, context):
    await update.message.reply_text("Help: This bot is working fine on Render.")

async def main():
    # Start the health check server in a separate thread
    threading.Thread(target=start_server, daemon=True).start()

    # Start the Telegram bot
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot started...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())


