"""Sales bot test previews. Master prompt: senior sales-team voice,
'we just finished a project nearby' opener, free in-home consult, NO
discount, body cap 120 words, ASCII hyphens only."""
import sys
from pathlib import Path

SHARED_ROOT = Path(__file__).resolve().parents[2] / "_shared"
sys.path.insert(0, str(SHARED_ROOT))

from core import make_samples  # noqa: E402

import run as bot_run  # noqa: E402


SIGNOFF = (
    "- The Sales Team\n"
    "Paradise Home Design Inc\n"
    "225 E Deerpath Rd, Lake Forest IL\n"
    "sales@paradisehomedesigninc.com\n"
    "(847) 681-9000\n"
    "See our work: paradisehomedesigninc.com/gallery.html"
)
PS_SPOUSE = ("P.S. if your spouse handles renovation calls, "
             "feel free to forward.")


SAMPLES = [
    {
        "subject": "Just finished a kitchen on Sheridan",
        "body_text": (
            "Hi Catherine, our crew just finished a kitchen renovation in "
            "Lake Forest last week. Adelphi cabinets, a quartz waterfall "
            "island, and Calacatta marble through to the family room.\n\n"
            "Before we move to the next job we have two free in-home "
            "design consults open in Winnetka this month. Our designer "
            "brings sketches, finish samples, and real numbers, no "
            "commitment.\n\n"
            "Paradise has been on Deerpath in Lake Forest for 38 years. "
            "We carry Adelphi, Candlelight, Medallion, and Fabuwood, and "
            "the showroom on Deerpath is open if you'd rather walk "
            "through samples first.\n\n"
            "Would Tuesday or Thursday evening work for a 30-minute "
            "walkthrough at your place?\n\n"
            f"{SIGNOFF}\n\n{PS_SPOUSE}"
        ),
        "hero_key": "kitchen_marble_arch",
        "thumb_keys": ["kitchen_marble_brass", "kitchen_black_island", "kitchen_white_pendants"],
        "fname": "01_catherine_winnetka.html",
    },
    {
        "subject": "Two open consult slots in Highland Park",
        "body_text": (
            "Hi Robert, we just wrapped a primary bath up the road in "
            "Glencoe. Walnut double vanity, marble counters, and a "
            "walk-in shower with seamless glass.\n\n"
            "Before the crew moves to the next job we have two free "
            "in-home design consults open in Highland Park this month. "
            "Our designer brings sketches, finish samples, and real "
            "numbers, no commitment.\n\n"
            "Paradise has been on Deerpath in Lake Forest for 38 years. "
            "We're BBB-accredited and our portfolio is on our site and "
            "at the showroom.\n\n"
            "Would Tuesday or Saturday morning work for a 30-minute "
            "walkthrough at your place?\n\n"
            f"{SIGNOFF}"
        ),
        "hero_key": "bath_double_vanity",
        "thumb_keys": ["kitchen_white_pendants", "kitchen_white_modern", "kitchen_marble_brass"],
        "fname": "02_robert_highland_park.html",
    },
    {
        "subject": "Cabinet showroom is open Saturdays",
        "body_text": (
            "Hi Priya, a kitchen we finished in Winnetka just hit our "
            "gallery. Black-stained cabinetry, brass pendants, and a "
            "Calacatta island that anchors the whole room.\n\n"
            "Before the crew moves on we have two free in-home design "
            "consults open in Lake Forest this month. Our designer "
            "brings sketches, finish samples, and real numbers, no "
            "commitment.\n\n"
            "Paradise has been on Deerpath for 38 years. The Deerpath "
            "showroom is open Saturdays if you'd rather walk through "
            "Adelphi, Medallion, and Fabuwood samples in person first.\n\n"
            "Would Tuesday afternoon or Saturday morning work for the "
            "in-home walkthrough?\n\n"
            f"{SIGNOFF}\n\n{PS_SPOUSE}"
        ),
        "hero_key": "kitchen_marble_brass",
        "thumb_keys": ["kitchen_black_island", "kitchen_marble_arch", "kitchen_white_pendants"],
        "fname": "03_priya_lake_forest.html",
    },
    {
        "subject": "Just wrapped a bath in Wilmette",
        "body_text": (
            "Hi Greg, we just wrapped a primary bath in Wilmette last "
            "week. Walnut vanity, marble counters, and a walk-in shower "
            "with custom niche.\n\n"
            "Before our crew moves to the next job we have two free "
            "in-home design consults open in Glencoe this month. Our "
            "designer brings sketches, finish samples, and real numbers, "
            "no commitment.\n\n"
            "Paradise has been on Deerpath for 38 years. We carry "
            "Adelphi, Candlelight, Medallion, and Fabuwood, and the "
            "showroom is open Saturdays.\n\n"
            "Would Tuesday or Thursday evening work for a 30-minute "
            "walkthrough at your place?\n\n"
            f"{SIGNOFF}"
        ),
        "hero_key": "kitchen_marble_brass",
        "thumb_keys": ["kitchen_marble_arch", "kitchen_white_chandeliers", "bath_double_vanity"],
        "fname": "04_greg_glencoe.html",
    },
    {
        "subject": "Open to a 30-minute walkthrough?",
        "body_text": (
            "Hi Allison, our crew just finished a kitchen in Burr Ridge "
            "last week. White cabinetry, a quartz island, and oak floors "
            "through to the dining room.\n\n"
            "Before we move to the next job we have two free in-home "
            "design consults open in Hinsdale this month. Our designer "
            "brings sketches, finish samples, and real numbers, no "
            "commitment.\n\n"
            "Paradise has been on Deerpath in Lake Forest for 38 years. "
            "We carry Adelphi, Candlelight, Medallion, and Fabuwood.\n\n"
            "Would Tuesday or Thursday evening work for a 30-minute "
            "walkthrough at your place?\n\n"
            f"{SIGNOFF}\n\n{PS_SPOUSE}"
        ),
        "hero_key": "kitchen_white_modern",
        "thumb_keys": ["kitchen_white_pendants", "kitchen_white_chandeliers", "kitchen_marble_brass"],
        "fname": "05_allison_hinsdale.html",
    },
    {
        "subject": "Worth a look on Deerpath",
        "body_text": (
            "Hi Daniel, a kitchen we finished in Glenview just hit our "
            "gallery. Navy island, gray cabinetry, and quartz counters "
            "carried through to the breakfast nook.\n\n"
            "Before the crew moves on we have two free in-home design "
            "consults open in Glenview this month. Our designer brings "
            "sketches, finish samples, and real numbers, no commitment.\n\n"
            "Paradise has been on Deerpath for 38 years and the Deerpath "
            "showroom is open Saturdays for cabinet, stone, and "
            "hardware samples.\n\n"
            "Would Tuesday afternoon or Saturday morning work for a "
            "30-minute walkthrough at your place?\n\n"
            f"{SIGNOFF}"
        ),
        "hero_key": "kitchen_navy_island_small",
        "thumb_keys": ["kitchen_white_modern", "kitchen_white_pendants", "kitchen_traditional_cream"],
        "fname": "06_daniel_glenview.html",
    },
]


if __name__ == "__main__":
    paths = make_samples.generate(bot_run.CFG, SAMPLES)
    for p in paths:
        print("wrote", p)
