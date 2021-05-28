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


from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant

from DaisyXMusic.helpers.decorators import authorized_users_only, errors
from DaisyXMusic.services.callsmusic.callsmusic import client as USER


@Client.on_message(filters.command(["userjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Məni öz grupuna admin olaraq əlavə edin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "GroupMuzikAz"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "İstədiyiniz kimi buraya qoşuldum")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistan onsuzda grupdadı</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 Flood Xətası 🔴 \nİstifadəçi {user.first_name} Grupunuza qatıla bilmədi bunu səbəbi Asistan bir çox qurupda olması və ya adminlərdən biri onu grupda banladı"
                        "\n\nVə ya @GroupMuzikSup support grupundan dəstək istəyin</b>",
        )
        return
    await message.reply_text(
        "<b>Asistan grupunuza qatıldı</b>",
    )


@USER.on_message(filters.group & filters.command(["userleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b> İstifadəçi qrupunuzu tərk edə bilmədi! Daşqın ola bilər."
             "\n\nVə ya əl ilə məni Qrupunuza atın </b>",
        )
        return

@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor channel first</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your channel</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel."
            "\n\nOr manually add @DaisyXhelper to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
    
