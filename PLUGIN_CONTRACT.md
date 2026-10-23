# Plugin Contract — GitHub Operations Engineering

**Status:** Build-time and runtime architectural contract for the four planned domain Skills. Authored 2026-10-23. **No domain Skill or distributable plugin is claimed implemented by this file.** The target-host manifest, finalized packaging, domain acceptance evidence and domain-2/3/4 goal/use-case documents remain future deliverables.

## 1. Purpose and behavior

Deliver a reusable **GitHub Operations Engineering Plugin**, usable from Codex and other explicitly supported coding-agent hosts, to inspect a target repository's actual requirements and engineer, implement, operate and verify GitHub repository/organization governance, Actions/CI/CD quality engineering, security/software supply chain, and release/deployment/reliability.

For every target project, derive the design from its actual files, policies, user intent and granted access, then discover suitable mature GitHub Actions, reusable workflows, GitHub Apps and Marketplace integrations on demand. The plugin must eventually be able to engineer and verify **its own** CI/CD. It is **not** a static YAML template collection and is **not** an assumption that any agent may access private repositories, secrets or deployment accounts.

- **Build time:** approved goals/use cases + curated upstream Skills/Agent profiles + shared discovery tools + current official references → Skill Creator/augmentation → four domain Skills with selective knowledge and durable handoffs.
- **Runtime:** host agent (Codex/Cursor/etc.) activates relevant domain Skill(s), inspects target project through shared tools and official sources, and proposes/implements authorized changes; GitHub Actions and appropriate GitHub-integrated services provide the actual pipeline execution.
- **Assurance:** decisions and applicable capabilities trace to concrete use cases and evidence. GitHub runs, checks, artifacts, policy settings and deployments are verified separately. Classify findings **Passed / Failed / Blocked / Not Verified**, never fabricate success.
- **Deferred:** advanced Context/Knowledge Retrieval layer (RAG, indexing, search infrastructure, vector databases or alternatives), beyond the current direct tool-based retrieval, is a later architecture phase after domain Skills.
- **Not required by default:** bespoke orchestration, multiple running agents, plugin hooks, locally installed CI/security scanners, predownloaded third-party workflows or a local GitHub Actions runner.

## 2. Project documents and authority

| File | Responsibility |
| --- | --- |
| `AGENTS.md` | Lightweight entrypoint/context router; required reading order and cross-agent conduct. |
| `BUILD_STATE.md` | Factual stage/checkpoint, evidence, blockers and cross-session handoff, **not** a second contract. |
| `GOAL_AND_USE_CASES.md` | **Existing approved CI/CD & Quality Engineering** domain goals and use cases only (currently first domain). |
| `SHARED_TOOL_CAPABILITIES.md` | Shared tools, availability, verification, search/retrieval and operational boundaries for every creator/domain. |
| `PLUGIN_CONTRACT.md` | This product/interface/domain/output contract; source of intended boundaries, not proof of implementation. |
| `requirements/<domain>/GOAL_AND_USE_CASES.md` | **Future** approved goals/use cases for the other three domains. Do not imply these files already exist. |
| `skills/<domain>/SKILL.md` + `references/` | **Future** runtime domain instructions and just-in-time knowledge after Skill Creator/augmentation. |
| `docs/domain-handoffs/<domain>.md` | **Future** domain handoff for Plugin Creator: contracts/evidence/gaps after that Skill is built. |

This file describes expected interfaces without creating runtime directories, deploying integrations or picking a finalized manifest prematurely. Source repo inventory remains external to this repository in the shared workstation directory.

## 3. Shared inputs for ANY domain Skill Creator

The coding agent running the Skill Creator must:

1. Read `AGENTS.md`, reconcile `BUILD_STATE.md`, read `SHARED_TOOL_CAPABILITIES.md`, then this contract. Obtain the approved domain-specific goal/use-case file. If not authored yet, stop that domain's creation and report the missing requirement rather than inventing owner requirements.
2. Inspect actual tool availability in its host (`gh`, GitHub MCP/connector, Context7, Web Retrieval, Scrapling and reported `gh-aw`). Reuse existing capabilities; identify login/scope/provider gaps instead of reinstalling everything.
3. Find the provenance/manifest of curated source Skills, Agents and their supporting references in `K:\tools for plugins\Tools\ci-cd-context\source-manifest.json` when accessible. Filter by *domain goal and scenario*, not by filename alone. Source IDs, acquisition counts and source-file completeness must be checked, not presumed.
4. Extract relevant variants: triggering conditions, engineering decisions, supported alternatives, failure modes, implementation constraints, safe tool usage and verification evidence. Track source revision and resolve conflicts with current authoritative docs.
5. Produce a portable Agent Skills-compatible `SKILL.md` (valid YAML `name` and `description` frontmatter, clear invocation triggers, decision workflow, tool prerequisites, evidence rules, and targeted reference links), plus the minimum genuinely needed `references/` content. Optional `scripts/` and `assets/` only with proven need, proper licensing and authorized scope.
6. Deliver the domain handoff and coverage mapping described below. A Skill Creator output or reference inventory **is not automatically behavioral pass, host compatibility, package success or authorized release**.

**Shared tool-use contract:** every domain may use the *same* GitHub CLI, MCP and documentation retrieval connections. No separate copy of an MCP server per Skill. Expose dependencies as capabilities with connection/authorization checks and documented fallbacks, not hardcoded workstation paths inside distributable Skills.

**Input readiness statuses:** `READY` (approved goal/cases and source access), `PARTIAL` (context gaps), `BLOCKED` (essential goals/permissions/contract missing). Do not turn a `PARTIAL` result into implicit permission to fabricate defaults.

## 4. Domain 1 — CI/CD & Quality Engineering

**Runtime Skill path (future):** `skills/ci-cd-quality-engineering/SKILL.md`.

**Purpose:** design, create, inspect, improve, debug and verify GitHub Actions CI systems, test/eval strategies and enforceable quality gates for real repositories, including the plugin's own CI. Handle runner and dependency constraints, untrusted PR events, workflow conditions/DAGs, matrix, caches, reusable workflows, merge queues, concurrency, cost, flakiness and failure evidence.

**Inputs**
- **Existing** `GOAL_AND_USE_CASES.md` (first domain's goals and production incident scenarios).
- Target repo context, actual workflow/test/build topology and current required-check/run history if available.
- Relevant source material: `ci-cd-and-automation`, `github-actions-advanced`, `github-actions-debugger`, `github-actions-templates`, `ci-cd-pipeline-builder`, `github-actions-efficiency`, `create-github-action-workflow-specification`, `github-actions-runtime-upgrade-conventions`, `github-actions-expert` and pertinent quality/QA sources, all confirmed against the inventory.
- Shared capabilities CAP-01..CAP-10 **as relevant**, current GitHub Actions documentation, discovered maintained Actions, approved constraints.

**Required Skill output after augmentation**
- `skills/ci-cd-quality-engineering/SKILL.md`
- `skills/ci-cd-quality-engineering/references/workflow-design-and-execution.md` — triggers, DAG/matrix/concurrency/reuse/runners, chosen variants and constraints.
- `skills/ci-cd-quality-engineering/references/quality-gates-and-evaluations.md` — code/tests/evals, required status semantics, evidence, relevant tools on GitHub runners.
- `skills/ci-cd-quality-engineering/references/diagnostics-and-failure-recovery.md` — failed/cancelled/flaky/blocked run diagnosis, logs and remediations.
- `docs/domain-handoffs/ci-cd-quality-engineering.md` — domain readiness, evidence, capability-to-use-case mapping, cross-domain dependencies, open gaps, and next Plugin Creator input.

**Runtime task output:** scoped CI design/changes + configured quality-gate/check semantics + GitHub execution/status/artifact evidence when runnable; explicitly blocked/not-verified when inaccessible. Delegate platform governance, supply-chain hardening and deployment decisions to the appropriate other domain(s).

## 5. Domain 2 — GitHub Platform & Governance

**Runtime Skill path (future):** `skills/github-platform-governance/SKILL.md`.

**Purpose:** engineer repository/organization governance: branch protection and rulesets, permissions and roles, GitHub Apps, repository fleet standardization, cross-repo automation, PR/issue/merge queue policies, secure automation identities, audit and config-drift remediation. No claims that unsupported API scopes are available.

**Inputs**
- **Not yet authored:** `requirements/github-platform-governance/GOAL_AND_USE_CASES.md` (approved goals and heavy production cases required before creation).
- Target repo/org visibility, actual permissions, rulesets and policy requirements; source inventory + CAP-01..CAP-10 as relevant.
- Curated source candidates: `repo-standardizer`, `gh`, `gh-skill`, `acquire-codebase-knowledge`, `senior-devops`, GitHub operations/Agent profiles and official GitHub repository, rulesets and App docs.

**Required Skill output after augmentation**
- `skills/github-platform-governance/SKILL.md`
- `skills/github-platform-governance/references/repository-and-organization-governance.md`
- `skills/github-platform-governance/references/identity-permissions-and-rulesets.md`
- `skills/github-platform-governance/references/cross-repository-automation-and-incidents.md`
- `docs/domain-handoffs/github-platform-governance.md`

**Runtime task output:** verified governance/automation plan and authorized API/settings changes, permission matrix, policy/drift evidence and exact access blockers. Contract with CI domain on branch/required-check semantics.

## 6. Domain 3 — Security & Software Supply Chain

**Runtime Skill path (future):** `skills/security-supply-chain/SKILL.md`.

**Purpose:** secure source, contributors, workflows, dependencies and build/release artifacts; engineer SAST/SCA, secret protections, risk-adapted dependency integrity, SBOM, provenance/attestation, signing, trust boundaries and policy checks using selected GitHub-integrated controls rather than installing scanners on the user's workstation.

**Inputs**
- **Not yet authored:** `requirements/security-supply-chain/GOAL_AND_USE_CASES.md`.
- Target threat model, current org security policies, package ecosystem, registry/deployment trust, permissions and required evidence; CAP-01..CAP-10 as relevant.
- Curated source candidates: `github-actions-hardening`, `agent-supply-chain`, `pinact`, `senior-security`, `senior-secops`, `threat-model-analyst`, `codeql`, `dependabot`, `secret-scanning`, `security-review`, `agent-owasp-compliance` and official standards; verify each candidate is actually in the local source inventory before relying on it.

**Required Skill output after augmentation**
- `skills/security-supply-chain/SKILL.md`
- `skills/security-supply-chain/references/threat-model-and-trust-boundaries.md`
- `skills/security-supply-chain/references/dependencies-build-artifacts-and-provenance.md`
- `skills/security-supply-chain/references/security-gates-and-audit-evidence.md`
- `docs/domain-handoffs/security-supply-chain.md`

**Runtime task output:** selected enforceable controls and CI integrations, documented privileges/threat assumptions, source/artifact integrity and audit evidence; distinguish installed or configured controls from passing controls. Work with CI and Release domains for gate and promotion enforcement.

## 7. Domain 4 — Release, Deployment & Reliability

**Runtime Skill path (future):** `skills/release-deployment-reliability/SKILL.md`.

**Purpose:** design and operate publication/release/deployment pipelines and their reliability characteristics: environments, approvals, release versioning, artifact promotion, OIDC/identity and secret scope, deployments across targets, progressive rollout, rollback/recovery, incident diagnosis, observability, concurrency and idempotence.

**Inputs**
- **Not yet authored:** `requirements/release-deployment-reliability/GOAL_AND_USE_CASES.md`.
- Actual build artifact and release policy, deployment target/platform, secrets/environment access, production SLOs/rollback constraints, run evidence; CAP-01..CAP-10 as relevant.
- Curated source candidates: `devops-rollout-plan`, `senior-devops`, `ci-cd-and-automation`, `github-actions-advanced`, `github-actions-debugger`, `github-release`, `agentic-workflows` and official platform/docs, only when available and relevant.

**Required Skill output after augmentation**
- `skills/release-deployment-reliability/SKILL.md`
- `skills/release-deployment-reliability/references/release-and-artifact-promotion.md`
- `skills/release-deployment-reliability/references/deployment-safety-and-recovery.md`
- `skills/release-deployment-reliability/references/observability-incidents-and-runbooks.md`
- `docs/domain-handoffs/release-deployment-reliability.md`

**Runtime task output:** release/deployment architecture and approved workflow changes, environment/permission requirements, rollback and incident response plans, actual release/deployment evidence; **never claim a successful deployment absent a verified target run and health/acceptance evidence**.

## 8. Standard output and handoff interface (all domains)

Every authored domain Skill must meet the [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx): required `SKILL.md`, optional `references/`, `scripts/`, `assets/`. The specific reference Markdown deliverables in sections 4–7 are the **target organization**; creator may propose a justified split/rename with the same capabilities and update the contract before replacing committed paths.

**Each domain handoff** `docs/domain-handoffs/<domain>.md` must state:
1. Domain identifier, artifact paths, state (not started / created / validated / blocked), revision/host.
2. Approved input goal/use-case file and source/variant provenance (manifest IDs/revisions/links).
3. Capability-to-use-case mapping, activation triggers, overlapping skills, tool interfaces, applicable safety/permission boundaries.
4. Concrete output artifacts, handoff dependencies on the other domains and consuming Plugin Creator.
5. Evaluation evidence separated by **structure, behavior, host runtime, GitHub integration** (with exact pass/fail/blocked/not-run and evidence).
6. Missing requirements, permissions, operator actions and unverified assumptions.

The cross-domain consumer should be able to invoke relevant Skills together using normal host Skill discovery. No required large centralized Documentation Skill or custom dispatcher unless scenario evidence demonstrates that default discovery is insufficient.

## 9. Target runtime/plugin packaging contract

- Build one **portable plugin** containing the four domain Skills (once created), shared integration descriptions and only the runtime assets actually needed. Current official [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins) describes a root `plugin.json` manifest, `skills/`, optional `mcp.json`, and optional hooks/assets. Other hosts may have compatibility overlays; select and validate against their official documentation during Plugin Creator phase.
- A **tool capability is not the same as a bundled MCP server**. Use existing host connections where supported, or declare a narrowly configured MCP dependency with explicit authentication/setup requirements; never embed a user's Windows `K:` paths, secret keys or internal machine state in the distributed plugin.
- Distinguish **runtime domain Skills** from **upstream source Skills/Agent profiles** in the shared tools repository. The latter are never enabled blindly and do not all get packaged.
- Skills handle reusable decision workflows and on-demand references; MCP/CLI handles actual retrieval and authorized actions; GitHub/marketplace services and runners handle deterministic execution. Agentic workflows via `gh-aw` are an **optional** capability for reasoning-dependent GitHub operations, never a mandatory replacement for CI.
- Hooks are **not a default dependency**. Add them later only for a specific security/lifecycle invariant, with host support, trust model and permissions verified. Enforce actual repository policies with GitHub-native controls (rulesets, required checks, environments), not documentation alone.
- The plugin must support **self-application** of CI quality gates and eventual security/release evidence without presuming its own CI already exists.
- Installation, discoverability, compatibility, successful Skill activation, and successful GitHub-hosted execution are **distinct** evidence levels.

## 10. Acceptance and change control

The first implementation request is **Domain 1 Skill Creator/augmentation** only, after confirming its input and source/tool readiness. The other domains require their own owner-approved goal/use-case catalogs before creation; no automatic domain creation in this documentation commit.

Before authorizing downstream Skill/Plugin Creator, check source licensing and injection risk, tool reachability/scope, domain scenario coverage and decisions, target-host compatibility, missing credentials/secrets/runner/deployment targets, actual GitHub policy constraints, and relevant host packaging documentation. Do not promise universal success for every repository or mask "blocked" with a green file check.

**Documentation commit outcome:** only `SHARED_TOOL_CAPABILITIES.md`, `PLUGIN_CONTRACT.md`, `AGENTS.md` router wiring and truthful `BUILD_STATE.md` checkpoint are in scope; no Skill generated, no package built, no CI/security tools installed, no Actions run and no deployment performed.
