import sanitizer

# Raw test data containing mixed cases, punctuation-like words, and banned words
raw_words: list[str] = ["AI", "SPAM", "Engineering", "junk", "PYTHON", "spam", "CODE"]

# A set of banned words (mix of lowercase and capitalized to test case-insensitive filtering)
banned_words: tuple[str] = ("spam", "Junk")

# Raw test scores or metrics
test_scores: list[int] = [10, 25, 40, 50, 100]

# Test cases to iterate through in your main.py file:
mode_scale: str = "SCALING"         # Should multiply every number by a factor (e.g., * 2)
mode_filter: str = "filter"      # Should keep only numbers >= 50
mode_power: str = "expo"     # Should square every number (** 2)
mode_invalid: str = "random_mode"   # Should hit your wildcard fallback and return []

print(sanitizer.text_sanitizer(raw_words,banned_words))
print(sanitizer.metric_router(test_scores,mode_scale))