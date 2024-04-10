from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final ='6955294375:AAFQfAODKDoxSwTS_GxvdZdfGvyrRtBUiDo'
BOT_USERNAME: Final ='@leanlan_bot'

#Commands
async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to Language Learning bot!')

async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am LL! How can I help you?')

async def custom_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

#Responses
    def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'