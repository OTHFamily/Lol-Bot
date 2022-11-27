from pyrogram import idle
from uvloop import install

from Pmo.misc import git
from Pmo.config import LOGS_ID
from Pmo import app, logs, loop


async def main():
    try:
        await app.start()
        me = await app.get_me()
        try:
            await app.send_message(
                LOGS_ID, "[🔥 BOT SUDAH DIAKTIFKAN! 🔥]"
            )
        except BaseException:
            pass
        logs.info(
            f"Started as {me.first_name} | [ {me.id} ]"
        )
    except Exception as a:
        logs.warning(a)
    logs.info(f"[🔥 BOT BERHASIL DIAKTIFKAN! 🔥]")
    await idle()


if __name__ == "__main__":
    logs.info("Starting Bot")
    install()
    git()
    loop.run_until_complete(main())
