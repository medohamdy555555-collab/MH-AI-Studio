from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في MH AI Studio\n\n"
        "📥 ابعت أي لينك فيديو (YouTube - TikTok - Instagram - Facebook)\n"
        "وسأحلله تلقائيًا."
    )


def register_start_handler(app):
    app.add_handler(CommandHandler("start", start))
