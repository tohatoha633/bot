import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types,html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
TOKEN = "8041784280:AAEg2XiiwMw6DT43r2KVvDNfW1UC_xpBUEg"


dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"""Salom! 👋\n
Men rasm yaratib beruvchi botman.\n\n
🖼️ <i> Iltimos, yaratmoqchi bo‘lgan rasmingizni ingliz tilida tasvirlab bering. Shunda men siz uchun tayyor rasm yaratib bera olaman.</i>\n\n
⚠️ Eslatma: rasm tavsifi faqat ingliz tilida bo‘lsin. Masalan: <b>"Black Car" </b> """)


@dp.message()
async def image_creator(message: types.Message):
    idea = message.text.strip()

    if not idea:
        await message.answer("❗ Iltimos, g‘oya matnini yubor.")
        return

    await message.answer("🧠 Rasm yaratilmoqda, biroz kuting...")

    image_url = f"https://image.pollinations.ai/prompt/{idea.replace(' ', '%20')}"

    try:
        await message.answer_photo(photo=image_url, caption=f"🖼 G‘oyang bo‘yicha rasm tayyor")
    except Exception as e:

        await message.answer(f"❌ Xatolik: {e}\nRasmni yaratib bo‘lmadi, boshqa g‘oya yuborib ko‘ring.")


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

