import os

class Config(object):
    # API এবং Token সেটিংস
    API_ID = int(os.environ.get("API_ID", 36701545))
    API_HASH = os.environ.get("API_HASH", "92e8025812ade7acc47f9dc8057b34ad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8599452472:AAFir1VzQ8jPFwuSCWYrjk81BOeCFHZh-48")
    
    # ডাটাবেস এবং ওনার আইডি
    OWNER_ID = int(os.environ.get("OWNER_ID", 5318110377))
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Alpha:001100@cluster0.mp2hbsi.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = os.environ.get("DB_NAME", "CodeXBot")

    # ফাইল স্টোরেজ চ্যানেল এবং আপনার নতুন ফোর্স সাবস্ক্রাইব চ্যানেল
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1003820981442)) 
    FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", -1003814864297))

    # আপনার দেওয়া কাস্টম ওয়েলকাম টেক্সট
    START_MSG = os.environ.get("START_MSG", """<b>🔐 Secure Your Files in Seconds!</b>

📁 Videos | 📸 Photos | 📄 Documents

🚀 Generate Safe Links Instantly with Our Drive File Bot
💾 Keep your important files protected, anytime & anywhere!""")
    
    # অতিরিক্ত কনফিগারেশন
    AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", 600))
    PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False")
    PORT = int(os.environ.get("PORT", "8080"))
