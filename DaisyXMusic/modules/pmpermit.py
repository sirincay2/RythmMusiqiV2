# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import filters
from pyrogram.types import Message

from DaisyXMusic.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Salam bu @GroupMuzikBot Asistan hesabıdır!\n\n👉 **BOT GRUPA QATILMAZSA BOTU ƏL İLƏ GRUPA QATİN**\n\n**QAYDALAR**❗️\n- Hesaba gizli məlumatıarınızı yazmayın\n- Hesabı kontakta əlavə etməyin\n- Hesabı gizli gruplarınıza əlavə etməyin\n\nUnutmayın ki admin asistan hesabına yazılan mesaları görur\nQaydalara əməl etmədiyiniz halda hər hansı bir prablem olarsa **GROUP MUZİK BOT** admini heçbir məsuliyət daşımır❗️ \n\n**Bota bağlı köməyə ehtiyacınız olarsa dəstək grupuna və ya bot sahibindən kömək alın\n\nDəstək grupu: @GroupMuzikSup\nBot Sahibi: @Samil",
    )
    return
