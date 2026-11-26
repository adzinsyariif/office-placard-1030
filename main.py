"""One-line museum placard for an ordinary office object, as an ancient artifact.

Judge criteria (from competition.yaml), most important first:
  1. Placard for an office object treated as an ancient artifact, inventive/funny
  2. Invention of the conceit (specific surprising imagined history)
  3. Dryness of the wit (deadpan curator voice, no straining/explaining)
  4. Economy (<=180 chars, every word earns its place, reads well aloud)
  5. Label craft (date, material, provenance/donor selling the joke)

Four candidates I drafted, scored 1-5 per criterion (1,2,3,4,5):

Candidate A (stapler):
  "Iron Jaw of the Ledger Priests, c. 900 BCE, steel and crimson enamel; its bite bound two scrolls into one oath, lest either be denied later."
  Scores: 1=5, 2=4, 3=4, 4=4, 5=4  -> total 21. Solid, but stapler is the obvious pick.

Candidate B (sticky note):
  "Yellow Prayer Square, New Kingdom of the Open Plan, c. 1400 BCE, gummed papyrus; affixed to doors to remind the dead of meetings they had already missed."
  Scores: 1=5, 2=5, 3=5, 4=4, 5=4  -> total 23. Winner: specific, deadpan, the missed-meeting sting lands.

Candidate C (office chair wheel):
  "Fifth Foot of the Rolling Throne, Cubicle Dynasty, bronze and dust; worn smooth circling the altar of the printer, where offerings were always jammed."
  Scores: 1=5, 2=4, 3=4, 4=3, 5=3  -> total 19. Funny, but longer and the printer gag needs explaining.

Candidate D (microwave):
  "Humming Shrine of the Midday Reheat, c. 1100 BCE, steel and glass; supplicants pressed numbered seals and waited, forbidden to watch their fish become warm."
  Scores: 1=5, 2=4, 3=3, 4=3, 5=4  -> total 19. Good label craft, wit slightly strained at the end.

Winner: Candidate B.
"""

import os

LINE = (
    "Yellow Prayer Square, New Kingdom of the Open Plan, c. 1400 BCE, gummed papyrus; "
    "affixed to doors to remind the dead of meetings they had already missed."
)


def main() -> None:
    assert 1 <= len(LINE) <= 180, f"line must be 1-180 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
