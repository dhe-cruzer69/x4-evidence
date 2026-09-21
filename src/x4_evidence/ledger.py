from enum import Enum
from typing import Any
from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

class EvidenceStatus(str, Enum):
    OBSERVED = "OBSERVED"
    CORRELATED = "CORRELATED"
    HYPOTHESIS = "HYPOTHESIS"
    VALIDATED = "VALIDATED"
    UNKNOWN = "UNKNOWN"

@dataclass
class Claim:
    claim: str
    status: EvidenceStatus = EvidenceStatus.HYPOTHESIS
    evidence: list[dict[str, Any]] = field(default_factory=list)
    claim_id: str = field(default_factory=lambda: "clm_" + uuid.uuid4().hex[:12])
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    verified_by: str | None = None

    def add_evidence(self, key: str, value: Any, source: str = "automated") -> None:
        self.evidence.append({
            "key": key,
            "value": value,
            "source": source,
            "ts": datetime.now(timezone.utc).isoformat(),
        })

class EvidenceLedger:
    """No claim becomes VALIDATED without evidence."""

    def __init__(self, min_evidence: int = 1):
        self.min_evidence = min_evidence
        self._claims: dict[str, Claim] = {}

    def register(self, claim: Claim) -> Claim:
        self._claims[claim.claim_id] = claim
        return claim

    def validate(self, claim: Claim) -> Claim:
        if len(claim.evidence) >= self.min_evidence and claim.status != EvidenceStatus.UNKNOWN:
            claim.status = EvidenceStatus.VALIDATED
            claim.verified_by = "x4-evidence"
        else:
            claim.status = EvidenceStatus.UNKNOWN
        self._claims[claim.claim_id] = claim
        return claim

    def get(self, claim_id: str) -> Claim | None:
        return self._claims.get(claim_id)
