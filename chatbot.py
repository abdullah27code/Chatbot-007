#!/usr/bin/env python3
"""Ultra Engaging CLI Chatbot.

Run:
    python3 chatbot.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class StyleProfile:
    persona: str
    opening: str
    insight: str
    hook: str


class EngagingChatbot:
    """Rule-based, mode-switching chatbot focused on engaging conversation."""

    def __init__(self) -> None:
        self.turn = 0

    def _detect_mode(self, text: str) -> str:
        lowered = text.lower()

        technical_keywords = {
            "code", "python", "api", "bug", "error", "database", "sql", "algorithm", "deploy"
        }
        business_keywords = {
            "startup", "revenue", "marketing", "sales", "strategy", "product", "growth", "funnel"
        }
        life_keywords = {
            "life", "motivation", "stress", "anxiety", "purpose", "habit", "discipline", "relationship"
        }

        if any(word in lowered for word in technical_keywords):
            return "technical"
        if any(word in lowered for word in business_keywords):
            return "business"
        if any(word in lowered for word in life_keywords):
            return "life"
        return "casual"

    def _profile_for_mode(self, mode: str, user_text: str) -> StyleProfile:
        if mode == "technical":
            return StyleProfile(
                persona="Expert Engineer",
                opening="Good, let's work this like a systems engineer.",
                insight="Most technical issues are not hard because they're complex; they're hard because the wrong layer is being debugged.",
                hook="Want the fast path or the deep diagnostic path?",
            )

        if mode == "business":
            return StyleProfile(
                persona="Strategic Thinker",
                opening="Let's treat this like a strategy room decision.",
                insight="Growth usually stalls at one hidden bottleneck: message, channel, or conversion. Only one is the true constraint.",
                hook="Do you want a 7-day test plan or a full 90-day strategy map?",
            )

        if mode == "life":
            return StyleProfile(
                persona="Philosophical Mentor",
                opening="Let's slow this down and hit what actually matters.",
                insight="Clarity often arrives after action, not before it — motion creates meaning.",
                hook="Should we build a tiny daily protocol or challenge the belief behind this first?",
            )

        # casual
        playful_twist = "You gave me a short message; that usually means there is a bigger question under it."
        if len(user_text.split()) > 10:
            playful_twist = "You think fast. Let's make sure your next move is as sharp as your thinking."

        return StyleProfile(
            persona="Charismatic Friend",
            opening="Nice. Let's make this conversation worth your time.",
            insight=playful_twist,
            hook="Pick one: quick answer, bold answer, or uncomfortable-but-useful answer?",
        )

    def _mirror(self, text: str) -> str:
        words = re.findall(r"\w+", text)
        if not words:
            return "Say one real thing on your mind, and we'll build from there."

        if len(words) <= 4:
            return "Short input, clear intent — you're optimizing for signal. I respect that."
        if len(words) <= 12:
            return "Good framing. You gave enough detail to be useful without drowning the signal."
        return "Strong context. You're thinking in systems, not slogans."

    def respond(self, user_text: str) -> str:
        self.turn += 1

        mode = self._detect_mode(user_text)
        profile = self._profile_for_mode(mode, user_text)
        mirror = self._mirror(user_text)

        response_blocks = [
            f"[{profile.persona} Mode]",
            profile.opening,
            mirror,
            f"Aha: {profile.insight}",
            f"Next: {profile.hook}",
        ]

        if self.turn % 3 == 0:
            response_blocks.insert(
                3,
                "Pattern break: The answer you're asking for might be useful, but the question you're *not* asking is probably the one that changes everything.",
            )

        return "\n".join(response_blocks)


def main() -> None:
    bot = EngagingChatbot()
    print("Ultra Engaging Chatbot hazır. Çıkmak için 'exit' yaz.")

    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in {"exit", "quit"}:
            print("Bot: Güçlü sorularla geri dön. Buradayım.")
            break

        print("Bot:")
        print(bot.respond(user_text))
        print()


if __name__ == "__main__":
    main()
