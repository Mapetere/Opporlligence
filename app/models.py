from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class Source:
    """An external information source."""

    source_id: str
    title: str
    url: str
    published_at: datetime
    publisher: str
    text: str
    location: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Event:
    """A normalized representation of a meaningful real-world development."""

    event_id: str
    title: str
    occurred_at: datetime
    location: str | None
    event_type: str
    entities: tuple[str, ...]
    what_changed: str
    previous_state: str | None
    new_state: str | None
    source_ids: tuple[str, ...]


@dataclass(frozen=True)
class Opportunity:
    """A candidate opportunity produced by the reasoning engine."""

    opportunity_id: str
    claim: str
    gap: str
    affected_users: tuple[str, ...]
    evidence: tuple[str, ...]
    contradictions: tuple[str, ...]
    unknowns: tuple[str, ...]
    confidence: float
    urgency: str
    recommendation: str

    def is_actionable(self) -> bool:
        return self.confidence >= 0.70 and self.recommendation in {
            "INVESTIGATE",
            "BUILD",
        }
