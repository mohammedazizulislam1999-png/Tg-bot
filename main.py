import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION"]

client = TelegramClient(
    StringSession(session),
    api_id,
    api_hash
)

@client.on(events.NewMessage(pattern=r'(?i)^apay$'))
async def pay(event):
    await event.reply("""
💳 **ARS TOPUP BD — PAYMENT GATEWAY**
═════════════════════════

🏷️ **bKash (Merchant)**
▶ `01331202837`

🏷️ **bKash (Personal)**
▶ `01957858795`

🏷️ **Nagad (Personal)**
▶ `01957858795`

🏷️ **Rocket (Personal)**
▶ `01957858795`

🏷️ **Upay (Personal)**
▶ `01957858795`

═════════════════════════
⚠️ *টাকা পাঠানোর পর অবশ্যই Transaction ID অথবা Screenshot প্রদান করুন।*
""")

# =========================
# PRIVATE AUTO CALCULATOR
# =========================

@client.on(events.NewMessage)
async def auto_calc(event):

    # শুধু আপনার নিজের message
    if not event.out:
        return

    try:
        text = event.raw_text.strip()

        # Command ignore
        if text.startswith("/"):
            return

        # শুধু operator থাকলে calculator চলবে
        if not any(op in text for op in ["+", "-", "*", "/"]):
            return

        # শুধু valid character allow
        allowed = "0123456789+-*/(). "

        if not all(ch in allowed for ch in text):
            return

        result = eval(text)

        await event.reply(f"""
✓ Cᴀʟᴄᴜʟᴀᴛɪᴏɴ Cᴏᴍᴘʟᴇᴛᴇᴅ

➦ Iɴᴘᴜᴛ :
➥ `{text}`

➦ Rᴇsᴜʟᴛ :
➥ `{result}`

━━━━━━━━━━━━━━━━━━
""")

    except ZeroDivisionError:
        await event.reply("""
❌ Cᴀʟᴄᴜʟᴀᴛɪᴏɴ Fᴀɪʟᴇᴅ

➥ Cannot divide by zero.

━━━━━━━━━━━━━━━━━━
""")

    except Exception:
        pass

print("✅ Userbot Running...")

with client:
    client.run_until_disconnected()
