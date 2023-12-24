import flag
from countryinfo import CountryInfo

from DAXXROBOT import BOT_USERNAME
from DAXXROBOT import telethn as borg
from DAXXROBOT.events import register


@register(pattern="^/country (.*)")
async def msg(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lol = input_str
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await event.reply("Country Not Available Currently")
    name = a.get("name")
    bb = a.get("altSpellings")
    hu = "".join(f"{p},  " for p in bb)
    area = a.get("area")
    hell = a.get("borders")
    borders = "".join(f"{fk},  " for fk in hell)
    WhAt = a.get("callingCodes")
    call = "".join(f"{what}  " for what in WhAt)
    capital = a.get("capital")
    fker = a.get("currencies")
    currencies = "".join(f"{FKer},  " for FKer in fker)
    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
        po = iSo.get(hitler)
        iso += f"{po},  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)

    languages = a.get("languages")
    lMAO = "".join(f"{lmao},  " for lmao in languages)
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = "".join(f"{jerry},   " for jerry in tik)
    GOT = a.get("tld")
    lanester = "".join(f"{targaryen},   " for targaryen in GOT)
    wiki = a.get("wiki")

    caption = f"""<b><u>ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀᴇᴅ sᴜᴄᴇssғᴜʟʟʏ </b></u>

<b>ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ :</b> {name}
<b>ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ sᴘᴇʟʟɪɴɢs :</b> {hu}
<b>ᴄᴏᴜɴᴛʀʏ ᴀʀᴇᴀ :</b> {area} square kilometers
<b>ʙᴏʀᴅᴇʀs :</b> {borders}
<b>ᴄᴀʟʟɪɴɢ ᴄᴏᴅᴇs  :</b> {call}
<b>ᴄᴏᴜɴᴛʀʏ's ᴄᴀᴘɪᴛᴀʟ :</b> {capital}
<b>ᴄᴏᴜɴᴛʀʏ's ᴄᴜʀʀᴇɴᴄʏ :</b> {currencies}
<b>ᴄᴏᴜɴᴛʀʏ's ғʟᴀɢ :</b> {okie}
<b>ᴅᴇᴍᴏʏᴍ:</b> {HmM}
<b>ᴄᴏᴜɴᴛʀʏ ᴛʏᴘᴇ :</b> {EsCoBaR}
<b>ɪsᴏ ɴᴀᴍᴇs :</b> {iso}
<b>ʟᴀɴɢᴜᴀɢᴇs :</b> {lMAO}
<b>ɴᴀᴛɪᴠᴇ ɴᴀᴍᴇs :</b> {nonive}
<b>ᴘᴏᴘᴜʟᴀᴛɪᴏɴs :</b> {waste}
<b>ʀᴇɢɪᴏɴ :</b> {reg}
<b>sᴜʙ ʀᴇɢɪᴏɴ :</b> {sub}
<b>ᴛɪᴍᴇ ᴢᴏɴᴇs :</b> {tom}
<b>ᴛᴏᴛᴀʟ ʟᴇᴠᴇʟ ᴅᴏᴍᴀɪɴ :</b> {lanester}
<b>ᴡɪᴋɪᴘᴇᴅɪᴀ:</b> {wiki}

<u>ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀᴇᴅ ʙʏ @{BOT_USERNAME}</u>
"""

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        link_preview=None,
    )


__help__ = """
ɪ ᴡɪʟʟ ɢɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴄᴏᴜɴᴛʀʏ

 ❍ /country <ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ>*:* ɢᴀᴛʜᴇʀɪɴɢ ɪɴғᴏ ᴀʙᴏᴜᴛ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛʀʏ
"""

__mod_name__ = "Cᴏᴜɴᴛʀʏ"
