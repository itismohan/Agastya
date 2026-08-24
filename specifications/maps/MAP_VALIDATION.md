# Map Export Validation

| Export | Validation result | Findings |
|---|---|---|
| `AGASTYA_APPROVED_PLATFORM_DEPENDENCY_DATA_FLOW.png` | Pass | Full approved-scope reference graph rendered successfully. It includes approved `SPEC-001` through `SPEC-011` and explicitly excludes draft `SPEC-012`. Its wide layout is best used as a zoomable reference. |
| `AGASTYA_APPROVED_PLATFORM_DEPENDENCY.png` | Pass | Readable dependency map rendered successfully. It shows the foundational model, governance, execution/delivery, Ledger, observability and HA/DR overlays. Minor long-edge crossings are expected in a complete cross-cutting dependency graph; node labels, arrowheads and recovery overlays remain legible. |

| `AGASTYA_APPROVED_PLATFORM_DATA_FLOW.png` | Pass | The revised top-to-bottom governed data-flow map rendered successfully at a practical landscape ratio. It makes the client → Gateway → policy/workspace/specification → orchestration/tool/Vault → Ledger → streaming → client path explicit, while preserving telemetry and HA/DR as dotted operational overlays. |

All three PNG exports and their deterministic Mermaid sources are ready for delivery. The full map is the zoomable reference; the dependency and data-flow maps are the day-to-day readable views.

## Coverage check

The consolidated source contains **all approved platform specifications `SPEC-001` through `SPEC-011`** as architecture nodes. Its sole `SPEC-012` reference is the explicit scope annotation that marks the draft compliance/data-residency specification as excluded from the approved-only architecture. File existence and deterministic source/PNG export checks passed.
