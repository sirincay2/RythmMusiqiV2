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

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "👋 **Salam [{}](tg://user?id={})!**\nMən Telegram gruplarında səsli söhbətdə musiqi dinləmək üçün yaradılan botam\nMəni grupa əlavə edərək admin hüquqları verin\nƏmrlər və daha ətraflı məlumat üçün /help."
      HELP_MSG = [
        ".",
f"""
Telegram {PROJECT_NAME} Haqqında Kömək və əmrlər! 

**QURULUM**

1. Botu Grupa Əlavə edin
2. Botu Admin edin
3. Səsli söhbəti başladın
4. Adminlərdən biri mahnı adı yazmadan sadəcə /play göndərin 
- Bu zaman @{ASSISTANT_NAME} grupa qatılmaıdı qatılmazsa əl ilə qatın
5. /play [Mahnı adı] Və asistan səsli söhbətdə mahnı oxumaga davam edəcəkdir!


**ƏMRLƏR**
- /play: [Mahnı adı] 
- /play [Bir mahnıya yanıt]: Yanıt verdiyiniz mahnını oxuyur

**ADMİN**

- /player: Musiqi idarə panelini açır
- /skip: Mahnılar arası keçid edir
- /pause: Mahnıya ara verir
- /resume: Ara verilən mahnıya davam edir
- /end: Mahnını dayandırır
- /current: Hazırda oxuyan mahnını göstərir
- /playlist: Hazırda tələb olunan mahnı siyası

**Kanal Muzik grulumu üçün irəli**
""",    
f"""
**QURULUM**
Botu və asistan kanala admin olaraq əlavə edin!
Ardından kanalın bağlı olduğu qrupda əmirlərdən istifadə edin

⚠️**KANALDA SƏSLİ SÖHBƏTİ AÇMAĞI UNUTMAYIN**⚠️

**Kanal Muzik Əmrlər**

- /cplay: [Mahnı adı] 
- /cplayer: Musiqi idarə panelini açır
- /cskip: Mahnılar arası keçid edir
- /cpause: Mahnıya ara verir
- /cresume: Ara verilən mahnıya davam edir
- /cend: Mahnını dayandırır
- /ccurrent: Hazırda oxuyan mahnını göstərir
- /cplaylist: Hazırda tələb olunan mahnı siyası
- /userbotjoinchannel - Asistanı grupa əlavə et
""",
f"""
**Daha çox**

- /yenile: Grupda admin siyahısını yeniləyir
- /userjoin: @{ASSISTANT_NAME} grupa dəvət et

/play, /current  və /playlist Xaric digər əmrlər adminlər üçündür
""",
"""
👋 **Salam**\nMən Telegram gruplarında səsli söhbətdə musiqi dinləmək üçün yaradılan botam\nMəni grupa əlavə edərək admin hüquqları verin\nƏmrlər və daha ətraflı məlumat üçün /help.
"""
      ]
