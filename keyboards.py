# ==========================
# keyboards.py
# Version 2.0
# ==========================

from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# ==========================
# Main Menu
# ==========================

def main_menu():

    keyboard = [

        ["🎮 شروع بازی"],

        ["👤 پروفایل", "🏆 رتبه‌بندی"],

        ["🛒 فروشگاه", "🎁 جایزه روزانه"],

        ["🎯 ماموریت‌ها", "🏅 دستاوردها"],

        ["🎡 گردونه شانس", "👥 دعوت دوستان"],

        ["⚙️ تنظیمات"]

    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True
    )


# ==========================
# Game Keyboard
# ==========================

def game_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "💡 راهنما",
                callback_data="hint_menu"
            )
        ],

        [
            InlineKeyboardButton(
                "🔄 جابجایی",
                callback_data="shuffle"
            ),

            InlineKeyboardButton(
                "⏭ رد مرحله",
                callback_data="skip"
            )
        ],

        [
            InlineKeyboardButton(
                "🛒 فروشگاه",
                callback_data="shop"
            )
        ],

        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================
# Hint Menu
# ==========================

def hint_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "🔤 حرف اول (30 🪙)",
                callback_data="hint_first"
            )
        ],

        [
            InlineKeyboardButton(
                "🔠 حرف آخر (40 🪙)",
                callback_data="hint_last"
            )
        ],

        [
            InlineKeyboardButton(
                "❌ حذف دو حرف (50 🪙)",
                callback_data="hint_remove"
            )
        ],

        [
            InlineKeyboardButton(
                "🔄 بهم‌ریختن جدید (20 🪙)",
                callback_data="shuffle"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="back_game"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================
# Shop
# ==========================

def shop_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "❤️ خرید قلب",
                callback_data="buy_heart"
            )
        ],

        [
            InlineKeyboardButton(
                "💎 خرید جم",
                callback_data="buy_gem"
            )
        ],

        [
            InlineKeyboardButton(
                "💡 خرید راهنما",
                callback_data="buy_hint"
            )
        ],

        [
            InlineKeyboardButton(
                "⭐ VIP",
                callback_data="buy_vip"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================
# Missions
# ==========================

def mission_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "🎯 دریافت جایزه",
                callback_data="claim_mission"
            )
        ],

        [
            InlineKeyboardButton(
                "🔄 بروزرسانی",
                callback_data="refresh_mission"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================
# Leaderboard
# ==========================

def leaderboard_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "🌍 جهانی",
                callback_data="leader_global"
            ),

            InlineKeyboardButton(
                "👥 دوستان",
                callback_data="leader_friends"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================
# Settings
# ==========================

def settings_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "🌙 حالت شب",
                callback_data="dark_mode"
            )
        ],

        [
            InlineKeyboardButton(
                "🔔 اعلان‌ها",
                callback_data="notifications"
            )
        ],

        [
            InlineKeyboardButton(
                "🌍 زبان",
                callback_data="language"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="home"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)