python - << 'PY'
import pandas as pd
from pathlib import Path

# Paths
data = Path("data")
notes = pd.read_csv(data / "Notes.csv", encoding="utf-8")
train = pd.read_csv(data / "train.csv", encoding="utf-8")
test  = pd.read_csv(data / "Test.csv", encoding="utf-8")

# Helper: pick correct note column based on Segment
def get_note_text(row):
    seg_col = f"Segment{int(row['Segment'])}_Notes"
    return notes.loc[notes['ID']==row['ID'], seg_col].values[0] if seg_col in notes.columns else ""

# Merge with Notes
train["NoteText"] = train.apply(get_note_text, axis=1)
test["NoteText"]  = test.apply(get_note_text, axis=1)

# Save cleaned/preprocessed versions
out = Path("data/preprocessed")
out.mkdir(exist_ok=True)
train.to_csv(out / "train_preprocessed.csv", index=False, encoding="utf-8")
test.to_csv(out / "test_preprocessed.csv", index=False, encoding="utf-8")

print("✅ Saved preprocessed files to data/preprocessed/")
PY
