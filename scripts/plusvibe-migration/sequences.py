import json
import re

# Sequence B — Product Category angle (UK/USA Amazon Seller list, no rating data)
# Source: OUTPUT/Campaign Tracking/Cüneyt - Starfix Revised Sequences (Cleaned Database, 2026-08-21).md
#
# Instantly -> PlusVibe conversion applied:
#   {{first_name}}       -> {{first_name}}              (unchanged — PlusVibe uses snake_case too)
#   {{company_name}}     -> {{company_name}}            (unchanged)
#   {{product_category}} -> {{custom_product_category}} (custom vars take a "custom_" prefix)
#   {{sender_signature}} -> {{sender_signature}}        (unchanged)
#   {{RANDOM | a | b | c}} -> unchanged
#
# PLATFORM CONSTRAINT: PlusVibe allows only ONE variable per spintax section, so
# the drafted copy — which nested {{company_name}} AND {{product_category}} inside
# single RANDOM blocks — had to be restructured. Every merge field now sits OUTSIDE
# the spintax, with the varied wording kept intact. Meaning is unchanged.

E1_SUBJECT = ("{{RANDOM | question about your | quick note on your | worth flagging on your}} "
              "{{custom_product_category}} listings")

E1_BODY = [
    "Hi {{first_name}},",
    "I took a look at {{company_name}}'s {{custom_product_category}} listings on Amazon. "
    "{{RANDOM | A few of the reviews read more like delivery or seller complaints than actual product feedback. "
    "| Some of the reviews seem off-topic — more about shipping or service than the product itself. "
    "| Several reviews look like they shouldn't count against the product rating at all.}}",
    "{{RANDOM | Amazon's Community Guidelines don't actually allow reviews like that to stay on a listing, even though most sellers never challenge them. "
    "| Under Amazon's own guidelines, reviews like that usually don't qualify to remain on the product page — most sellers just don't know they're removable. "
    "| Those kinds of reviews technically violate Amazon's Community Guidelines, but very few sellers ever flag them.}}",
    "{{RANDOM | We can run a free, closer check and send back exactly which reviews look removable — no cost either way. "
    "| Happy to run a no-cost audit on your listing and show you what's realistically removable. "
    "| We can check the listing free of charge and send you a breakdown, no obligation.}}",
    "{{RANDOM | Want me to send it over? | Worth a look? | Interested in seeing the breakdown?}}",
    "{{sender_signature}}",
]

E2_SUBJECT = ("{{RANDOM | following up | quick nudge | still worth checking}} "
              "— {{company_name}}'s Amazon listings")

E2_BODY = [
    "Hi {{first_name}},",
    "Circling back on {{company_name}}'s {{custom_product_category}} listings. "
    "{{RANDOM | Most sellers are surprised how many of their reviews actually qualify for removal once we look closely. "
    "| It's common for brands in this space to have a few reviews that never should have been approved in the first place. "
    "| It's worth a closer look at what might be pulling those ratings down.}}",
    "{{RANDOM | We only get paid if a review actually comes down, so there's no risk in checking. "
    "| This is fully success-based — you pay only for reviews that are actually removed. "
    "| No subscription, no flat fee. You only pay for what we successfully remove.}}",
    "{{RANDOM | We've worked through thousands of these cases as an Amazon SPN partner, so we know which ones are worth pursuing and which aren't. "
    "| We do this daily as an Amazon SPN partner — we know Amazon's internal process well enough to push past the first auto-reply. "
    "| Between similar cases, we've removed well over 5,000 reviews across categories like this one.}}",
    "{{RANDOM | Still happy to run the free check whenever works. | Want me to send over what we'd find? "
    "| Send the word whenever's convenient and I'll get you the breakdown.}}",
    "{{sender_signature}}",
]

E3_SUBJECT = "{{RANDOM | should I close this out? | last note on this | one more try before I stop}}"

E3_BODY = [
    "Hi {{first_name}},",
    "{{RANDOM | I'll leave it here for now — didn't want this to just sit unanswered in your inbox. "
    "| This is my last note on this, don't want to keep nudging if it's not a priority right now. "
    "| Not trying to be a pest, so this'll be my last message on it.}}",
    "{{RANDOM | If those reviews ever become worth a look, the free check still stands — just reply and I'll run it. "
    "| If this becomes relevant later, happy to pick this back up anytime. "
    "| The offer's open whenever it's useful, just reply and we'll take it from there.}}",
    "{{RANDOM | If it's not the right time, no worries at all, just let me know and I'll close this out. "
    "| All good either way, just say the word and I'll stop following up. "
    "| Totally fine if it's not a priority, just a quick reply and I'll drop it.}}",
    "{{sender_signature}}",
]

ALLOWED_VARS = {"first_name", "company_name", "custom_product_category", "sender_signature"}


def spintax_blocks(text):
    """Yield the inner text of each top-level {{RANDOM ...}} block."""
    for m in re.finditer(r"\{\{\s*RANDOM", text, re.I):
        depth, i = 0, m.start()
        while i < len(text):
            if text.startswith("{{", i):
                depth += 1
                i += 2
            elif text.startswith("}}", i):
                depth -= 1
                i += 2
                if depth == 0:
                    yield text[m.start():i]
                    break
            else:
                i += 1


def check(text, where):
    """PlusVibe permits at most one variable per spintax section; we allow zero."""
    for block in spintax_blocks(text):
        inner = block[len("{{RANDOM"):-2]
        nested = re.findall(r"\{\{\s*([a-zA-Z_]+)\s*\}\}", inner)
        assert not nested, f"{where}: variable(s) {nested} nested inside a RANDOM block"
    used = set(re.findall(r"\{\{\s*([a-zA-Z_]+)\s*\}\}", text))
    unknown = used - ALLOWED_VARS - {"RANDOM"}
    assert not unknown, f"{where}: unknown variable(s) {unknown}"
    assert text.count("{{") == text.count("}}"), f"{where}: unbalanced braces"


def html(paragraphs):
    """Render drafted plain-text paragraphs as the HTML body PlusVibe expects."""
    return "".join(f"<p>{p}</p>" for p in paragraphs)


def build_sequences():
    steps = [
        (1, 3, "E1 - Product Category (Day 0)", E1_SUBJECT, E1_BODY),
        (2, 4, "E2 - Follow-up (Day 3)", E2_SUBJECT, E2_BODY),
        # Step 3 is the last email so its wait_time is never used, but the API
        # rejects 0 — it carries the minimum allowed value.
        (3, 1, "E3 - Break-up (Day 7)", E3_SUBJECT, E3_BODY),
    ]
    out = []
    for step, wait, name, subject, body in steps:
        check(subject, f"step {step} subject")
        for i, para in enumerate(body):
            check(para, f"step {step} body para {i + 1}")
        out.append({"step": step, "wait_time": wait, "variations": [
            {"variation": "A", "name": name, "subject": subject, "body": html(body)}]})
    return out


if __name__ == "__main__":
    print(json.dumps(build_sequences(), indent=2, ensure_ascii=False))
