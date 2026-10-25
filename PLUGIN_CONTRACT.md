# GitHub Operations Engineering: plugin contract

Contract authored 2026-10-23 for four domain Skills. This file defines required behavior and interfaces; [BUILD_STATE.md](BUILD_STATE.md) owns current completion, revision and verification status. Required-output lists below are obligations, not evidence that an artifact is absent or complete.

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
| `skills/<domain>/SKILL.md` + `references/` | Runtime instructions and knowledge loaded as needed; consult build state for authored domains. |
| `docs/domain-handoffs/<domain>.md` | Dated domain evidence, dependencies and gaps for Plugin Creator; historical observations are not current tool access. |

The source inventory is in the shared workstation directory, outside this repository. These interfaces do not authorize creating runtime directories, deploying integrations or finalizing a manifest.

Use each source for the fact it owns: the current owner request and approved requirements define intended behavior; local files/code show existing behavior; dated commands/runs establish only their observed scope; current official documentation defines platform semantics. When they disagree, name both sources, revisions and the consequence. Resolve implementation drift against approved intent; surface an impossible platform requirement for an owner decision. Do not silently rewrite requirements or promote historical evidence into a current success claim.

For build-time work, load only the relevant domain section, selected goals/cases and source variants after the entry checks. Consumer runtime uses the domain Skill and task-relevant references; this repository's build documents, source inventory and handoffs are not runtime prerequisites. Existing file/search/document tools provide selective loading; this does not authorize the deferred retrieval layer.

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

Runtime Skill path: `skills/ci-cd-quality-engineering/SKILL.md`. See `BUILD_STATE.md` for authoring and verification status.

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

- **Not yet supplied:** owner-approved `requirements/github-platform-governance/GOAL_AND_USE_CASES.md`, including production cases. Author this requirements artifact and resolve its acceptance boundaries before asking Skill Creator to produce Domain 2; the candidate sources below do not substitute for approved requirements.
- Target repository/organization visibility, permissions, rulesets and policy requirements; source inventory and relevant CAP-01..CAP-10 capabilities.
- Source Skill/Agent candidates: `repo-standardizer`, `gh`, `gh-skill`, `acquire-codebase-knowledge`, `senior-devops` and relevant GitHub operations/Agent profiles. Resolve their actual identities, revisions, references and license from the source manifest before using them; these are augmentation candidates, not activated runtime dependencies.
- Authoritative GitHub sources: repository/organization/enterprise governance policies and [ruleset documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [effective rules for a branch](https://docs.github.com/en/rest/repos/rules), [organization ruleset REST APIs](https://docs.github.com/en/rest/orgs/rules), GitHub App installation/authentication and permission documentation, repository/team/custom-role administration, [organization audit logs](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization) and current [ruleset migration guidance](https://github.blog/changelog/2026-10-20-bulk-migrate-branch-protections-to-rulesets-for-a-repository).
- Maintained implementation/reference candidates, evaluated per consumer scope rather than bundled by default: [GitHub ruleset recipes](https://github.com/github/ruleset-recipes) for importable policy patterns; [GitHub Terraform provider](https://github.com/integrations/terraform-provider-github) for declarative multi-repository/team/ruleset management and drift; [GitHub Safe Settings](https://github.com/github-community-projects/safe-settings) for centrally managed policy-as-code and hierarchical repository/organization settings; [Probot](https://github.com/probot/probot) only where genuinely custom GitHub App event-driven behavior is needed. Reuse native GitHub rulesets/settings and `gh api` or an authenticated GitHub MCP capability for targeted operations rather than imposing fleet-management infrastructure on a single repository.

### Governance-specific research and decision obligations

1. **Effective policy, not only stored configuration:** inspect applicable repository, organization and enterprise rulesets, classic branch protection, enforcement state, target criteria/custom properties, bypass actors and the actual branch's effective rules. Compare required-check producers and merge-queue events with Domain 1. Plan migrations without briefly dropping existing protections; prefer GitHub's maintained import/preview capabilities where available.
2. **Identity and authority:** derive a per-operation permission matrix for user, team, custom role, GitHub App installation and automation identity. Distinguish read access, token scope, App installation coverage, organization ownership and effective authorization; no broad owner/PAT token or fabricated access. Confirm the current API/tool actually exposes each operation before promising automation.
3. **Repository-fleet governance:** compare native organization rulesets, an existing Terraform/OpenTofu GitHub provider setup, and Safe Settings against repository count, policy ownership, drift/reconciliation requirements, GitHub plan, migration and rollback needs. Evaluate GitHub App auth, review of proposed changes, state ownership, import/adoption and destructive-change risk; do not activate competing configuration owners for the same settings by default.
4. **Audits and incidents:** bind policy changes, permission grants, App installation changes and bypass events to timestamp, actor, target and authoritative available evidence. Account for plan-restricted audit-log APIs, limited retention and partial/inaccessible results; never claim an organization-wide audit from one repository's event stream.
5. **Product boundary and acceptance:** model organization/enterprise capabilities as conditional on the consumer's plan, role and granted access. Produce a scoped governance inventory, intended-to-effective policy comparison, drift/exception evidence and precise authorized changes or blockers. An available source Skill, provider schema, policy file or successful API write is not proof the resulting governance is enforced.

### Required outputs after augmentation

- `skills/github-platform-governance/SKILL.md`
- `skills/github-platform-governance/references/repository-and-organization-governance.md`: repository fleet standards, organization/enterprise policy, custom properties, native rulesets versus declarative governance, import and drift.
- `skills/github-platform-governance/references/identity-permissions-and-rulesets.md`: effective branch protection/ruleset inheritance, bypass and check-source correctness, GitHub App installation identities, role/scope/authorization boundaries.
- `skills/github-platform-governance/references/cross-repository-automation-and-incidents.md`: safe fleet changes, configuration ownership, audit logs, policy-drift investigation, migration/rollback and failure evidence.
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

Domain 1 Skill Creator/augmentation is the first domain-authoring stage; resume from the verified checkpoint rather than recreating existing outputs. Domains 2 through 4 require separate owner-approved goals/use cases before creation.

Before downstream Skill or Plugin creation, check source licensing and injection risk, tool access/scopes, scenario coverage and decisions, host compatibility, credentials, secrets, runners, deployment targets, GitHub policies and packaging documentation. Report unresolved prerequisites as blocked; a file check alone cannot establish success across repositories.

Authoring/augmentation, behavioral evaluation, packaging/activation, Actions execution and deployment are separate authorization and evidence stages. A context-document repair does not authorize advancing any of them. Current completed work and the next dependency belong in `BUILD_STATE.md`.
