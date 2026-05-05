# Paradise Sales Email Bot

## What this is

Cold-outreach bot for **Paradise Home Design Inc.** signed by **The Sales Team**
(sales@paradisehomedesigninc.com). Polished senior-rep voice, "we just
finished a project nearby" angle, free in-home design consult. **No
discount** on this bot - Brady's bot owns the credit lane.

## Pitch contract

See `MASTER_PROMPT.md`. Body cap 120 words, ASCII hyphens only, banned
words enforced.

## Sender

- Name: Paradise Home Design - Sales
- Email: sales@paradisehomedesigninc.com
- Sign-off: "- The Sales Team / Paradise Home Design Inc / 225 E Deerpath Rd, Lake Forest IL"

## Commands

```bash
python run.py load data/sample_leads.csv
python run.py verify
python run.py preview 6
python run.py draft 50
```

## Architecture

Same shared core as Brady. Different master prompt, sender, and accent
colour. Cross-bot dedupe via `../../_shared/data/dedupe.db` so a single
homeowner never sees both Brady's and Sales's emails.
