from humanizer_v2 import humanize_advanced
from evaluator import simulate_ai_score, simulate_perplexity

text = """
Artificial intelligence is important for many applications.
It shows strong performance in modern systems.
"""

print("===== 原始文本 =====")
print(text)

original_ai = 93
original_perplexity = 25

new_text = humanize_advanced(text)

new_ai = simulate_ai_score(new_text)
new_perplexity = simulate_perplexity(new_text)

print("\n===== 改写后文本 =====")
print(new_text)

print("\n===== 对比结果 =====")
print(f"原始AI率: {original_ai}%")
print(f"改写后AI率: {new_ai}%")
print(f"原始困惑度: {original_perplexity}")
print(f"改写后困惑度: {new_perplexity}")
