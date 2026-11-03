# Programmes: several research programmes in one store

The store holds research programmes side by side (roadmap item 12). The Transport
Papers are one programme, `transport-papers`, and the default. Standard physics is
another, `standard`: textbook results, measured quantities and conventions, entered
once and cited by every programme that builds on them. A further programme is
added beside these two without editing either of them.

## Where a programme is declared

Three places, from the top down.

1. **store/config.yaml.** `programmes` maps each programme id to its description;
   `default_programme` names the programme of every entity that does not say.

   ```yaml
   default_programme: transport-papers
   programmes:
     transport-papers:
       title: The Transport Papers
       about: "the Transport Papers series: ..."
       maintainers: [leon]          # optional
     standard:
       title: Standard physics
       about: "standard physics imported once: ..."
   ```

   Ids are lowercase words joined by hyphens (`[a-z][a-z0-9-]*`); `title` is
   required, `about` and `maintainers` are optional.

2. **store/subjects.yaml.** Every subject carries `programme: <id>`. A subject
   holds the entities of one programme, so the map and generated documents never
   mix two programmes in one column or section. Subjects may be empty: the page
   hides a subject with no entities, and documents only draw sections from the
   entities they select.

3. **The entity.** An entity of the default programme needs nothing. Any other
   entity sets `programme: <id>` in its front matter, beside `subject`. The field
   is not substantive: adding or changing it needs no version bump.

## Adding a programme

1. Add the id under `programmes` in store/config.yaml, with title and about.
2. Add its subjects to store/subjects.yaml, each with `programme: <id>` and a
   `side` (metric, algebra, car, matter or synthesis).
3. File its entities with `programme: <id>` and `subject:` one of its subjects.
   Give them their own id prefixes so they cannot collide with another
   programme's ids.
4. Cite other programmes' results through ordinary `uses` (or, for a postulate,
   `assumes`) edges with a pinned version, exactly as within a programme.
5. Run `python3 -m tp check --store store --layers 1,2,3 --keep-going`.

Nothing in the existing programmes changes: `default_programme` stays as it is,
and the existing entities keep resolving to it. tests/test_programmes.py adds a
programme to the fixture this way and asserts that no earlier file is touched.

## How standard physics enters

- **Once.** A textbook theorem, a classification or a measured value is one entity
  in the `standard` programme, not a Fact restated in each paper that uses it.
  Before filing one, search for it (MCP `search_claims` with
  `programme: standard`).
- **As an imported Fact.** Status `imported`, with `imported_from` giving the
  source: `citation` (author, title, edition), `locator` (theorem, equation or
  page) and `doi` or `url` where one exists. No derivations; the proof lives in
  the source.
- **Checked where a finite core exists.** If a finite or exact core can be
  computed (the real Clifford classification over small signatures, a CAR
  identity on one mode, a closed-form horizon quantity), attach a check.py and
  list it in `checked_by`, so the import is evidence, not only a citation.
- **Programmes depend on it through `uses` edges.** A paper's result that rests on
  a standard result lists `std-...@n` among its premises. The paper's own
  "Fact (imported)" text still cites the source in prose; the store keeps one
  entity for it.
- **Quantities live in `standard-quantities`.** Measured and defined constants are
  `quantity` entities (store/quantities/, `programme: standard`, subject
  `standard-quantities`) with value, uncertainty, units, source and date. Results
  pin them through `quantities:`; checks read values from them rather than
  hard-coding a record value.
- **Subjects.** `standard-quantities`, `standard-gr` (general relativity and GTG
  textbook results), `standard-qft` (quantum field theory and representation
  theory), `standard-algebra` (Clifford algebras and the classification of
  quadratic forms).
- New imported entities need a maintainer (CONTRIBUTING.md), in any programme.

## What the validator enforces (E218)

E218 is on only when config.yaml has a `programmes` key. Then it is an error when:

- `programmes` is not a mapping from valid ids to entries with a `title`;
- `default_programme` names an id that is not registered;
- a subject's `programme` is not registered;
- an entity's programme (its own field, else `default_programme`) is missing or
  not registered.

The schema checks the field's form (`[a-z][a-z0-9-]*`); E208 still requires every
entity's `subject` to exist in subjects.yaml.

## Reading by programme

- MCP: `list_programmes` lists each programme with its subjects and entity counts;
  `list_entities`, `search_claims` and `list_subjects` take an optional
  `programme` filter; every entity summary carries `programme`.
- Code: `tp.validate.programme_of(store, entity)` resolves an entity's programme.
- The page carries each result's programme in its data and the registered
  programmes in `DATA.programmes`.
