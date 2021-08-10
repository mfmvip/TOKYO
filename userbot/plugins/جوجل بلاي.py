"""Fetch App Details from Playstore.
.app <app_name> to fetch app details.
.appr <app_name>  to fetch app details with Xpl0iter request link.
  ©TOKYO™ - @MFMVIP """

import bs4
import requests

from userbot import bot
Name = bot.me.first_name

@icss.on(icss_cmd(pattern="تطبيق (.*)"))
@icss.on(sudo_cmd(pattern="تطبيق (.*)", allow_sudo=True))
async def apk(event):
    app_name = event.pattern_match.group(1)
    event = await eor(event, "**✘ ∫ ججاري البحث عـن التطبيق**")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details = "<b>𓆰 " + app_name + " 𓆪</b>"
        app_details += (
            "\n\n<b>✘ ∫ المطور :</b> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<b>✘ ∫ تقييم التطبيق :</b> " + app_rating.replace(
            "صـنفت ", "⭐ "
        ).replace(" out of ", "/").replace(" الـنجوم", "", 1).replace(
            " الـنجوم", "⭐ "
        ).replace(
            "خـمس", "5"
        )
        app_details += (
            "\n<b>✘ ∫ الـمميزات :</b> <a href='"
            + app_link
            + "'>لتحميلها من سوق بلي</a>"
        )
        app_details += f"\n\n    𓍹 {Name} 𓍻"
        await event.edit(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.edit("** لم يتم العثور على نتائج البحث يرجى وضع اسم تطبيق متوفر ❕**")
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))

CMD_HELP.update(
    {
        "جوجل بلاي": "**Plugin :** `جوجل بلاي`\
        \n**Syntax : **`.تطبيق [اسم التطبيق]`\
        \n**Usage: **searches the app in the playstore and provides the link to the app in playstore and fetchs app details \
        "
    }
)
