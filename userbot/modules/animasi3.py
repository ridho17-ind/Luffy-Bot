from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.luffy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku luffy`")
    sleep(3)
    await typew.edit("`17 Tahun`")
    sleep(3)
    await typew.edit("`Kelas 12`")
    sleep(1)
    await typew.edit("`Tinggal Di Bangka belitung, Salam Kenal:)`")


@register(outgoing=True, pattern='^.elsa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai perkenalkan namaku elsa`")
    sleep(3)
    await typew.edit("`17 Tahun`")
    sleep(3)
    await typew.edit("`Kelas 12`")
    sleep(1)
    await typew.edit("`Asal kota malang, salken yah:)`")


@register(outgoing=True, pattern='^ilyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")


@register(outgoing=True, pattern='^.pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Bapaknya Udin Di Makan Udang`")
    sleep(2)
    await typew.edit("`Cuma Sendiri nih Senggol Dong`")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Awali perkataan dengan dengan salam`")
    sleep(1)
    await typew.edit("`Assalamualaikum Asuuuu`")


CMD_HELP.update({
    "animasi3":
     "CMD`.pe`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`.luffy`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`.elsa`\
\npenjelasan: Cek lh asw.\
\n\nCMD:`.ilyu`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`p`\
\nPenjelasan: Cek lah asw.\
\n\nCMD:`.semangat`\
\nPenjelasan: Cek lah asw."
})
