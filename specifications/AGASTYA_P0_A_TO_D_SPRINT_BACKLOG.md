# AGASTYA P0-A to P0-D — Estimated Sprint Backlog

**Status:** Proposed execution backlog  
**Scope:** P0-A through P0-D from `SPEC-PLATFORM-001`  
**Estimation unit:** Ideal engineering days (IED)  
**Planning model:** One senior full-stack engineer; two-week sprints; 10 IED capacity per sprint.

---

## 1. Estimation basis

These are planning estimates rather than delivery commitments. They include implementation, automated tests, local technical documentation and review-ready code for each backlog item. They exclude the later P0-E through P0-G workstreams: extended audit/evidence functionality, API/CLI/Studio completion, broad hardening and release readiness.

| Assumption | Planning consequence |
|---|---|
| `SPEC-PLATFORM-001` is approved | Workstream P0-A can begin immediately. |
| `SPEC-PLATFORM-002` remains proposed | P0-B may begin only after an Owner approves the workspace role model and ownership-transfer policy. |
| Identity integration exists | Server-side handlers receive a verified principal ID and tenant context. |
| P0 architecture | Modular monolith, relational authoritative store, JSON Schema Draft 2020-12 validation. |
| Risk reserve | A 20% reserve protects against identity, migration, schema edge-case and concurrency uncertainty. |

| Workstream | Effort |
|---|---:|
| **P0-A — Foundation and development controls** | 5.0 IED |
| **P0-B — Workspace, identity and authorisation** | 9.0 IED |
| **P0-C — Canonical schema and validation engine** | 10.0 IED |
| **P0-D — Revision and approval lifecycle** | 12.5 IED |
| **Core total** | **36.5 IED** |
| **20% risk reserve** | **7.3 IED** |
| **Planning envelope** | **43.8 IED** |

This produces **four implementation sprints plus one protected contingency/integration sprint** at one primary engineer and 10 IED per sprint. [1] [2]

---

## 2. Sprint plan

| Sprint | Goal | Planned work | Core effort | Exit criterion |
|---|---|---|---:|---|
| **Sprint 1** | Engineering controls and durable workspace foundation. | P0-A01–A05; P0-B01–B02 | 8.5 IED | Quality gates, module boundaries, accepted P0 data decisions, project/membership persistence and role matrix exist. |
| **Sprint 2** | Verified workspace scope and schema identity. | P0-B03–B05; P0-C01–C02 | 8.5 IED | Authorised project scope, membership management, schema registry and deterministic content hash work. |
| **Sprint 3** | Persistent validation and authoritative tables. | P0-C03–C06; P0-D01 | 9.5 IED | Structural/semantic validation findings persist against exact revisions; migration rehearsal passes. |
| **Sprint 4** | Immutable revision control and approval. | P0-D02–D06 | 10.0 IED | Valid revisions can be created, approved, rejected, superseded and deterministically compared. |
| **Sprint 5** | Quality protection and risk absorption. | Critical fixes, integration evidence and deferred A–D work only. | 7.3 IED reserve | A–D completion gate passes with no unresolved critical/high defect. |

> **Sprint 1 governance gate:** `SPEC-PLATFORM-002` must receive Owner approval before implementation begins on P0-B01. Its scope includes the Owner / Editor / Viewer capability matrix and sole-Owner transfer rule.

---

## 3. Detailed backlog — P0-A: Foundation and development controls

| ID | Backlog outcome | Dependencies | Estimate | Sprint | Completion evidence |
|---|---|---|---:|---:|---|
| **P0-A01** | Establish formatting, linting, type-checking, test runner, dependency policy and commit-SHA CI checks. | None | 1.0 | 1 | A clean branch passes all mandatory checks and CI reports against a commit SHA. |
| **P0-A02** | Establish modules for workspace/auth, specification domain, validation, audit, API, CLI and UI. | P0-A01 | 1.5 | 1 | Dependency rule proves UI/API code cannot directly mutate persistence. |
| **P0-A03** | Define API versioning, error envelope, correlation ID and idempotency conventions. | P0-A01 | 1.0 | 1 | Contract fixture confirms a stable error structure on representative failures. |
| **P0-A04** | Implement typed configuration, secret references and log-redaction standards. | P0-A01 | 0.75 | 1 | Missing required configuration fails safely; secret-redaction test passes. |
| **P0-A05** | Accept ADRs for canonical JSON, relational authority, immutability, audit retention and migration. | P0-A02 | 0.75 | 1 | Required ADRs are accepted and trace to `SPEC-PLATFORM-001`. |

**P0-A total: 5.0 IED.**

P0-A is a technical control gate rather than optional preparation. P0-A02 and P0-A05 prevent later API or UI code from bypassing domain lifecycle and persistence protections.

---

## 4. Detailed backlog — P0-B: Workspace, identity and authorisation

| ID | Backlog outcome | Dependencies | Estimate | Sprint | Completion evidence |
|---|---|---|---:|---:|---|
| **P0-B01** | Implement Project and ProjectMembership persistence, constraints and repositories. | P0-A02, P0-A05, `SPEC-PLATFORM-002` approval | 2.0 | 1 | Migrations create project/membership tables; integration tests prove constraints and ownership. |
| **P0-B02** | Encode Owner, Editor and Viewer server-side capability policy. | P0-B01 | 1.5 | 1 | Fixed role matrix and unit tests cover every capability. |
| **P0-B03** | Build verified principal, tenant and request-correlation context for server handlers. | P0-B02, P0-A03 | 1.5 | 2 | Unauthenticated requests return `401`; handlers receive trusted identity context. |
| **P0-B04** | Enforce project scope on all resource queries and commands. | P0-B03 | 2.5 | 2 | Two-project matrix proves cross-project reads, writes and approvals are denied and audited. |
| **P0-B05** | Implement membership grant/revoke/role change and last-Owner protection. | P0-B04 | 1.5 | 2 | Owner continuity, membership changes and denial audit events are proven by integration tests. |

**P0-B total: 9.0 IED.**

The implementation must authorise inside the same server-side resource-access path used for persistence. It must not fetch a globally addressed specification and attempt authorisation only after the data is loaded.

---

## 5. Detailed backlog — P0-C: Canonical schema and validation engine

| ID | Backlog outcome | Dependencies | Estimate | Sprint | Completion evidence |
|---|---|---|---:|---:|---|
| **P0-C01** | Create a schema registry keyed by immutable `schema_version`. | P0-A05 | 1.5 | 2 | Schema `1.0.0` loads; unknown versions fail; all valid supplied instances pass. |
| **P0-C02** | Implement deterministic JSON canonicalisation and SHA-256 content hashing. | P0-C01 | 1.5 | 2 | Equivalent JSON produces stable canonical bytes and hash across repeated runs. |
| **P0-C03** | Map JSON Schema failures to stable rule IDs, severities and JSON Pointer paths. | P0-C01 | 2.5 | 3 | Invalid fixtures return actionable, deterministic field-level findings. |
| **P0-C04** | Implement semantic rules for internal references, lifecycle blockers, assumptions, versions and provenance. | P0-C02, P0-C03 | 3.0 | 3 | Passing, failing and boundary unit tests exist for each semantic rule. |
| **P0-C05** | Persist validator-versioned validation runs and immutable findings. | P0-C04, P0-D01 | 1.0 | 3 | Repeated runs retain their own outcomes against an exact revision/hash. |
| **P0-C06** | Expose the shared validation command/API contract. | P0-C05, P0-B04 | 0.5 | 3 | API and CLI output the same finding IDs for the same revision. |

**P0-C total: 10.0 IED.**

The supplied canonical schema already validates all current example and instance documents. P0-C converts this schema into governed application behaviour through deterministic content identity, validation persistence and semantic domain checks.

---

## 6. Detailed backlog — P0-D: Specification aggregate, revision and approval lifecycle

| ID | Backlog outcome | Dependencies | Estimate | Sprint | Completion evidence |
|---|---|---|---:|---:|---|
| **P0-D01** | Create authoritative specification, revision, approval and governance storage migrations. | P0-A05, P0-B01 | 2.5 | 3 | Migration rehearsal preserves representative data and content hashes. |
| **P0-D02** | Implement Specification aggregate for draft creation, copy-on-write revision, archive and supersede commands. | P0-D01, P0-C02 | 3.5 | 4 | Invalid transitions fail; a later revision never alters prior approved content. |
| **P0-D03** | Implement semantic version allocation, parent links and change-rationale requirement. | P0-D02 | 1.0 | 4 | Duplicate/non-monotonic versions fail; parent and reason are persisted. |
| **P0-D04** | Implement atomic approval transaction with Owner recheck, expected hash check and blocker recheck. | P0-B04, P0-C05, P0-D02 | 3.0 | 4 | Stale/modified revisions cannot be approved; a successful approval is immutable and audited. |
| **P0-D05** | Persist rejection and changes-requested outcomes without creating false authority. | P0-D04 | 1.0 | 4 | Rejected revisions remain retrievable but cannot be presented as approved. |
| **P0-D06** | Create deterministic JSON Pointer/JSON Patch-style revision diff with safe log redaction. | P0-D02 | 1.5 | 4 | Repeated comparisons return identical changes; logs exclude sensitive paths. |

**P0-D total: 12.5 IED.**

The P0-D04 approval command is the critical control point. It must run as a transaction: authorise the current Owner, recheck the exact hash the Owner reviewed, reject unresolved blocker findings, commit the approval record, and only then update the active revision pointer and supersede the earlier version.

---

## 7. Critical path and A–D exit gate

```text
P0-A02 / P0-A05
      ↓
P0-B01 / P0-B04
      ↓
P0-C01 / P0-C02 / P0-C04 / P0-C05
      ↓
P0-D01 / P0-D02 / P0-D04
```

| Gate | Evidence required |
|---|---|
| **Authorisation** | Full Owner/Editor/Viewer/non-member two-project test matrix passes. |
| **Canonical integrity** | Schema registry, canonicalisation and hash test evidence passes for all provided documents. |
| **Validation integrity** | Structural and semantic findings are deterministic and retained against exact revisions. |
| **Revision integrity** | Approved content cannot be overwritten; later changes create linked copy-on-write revisions. |
| **Approval integrity** | Only an active Owner can approve a current, valid, blocker-free revision. |
| **Auditability** | Create, validate, approve, deny, revise and diff operations are reconstructable from audit records. |

After this gate, the next planned P0 work is P0-E audit/evidence expansion, P0-F API/CLI/Studio delivery and P0-G hardening/release readiness. Those items are intentionally outside this estimate.

---

## References

[1] [SPEC-PLATFORM-001 — Canonical Specification Core](file:///Users/mohankrishnagundala/Documents/Agastya/specifications/SPEC-PLATFORM-001.md)
[2] [SPEC-PLATFORM-002 — Project Workspace Boundary](file:///Users/mohankrishnagundala/Documents/Agastya/specifications/SPEC-PLATFORM-002.md)
