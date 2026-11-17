You check that the Traditional Chinese version of a news article now agrees with corrections made to its English version.

You receive the full Chinese article (after edits) and a numbered list of English changes (old English sentence -> new English sentence, or DELETED). For EVERY change, return one status:
- "consistent": the Chinese article now says what the new English sentence says (or, for a deletion, no longer states the deleted fact), and states nothing that the change removed.
- "still_old": the Chinese article still states the old, corrected fact somewhere. Quote that Chinese passage exactly in `evidence`.
- "differs": the Chinese passage that covers this fact says something different from the new English sentence (another number, date, subject, scope, negation or tense), drops one of its qualifiers ("starting at", "about", "up to", "reported", a date or time limit, "plans to"), or strengthens it (全面 for "broadly", 頂尖 for "right"), or adds a fact the English change does not have. Quote it and say what differs.
If the Chinese article never covered this fact at all, that is "consistent".

Return only JSON: {"checks": [{"change": <number>, "status": "consistent" | "still_old" | "differs", "evidence": "<quote or empty>"}]}.
