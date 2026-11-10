"""JSON Schema for entity front matter (layer 1, shape)."""

PIN = {"type": "string",
       "pattern": r"^[a-z][a-z0-9-]*(\.[a-z0-9][a-z0-9-]*)+@[1-9][0-9]*$"}
ID = {"type": "string", "pattern": r"^[a-z][a-z0-9-]*(\.[a-z0-9][a-z0-9-]*)+$"}
PINS = {"type": "array", "items": PIN}
IDS = {"type": "array", "items": ID}

DERIVATION = {
    "type": "object",
    "required": ["name"],
    "additionalProperties": False,
    "properties": {
        "name": {"type": "string", "pattern": r"^[a-z0-9][a-z0-9-]*$"},
        "uses": PINS,
        "assumes": PINS,
        "proof": {"type": ["string", "null"]},
        "conditional": {"type": "boolean"},
        "note": {"type": "string"},
    },
}

EVIDENCE = {
    "type": "object",
    "required": ["kind"],
    "additionalProperties": False,
    "properties": {
        # check:  checks/<file>.py::<function>, new-style, premise-tracked
        # legacy: a series verify script, matched by statement tags
        # lean:   a Lean theorem name
        # proof:  the derivation's proof text only, not machine-checked
        "kind": {"enum": ["check", "legacy", "lean", "proof"]},
        "ref": {"type": "string"},
        "script": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}},
        "derivation": {"type": "string"},
    },
}

IMPORT = {
    "type": "object",
    "required": ["citation"],
    "additionalProperties": False,
    "properties": {
        "citation": {"type": "string"},
        "key": {"type": "string"},
        "locator": {"type": "string"},
        "doi": {"type": "string"},
        "url": {"type": "string"},
        "series": {"type": "boolean"},
    },
}

ENTITY = {
    "type": "object",
    "required": ["id", "kind", "version", "title", "status",
                 "proposed_by", "ai_involved"],
    "additionalProperties": False,
    "properties": {
        "id": ID,
        "kind": {"enum": ["claim", "object", "prediction", "question", "note", "quantity"]},
        "version": {"type": "integer", "minimum": 1},
        "title": {"type": "string", "minLength": 1},
        "status": {"type": "string"},
        "region": {"type": "string"},
        "subject": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
        "about": IDS,
        "comments_on": IDS,
        "reading_of": {"type": "array", "items": {"enum": ["metric", "car"]}},
        "derivations": {"type": "array", "items": DERIVATION},
        "checked_by": {"type": "array", "items": EVIDENCE},
        "specialises": PINS,
        # the foundation layer: postulates that are mathematical primitives of the whole graph
        # (the bit and what follows), kept out of the premise ledger, and the edges that root
        # entities in them (see store/conventions.md, "The foundation")
        "foundation": {"type": "boolean"},
        "founded_on": PINS,
        "equivalent_to": PINS,
        "contradicts": PINS,
        "supports": PINS,
        "tests": PINS,
        "kills": PINS,
        "fitted_to": {"type": "array", "items": {"type": "string"}},
        "imported_from": {"type": "array", "items": IMPORT},
        "lineage": {
            "type": "object", "additionalProperties": False,
            "properties": {k: IDS for k in
                           ("derived_from", "supersedes", "inverts", "motivated_by")},
        },
        "kill_condition": {
            "type": "object", "additionalProperties": False,
            "properties": {"threshold": {"type": "string"},
                           "data_source": {"type": "string"},
                           "registered": {"type": "string"}},
        },
        "observations": {"type": "array", "items": {
            "type": "object", "required": ["date", "dataset", "result"],
            "additionalProperties": False,
            "properties": {"date": {"type": "string"}, "dataset": {"type": "string"},
                           "result": {"type": "string"},
                           "verdict": {"enum": ["consistent", "tension", "contested",
                                                "refutes", "confirms", "pending"]},
                           "source": {"type": "string"}}}},
        "settled_by": IDS,
        "refuted_by": IDS,
        "notation": {"type": "array", "items": {"type": "string"}},
        "constructor": {"type": "string"},
        "ledger": {"enum": ["essential", "convenient", "absent"]},
        "locators": {"type": "object"},
        "proposed_by": {
            "type": "object", "required": ["kind"], "additionalProperties": False,
            "properties": {"kind": {"enum": ["human", "ai", "extraction"]},
                           "session": {"type": "string"},
                           "author": {"type": "string"}},
        },
        "ai_involved": {"enum": ["yes", "no", "unknown"]},
        # who did what, and which model where that is on record (tp/credit.py)
        "credit": {"type": "array", "items": {
            "type": "object", "required": ["name", "role"], "additionalProperties": False,
            "properties": {"name": {"type": "string", "minLength": 1},
                           "role": {"type": "string", "minLength": 1},
                           "source": {"type": "string"},
                           # optional: the person's ORCID iD (bare, 0000-0000-0000-000X), carried
                           # into the Zenodo record's contributors at each release (tp/releases.py)
                           "orcid": {"type": "string",
                                     "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"},
                           # optional: person or ai; when absent, a name of a known model family
                           # reads as ai (tp/releases.py is_model)
                           "kind": {"enum": ["person", "ai"]},
                           # the version an amendment produced; absent for the original credit
                           "version": {"type": "integer", "minimum": 1}}}},
        # what each amendment did (tp/amend.py): a correction fixes a proof, a check, a status or a
        # link and leaves the statement; a restatement changes the statement
        "amendments": {"type": "array", "items": {
            "type": "object", "required": ["version", "kind", "defect"], "additionalProperties": False,
            "properties": {"version": {"type": "integer", "minimum": 2},
                           "kind": {"enum": ["correction", "restatement"]},
                           # what was wrong with the accepted version, specifically
                           "defect": {"type": "string", "minLength": 30},
                           # optional: a check of this result that shows the defect is fixed
                           "evidence": {"type": "string"}}}},
        # where geometric algebra is not the language of the result, and why (tp/galang.py)
        "outside_ga": {"type": "object", "required": ["kind", "why"], "additionalProperties": False,
                       "properties": {"kind": {"enum": ["imported", "complex-analysis", "bridge", "other"]},
                                      "why": {"type": "string", "minLength": 20}}},
        "review": {"enum": ["draft", "typed", "reviewed"]},
        # how far a human has taken it (roadmap item 8); signoffs record each sign-off
        "trust": {"enum": ["ai-proposed", "ai-refereed", "human-read", "human-checked",
                           "published"]},
        "signoffs": {"type": "array", "items": {
            "type": "object", "required": ["by", "date", "version", "level"],
            "additionalProperties": False,
            "properties": {"by": {"type": "string"}, "date": {"type": "string"},
                           "version": {"type": "integer", "minimum": 1},
                           "level": {"enum": ["human-read", "human-checked"]},
                           "note": {"type": "string"}}}},
        # the research programme the entity belongs to (roadmap item 12); default in config
        "programme": {"type": "string", "pattern": r"^[a-z][a-z0-9-]*$"},
        # machine-readable form of the statement (roadmap item 11): exact Python
        # expressions, evaluated in the namespace of the entity's own check.py
        "payload": {"type": "array", "items": {
            "type": "object", "required": ["kind", "python"], "additionalProperties": False,
            "properties": {"kind": {"enum": ["identity", "value", "inequality", "count",
                                             "classification"]},
                           "python": {"type": "string"},
                           "clause": {"type": "string"},
                           "quantity": ID,
                           "note": {"type": "string"}}}},
        # quantities this entity's statement or check uses (roadmap item 10)
        "quantities": PINS,
        # quantity entities only
        "quantity": {
            "type": "object", "required": ["symbol", "value", "units", "source"],
            "additionalProperties": False,
            "properties": {"symbol": {"type": "string"},
                           "value": {"type": "string"},
                           "uncertainty": {"type": "string"},
                           "units": {"type": "string"},
                           "dimension": {"type": "string"},
                           "exact": {"type": "boolean"},
                           "source": IMPORT,
                           "date": {"type": "string"},
                           "note": {"type": "string"}}},
        "extraction": {"type": "object"},
        "aliases": {"type": "array", "items": {"type": "string"}},
    },
}

STATUSES = {
    "claim": ("proved", "imported", "conjectured", "refuted", "postulate"),
    "object": ("defined",),
    "prediction": ("live", "confirmed", "killed"),
    "question": ("open", "settled"),
    # a note is commentary on other entities: a remark or a worked example.
    # It asserts nothing the graph relies on, so nothing may use it.
    "note": ("remark", "example", "setting"),
    # a quantity: a measured value with its uncertainty, an exact defined value, or one
    # derived in the store
    "quantity": ("measured", "defined", "derived"),
}
