import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def approve_request(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    request = update.chat_join_request

    try:
        await context.bot.approve_chat_join_request(
            chat_id=request.chat.id,
            user_id=request.from_user.id
        )
        logging.info("Join request approved successfully")

    except Exception:
        logging.exception("Failed to approve join request")

def main():
    token = os.environ.get("BOT_TOKEN", "").strip()

    if not token:
        raise RuntimeError("BOT_TOKEN is missing")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(
        ChatJoinRequestHandler(approve_request)
    )

    print("Telegram Auto Approve Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
