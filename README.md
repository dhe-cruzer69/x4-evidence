# X4 Evidence

**Verification before success.** Evidence ledger for AI agents.

No claim is marked PASS / VALIDATED without machine-readable evidence.

## Evidence States

```
OBSERVED → CORRELATED → HYPOTHESIS → VALIDATED
                                 ↘ UNKNOWN — HUMAN REVIEW REQUIRED
```

## Core API

```python
from x4_evidence import EvidenceLedger, Claim

ledger = EvidenceLedger()

claim = Claim(
    claim="Deployment succeeded",
    status="HYPOTHESIS",
    evidence=[],
)

# Attach evidence
claim.add_evidence("deployment_id", "dep_abc123")
claim.add_evidence("health_check", "200 OK")
claim.add_evidence("smoke_test", "all green")

# Only promote when sufficient evidence exists
result = ledger.validate(claim)
# → status becomes VALIDATED or stays UNKNOWN
```

## Principles

- Execution ≠ Success
- Every important claim carries an evidence object
- Timestamps, hashes, and verifier identity are recorded
- `UNKNOWN` is a first-class state, never silently upgraded

## Integration

Designed to sit after the agent loop and before any “done” status is emitted to humans or downstream systems.

Part of the X4 / ARIEX4Ops portfolio.

Apache-2.0
