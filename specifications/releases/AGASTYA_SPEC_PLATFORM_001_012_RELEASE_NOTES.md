# AGASTYA Platform Specification Suite — Release Notes

| Field | Release summary |
|---|---|
| **Release scope** | `SPEC-PLATFORM-001` through `SPEC-PLATFORM-012` |
| **Release type** | **Specification baseline** — a governed platform design release, not a production-runtime release |
| **Authoritative artifacts** | Canonical JSON Schema, versioned specification instances, detailed design documents, dependency/data-flow maps, and validation utility |
| **Status at release** | `001–011` are approved for their stated design boundaries; `012` remains a draft pending specialist approval. |
| **Core principle** | Intent, policy, evidence and production reality remain traceably connected; generated code or agent output is never accepted as truth by assertion alone. [1] |

> **Release outcome:** AGASTYA now has an end-to-end specification architecture for governed AI-native engineering: from project-scoped intent and execution, through evidence, security, API and streaming, to observability, resilience and enterprise data governance.

## Executive summary

This release establishes the **platform control plane** needed to make AI-assisted software delivery traceable and governable. The core foundation defines a canonical specification model and strict project boundary. The execution plane introduces policy-gated multi-agent orchestration and extension tooling. The evidence, security and API layers ensure that material actions are authenticated, authorised, reconstructable and safely exposed to clients. The final operational layers define observability, disaster recovery, and draft compliance/data-residency controls. [1] [2] [3]

| Capability family | Included specifications | Primary release value |
|---|---|---|
| **Intent and scope** | 001, 002 | A versioned source of engineering intent within an exact tenant/project boundary. |
| **Execution and extensibility** | 003, 006, 008 | Controlled agent work, bounded tools, and authorised real-time client notifications. |
| **Trust and protection** | 004, 005, 009 | Immutable evidence, opaque secret handling, and enterprise policy enforcement. |
| **Platform access** | 007 | A secure versioned API and SDK contract for product and integration clients. |
| **Operational assurance** | 010, 011 | Correlated telemetry and evidence-backed continuity/recovery design. |
| **Enterprise governance** | 012 | A draft policy layer for classification, residency, retention and deletion governance. |

## Highlights

The suite introduces a **canonical specification system** with lifecycle status, requirements, architecture decisions, verification mappings, provenance and traceability. `SPEC-PLATFORM-001` is the authoritative model that every later specification extends. `SPEC-PLATFORM-002` adds project-scoped ownership, membership and resource isolation; together they make intent and access context explicit before execution begins. [1] [2]

The **governed execution model** is defined by `SPEC-PLATFORM-003`, `005`, `006` and `009`. Agents receive only bounded tasks and policy-granted capability; tool execution is mediated by signed manifests and a restricted runtime; secret values remain outside agent context and are served by opaque, purpose-bound leases. Every material decision, task, invocation and lease lifecycle transition produces durable evidence. [3] [5] [6] [9]

The **operational model** joins the Evidence Ledger, Gateway, streaming layer, telemetry and HA/DR design. API commands produce durable state and evidence; safe Ledger events are distributed through authorised channels; clients re-read authoritative resources through the API. Telemetry adds correlation and operational evidence but does not replace the approved specification or verification truth. [4] [7] [8] [10] [11]

## Specification-by-specification release notes

| ID | Status | Released design capability | Key governance boundary | Source |
|---|---|---|---|---|
| **001** | Approved `v1.0.0` | **Canonical Specification Core** with versioned intent, requirements, rules, architecture, verification and traceability. | Specifications, not code or AI assertions, are the primary expression of intended behaviour. | [1] |
| **002** | Approved `v1.0.0` | **Project Workspace Boundary** with Owner, Editor and Viewer scope, membership and project isolation. | Every resource/action is bound to an exact project; sole-Owner transfer is explicit and atomic. | [2] |
| **003** | Approved detailed design `v0.1.0` | **Multi-Agent Orchestration** with durable plans/tasks, policy-before-dispatch, approvals, budgets and evidence. | No autonomous change, external provider use or tool-enabled execution is authorised without its stated child gates. | [3] |
| **004** | Approved detailed design `v0.1.0` | **Event-Driven Audit & Evidence Ledger** with append-only records, integrity controls, outbox and rebuildable projections. | Corrections supersede rather than mutate evidence; event delivery is governed and idempotent. | [4] |
| **005** | Approved detailed design `v0.1.0` | **Credential & Secret Vault** with provider-managed encryption, opaque short-lived leases, rotation and revocation. | Secrets must not enter agent context, client responses, logs, Ledger payloads or tool outputs. | [5] |
| **006** | Approved detailed design `v0.1.0` | **Plugin & Tool Extension Runtime** with immutable manifests, trust validation, sandboxing and capability grants. | Read-only signed internal extension planning is the only permitted initial scope; no third-party package or write path is enabled. | [6] |
| **007** | Approved detailed design `v0.1.0` | **Unified API Gateway & Client SDK** using a contract-first `/api/v1` boundary, idempotency, concurrency and durable operations. | Project scope and policy decisions are enforced centrally; public exposure and SDK publication remain gated. | [7] |
| **008** | Approved detailed design `v0.1.0` | **Real-Time Streaming & WebSocket Subscriptions** with authorised channels, bounded replay, resync and backpressure. | Streams are notifications, not source of truth; API resources and Ledger events remain authoritative. | [8] |
| **009** | Approved detailed design `v0.1.0` | **Enterprise Security & RBAC Governance** with scoped roles, contextual policy, separation of duties and privileged-access controls. | Policy enforcement points default to deny and apply to API, agents, tools, Vault and streaming. | [9] |
| **010** | Approved detailed design `v0.1.0` | **Observability, Telemetry & Distributed Tracing** with safe correlated signals, SLO/SLI boundaries and evidence references. | Telemetry is informative operational evidence, not approval, verification or specification truth. | [10] |
| **011** | Approved detailed design `v0.1.0` | **High Availability & Disaster Recovery** with tiered recovery profiles, restore validation, reconciliation and recovery evidence. | Recovery preserves trust boundaries and requires defined business-risk objectives before production commitments. | [11] |
| **012** | **Draft** `v0.1.0` | **Enterprise Compliance & Data Residency** covering classification, location, lifecycle, retention, hold, deletion and egress governance. | It makes no legal/certification claim and requires specialist approval before commitments or production policy settings. | [12] |

## Architecture and data-flow impact

The release formalises a single governed path: client requests enter through the API Gateway, are scoped by Workspace and evaluated by Enterprise RBAC, then query or change the Specification Core. Approved specifications can inform orchestration; orchestration delegates only policy-scoped tool invocations; tools obtain an opaque Vault lease only when needed. Material actions become Ledger evidence, and safe project-scoped events become streaming notifications. [2] [3] [4] [5] [6] [7] [8] [9]

| Architectural rule | Release consequence |
|---|---|
| **Policy before dispatch** | No agent task, tool capability, secret lease, stream subscription or material API action should bypass a context-specific decision. |
| **Ledger as durable proof** | Material state changes and governed decisions must be reconstructable from append-only evidence rather than inferred from logs. |
| **API and Ledger authority** | Streaming accelerates awareness; it does not replace authoritative resource reads or evidence records. |
| **Telemetry is safe and secondary** | Trace/log/metric signals are correlated to operational context but cannot establish requirement satisfaction on their own. |
| **Recovery is governed work** | Restore, failover and reconciliation actions create evidence and must re-establish control-plane integrity before normal writes resume. |

## Approval state and delivery gates

The release approves detailed design; it does **not** approve unrestricted runtime deployment. The following gates remain deliberately active.

| Gate | Why it remains active | Affected specifications |
|---|---|---|
| **Infrastructure and provider ADRs** | Storage, queue, runtime, secret-provider, identity-provider and telemetry-provider choices must be assessed against security and operational needs. | 003–011 |
| **Policy and identity child contracts** | Authentication, workloads, step-up, privileged access and enforcement-point implementation require explicit contracts. | 005, 007, 009 |
| **External execution controls** | External model providers, write-capable tools, third-party packages, egress and production secret usage require independent approval. | 003, 005, 006, 012 |
| **Operational commitments** | SLOs, RTO/RPOs, retention, alert routing, regional recovery and recovery exercises need quantified business-risk decisions. | 010, 011, 012 |
| **Legal, privacy and commercial review** | Residency, processor, transfer, retention and deletion commitments require qualified stakeholder approval. | 012 |

## Recommended next release sequence

The next delivery release should create and approve the lowest-level implementation contracts before building runtime services. The logical order remains: Canonical Specification Core and Workspace Boundary; Ledger and RBAC; Vault and Gateway; Orchestration and Tool Runtime; Streaming; Observability; HA/DR; then Compliance/Data Residency as its specialist governance profile. This is a dependency order, not a promise of simultaneous production rollout. [1] [2] [4] [5] [7] [9] [10] [11] [12]

## Release artifacts

| Artifact | Location |
|---|---|
| Canonical JSON Schema | `specifications/schemas/agastya-canonical-specification.schema.json` |
| Canonical specification instances | `specifications/instances/` |
| Detailed platform specifications | `specifications/SPEC-PLATFORM-001.md` through `SPEC-PLATFORM-012.md` |
| Dependency/data-flow maps | `specifications/maps/` |
| Schema-validation utility | `specifications/validate_examples.py` |

## References

[1] [SPEC-PLATFORM-001 — Canonical Specification Core](../SPEC-PLATFORM-001.md)
[2] [SPEC-PLATFORM-002 — Project Workspace Boundary](../SPEC-PLATFORM-002.md)
[3] [SPEC-PLATFORM-003 — Multi-Agent Orchestration Layer](../SPEC-PLATFORM-003.md)
[4] [SPEC-PLATFORM-004 — Event-Driven Audit & Evidence Ledger](../SPEC-PLATFORM-004.md)
[5] [SPEC-PLATFORM-005 — Secure Credential & Secret Vault Layer](../SPEC-PLATFORM-005.md)
[6] [SPEC-PLATFORM-006 — Plugin & Tool Extension Runtime](../SPEC-PLATFORM-006.md)
[7] [SPEC-PLATFORM-007 — Unified API Gateway & Client SDK Layer](../SPEC-PLATFORM-007.md)
[8] [SPEC-PLATFORM-008 — Real-Time Streaming & WebSocket Subscriptions Layer](../SPEC-PLATFORM-008.md)
[9] [SPEC-PLATFORM-009 — Enterprise Security & RBAC Governance Layer](../SPEC-PLATFORM-009.md)
[10] [SPEC-PLATFORM-010 — Observability, Telemetry & Distributed Tracing Layer](../SPEC-PLATFORM-010.md)
[11] [SPEC-PLATFORM-011 — High Availability & Disaster Recovery Layer](../SPEC-PLATFORM-011.md)
[12] [SPEC-PLATFORM-012 — Enterprise Compliance & Data Residency Layer](../SPEC-PLATFORM-012.md)
