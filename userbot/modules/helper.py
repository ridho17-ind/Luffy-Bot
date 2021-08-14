""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.thelp$")
async def usit(e):
    await e.edit(
        f"**Hai Tuan {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Mastah](t.me/Rorflame)"
        "\n[Repo](https://github.com/Abror0110/luffy_Bot)"
        "\n[Instagram Mastah](Instagram.com/achmd_abror)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Abror0110/luffy-Bot/luffy-Bot/varshelper.txt)")


CMD_HELP.update({
    "linuxhelper":
    "CMD`.lhelp`\
\nPenjelasan: Bantuan Untuk 💀Luffy_Bot💀.\
\nCMD`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
