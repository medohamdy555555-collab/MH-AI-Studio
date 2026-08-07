from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes
from services.youtube import download_video
import os


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    url = context.user_data.get("url")

    if not url:
        await query.message.reply_text("❌ لم يتم العثور على الرابط.")
        return

    if query.data == "video":

        msg = await query.message.reply_text("⏳ جاري تحميل الفيديو...")

        try:

            file_path, info = download_video(url)

            with open(file_path, "rb") as video:
                await query.message.reply_video(
                    video=video,
                    caption=f"🎬 {info['title']}"
                )

            os.remove(file_path)

            await msg.delete()

        except Exception as e:
            await msg.edit_text(f"❌ {e}")

    elif query.data == "audio":

        await query.message.reply_text(
            "🚧 سيتم إضافة MP3 في الخطوة القادمة."
        )


def register_buttons_handler(app):
    app.add_handler(
        CallbackQueryHandler(button_click)
    )
