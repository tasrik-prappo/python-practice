import math
def text_sanitizer(words: list, banned_words: tuple) -> list:
    refined_words: list = [word.lower() for word in words if word.lower() not in banned_words]
    return refined_words

def metric_router(nums: list, op: str) -> list:
    match op.lower():
        case "scaling":
            return [math.e * num for num in nums]
        case "filter":
            return [num for num in nums if num > 50]
        case "expo":
            return [num ** 2 for num in nums]
        case _:
            return []
