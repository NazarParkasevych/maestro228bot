import logging
import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} i am your personal helper.')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'I am ready to work.')

async def school(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'You study in VPU29')
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.lower()
    if 'hello' in message:
        if update.effective_user.last_name:
            reply_text = f'Hello {update.effective_user.first_name} {update.effective_user.last_name}!'
        else:
            reply_text = f'Hello {update.effective_user.first_name}!'

    elif 'goodbye' in message:
        if update.effective_user.last_name:
            reply_text = f'Goodbye {update.effective_user.first_name} {update.effective_user.last_name}!'
        else:
            reply_text = f'Goodbye {update.effective_user.first_name}!'

    else:
        reply_text = 'I dont understand you!'

    await update.message.reply_text(reply_text)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("school", school))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


app.run_polling()



