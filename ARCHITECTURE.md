# Architecture

Opporlligence is designed as a reasoning pipeline rather than a single prompt.

```text
Sources
  ↓
Ingestion
  ↓
Normalization + deduplication
  ↓
Event extraction
  ↓
Historical/contextual memory
  ↓
Change detection
  ↓
Relationship discovery
  ↓
Gap detection
  ↓
Opportunity generation
  ↓
Counter-evidence / contradiction testing
  ↓
Ranking
  ↓
Opportunity memory + alerts
```

## Core concepts

### Source
A piece of external information: article, announcement, discussion, release note, regulatory notice, company update, job-market signal, or another supported source.

### Event
A normalized representation of something that happened or changed.

An event should capture:

- what happened;
- when it happened;
- where it matters;
- entities involved;
- what the previous state was;
- what the new state is;
- evidence supporting the interpretation.

### Change
A meaningful difference between an earlier state and a later state. Change detection is central because an isolated fact is usually less useful than understanding what became different.

### Gap
A missing capability, unmet need, friction point, displaced workflow, newly created constraint, or other unresolved condition exposed by a change.

### Opportunity
A gap that has enough evidence and significance to justify investigation. An opportunity is not automatically a startup or product.

### Contradiction
Evidence that weakens or disproves an opportunity. The system must actively search for it.

### Opportunity memory
A persistent record of opportunities so that the system can determine whether an opportunity is strengthening, decaying, already solved, becoming crowded, or changing form.

## Reasoning lenses

The first implementation will support explicit lenses such as:

- unsolved problems;
- newly available capabilities;
- market transitions;
- regulatory changes;
- technological convergence;
- falling costs;
- rising costs or accessibility barriers;
- developer and operational pain;
- replacement/displacement;
- Zimbabwe-specific constraints;
- newly connected systems or ecosystems.

The architecture should eventually allow the system to discover additional useful lenses rather than treating this list as permanent.

## Important boundary

The user capability model is downstream of discovery. It can help rank execution paths later, but it must not prevent the intelligence engine from discovering opportunities that require skills, partners, capital, infrastructure, or technology the user does not currently possess.
