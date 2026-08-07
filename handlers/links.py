from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, ContextTypes, filters

from services.youtube import get_video_info


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = update.message.text
    context.user_data["url"] = url

    await update.message.reply_text("⏳ جاري تحليل الرابط...")

    try:
        info = get_video_info(url)

        title = info.get("title", "غير معروف")
        uploader = info.get("uploader", "غير معروف")
        duration = info.get("duration", 0)

        minutes = duration // 60
        seconds = duration % 60

        keyboard = [
            [
                InlineKeyboardButton(
                    "🎥 تحميل الفيديو",
                    callback_data="video",
                ),
                InlineKeyboardButton(
                    "🎵 MP3",
                    callback_data="audio",
                ),
            ]
        ]

        await update.message.reply_text(
            f"""✅ تم اكتشاف الفيديو

🎬 {title}

👤 {uploader}

⏱️ {minutes}:{seconds:02d}
""",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    except Exception as e:
        await update.message.reply_text(f"❌ {e}")


def register_links_handler(app):
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_link,
        )
    )
