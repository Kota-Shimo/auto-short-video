# config.py  – 2 スピーカー用ボイスを全言語で分離
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# ── ディレクトリ ───────────────────────────────
BASE   = Path(__file__).parent
INPUT  = BASE / "input"
OUTPUT = BASE / "output"
TEMP   = BASE / "temp"
for d in (INPUT, OUTPUT, TEMP): d.mkdir(exist_ok=True)

# ── API キー ──────────────────────────────────
OPENAI_API_KEY      = os.getenv("OPENAI_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "")

# ── OpenAI TTS 用 (Alice 用, Bob 用) ───────────
VOICE_MAP = {
    "en": ("alloy",   "echo"),     # 英語 : 落ち着いた男性 / 落ち着いた女性
    "ja": ("nova",    "echo"),  # 日本語 : 女性 / 中性
    "pt": ("fable",   "onyx"),     # ポルトガル語 : やや明るい / 低め
    "id": ("alloy",   "fable"),    # インドネシア語 : 落ち着き / 明るめ
}
# 必要に応じてボイス名は自由に差し替えてください
