# AGASTYA — Specification-Driven Delivery Roadmap (P0–P3)

**Author:** Manus AI  
**Status:** Proposed roadmap  
**Source of direction:** `README.md`  
**Purpose:** Sequence AGASTYA into four releasable product increments that build the specification-first core before advanced autonomy, enterprise governance, and ecosystem features.

---

## 1. Product delivery thesis

AGASTYA must be built as the product it promises to be: a **specification-driven engineering control plane**, not a code-generation interface. Each product increment should therefore be governed by an approved, versioned specification; implemented through explicit contracts; verified independently; linked to evidence; and released only when its defined quality gate is satisfied.

> “Code is not the source of truth. The specification represents intended behavior. Implementation is a realization of the specification. Tests provide evidence. Production telemetry provides runtime evidence.” [1]

The roadmap preserves the mandatory strategic order stated in the product specification: **Specification Core → Living Specification Graph → Verification → SRS → Drift → Change Impact → Agent Control Plane → Brownfield Intelligence → Enterprise Governance → Open Ecosystem**. It deliberately avoids building a broad agent marketplace, unrestricted autonomy, or provider-specific product logic before the core engineering intelligence is proven valuable. [1]

| Priority | Release intent | Commercial / product outcome |
|---|---|---|
| **P0** | Establish the authoritative specification foundation and internal engineering discipline. | A team can create, validate, approve, version, and audit a governing specification. |
| **P1** | Deliver the first trusted vertical slice from specification to evidence. | A team can link a specification to a repository, verify a bounded change, and understand conformance. |
| **P2** | Deliver the flagship differentiation: drift, impact, controlled AI execution, and brownfield understanding. | A team can safely assess and execute change in an existing system with evidence-backed release readiness. |
| **P3** | Harden AGASTYA for enterprise scale, continuous verification, and extensibility. | An organisation can govern AI-native engineering across teams, environments, providers, and domains. |

---

## 2. Common specification-driven delivery rules

No item may enter implementation merely because it appears on a backlog. Every P0–P3 work item must have a **parent specification ID**, a defined owner, acceptance criteria, risk classification, test requirements, architecture decision record (ADR) where material, and traceability links to its implementation and evidence.

| Delivery control | Required rule |
|---|---|
| **Specification state** | Work begins only after the governing specification moves from `DRAFT` through validation to `APPROVED`; exceptions must be recorded explicitly. |
| **Requirement quality** | Requirements must be unambiguous, testable, and connected to acceptance criteria, business rules, and applicable non-functional requirements. |
| **Traceability** | Each meaningful feature links: `Intent → Requirement → Specification → Architecture → Code → Test → Evidence`. |
| **Evidence** | Tests, validation results, security checks, and later production evidence are recorded as evidence—not assertions. |
| **Risk and approvals** | High-risk changes require impact analysis and human approval before implementation or release. |
| **Definition of done** | “Code compiles” and “tests pass” are insufficient. The feature must meet the AGASTYA definition of done: valid specification, contracts, implementation, verification, evidence, traceability, and no critical drift. [1] |

### Required spec pack for every increment

Each increment should begin with one **Release Specification** and several child specifications. The following minimum pack will make the program executable and auditable.

| Artifact | P0 requirement | P1–P3 evolution |
|---|---|---|
| `INTENT` | Defines the user problem, value hypothesis, success signal, and exclusions. | Updated only through governed change control. |
| `SPEC` | Contains functional and non-functional requirements, acceptance criteria, risks, assumptions, and dependencies. | Versioned and connected to implementation and runtime evidence. |
| `ADR` | Captures material architecture choices and trade-offs. | Required for boundary, data model, provider, and security decisions. |
| `CONTRACT` | Defines APIs, domain events, schemas, and user-facing behaviour. | Grows from REST contracts to events, streaming, webhooks, and async jobs. |
| `TEST-SPEC` | Defines expected functional, contract, security, accessibility, and performance evidence. | Becomes increasingly executable. |
| `EVIDENCE` | Records verification result, source, timestamp, version, confidence, and observed behaviour. | Incorporates CI/CD and production signals. |

---

# P0 — Specification Core and Engineering Foundation

## 3. Objective

P0 establishes the first **authoritative source of engineering intent**. It is the smallest usable product foundation on which every later AGASTYA capability depends. The P0 objective is not to analyse a repository or generate code; it is to enable a team to write, validate, approve, version, navigate, and audit a canonical specification.

At P0 completion, AGASTYA should credibly answer: **What are we trying to build, what has been approved, what remains unknown, and which version governs the work?**

## 4. In-scope capabilities

| Capability | P0 scope | Required evidence of completion |
|---|---|---|
| **Workspace and project boundary** | A minimal project workspace with user identity, project membership, and project-scoped data. Start with a simple role model: Owner, Editor, Viewer. | Cross-project access tests and audit records show isolation at the workspace level. |
| **Canonical specification model** | Store the versioned canonical schema from the README: intent, requirements, rules, constraints, assumptions, contracts, workflows, NFRs, risks, questions, traceability, evidence, and change history. | Schema validation tests; migration tests; an approved example specification. |
| **Specification Studio** | Structured editor with a Markdown/YAML mode, validation messages, open questions, assumptions, and acceptance criteria. The visual experience should remain calm, information-dense, and non-chatbot-like. | A user can author, validate, save, compare, and inspect a specification version. |
| **Specification lifecycle** | Implement `DRAFT → ANALYSING → PROPOSED → VALIDATING → APPROVED → IMPLEMENTING → VERIFYING → ACTIVE`; later states can be visible but deferred from complex workflow automation. | Illegal state-transition tests; a complete approval audit trail. |
| **Change control and diff** | Version every mutation, including before/after, reason, author, timestamp, risk, and approval. | Two versioned changes with a visible semantic diff and rollback-safe history. |
| **Specification validation** | Validate required fields, acceptance-criteria testability, referential integrity, unresolved questions, and basic contradiction rules. | Validation report identifies valid, blocked, and assumption-based sections correctly. |
| **Audit and evidence primitives** | Append-only audit-event model and evidence record model. | All specification creation, edits, validation, and approvals are reconstructable. |
| **Developer entry point** | `agastya init`, `agastya specify`, `agastya validate`, and `agastya status` commands, backed by stable API contracts. | CLI and web UI operate on the same domain model and API. |

## 5. Explicit P0 non-goals

P0 must **not** attempt a graph database, repository analysis, AI coding-agent orchestration, automated test execution, SRS, drift detection, multi-provider routing, CI/CD gates, production telemetry, marketplace, or advanced enterprise SSO. A design that anticipates these capabilities is valuable; an implementation that prematurely builds them is not.

## 6. P0 exit gate

P0 is complete only when a pilot user can create a project, author a canonical specification, resolve or explicitly record ambiguities, validate it, secure an approval, create a subsequent version with a clear diff, and retrieve the exact governing version through UI, CLI, and API. All essential flows must have automated tests and immutable audit evidence.

> **P0 product demo:** “Here is the approved, machine-readable engineering contract for a change; here are its assumptions, acceptance criteria, owner, approval, and complete version history.”

---

# P1 — Trusted Specification-to-Evidence Vertical Slice

## 7. Objective

P1 proves the platform’s central promise with a bounded, end-to-end workflow. A user connects one repository, maps a small but meaningful subset of artefacts to an approved specification, executes specification-derived verification, and receives an evidence-backed reliability result.

At P1 completion, AGASTYA should answer: **Does this bounded implementation satisfy this approved specification, and what evidence supports the answer?**

## 8. In-scope capabilities

| Capability | P1 scope | Required evidence of completion |
|---|---|---|
| **Repository connection** | Connect one Git provider and a repository through read-only access. Capture commit, branch, pull-request, and file metadata. | Connection permission boundary tests and a reproducible repository snapshot. |
| **Living Specification Graph v1** | Use an authoritative relationship layer to model Specification, Requirement, Contract, Component, File/Code unit, Test, Verification Run, and Evidence. Support `IMPLEMENTS`, `SATISFIES`, `VALIDATES`, `VERIFIES`, `DERIVED_FROM`, and `AFFECTS`. | Bidirectional traversal shows requirement-to-code-to-test-to-evidence and reverse navigation. |
| **Traceability workflow** | Allow manual and assisted linking of requirements to contracts, code units, and tests. Never claim a link is verified without evidence. | Link provenance, confidence, and source are visible; unsupported links are marked as proposals. |
| **Executable specification v1** | Support a deliberately narrow set of executable forms: API contracts such as OpenAPI/JSON Schema and behaviour examples such as Gherkin or structured acceptance criteria. | Contract validation and one behaviour-derived test are run against a sample service. |
| **Verification Engine v1** | Run configured unit, integration, API, and contract checks through an asynchronous job model. Store expected behaviour, observed behaviour, rule, status, timestamp, versions, and confidence. | A verification report persists correct passing, failing, and blocked outcomes. |
| **Evidence Fabric v1** | Ingest test execution and contract-validation outputs as immutable evidence linked to relevant graph nodes. | Evidence survives a refresh and is tied to a spec and implementation version. |
| **SRS v1** | Calculate an explainable score from only measured inputs: requirement coverage, contract compliance, test evidence, traceability, and freshness. Missing data lowers confidence rather than being fabricated. | Score breakdown, formula version, source evidence, and “unknown” dimensions are visible. |
| **Execution terminal** | Stream job status, validation events, warnings, and verification summaries to the UI without blocking the interaction flow. | Users can monitor queued, running, completed, failed, and blocked verification runs. |

## 9. P1 non-goals

P1 does not need full semantic code understanding, broad language support, autonomous agent execution, production deployment, a complete drift taxonomy, automatic change implementation, or a complete SRS across every README metric. It must be **accurate about its limited coverage**, rather than simulate broad intelligence.

## 10. P1 exit gate

Using a reference repository and a deliberately introduced contract or behaviour defect, the product must demonstrate this sequence:

```text
Approved specification → linked requirement and contract → repository revision
→ verification run → failing evidence → traceable explanation → evidence-backed SRS change
```

The score and verdict must identify coverage limitations. No element may be displayed as verified if its only source is an LLM assertion or a manually entered status without supporting evidence.

> **P1 product demo:** “This endpoint violates requirement R-014 / contract C-003 in commit `abc123`; the verification run and evidence are linked, and the reliability score changed for stated reasons.”

---

# P2 — Change Intelligence, Controlled AI Execution, and Brownfield Value

## 11. Objective

P2 delivers AGASTYA’s differentiation for real engineering teams: it turns the specification graph and evidence layer into a system for detecting drift, analysing the blast radius of change, coordinating bounded AI work, and understanding existing systems.

At P2 completion, AGASTYA should answer: **What will this change affect, what has drifted, what can an AI agent safely do, and is the release ready?**

## 12. In-scope capabilities

| Capability | P2 scope | Required evidence of completion |
|---|---|---|
| **Change Impact Engine v1** | From an approved specification change, traverse the graph to identify affected requirements, rules, contracts, code, tests, services, controls, and deployments. Produce risk and confidence. | Seeded changes report known downstream impact, unknown coverage, and human-approval requirements. |
| **Drift Engine v1** | Detect specification, contract, test, documentation, and architecture drift where reliable rules exist. Use `INFO` through `CRITICAL` severity. | Purposefully injected drift creates a linked, explainable drift finding with a reproducible rule. |
| **Brownfield Intelligence v1** | Analyse a connected repository for services, APIs, dependencies, entities, tests, and potentially undocumented behaviour. Generate proposed—not authoritative—specification content and graph links. | Findings are labelled with confidence and provenance; a human can approve, reject, or edit them. |
| **Agent Control Plane v1** | Register specialised agents, define tasks, permissions, risk, expected output, evidence, retry policy, and approval requirements. Start with one provider-neutral development/test adapter. | An agent task has a complete state history and cannot exceed granted tool or repository permissions. |
| **Controlled implementation workflow** | An approved, low-risk change can generate a proposed patch or pull request only after impact analysis and policy check. High-risk changes stop at a human approval gate. | End-to-end audit trail: approved spec → impact → agent task → proposed patch → tests → verification. |
| **Policy and approval gates v1** | Implement policies for critical drift, SRS threshold, agent permissions, protected branches, and release readiness. | A policy failure blocks a defined action and records reason, policy version, and approver where relevant. |
| **CI/CD integration v1** | Expose a check that reports specification compliance, selected SRS dimensions, critical drift count, and verification evidence for a pull request or pipeline. | A deliberately non-compliant change fails the quality gate. |
| **Release readiness v1** | Summarise functional verification, security/test evidence, drift, rollback plan reference, and required approvals. | Release cannot be marked ready while mandatory evidence is absent or critical drift exists. |

## 13. P2 non-goals

P2 must not grant unrestricted production access to agents, automatically deploy production changes, silently accept model-generated specifications, or treat repository inference as authoritative fact. It is also not the point to build every agent type, complete all programming-language parsers, or support every Git and CI provider.

## 14. P2 exit gate

A brownfield demonstration must connect a non-trivial application, propose an initial living specification, expose unknown behaviour, accept an approved business-rule change, calculate its impact, generate a bounded proposal through an approved agent task, verify the resulting patch, identify any remaining drift, and produce a defensible release-readiness decision.

> **P2 product demo:** “What happens if we make KYC mandatory?” becomes a governed impact report, a bounded implementation plan, a verified proposed change, and a release decision—not a blind code-generation request. [1]

---

# P3 — Enterprise Governance, Continuous Confidence, and Platform Extensibility

## 15. Objective

P3 turns the proven product into an enterprise platform capable of managing multiple projects, teams, environments, model providers, and continuously changing systems. The emphasis is trusted scale: robust tenancy, observability, resiliency, governance, integration breadth, and an extensible specification ecosystem.

At P3 completion, AGASTYA should answer: **Can the organisation consistently govern AI-native engineering across its portfolio, while maintaining continuous confidence and auditability?**

## 16. In-scope capabilities

| Capability | P3 scope | Required evidence of completion |
|---|---|---|
| **Enterprise tenant model** | Organisation, business unit, team, project, environment, scoped policies, and RBAC; introduce ABAC only for demonstrated policy needs. | Tenant-isolation, privilege-escalation, and scoped-policy test suites. |
| **Identity and security hardening** | Enterprise SSO, SCIM where required, secrets management, encryption, audit retention controls, dependency and supply-chain controls, and tool/agent authorisation. | Threat-model review, security verification evidence, and privileged-action audit trails. |
| **Continuous verification and freshness** | Scheduled or event-driven re-evaluation of code, tests, dependencies, infrastructure, runtime, and security evidence. Track `FRESH`, `AGING`, `STALE`, and `UNKNOWN`. | A changed dependency or production signal results in an updated freshness and verification state. |
| **Production evidence integration** | Connect deployments, logs, metrics, traces, incidents, and alerts to the graph. Production evidence may recommend curation but never silently rewrites authoritative intent. | An incident is traceable to affected requirements and produces a governed curation recommendation. |
| **Provider orchestration and AI FinOps** | Multi-provider model routing based on task complexity, latency, cost, privacy, context, reliability, and policy. Track model use, cost, quality, and failures. | Routing decisions, costs, and policy overrides are observable and auditable. |
| **Platform resilience and observability** | Durable async workflows, queues, retries, idempotency, cancellation, backoff, dead-letter handling, distributed tracing, and operational dashboards. | Failure-injection tests prove that a provider or worker failure does not lose task state or corrupt evidence. |
| **Integration and domain extensibility** | Additional Git/CI/CD/observability adapters; domain specification packs; initial provider-neutral ASF repository layout and import/export. | A domain pack contributes validated rules and tests without changing the core domain model. |
| **Executive engineering health** | Organisation-level health dashboard for SRS, coverage, drift, verified change rate, agent success, cost, approval rate, and defect leakage. | Each metric has a documented formula, data lineage, freshness state, and drill-down evidence. |

## 17. P3 non-goals

A public marketplace should not precede proven domain-pack and integration extensibility. Fully autonomous production deployment is not a default goal; autonomy remains policy-scoped, risk-aware, and approval-bound. The platform must not expose private model reasoning as an audit substitute; it should retain concise rationale and verifiable evidence.

## 18. P3 exit gate

P3 is complete when a multi-team organisation can enforce scoped engineering policies, operate multiple provider adapters without core lock-in, receive continuous conformance and drift signals, trace a production incident back through evidence to intent, approve a curation change, and prove tenant-scoped auditability and resilience under operational failure.

> **P3 product demo:** “Our engineering portfolio is healthy because these specifications are fresh, these changes are verified, these risks are controlled, these policy exceptions are explicit, and this production evidence is connected to the governing intent.”

---

## 19. Dependency and sequencing map

```text
P0: Canonical specification + lifecycle + validation + audit
  ↓
P1: Graph v1 + repository link + executable contracts + verification + SRS v1
  ↓
P2: Drift + impact + brownfield proposals + governed agent work + CI/release gate
  ↓
P3: Enterprise tenant/governance + continuous verification + production evidence + extensibility
```

| Capability | Earliest safe priority | Why it cannot move earlier |
|---|---:|---|
| Canonical specification and approval | P0 | Later graph, agent, and verification features require an authoritative object to govern. |
| Repository traceability graph | P1 | The graph must relate to stable versioned specifications and artefact identifiers. |
| Reliability score | P1 | It must be derived from actual verification and traceability evidence, not estimates. |
| Drift detection | P2 | It requires a baseline of specification, implementation, test, and evidence relationships. |
| AI implementation agent | P2 | The agent needs specifications, risk classification, permissions, approvals, and verification. |
| Brownfield analysis | P2 | Its output must enter as proposed information into the P0/P1 governance and graph model. |
| Continuous production reconciliation | P3 | It requires mature security, integrations, evidence provenance, and operational resilience. |
| Marketplace / ecosystem | Post-P3 | The core format, domain-pack model, and product value must first be proven. |

---

## 20. First execution recommendation

Begin with **P0 / SPEC-PLATFORM-001: Canonical Specification Core**. Do not open a broad technical implementation backlog yet. First produce and approve the following child specifications:

| First specification | Governs | First decision required |
|---|---|---|
| `SPEC-PLATFORM-001` | Canonical Specification Core | What is the minimal authoritative schema and its versioning contract? |
| `SPEC-PLATFORM-002` | Project and workspace boundary | What data is project-scoped, and what role model is mandatory on day one? |
| `SPEC-PLATFORM-003` | Specification lifecycle and approval workflow | Which transitions, approvers, and exceptions are supported in P0? |
| `SPEC-PLATFORM-004` | Studio and validation experience | How are structured, Markdown, and YAML representations kept consistent? |
| `SPEC-PLATFORM-005` | Audit, evidence, and traceability primitives | What is immutable, what is versioned, and what evidence metadata is required? |
| `SPEC-PLATFORM-006` | P0 API and CLI contracts | Which stable API resources and commands are public from the first release? |
| `ADR-001` | Authoritative data-model boundary | How authoritative relational state, artefacts, and future graph relations are separated. |
| `TEST-SPEC-P0-001` | P0 verification plan | Exact acceptance, security, lifecycle, and audit tests required for the P0 exit gate. |

The first development cycle should implement one thin vertical slice: **create a project → author a draft specification → validate → approve → version the specification → view audit and diff → retrieve it through API and CLI**. This is the smallest increment that both delivers product value and proves AGASTYA is being built according to its own specification-first philosophy.

---

## 21. Roadmap health metrics

Roadmap progress should be assessed by verified outcomes, not completed tickets or generated lines of code.

| Metric | P0 target | P1 target | P2 target | P3 target |
|---|---:|---:|---:|---:|
| Approved feature specifications | 100% of P0 scope | 100% of P1 scope | 100% of P2 scope | 100% of P3 scope |
| Acceptance criteria with automated evidence | ≥ 80% | ≥ 85% | ≥ 90% | ≥ 95% |
| Traceability coverage | Spec-to-acceptance | Requirement-to-test | Requirement-to-code-to-evidence | Portfolio and runtime traceability |
| SRS reporting | Not applicable | Evidence-backed limited dimensions | Expanded with drift/impact evidence | Fresh, continuously updated organisation view |
| Critical ungoverned changes | 0 | 0 | 0 | 0 |
| AI task actions outside policy | 0 | 0 | 0 | 0 |

---

## 22. Decision

The proposed sequence is:

> **P0 establishes trust in the specification. P1 establishes trust in verification. P2 establishes trust in change and controlled AI execution. P3 establishes trust at enterprise scale.**

This ordering protects the product’s strategic differentiation. AGASTYA succeeds only if it makes AI-native engineering more trustworthy than ungoverned code generation; it should therefore optimise each release for **intent fidelity, evidence, controlled autonomy, and verified engineering throughput**. [1]

---

## References

[1] [AGASTYA README — local project master specification](file:///Users/mohankrishnagundala/Documents/Agastya/README.md)
