# X4 Evidence

**Verification before success.** Evidence ledger for AI agents.

No claim is marked `PASS` / `VALIDATED` without machine-readable evidence.

## Evidence States

```
OBSERVED → CORRELATED → HYPOTHESIS → VALIDATED
                                 ↘ UNKNOWN — HUMAN REVIEW REQUIRED
```

## Core API

```python
from x4_evidence import EvidenceLedger, Claim, EvidenceStatus

ledger = EvidenceLedger(min_evidence=2)

claim = Claim(claim="Deployment succeeded", status=EvidenceStatus.HYPOTHESIS)
claim.add_evidence("deployment_id", "dep_abc123")
claim.add_evidence("health_check", "200 OK")
claim.add_evidence("smoke_test", "all green")

result = ledger.validate(claim)
assert result.status == EvidenceStatus.VALIDATED
```

## Principles

- Execution ≠ Success
- Every important claim carries an evidence object
- Timestamps, sources, and verifier identity are recorded
- `UNKNOWN` is a first-class state, never silently upgraded

## Integration

Sits after the agent loop and before any “done” status is emitted.

Part of the [X4 / ARIEX4Ops](https://github.com/dhe-cruzer69) portfolio.

Apache-2.0
