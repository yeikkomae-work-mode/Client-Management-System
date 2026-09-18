import json
import re

# Sequence A — Star Rating angle. Source: the "Amazon Seller" campaign drafted
# directly in Instantly (id 981b5d19-ea6b-412d-8c98-c00880e35e0a, status DRAFT,
# never sent — pulled live via API on 2026-08-26). This is Variant A (Rating) of
# that campaign's 2-variant sequence; Variant B (Product Type) doesn't apply here
# since all 964 leads in this campaign have Rating populated and none have Product Type.
#
# Instantly -> PlusVibe conversion applied:
#   {{firstName}} / {{first_name}}   -> {{first_name}}
#   {{companyName}} / {{company_name}} -> {{company_name}}
#   {{Rating}} / {{star_rating}}     -> {{custom_rating}}   (custom vars take a "custom_" prefix)
#   {{accountSignature}}             -> {{sender_signature}} (PlusVibe's native signature var)
#   {{RANDOM | a | b | c}}           -> unchanged
#
# PLATFORM CONSTRAINT (confirmed building the earlier UK/USA Seller campaign):
# PlusVibe allows only ONE variable per spintax section. The Instantly draft nests
# {{companyName}} and {{Rating}} inside RANDOM blocks together, and the subject nests
# a different single variable inside each of its 3 RANDOM branches. Both patterns are
# restructured here with every merge field outside the RANDOM blocks, wording kept intact.

E1_SUBJECT = ("{{RANDOM | found something on | quick note on | worth a look at}} "
              "{{company_name}}'s {{custom_rating}}-star Amazon listing")

E1_BODY = [
    "Hi {{first_name}},",
    "I took a look at {{company_name}}'s Amazon listing, currently sitting at {{custom_rating}} stars. "
    "{{RANDOM | I noticed a few reviews that read more like delivery or seller complaints than actual product feedback. "
    "| I spotted some reviews that seem off-topic — more about shipping or service than the product itself. "
    "| I found reviews that look like they shouldn't count against the rating.}}",
    "{{RANDOM | Amazon's Community Guidelines don't actually allow reviews like that to stay on a listing, even though most sellers never challenge them. "
    "| Under Amazon's own guidelines, reviews like that usually don't qualify to remain on the product page — most sellers just don't know they're removable. "
    "| Those kinds of reviews technically violate Amazon's Community Guidelines, but very few sellers ever flag them.}}",
    "{{RANDOM | We can run a free, closer check and send back exactly which reviews look removable — no cost either way. "
    "| Happy to run a no-cost audit on your listing and show you what's realistically removable. "
    "| We can check the listing free of charge and send you a breakdown, no obligation.}}",
    "{{RANDOM | Want me to send it over? | Worth a look? | Interested in seeing the breakdown?}}",
    "{{sender_signature}}",
]

E2_SUBJECT = ("{{RANDOM | following up on | quick nudge on | still worth checking}} "
              "the {{custom_rating}}-star listing")

E2_BODY = [
    "Hi {{first_name}},",
    "Circling back on {{company_name}}'s {{custom_rating}}-star listing. "
    "{{RANDOM | Most sellers are surprised how many of their reviews actually qualify for removal once we look closely. "
    "| It's common for brands at that rating range to have a few reviews that never should have been approved in the first place. "
    "| Worth a closer look at what might be pulling the rating down from where it could be.}}",
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

ALLOWED_VARS = {"first_name", "company_name", "custom_rating", "sender_signature"}


def spintax_blocks(text):
    for m in re.finditer(r"\{\{\s*RANDOM", text, re.I):
        depth, i = 0, m.start()
        while i < len(text):
            if text.startswith("{{", i):
                depth += 1; i += 2
            elif text.startswith("}}", i):
                depth -= 1; i += 2
                if depth == 0:
                    yield text[m.start():i]; break
            else:
                i += 1


def check(text, where):
    for block in spintax_blocks(text):
        inner = block[len("{{RANDOM"):-2]
        nested = re.findall(r"\{\{\s*([a-zA-Z_]+)\s*\}\}", inner)
        assert not nested, f"{where}: variable(s) {nested} nested inside a RANDOM block"
    used = set(re.findall(r"\{\{\s*([a-zA-Z_]+)\s*\}\}", text))
    unknown = used - ALLOWED_VARS - {"RANDOM"}
    assert not unknown, f"{where}: unknown variable(s) {unknown}"
    assert text.count("{{") == text.count("}}"), f"{where}: unbalanced braces"


def html(paragraphs):
    return "".join(f"<p>{p}</p>" for p in paragraphs)


def build_sequences():
    steps = [
        (1, 3, "E1 - Rating (Day 0)", E1_SUBJECT, E1_BODY),
        (2, 4, "E2 - Follow-up (Day 3)", E2_SUBJECT, E2_BODY),
        (3, 1, "E3 - Break-up (Day 7)", E3_SUBJECT, E3_BODY),  # wait_time unused on last step, API min is 1
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
