
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ FC Mobile Market Assistant запущен!\n\n"
        "Команда расчёта прибыли:\n"
        "/profit цена_покупки цена_продажи\n\n"
        "Пример: /profit 100000000 120000000"
    )

async def profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        buy = int(context.args[0])
        sell = int(context.args[1])

        if buy <= 0 or sell < 0:
            raise ValueError

        revenue = sell * 0.90
        result = revenue - buy

        await update.message.reply_text(
            f"📊 Расчёт сделки\n"
            f"Покупка: {buy:,}\n"
            f"Продажа: {sell:,}\n"
            f"После комиссии 10%: {revenue:,.0f}\n"
            f"Прибыль: {result:,.0f} монет"
        )
    except (IndexError, ValueError):
        await update.message.reply_text(
            "Используй: /profit цена_покупки цена_продажи"
        )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("Не найден TELEGRAM_BOT_TOKEN")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profit", profit))
    app.run_polling()

if __name__ == "__main__":
    main()
