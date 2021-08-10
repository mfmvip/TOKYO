# LOVEGif for TOKYO by: @MFMVIP

from .. import reply_id as rd
from . import *


@icssbot.on(icss_cmd(outgoing=True, pattern="ح1$"))
@icssbot.on(sudo_cmd(pattern="ح1$", allow_sudo=True))
async def vegif(icss):
    if icss.fwd_from:
        return
    Ti = await rd(icss)
    if ve_gif:
        icss_caption = f"**{LOVE}**\n"
        icss_caption += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        icss_caption += f"**↫ المتـحركه الاولى 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ve_gif, caption=icss_caption, reply_to=Ti
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ح2$"))
@icssbot.on(sudo_cmd(pattern="ح2$", allow_sudo=True))
async def vegif(icss):
    if icss.fwd_from:
        return
    th = await rd(icss)
    if ve_gif2:
        icss_caption = f"**{LOVE}**\n"
        icss_caption += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        icss_caption += f"**↫ المتـحركه الثانيه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ve_gif2, caption=icss_caption, reply_to=th
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ح3$"))
@icssbot.on(sudo_cmd(pattern="ح3$", allow_sudo=True))
async def vegif(icss):
    if icss.fwd_from:
        return
    kh = await rd(icss)
    if ve_gif3:
        icss_caption = f"**{LOVE}**\n"
        icss_caption += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        icss_caption += f"**↫ المتـحركه الثالثه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ve_gif3, caption=icss_caption, reply_to=kh
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ح4$"))
@icssbot.on(sudo_cmd(pattern="ح4$", allow_sudo=True))
async def vegif(icss):
    if icss.fwd_from:
        return
    wh = await rd(icss)
    if ve_gif4:
        vec = f"**{LOVE}**\n"
        vec += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        vec += f"**↫ المتـحركه الرابعه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ve_gif4, caption=vec, reply_to=wh
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ح5$"))
@icssbot.on(sudo_cmd(pattern="ح5$", allow_sudo=True))
async def vegif(icss):
    if icss.fwd_from:
        return
    ih = await rd(icss)
    if ve_gif5:
        vec = f"**{LOVE}**\n"
        vec += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        vec += f"**↫ المتـحركه الخامسه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ve_gif5, caption=vec, reply_to=ih
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ح6$"))
@icssbot.on(sudo_cmd(pattern="ح6$", allow_sudo=True))
async def vegif(icss):
    if icss.fwd_from:
        return
    uh = await rd(icss)
    if ve_gif6:
        vec = f"**{LOVE}**\n"
        vec += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        vec += f"**↫ المتـحركه السادسه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ve_gif6, caption=vec, reply_to=uh
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ح7$"))
@icssbot.on(sudo_cmd(pattern="ح7$", allow_sudo=True))
async def vegif(icss):
    if icss.fwd_from:
        return
    oh = await rd(icss)
    if ve_gif7:
        vec = f"**{LOVE}**\n"
        vec += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        vec += f"**↫ المتـحركه السابعه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ve_gif7, caption=vec, reply_to=oh
        )

