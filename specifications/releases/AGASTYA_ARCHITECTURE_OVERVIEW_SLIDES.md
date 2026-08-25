## Cover

# AGASTYA Platform Architecture

### From Intent to Verified Software

## Slide 1

# AGASTYA Makes Engineering Intent Governable

- A specification-driven control plane for AI-native software delivery
- Every material change links **intent → execution → verification → evidence**
- The platform is designed to make AI output traceable, policy-governed and reviewable

## Slide 2

# Twelve Specifications Form One Governed Platform

| Architecture domain | Platform specifications |
|---|---|
| Intent and scope | 001 Canonical Specification Core; 002 Project Workspace Boundary |
| Execution and delivery | 003 Multi-Agent Orchestration; 006 Tool Runtime; 008 Streaming |
| Trust and access | 004 Evidence Ledger; 005 Secret Vault; 007 API Gateway; 009 RBAC |
| Operations and enterprise policy | 010 Observability; 011 HA/DR; 012 Compliance & Data Residency |

## Slide 3

# Foundation Anchors Every Change

- **001 Canonical Specification Core** versions requirements, rules, architecture, verification and provenance
- **002 Project Workspace Boundary** binds each resource and action to an exact tenant/project context
- The approved specification is the authoritative expression of intended behaviour—not code, logs or an agent assertion

## Slide 4

# Policy and Evidence Create the Trust Core

- **009 RBAC Governance** evaluates identity, action, scope, context and approvals with deny-by-default enforcement
- **005 Secret Vault** provides opaque, short-lived, purpose-bound leases; secrets never enter agent context
- **004 Evidence Ledger** records material commands, decisions, tasks, leases and outcomes as durable proof

## Slide 5

# Agents Execute Only Within Explicit Boundaries

- **003 Orchestration** manages durable plans, tasks, approvals, budgets, retries and execution evidence
- **006 Plugin & Tool Runtime** admits signed manifests and capability-bounded, sandboxed invocation
- Policy is evaluated before dispatch; tool output is contained and linked to provenance

## Slide 6

# API and Streaming Expose a Single Authority

- **007 Unified API Gateway** is the contract-first `/api/v1` boundary for web, CLI, SDK and approved integrations
- **008 Streaming** delivers authorised project-scoped notifications, bounded replay and controlled resynchronisation
- Streaming improves awareness; API resources and Ledger events remain authoritative

## Slide 7

# Operational Signals Inform—Never Override—Truth

- **010 Observability** correlates metrics, logs and traces across API, policy, orchestration, tools, Vault, Ledger and streaming
- Safe telemetry references evidence but does not establish requirement satisfaction or approval
- SLO, error, queue, retry and backpressure signals make operational health measurable

## Slide 8

# Recovery Restores Trust Before Throughput

- **011 High Availability & Disaster Recovery** defines tiered recovery, restore validation, reconciliation and exercise evidence
- Trust, policy, keys, authoritative data and Ledger integrity are re-established before normal writes resume
- Recovery uses fenced, authorised procedures rather than implicit privilege or unverified state

## Slide 9

# Compliance Extends the Control Plane to Data

- **012 Enterprise Compliance & Data Residency** is the current draft layer
- It governs classification, residency, processors, egress, retention, legal hold, deletion and recovery reactivation
- It makes no legal or certification claim until specialist policy and approval gates are satisfied
- Provider, external-execution, privileged-access, production-resilience and data commitments remain explicit release gates

## Slide 10

# The Governed Engineering Flow

1. Client enters through the API Gateway
2. RBAC evaluates identity, action, scope and approval context
3. Workspace and Specification Core resolve authoritative intent
4. Orchestration invokes policy-scoped tools and opaque Vault leases when required
5. Ledger records proof; Streaming publishes safe project-scoped notifications

## Slide 11

# Build Software That Can Explain Itself

### Specify. Verify. Govern. Evolve.
