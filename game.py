# ==========================
# game.py
# Version 2.0
# ==========================

import json
import random
from pathlib import Path


BASE_DIR = Path(__file__).parent
WORDS_FILE = BASE_DIR / "words.json"


class Game:

    def __init__(self):
        self.reload()

    # -------------------------

    def reload(self):
        with open(WORDS_FILE, "r", encoding="utf-8") as f:
            self.stages = json.load(f)

    # -------------------------

    def total_stages(self):
        return len(self.stages)

    # -------------------------

    def get_stage(self, stage_id):

        for stage in self.stages:

            if stage["id"] == stage_id:
                return stage

        return None

    # -------------------------

    def exists(self, stage_id):

        return self.get_stage(stage_id) is not None

    # -------------------------

    def get_answer(self, stage_id):

        stage = self.get_stage(stage_id)

        if stage:
            return stage["answer"]

        return None

    # -------------------------

    def get_reward(self, stage_id):

        stage = self.get_stage(stage_id)

        if stage:
            return stage["reward"]

        return 0

    # -------------------------

    def get_xp(self, stage_id):

        stage = self.get_stage(stage_id)

        if stage:
            return stage["xp"]

        return 0

    # -------------------------

    def normalize(self, text):

        if text is None:
            return ""

        return (
            text.strip()
            .replace("ي", "ی")
            .replace("ك", "ک")
            .replace("‌", "")
            .replace(" ", "")
            .lower()
        )

    # -------------------------

    def check_answer(self, stage_id, answer):

        correct = self.get_answer(stage_id)

        if correct is None:
            return False

        return self.normalize(answer) == self.normalize(correct)

    # -------------------------

    def stage_text(self, stage_id):

        stage = self.get_stage(stage_id)

        if stage is None:

            return (
                "🎉 تبریک!\n\n"
                "تمام مراحل را تمام کردی.\n"
                "منتظر مراحل جدید باش ❤️"
            )

        return f"""
━━━━━━━━━━━━━━━━━━

🎮 مرحله {stage['id']} از {self.total_stages()}

🔤 حروف

{stage['letters']}

━━━━━━━━━━━━━━━━━━

💡 اگر گیر کردی از راهنما استفاده کن.
"""

    # -------------------------

    def first_letter(self, stage_id):

        answer = self.get_answer(stage_id)

        if answer:
            return answer[0]

        return ""

    # -------------------------

    def last_letter(self, stage_id):

        answer = self.get_answer(stage_id)

        if answer:
            return answer[-1]

        return ""

    # -------------------------

    def shuffled_letters(self, stage_id):

        stage = self.get_stage(stage_id)

        if stage is None:
            return ""

        letters = list(stage["letters"])

        random.shuffle(letters)

        return "".join(letters)

    # -------------------------

    def hidden_answer(self, stage_id):

        answer = self.get_answer(stage_id)

        if answer is None:
            return ""

        result = []

        for i, ch in enumerate(answer):

            if i == 0:
                result.append(ch)

            else:
                result.append("◽")

        return " ".join(result)


game = Game()

