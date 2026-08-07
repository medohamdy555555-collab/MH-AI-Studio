from telegram.ext import Application

from config import TOKEN
from handlers.start import register_start_handler
from handlers.links import register_links_handler
from handlers.buttons import register_buttons_handler


def main():
    app = Application.builder().token(TOKEN).build()

    register_start_handler(app)
    register_links_handler(app)
    register_buttons_handler(app)

    print("✅ MH AI Studio Started")

    app.run_polling()


if __name__ == "__main__":
    main()
