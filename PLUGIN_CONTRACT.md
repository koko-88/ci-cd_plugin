# GitHub Operations Engineering: plugin contract

Status: build-time and runtime contract for four planned domain Skills, authored 2026-10-23. Domain Skills and plugin packaging are pending. Target-host manifests, final packaging, domain acceptance evidence and goal/use-case documents for domains 2 through 4 remain future deliverables.

## 1. Purpose and behavior

Build a reusable GitHub Operations Engineering Plugin for Codex and other explicitly supported coding-agent hosts. It must inspect a target repository's requirements and support authorized implementation, operation and verification across repository/organization governance, Actions and CI/CD quality, security and software supply chain, and release, deployment and reliability.

Choose the design from the target project's files, policies, user intent and granted access. Discover maintained GitHub Actions, reusable workflows, GitHub Apps and Marketplace integrations as needed. The plugin must eventually engineer and verify its own CI/CD. Static YAML templates alone do not meet this goal. Access to private repositories, secrets and deployment accounts requires the appropriate grants.

- Build time: approved goals/use cases, selected upstream Skills/Agent profiles, shared discovery tools and current official references feed Skill Creator/augmentation. Outputs are four domain Skills with task-specific knowledge and durable handoffs.
- Runtime: the host agent activates relevant Skills, inspects the project through shared tools and official sources, and proposes or implements authorized changes. GitHub Actions and integrated services execute the pipelines.
- Assurance: trace decisions and capabilities to use cases and evidence. Verify runs, checks, artifacts, policy settings and deployments separately. Report Passed / Failed / Blocked / Not Verified.
- Deferred work: design advanced Context/Knowledge Retrieval, including RAG, indexing, search infrastructure, vector databases or alternatives, after the domain Skills. Direct retrieval through existing tools is available now.
- Optional infrastructure: custom orchestration, multiple running agents, hooks, local CI/security scanners, downloaded workflow packs and a local Actions runner are not default requirements.

## 2. Project documents and authority

| File | Responsibility |
| --- | --- |
| `AGENTS.md` | Entry point, context routing, reading order and cross-agent conduct. |
| `BUILD_STATE.md` | Current stage, checkpoint, evidence, blockers and session handoff. |
| `GOAL_AND_USE_CASES.md` | Approved CI/CD & Quality Engineering goals and use cases, currently the first domain. |
| `SHARED_TOOL_CAPABILITIES.md` | Shared tools, availability, verification, retrieval and operating boundaries. |
| `PLUGIN_CONTRACT.md` | Product boundaries, domain interfaces and required outputs. |
| `requirements/<domain>/GOAL_AND_USE_CASES.md` | Future approved requirements for the other three domains. |
| `skills/<domain>/SKILL.md` + `references/` | Future runtime instructions and knowledge loaded as needed. |
| `docs/domain-handoffs/<domain>.md` | Future domain evidence, dependencies and gaps for Plugin Creator. |

The source inventory is in the shared workstation directory, outside this repository. These interfaces do not authorize creating runtime directories, deploying integrations or finalizing a manifest.

## 3. Shared inputs for each domain Skill Creator

1. Read `AGENTS.md`, reconcile `BUILD_STATE.md`, then read `SHARED_TOOL_CAPABILITIES.md` and this contract. Obtain the approved domain goal/use-case file. If it is missing, report that dependency and stop creation for that domain.
2. Inspect host availability and access for `gh`, GitHub MCP/connector, Context7, Web Retrieval, Scrapling and the reported `gh-aw`. Reuse existing tools and identify login, scope or provider gaps.
3. Inspect `K:\tools for plugins\Tools\ci-cd-context\source-manifest.json` when accessible. Select source Skills, Agents and required references by domain goal and scenario. Check source IDs, acquisition counts and file completeness.
4. Extract relevant variants: triggers, decisions, alternatives, failure modes, implementation constraints, safe tool use and verification evidence. Record revisions and resolve conflicts against current authoritative documentation.
5. Produce a portable Agent Skills-compatible `SKILL.md` with valid YAML `name` and `description`, invocation triggers, decision workflow, tool prerequisites, evidence rules and targeted reference links. Include only needed `references/` content. Add `scripts/` or `assets/` only for a demonstrated need, with licensing and scope covered.
6. Deliver the domain handoff and coverage mapping in section 8. File creation alone does not establish behavioral correctness, host compatibility, successful packaging or release authorization.

All domains share GitHub CLI, MCP and documentation connections. Describe dependencies as capabilities with access checks and fallbacks. Do not duplicate MCP servers per Skill or hardcode workstation paths into distributable Skills.

Input readiness:

- `READY`: approved goals/cases and source access are available.
- `PARTIAL`: context gaps remain.
- `BLOCKED`: essential goals, permissions or contracts are missing.

A `PARTIAL` result requires resolving or reporting the gaps, without inventing defaults.

## 4. Domain 1: CI/CD & Quality Engineering

Future runtime Skill: `skills/ci-cd-quality-engineering/SKILL.md`.

Design, build, inspect, improve, debug and verify GitHub Actions CI, test/evaluation strategies and enforceable quality gates, including the plugin's own CI. Cover runners and dependencies, untrusted PR events, conditions and DAGs, matrices, caches, reusable workflows, merge queues, concurrency, cost, flakiness and failure evidence.

### Inputs

- Existing `GOAL_AND_USE_CASES.md`.
- Target repository workflows, test/build topology, required checks and run history where available.
- Source candidates: `ci-cd-and-automation`, `github-actions-advanced`, `github-actions-debugger`, `github-actions-templates`, `ci-cd-pipeline-builder`, `github-actions-efficiency`, `create-github-action-workflow-specification`, `github-actions-runtime-upgrade-conventions`, `github-actions-expert` and relevant quality/QA sources. Confirm each against the inventory.
- Relevant CAP-01..CAP-10 capabilities, current Actions documentation, maintained Actions and approved constraints.

### Required outputs after augmentation

- `skills/ci-cd-quality-engineering/SKILL.md`
- `skills/ci-cd-quality-engineering/references/workflow-design-and-execution.md`: triggers, DAG/matrix/concurrency/reuse/runners, selected variants and constraints.
- `skills/ci-cd-quality-engineering/references/quality-gates-and-evaluations.md`: code, tests, evaluations, required-status semantics, evidence and runner tools.
- `skills/ci-cd-quality-engineering/references/diagnostics-and-failure-recovery.md`: failed, cancelled, flaky or blocked run diagnosis, logs and remediation.
- `docs/domain-handoffs/ci-cd-quality-engineering.md`: readiness, evidence, capability-to-use-case mapping, cross-domain dependencies, gaps and Plugin Creator inputs.

Runtime output: scoped CI design/changes, quality-gate and check semantics, and GitHub run/status/artifact evidence where execution is possible. Mark inaccessible results blocked or not verified. Route governance, supply-chain and deployment decisions to the relevant domains.

## 5. Domain 2: GitHub Platform & Governance

Future runtime Skill: `skills/github-platform-governance/SKILL.md`.

Engineer repository and organization governance: branch protections and rulesets, permissions and roles, GitHub Apps, repository fleet standards, cross-repository automation, PR/issue/merge queue policies, secure automation identities, audits and configuration drift. Check actual API access before relying on a scope.

### Inputs

- Pending owner-approved requirements: `requirements/github-platform-governance/GOAL_AND_USE_CASES.md`, including production cases.
- Target repository/organization visibility, permissions, rulesets and policy requirements; source inventory and relevant CAP-01..CAP-10 capabilities.
- Source candidates: `repo-standardizer`, `gh`, `gh-skill`, `acquire-codebase-knowledge`, `senior-devops`, GitHub operations/Agent profiles, and official repository, ruleset and App documentation.

### Required outputs after augmentation

- `skills/github-platform-governance/SKILL.md`
- `skills/github-platform-governance/references/repository-and-organization-governance.md`
- `skills/github-platform-governance/references/identity-permissions-and-rulesets.md`
- `skills/github-platform-governance/references/cross-repository-automation-and-incidents.md`
- `docs/domain-handoffs/github-platform-governance.md`

Runtime output: verified governance/automation plan, authorized API or settings changes, permission matrix, policy/drift evidence and exact access blockers. Agree branch and required-check semantics with the CI domain.

## 6. Domain 3: Security & Software Supply Chain

Future runtime Skill: `skills/security-supply-chain/SKILL.md`.

Secure source, contributors, workflows, dependencies and build/release artifacts. Select GitHub-integrated controls for SAST/SCA, secret protection, dependency integrity, SBOM, provenance/attestation, signing, trust boundaries and policy checks. Keep pipeline scanners on runners, outside the user's shared workstation tools.

### Inputs

- Pending owner-approved requirements: `requirements/security-supply-chain/GOAL_AND_USE_CASES.md`.
- Target threat model, organization security policies, package ecosystem, registry/deployment trust, permissions and required evidence; relevant CAP-01..CAP-10 capabilities.
- Source candidates: `github-actions-hardening`, `agent-supply-chain`, `pinact`, `senior-security`, `senior-secops`, `threat-model-analyst`, `codeql`, `dependabot`, `secret-scanning`, `security-review`, `agent-owasp-compliance` and official standards. Confirm candidates exist in the source inventory before relying on them.

### Required outputs after augmentation

- `skills/security-supply-chain/SKILL.md`
- `skills/security-supply-chain/references/threat-model-and-trust-boundaries.md`
- `skills/security-supply-chain/references/dependencies-build-artifacts-and-provenance.md`
- `skills/security-supply-chain/references/security-gates-and-audit-evidence.md`
- `docs/domain-handoffs/security-supply-chain.md`

Runtime output: enforceable controls and CI integrations, privileges and threat assumptions, source/artifact integrity and audit evidence. Distinguish configured controls from passing controls. Coordinate gates and artifact promotion with CI and Release.

## 7. Domain 4: Release, Deployment & Reliability

Future runtime Skill: `skills/release-deployment-reliability/SKILL.md`.

Design and operate publication, release and deployment pipelines. Cover environments, approvals, versioning, artifact promotion, OIDC/identity and secret scope, deployment targets, progressive rollout, rollback/recovery, incident diagnosis, observability, concurrency and idempotence.

### Inputs

- Pending owner-approved requirements: `requirements/release-deployment-reliability/GOAL_AND_USE_CASES.md`.
- Actual artifacts and release policy, deployment target/platform, secret/environment access, production SLOs, rollback constraints and run evidence; relevant CAP-01..CAP-10 capabilities.
- Source candidates: `devops-rollout-plan`, `senior-devops`, `ci-cd-and-automation`, `github-actions-advanced`, `github-actions-debugger`, `github-release`, `agentic-workflows` and official platform documentation, when available and relevant.

### Required outputs after augmentation

- `skills/release-deployment-reliability/SKILL.md`
- `skills/release-deployment-reliability/references/release-and-artifact-promotion.md`
- `skills/release-deployment-reliability/references/deployment-safety-and-recovery.md`
- `skills/release-deployment-reliability/references/observability-incidents-and-runbooks.md`
- `docs/domain-handoffs/release-deployment-reliability.md`

Runtime output: release/deployment architecture and authorized workflow changes, environment and permission requirements, rollback and incident response plans, and actual release/deployment evidence. A successful deployment requires a verified target run and health/acceptance evidence.

## 8. Standard output and handoff interface

Each domain Skill must follow the [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx): required `SKILL.md` and optional `references/`, `scripts/`, `assets/`. Sections 4 through 7 define the target reference organization. A creator may propose a justified split or rename that preserves capabilities; update this contract before replacing committed paths.

Each `docs/domain-handoffs/<domain>.md` must include:

1. Domain identifier, artifact paths, revision/host and state: not started / created / validated / blocked.
2. Approved goal/use-case input and source/variant provenance, including manifest IDs, revisions and links.
3. Capability-to-use-case mapping, activation triggers, overlapping Skills, tool interfaces and safety/permission boundaries.
4. Output artifacts and dependencies for other domains and Plugin Creator.
5. Separate structure, behavior, host-runtime and GitHub-integration evidence, each with pass/fail/blocked/not-run and supporting evidence.
6. Missing requirements, permissions, operator actions and unverified assumptions.

Use normal host Skill discovery to invoke relevant domains together. A centralized Documentation Skill or custom dispatcher requires scenario evidence that normal discovery is insufficient.

## 9. Target runtime and plugin packaging

- Package the four domain Skills, shared integration descriptions and required runtime assets as one portable plugin after creation. The [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins) reference describes a root `plugin.json`, `skills/`, optional `mcp.json`, and optional hooks/assets. Select final manifests and any other-host compatibility overlays against official documentation during Plugin Creator work.
- Reuse host tool connections where supported. If bundling an MCP dependency is needed, configure it narrowly and state authentication/setup requirements. Exclude workstation `K:` paths, secrets and internal machine state.
- Package selected runtime Skills. Upstream Skills and Agent profiles in the shared source inventory are augmentation inputs and must be reviewed before activation or inclusion.
- Skills supply decision workflows and references; MCP/CLI provides retrieval and authorized actions; GitHub services and runners execute deterministic work. `gh-aw` remains optional for reasoning-dependent operations.
- Add hooks only for a demonstrated security or lifecycle invariant after checking host support, trust and permissions. Enforce repository policy through GitHub rulesets, required checks and environments.
- Support applying CI quality gates to the plugin itself and later collecting security/release evidence. Its CI is not assumed to exist already.
- Track installation, discovery, host compatibility, Skill activation and GitHub execution as separate evidence levels.

## 10. Acceptance and change control

Domain 1 Skill Creator/augmentation is the first implementation stage, once its inputs, sources and tools are ready. Domains 2 through 4 require separate owner-approved goals/use cases before creation.

Before downstream Skill or Plugin creation, check source licensing and injection risk, tool access/scopes, scenario coverage and decisions, host compatibility, credentials, secrets, runners, deployment targets, GitHub policies and packaging documentation. Report unresolved prerequisites as blocked; a file check alone cannot establish success across repositories.

The documentation checkpoint covered `SHARED_TOOL_CAPABILITIES.md`, `PLUGIN_CONTRACT.md`, routing in `AGENTS.md` and the `BUILD_STATE.md` handoff. Skill creation, packaging, CI/security tool installation, Actions execution and deployment remain separate stages.
