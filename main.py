import asyncio

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import TOKEN

from database import (
    add_user,
    get_user,
    add_reward,
    next_stage,
    remove_heart,
    get_profile,
    leaderboard,
    get_hearts,
    daily_reward
)

from game import get_stage, stage_text
from keyboards import main_menu



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(
        user.id,
        user.first_name
    )

    await update.message.reply_text(
        f"سلام {user.first_name} 👋\n"
        "به CodeMind خوش آمدی 🧠",
        reply_markup=main_menu()
    )



async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id


    if text == "🎮 شروع بازی":

        user = get_user(user_id)

        stage = get_stage(user[5])


        if stage is None:

            await update.message.reply_text(
                "🎉 همه مراحل را تمام کردی!"
            )

            return


        await update.message.reply_text(
            stage_text(user[5])
        )



    elif text == "👤 پروفایل":

        await update.message.reply_text(
            get_profile(user_id)
        )



    elif text == "🏆 رتبه بندی":

        users = leaderboard()

        msg = "🏆 رتبه بندی\n\n"

        for i, user in enumerate(users, 1):

            msg += (
                f"{i}- {user[0]}\n"
                f"🏆 Level: {user[1]}\n"
                f"⭐ XP: {user[2]}\n\n"
            )


        await update.message.reply_text(msg)



    elif text == "🎁 جایزه روزانه":

        result = daily_reward(user_id)


        if result:

            await update.message.reply_text(
                "🎁 جایزه روزانه دریافت شد!\n\n"
                "🪙 +50 سکه\n"
                "⭐ +20 XP\n"
                "❤️ +1 قلب"
            )

        else:

            await update.message.reply_text(
                "⏳ جایزه امروز را گرفتی.\n"
                "فردا دوباره بیا!"
            )



    elif text == "🎯 ماموریت ها":

        await update.message.reply_text(
            "🎯 ماموریت‌ها بزودی فعال می‌شوند."
        )



    elif text == "⚙️ تنظیمات":

        await update.message.reply_text(
            "⚙️ تنظیمات بزودی فعال می‌شود."
        )





async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = get_user(
        update.effective_user.id
    )


    if user is None:
        return


    hearts = get_hearts(user[0])


    if hearts <= 0:

        await update.message.reply_text(
            "💔 قلب نداری!"
        )

        return



    stage = get_stage(user[5])


    if stage is None:

        await update.message.reply_text(
            "🎉 بازی تمام شد!"
        )

        return



    if update.message.text.strip() == stage["answer"]:


        add_reward(
            user[0],
            stage["reward"],
            stage["xp"]
        )


        next_stage(
            user[0]
        )


        await update.message.reply_text(
            "✅ جواب درست بود!\n\n"
            f"🪙 +{stage['reward']} سکه\n"
            f"⭐ +{stage['xp']} XP"
        )


    else:


        remove_heart(
            user[0]
        )


        hearts = get_hearts(user[0])


        await update.message.reply_text(
            "❌ جواب اشتباه بود\n"
            f"❤️ قلب باقی مانده: {hearts}"
        )





app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    MessageHandler(
        filters.Regex(
            "^(🎮 شروع بازی|👤 پروفایل|🏆 رتبه بندی|🎁 جایزه روزانه|🎯 ماموریت ها|⚙️ تنظیمات)$"
        ),
        menu
    )
)


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        answer
    )
)


print("Bot Started...")


app.run_polling()




async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = get_user(
        update.effective_user.id
    )


    if user is None:
        return


    hearts = get_hearts(user[0])


    if hearts <= 0:

        await update.message.reply_text(
            "💔 قلب نداری!"
        )

        return



    stage = get_stage(user[5])


    if stage is None:

        await update.message.reply_text(
            "🎉 بازی تمام شد!"
        )

        return



    if update.message.text.strip() == stage["answer"]:


        add_reward(
            user[0],
            stage["reward"],
            stage["xp"]
        )


        next_stage(
            user[0]
        )


        await update.message.reply_text(
            "✅ جواب درست بود!\n\n"
            f"🪙 +{stage['reward']} سکه\n"
            f"⭐ +{stage['xp']} XP"
        )



    else:

        remove_heart(
            user[0]
        )

        hearts = get_hearts(
            user[0]
        )


        await update.message.reply_text(
            "❌ جواب اشتباه بود\n"
            "❤️ یک قلب کم شد\n\n"
            f"❤️ قلب باقی مانده: {hearts}"
        )





app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    MessageHandler(
        filters.Regex(
            "^(🎮 شروع بازی|👤 پروفایل|🏆 رتبه بندی|🎁 جایزه روزانه|🎯 ماموریت ها|⚙️ تنظیمات)$"
        ),
        menu
    )
)


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        answer
    )
)


print("Bot Started...")


app.run_polling()
