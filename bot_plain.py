from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 29417793
api_hash = "67f16bc01fc5cacded75a765f0cf9c14"
target_chat_id = -1002279826469

keywords = ["مين يحل","ابي مختص","ابغى","مين يحل","مين يشرح","ابي","أبغا","أبغى","ابغئ"]

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.text)
def handle_message(client: Client, message: Message):
    try:
        text = message.text.lower()
        if any(keyword in text for keyword in keywords):
            sender = message.from_user
            sender_name = f"{sender.first_name or ' '} {sender.last_name or ' '}".strip() if sender else "غير معروف"
            sender_username = f"@{sender.username}" if sender and sender.username else "غير متوفر"

            chat = message.chat
            chat_title = chat.title or "محادثة خاصة"
            chat_username = f"@{chat.username}" if chat.username else "خاص/غير متاح"

            if chat.username:
                message_link = f"https://t.me/{chat.username}/{message.id}"
            else:
                message_link = "غير متاح (ليست قناة عامة)"

            full_report = (
                "🚨 رسالة مشبوهة تم التقاطها:\n\n"
                f"📄 الرسالة:\n{message.text}\n\n"
                f"👤 المرسل: {sender_name} ({sender_username})\n"
                f"👥 من: {chat_title} ({chat_username})\n"
                f"🔗 رابط: {message_link}"
            )

            client.send_message(chat_id=target_chat_id, text=full_report)
            print("✅ تم إرسال تقرير الرسالة.")
    except Exception as e:
        print(f"❌ خطأ أثناء المعالجة: {e}")

app.run()