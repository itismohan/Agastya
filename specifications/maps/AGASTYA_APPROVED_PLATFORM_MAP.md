# AGASTYA — Consolidated Approved Platform Dependency & Data-Flow Map

| Field | Value |
|---|---|
| **Scope** | Approved platform specifications `SPEC-PLATFORM-001` through `SPEC-PLATFORM-011` |
| **Excluded** | `SPEC-PLATFORM-012` is still **DRAFT** and is intentionally excluded from the maps. |
| **Map types** | One consolidated reference map; one readable dependency map; one readable governed data-flow map. |
| **Source of truth** | The approved specification documents and canonical instances in `specifications/instances/`. |
| **Interpretation** | Solid arrows represent direct dependency, control or governed data movement. Dashed arrows represent operational telemetry or recovery-control overlay. |

> The **Event-Driven Audit & Evidence Ledger** is the durable evidence foundation, while the **API Gateway**, **RBAC Governance**, and **Workspace Boundary** are the principal access-control path. Operational telemetry is intentionally informative rather than authoritative, and HA/DR restores or validates the system without bypassing its trust boundaries.

## Export index

| File | Purpose |
|---|---|
| `AGASTYA_APPROVED_PLATFORM_DEPENDENCY_DATA_FLOW.mmd` | Full consolidated reference graph for all approved specifications. |
| `AGASTYA_APPROVED_PLATFORM_DEPENDENCY_DATA_FLOW.png` | Rendered full reference graph. |
| `AGASTYA_APPROVED_PLATFORM_DEPENDENCY.mmd` | Readable dependency-focused graph. |
| `AGASTYA_APPROVED_PLATFORM_DATA_FLOW.mmd` | Readable governed data-flow graph. |

## Approved specification responsibilities

| Spec | Layer | Primary responsibility | Key downstream relationships |
|---|---|---|---|
| **001** | Canonical Specification Core | Versioned engineering intent, requirements, approval and traceability model. | Supplies approved specification/revision context to orchestration; writes traceability and approval evidence. |
| **002** | Project Workspace Boundary | Tenant/project isolation and baseline membership boundary. | Supplies exact project context to API, specifications and orchestration. |
| **003** | Multi-Agent Orchestration | Durable governed agent planning, task execution and approval-gated actions. | Consumes approved specs and policy; invokes tools; writes task evidence. |
| **004** | Audit & Evidence Ledger | Append-only evidence, source events, outbox and reconstruction layer. | Receives material evidence from all platform boundaries; emits safe events to streaming. |
| **005** | Secure Credential & Secret Vault | Opaque, scoped secret/credential lease boundary. | Serves tool runtime only through brokered purpose-bound leases; records lifecycle evidence. |
| **006** | Plugin & Tool Extension Runtime | Signed, capability-bounded tool execution. | Receives orchestration grants, requests Vault leases, writes invocation/containment evidence. |
| **007** | Unified API Gateway & Client SDK | Contract-first external boundary and authoritative resource access. | Resolves policy/project context, dispatches commands, returns operation resources and records material API evidence. |
| **008** | Real-Time Streaming | Authorised project-channel delivery, replay and resync. | Consumes Ledger outbox events; notifies clients; relies on API for authoritative re-read. |
| **009** | Enterprise Security & RBAC | Identity, capability, policy, separation-of-duties and privileged-access decisions. | Governs API, Vault, orchestration, tools and streaming; records every material decision. |
| **010** | Observability, Telemetry & Tracing | Safe correlated operational metrics, logs and traces. | Observes all boundaries; links safe operational references to evidence but never changes engineering truth. |
| **011** | High Availability & Disaster Recovery | Recovery profiles, fail-safe posture, restore/reconciliation and recovery evidence. | Restores trust/data/evidence first, then resumes API, execution and streaming safely. |

## Governing control path

The normal client path begins at the **Unified API Gateway**. The Gateway requests identity, scope, action and context evaluation from **Enterprise Security & RBAC**, then binds the request to the **Project Workspace Boundary**. Only an allowed or explicitly approval-gated request may query or command the **Canonical Specification Core** or create a durable operation.

| Stage | Control question | Enforced by |
|---|---|---|
| Authentication and API contract | Who is calling, through which supported boundary, using which versioned contract? | API Gateway (007) |
| Tenant/project isolation | Which exact tenant/project and resource boundary applies? | Workspace (002) plus RBAC (009) |
| Policy decision | Is the requested action allowed, denied or waiting approval under current role, capability and context? | RBAC Governance (009) |
| Sensitive secret use | Does a registered tool need a scoped purpose-bound lease, without agent plaintext access? | Vault (005) plus Tool Runtime (006) |
| Durable proof | What command, policy decision, output, approval or recovery outcome must be reconstructable? | Evidence Ledger (004) |

## Governed engineering data flow

```text
Client request
  → API Gateway
  → RBAC policy decision
  → Project workspace and specification command/query
  → Approved specification context
  → Agent orchestration
  → Capability-bounded tool runtime
  → Opaque Vault lease, if policy permits
  → Durable task/tool/API/policy evidence in Ledger
  → Safe outbox event
  → Authorised WebSocket subscription
  → Client notification

The client returns to the API Gateway to re-read authoritative operation/resource state.
```

The streamed notification is intentionally **not** the source of truth. It identifies a scoped state change and safe cursor/reference; the versioned API resource and the Ledger remain authoritative.

## Operational and recovery overlays

| Overlay | Flow | Boundary preserved |
|---|---|---|
| **Telemetry** | Gateway, policy, orchestration, tool, Vault, Ledger and streaming emit safe correlation/operational signals to Observability. | Telemetry may reference evidence but does not establish verification/approval truth. |
| **Recovery** | HA/DR restores/validates policy and key readiness, authoritative data, Ledger integrity, outbox/consumer state, then API/execution/streaming. | Required unavailable controls fail safe; recovery cannot use implicit privilege or invent ledger/task state. |
| **Evidence** | Material commands, decisions, lease lifecycle, invocation outcomes, recovery actions and exercise results append to Ledger. | Evidence is project-scoped, immutable and linked through correlation/causation context. |

## Approved dependency order

The dependency order for implementation planning is **001 → 002 → 004 → 009 → 005 → 007 → 003 → 006 → 008 → 010 → 011**. This is a control/dependency sequence, not a statement that every service must be deployed at the same time. It reflects the fact that specifications, project isolation, evidence and policy must exist before tools, external interfaces, streaming and operational resilience are enabled.

## Deferred scope

`SPEC-PLATFORM-012 — Enterprise Compliance & Data Residency Layer` remains draft. It will become an additional cross-cutting policy overlay after approval, governing data inventory, classification, residency profiles, processors/egress, retention, hold, deletion and recovery reactivation. It is excluded from this approved-only map by design.

## References

[1] [SPEC-PLATFORM-001 — Canonical Specification Core](file:///Users/mohankrishnagundala/Documents/Agastya/specifications/SPEC-PLATFORM-001.md)
[2] [SPEC-PLATFORM-004 — Event-Driven Audit & Evidence Ledger](file:///Users/mohankrishnagundala/Documents/Agastya/specifications/SPEC-PLATFORM-004.md)
[3] [SPEC-PLATFORM-007 — Unified API Gateway & Client SDK Layer](file:///Users/mohankrishnagundala/Documents/Agastya/specifications/SPEC-PLATFORM-007.md)
[4] [SPEC-PLATFORM-009 — Enterprise Security & RBAC Governance Layer](file:///Users/mohankrishnagundala/Documents/Agastya/specifications/SPEC-PLATFORM-009.md)
[5] [SPEC-PLATFORM-011 — High-Availability & Disaster Recovery Layer](file:///Users/mohankrishnagundala/Documents/Agastya/specifications/SPEC-PLATFORM-011.md)
