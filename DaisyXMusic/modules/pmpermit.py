# Daisyxmusic (Telegram bot proje )


from pyrogram import filters
from pyrogram.types import Message

from DaisyXMusic.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Salam bu @RythmMusiqiBot Asistan hesabıdır!\n\n👉 **BOT GRUPA QATILMAZSA BOTU ƏL İLƏ GRUPA QATIN**\n\n**QAYDALAR**❗️\n- Hesaba gizli məlumatıarınızı yazmayın\n- Hesabı kontakta əlavə etməyin\n- Hesabı gizli gruplarınıza əlavə etməyin\n\nUnutmayın ki admin asistan hesabına yazılan mesaları görur\nQaydalara əməl etmədiyiniz halda hər hansı bir prablem olarsa **GROUP MUZİK BOT** admini heçbir məsuliyət daşımır❗️ \n\n**Bota bağlı köməyə ehtiyacınız olarsa dəstək grupuna və ya bot sahibindən kömək alın\n\nDəstək grupu: @AzRobotGroup\nBot Sahibi: @SirinCayBoss",
    )
    return
