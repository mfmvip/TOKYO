alv = (
"""
**©TOKYO - @MFMVIP
  - Plugin Alive** 
  - **Commend:** `.السورس`
  - **Function:** لعرض معلومات السورس
"""
)

import time
from platform import python_version
from telethon import version
from resources.strings import *

from . import ALIVE_NAME, StartTime, get_readable_time, icsv, mention
from . import reply_id as rd

DEFAULTUSER = ALIVE_NAME or "TOKYO"
ICSS_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/967209504b62689f5f770.jpg"
ICSS_TEXT = Config.CUSTOM_ALIVE_TEXT or "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 𓆪"
ICSEM = Config.CUSTOM_ALIVE_EMOJI or "  ⌔∮ "


@icssbot.on(admin_cmd(outgoing=True, pattern="السورس$"))
@icssbot.on(sudo_cmd(pattern="السورس$", allow_sudo=True))
async def ica(icss):
    if icss.fwd_from:
        return
    ics_id = await rd(icss)
    icsupt = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if ICSS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷ \n"
        ics_c += f"**{ICSEM} قاعدة البيانات ↫** `{check_sgnirts}`\n"
        ics_c += f"**{ICSEM} اصدار التليثون  ↫** `{version.__version__}\n`"
        ics_c += f"**{ICSEM} اصدار زد ثـون ↫** `{icsv}`\n"
        ics_c += f"**{ICSEM} اصدار البايثون ↫** `{python_version()}\n`"
        #        ics_c += f"**{ICSEM} مدة التشغيل ↫** `{icsupt}\n`"
        ics_c += f"**{ICSEM} المستخدم ↫** {mention}\n"
        ics_c += f"**{ICSEM} **  **𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n"
        ics_c += f"**{ICSEM} **  **𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP)𓆪\n"
        ics_c += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        await icss.client.send_file(
            icss.chat_id, ICSS_IMG, caption=ics_c, reply_to=ics_id
        )
        await icss.delete()
    else:
        await eor(
            icss,
            f"**{ICSS_TEXT}**\n\n"
            f"**{ICSEM} قاعدة البيانات ↫**  `{check_sgnirts}`\n"
            f"**{ICSEM} اصدار التليثون  ↫** `{version.__version__}\n`"
            f"**{ICSEM} اصدار زد ثـون ↫** `{icsv}`\n"
            f"**{ICSEM} اصدار البايثون  ↫** `{python_version()}\n`"
            f"**{ICSEM} مدة التشغيل ↫** `{icsupt}\n`"
            f"**{ICSEM} المستخدم ↫** {mention}\n",
        )


def check_data_base_heal_th():
    is_database_working = False
    output = "لم يتم تعيين قاعدة بيانات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "تعمل بنجاح"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update({"alive": f"{alv}"})
