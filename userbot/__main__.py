
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import ALIVE_NAME, BOTLOG_CHATID, BOT_VER, LOGS, UPSTREAM_REPO_BRANCH, bot
from userbot.modules import ALL_MODULES

INVALID_PH = (
    "\nERROR: Nomor Telepon yang kamu masukkan SALAH."
    "\nTips: Gunakan Kode Negara beserta nomornya atau periksa nomor telepon Anda dan coba lagi."
)

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {ALIVE_NAME} Membutuhkan Bantuan, Silahkan Gabung ke Grup https://t.me/RoseSupportGroups")

LOGS.info(
    f"Luffy-Userbot ⚙️ V{BOT_VER} [🦅 BERHASIL DIAKTIFKAN! 🦅]")


async def man_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, f"🦅 **Luffy-Userbot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{BOT_VER}@{UPSTREAM_REPO_BRANCH}`\n➠ **Ketik** `.alive` **untuk Mengecheck Bot**\n━━")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@RoseXmusic_support"))
        await bot(JoinChannelRequest("@RoseSupportGroups"))
    except BaseException:
        pass
bot.loop.create_task(Luffy_userbot_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
