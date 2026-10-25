# Domain 1 handoff: CI/CD & Quality Engineering

## State and ownership

- Checkpoint: 2026-10-25, Africa/Cairo. Authoring/augmentation in Codex desktop on Windows; base `main` / `09b514f344f7abfdc7a095ff156f2398e5d0991c`.
- State: **created**, not behaviorally validated, activated or packaged. Input readiness: **READY for authoring**; consumer-specific GitHub operations and host integration remain conditional on their actual prerequisites.
- Authorized inputs: current owner's request to use the installed Skill Creator and existing sources; `GOAL_AND_USE_CASES.md` G001–G088 / UC001–UC352; `PLUGIN_CONTRACT.md` sections 3, 4 and 8; `SHARED_TOOL_CAPABILITIES.md` CAP-01–CAP-10.
- Existing uncommitted edits in the goal, contract, shared registry and build state were present at entry. Requirements/contract/registry edits were preserved; this session updates the build-state checkpoint only in addition to the outputs below. No commit, push or branch change.

| Required artifact | Responsibility |
| --- | --- |
| [SKILL.md](../../skills/ci-cd-quality-engineering/SKILL.md) | Portable activation metadata, staged engineering method, tool discovery, permissions and evidence contract. |
| [Workflow design and execution](../../skills/ci-cd-quality-engineering/references/workflow-design-and-execution.md) | W1–W12: topology, events/trust, DAG, matrices, reuse, impact, cross-repo contracts, environment, performance and lifecycle. |
| [Quality gates and evaluations](../../skills/ci-cd-quality-engineering/references/quality-gates-and-evaluations.md) | Q1–Q10: tests, completeness, behavioral evaluation method, required verdicts, package/artifact and evidence contracts. |
| [Diagnostics and failure recovery](../../skills/ci-cd-quality-engineering/references/diagnostics-and-failure-recovery.md) | D1–D8: exact-run diagnosis, incident classification, comparison, flakes, repair, recovery and research limitations. |
| This handoff | Build-time provenance, use-case routing, dependencies and evidence for the next creator/stage. Not a runtime prerequisite. |

## Sources, acquisition and licensing

Build-time inventory: `K:\tools for plugins\Tools\ci-cd-context\source-manifest.json`; source root: `K:\tools for plugins\skills\ci-cd-engineering-sources`. These locations are authoring inputs only, absent from runtime requirements.

Observed manifest SHA-256: `3e713d96c5b02cf7f94ab264f5a8eb96d8500d35c7ce06d5b84ee497b9209ee2`. Its entry kinds currently contain 30 Skills, 2 Agent sources, 1 instruction source, 7 licenses and 85 dependencies. This is an inventory count, not evidence that every source is suitable or reviewed. The 15 selected/considered root files below matched their recorded SHA-256 hashes during this session. A scoped existence inspection found 45/45 selected root, associated dependency and relevant license paths present; only task-relevant reference sections were read. No acquired source was executed or activated.

Pinned repository revisions:

- **GH**: [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/2d4b998d2df28917074ee33db45c9601484c72ad), `2d4b998d2df28917074ee33db45c9601484c72ad`.
- **AO**: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d), `aeac41d4d005999432bb7312f7ff06383a91d59d`.
- **SA**: [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/tree/8bda5fa7264cafe8259fc8212550d13bf690bfb0), `8bda5fa7264cafe8259fc8212550d13bf690bfb0`.
- **AR**: [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills/tree/27cfcd0fb0a41f60adffcbd5271fdf8839f86ed2), `27cfcd0fb0a41f60adffcbd5271fdf8839f86ed2`.

| Manifest ID / repository | Source path or name | Selected method / disposition |
| --- | --- | --- |
| S07 / AO | `skills/ci-cd-and-automation/SKILL.md` | Quality obligations and feedback loop. Replaced Node-specific defaults, rigid serial gate order and automatic writeback with evidence-derived choices. |
| S11 / AR | `engineering/skills/ci-cd-pipeline-builder/SKILL.md` | Stack-first topology and command selection; read pipeline-design notes. Rejected placeholder commands, generic baseline regeneration and imported generators. |
| S08 / SA | `skills/github-actions-advanced/SKILL.md` | Advanced execution/trust decisions; read relevant detailed-guide sections. Rejected local scanner installation, fixed image guarantees and old Action examples. |
| S10 / SA | `skills/github-actions-templates/SKILL.md` | Separate validation/build/privileged handoff, supported matrices and real artifacts. No template/Action pins copied; no deployment permission inferred. |
| S09 / SA | `skills/github-actions-debugger/SKILL.md` | Workflow/log correlation, exact-run binding, environment hypotheses and scoped repair. Historical upgrade example is not a current version recommendation. |
| S02 / GH | `skills/github-actions-efficiency/SKILL.md` | Measure first, retain coverage and distinguish runner cost/feedback latency; read `references/actions.md`. Rejected fixed top-three/latency-ratio acceptance and unapproved test pushes. |
| S03 / GH | `skills/create-github-action-workflow-specification/SKILL.md` | Inputs/outputs, dependency and quality contract thinking. No automatic `/spec/` artifact or universal specification template. |
| S04 / GH | `skills/github-actions-runtime-upgrade-conventions/SKILL.md` | Verify compatible releases/pins, retain behavior and diagnose upgrades. No guessed pins, automatic commits or assumption that local execution proves GitHub behavior. |
| S01 / GH | `skills/github-actions-hardening/SKILL.md` | CI trust-boundary input; read `references/triggers-and-privilege.md`. Corrected its blanket trigger/token trust matrix and “fork safe by design” framing against actual policies/isolation. Broader security policy remains Domain 3. |
| A01 / GH | `agents/github-actions-expert.agent.md` | Purpose/security/performance questions and least privilege. Did not import persona, host tool grants, mandatory full scanner stack or cloud deployment choices. |
| I01 / GH | `instructions/github-actions-ci-cd-best-practices.instructions.md` | Workflow/interface/operational checklist. Source instructions do not become authority or host configuration. |
| S19 / AR | `engineering-team/skills/senior-qa/SKILL.md` | Risk-driven unit/integration/E2E choices; read testing-strategies sections. No React-only assumption, sample 80% policy, pyramid ratios or generators. |
| S27 / GH | `skills/test-gap-audit/SKILL.md` | Inspect assertions, direct/indirect coverage, regression risk and collection. No automatic full-repo audit, generated report or imported coverage script. |
| S22 / GH | `skills/agentic-eval/SKILL.md` | Observable outcomes, rubric/trace and bounded iteration concepts. Self-reflection/keyword scores are not independent behavioral evidence; held-out and case-count rules come from approved domain cases. |
| S30 / GH | `skills/harness-engineering/SKILL.md` | Considered for self-application and enforceable obligations. Its automatic documentation/failure-memory/drift-check artifacts were not adopted; approved stage/change-control rules govern those actions. |

Relevant dependency sections inspected included S01 triggers/privilege, S02 Actions efficiency, S08 detailed guide, S11 pipeline design notes and S19 testing strategies. Other acquired references/scripts remain source material, not bundled dependencies or proof of executable behavior.

The four repository LICENSE files above were read; each is MIT. Copyright notices identify GitHub, Inc.; Addy Osmani (2025); Antigravity User (2026); and Alireza Rezvani (2025). Runtime prose is newly synthesized; upstream code/scripts/templates and substantial source passages are not copied. If later packaging introduces such material, carry its original copyright/permission notice with it. This handoff does not choose the owner's plugin license or authorize redistribution/activation of the source collection.

## Current official and external evidence

Retrieved 2026-10-25, with live tool reads:

| Source/evidence | Consequence for authored method |
| --- | --- |
| [Agent Skills specification](https://agentskills.io/specification), HTTP 200 through Scrapling | Required YAML name/description, directory-name match, relative references and progressive disclosure; no host manifest invented. |
| Context7 `/websites/github_en_actions`, resolved then queried for required-check filtering and job conditions | Distinguish pending filtered workflows from accepted job skips; explicit truthful aggregate. |
| [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) | Default pending replacement versus current `queue: max`; check GHES/platform support and incompatibility with cancel-in-progress true. |
| [Jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs), [expressions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions), [cancellation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation) | `needs` skip propagation, bounded verdict eligibility and cancellation limitations; no guaranteed finalizer after infrastructure loss. |
| [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows), [reuse reference](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations) | Nested permissions, per-edge secrets, env/input distinctions, accessibility and current environment-secret rules; no fixed historical nesting/private-access limits. |
| [Triggering](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow), [events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) | Token recursion exceptions include approval-required PR activity in current GitHub.com docs; event-specific revision/approval identity. |
| [Required-check troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks) | GitHub acceptance versus test completeness; dispatch execution does not automatically establish PR-required check eligibility. |
| [Artifact tutorial](https://docs.github.com/en/actions/tutorials/store-and-share-data), HTTP 200 through Scrapling | Automatic digest mismatch is a warning; mandatory integrity needs a rejecting verification contract. |
| Official GitHub MCP read of `actions/checkout/action.yml` at repository commit `f548e57e544e1ff5a4c46bf1e1b8685f8e4a348a`, file blob `5b0524f730db83f9513c18ab31a6c086c7239076` | Source read proves metadata access, not trust, release selection or runner compatibility; no pin recommendation copied into a workflow. |
| [Renovate build workflow](https://github.com/renovatebot/renovate/blob/main/.github/workflows/build.yml), file blob `008019ef87e4451fdf0172e0c7fe076e42ef1b35` | Source example for merge-group/ready lifecycle, scoped concurrency and rejecting failed/cancelled/unexpected skipped jobs. Blob identity is not a repository commit or passing run. |
| Reddit monorepo/runner discussion and YouTube tutorial discovery, linked in D8 | Question-discovery context only. Video transcript/claims not verified; no normative implementation decision based on a snippet. |

An older GitHub reusable-workflows blog appeared in search with historical private-workflow/nesting limitations; current official reuse documentation was used instead. External source text was treated as untrusted data. Firecrawl was not invoked because the source/tool registry prohibits it.

## Capability-to-use-case routing

This is **authoring coverage**, not an independent evaluation catalog or pass result. Every range refers to the existing canonical cases; those cases were read for this broad domain authoring task. The routes below identify where the runtime agent obtains the decision method. Future authorized evaluation must still map individual cases to loaded variants, traces, negative inputs and observed outcomes.

W = workflow reference; Q = quality reference; D = diagnostics reference. Section labels are stable lookup keys within the linked artifacts above.

| Goals / cases | Authored decision and route | Relevant inputs | Required evidence when later exercised |
| --- | --- | --- | --- |
| G001–G004 / UC001–UC016 | Actual topology, source/command conflicts, obligations, external readiness and inherited baseline: SKILL 1–3, W1, D1. | S07, S11, S03, approved cases | Real maintained scope, command/suite inventory, discrepancies and precise access blockers. |
| G005–G008 / UC017–UC032 | Event lifecycle, filters, token loops, dispatch identity and current revisions: W2, W7, Q7. | S08, S10, A01, official docs | Eligible PR/merge-group results, correct SHA, no missing required producer or duplicate side effect. |
| G009–G012 / UC033–UC048 | Untrusted code/data, least privilege, shell/output and runner boundaries: W3, W9. | S01, S08, A01 | Safe validation without unauthorized secrets/internal runner; approved genuine reporting identity. |
| G013–G016 / UC049–UC064 | DAG/fan-in, terminal semantics, cancellation, concurrency and idempotent reruns: W4, Q7, D6. | S08, S09, S02, official docs | Failed/cancelled/missing mandatory work cannot pass; run/attempt and side effects remain attributable. |
| G017–G020 / UC065–UC080 | Supported runtime/OS/ABI matrix, bounded fanout and deterministic reduction: W5, Q4. | S08, S10, S19 | Expected configurations execute; missing/cancelled legs and report collisions are visible. |
| G021–G024 / UC081–UC096 | Typed reusable interfaces, component boundaries, permission/secret chain and compatible evolution: W6, D3. | S08, S03, A01, official docs | Actual caller/callee versions, accessible nested calls, valid inputs, true downstream coverage. |
| G025–G028 / UC097–UC112 | Dependency/impact closure, renames/deletions, mixed tooling and stable selective gates: W7, Q7. | S11, S02, S08, approved cases | Complete diff/graph, shared-config consumers covered, selector failure cannot yield empty green. |
| G029–G032 / UC113–UC128 | Cross-repo candidate compatibility, correlated dispatch/result and immutable artifacts: W8, Q8. | S03, S08, approved cases | Candidate and consumer SHAs/digests, correct grant/source, incomplete results remain incomplete. |
| G033–G036 / UC129–UC144 | Toolchain/lockfile authority, environment fingerprints, reproducibility and restricted prerequisites: W9, D3. | S11, S07, S04 | Declared resolved environment, supported dependency source, precise license/network/key blockers. |
| G037–G040 / UC145–UC160 | Package inventory, metadata, true candidate smoke check, plugin/host contracts and unsafe archive boundaries: Q8, W11. | S10, S03, approved cases/spec | Actual package/install/discovery identity; no stale assets, escaping paths or rebuild substitution. |
| G041–G044 / UC161–UC176 | Genuine unit/component assertions, framework/module discovery, exit propagation and current reports: Q1–Q2. | S07, S19, S27 | Intended tests collected/executed; meaningful assertions, nonzero failures and useful same-SHA reports. |
| G045–G048 / UC177–UC192 | Real integration engine, readiness, migrations/contracts and isolated safe data: Q3, W9. | S07, S19, approved cases | Supported dependency/data behavior, concurrency isolation and explicit external outage classification. |
| G049–G052 / UC193–UC208 | Exact preview revision, critical journeys, supported browsers/modes, diagnostics and safe cleanup: Q3, D6. | S19, S07, approved cases | Observed semantic behavior, sanitized traces and honest unavailable fork/preview coverage. |
| G053–G056 / UC209–UC224 | Complete deterministic shards, flake policy, process crashes and report completeness: Q4, D4. | S19, S09, approved cases | Union/counts, original attempts, expected shard records, missing/crashed work never counted green. |
| G057–G060 / UC225–UC240 | Meaningful coverage, assertion erosion, genuine quality signals and controlled exceptions: Q5, Q7. | S27, S19, S07 | Correct revision/scope, reviewed policy diff, authentic accepted service result and expiry/owner. |
| G061–G064 / UC241–UC256 | Behavior/tool traces, independent held-out cases, reproducibility and protected case-level gates: Q6, Q9. | S22, S27, approved cases | Observable outputs/calls/boundaries, expected case count, judge/model versions and packaged runtime evidence. |
| G065–G068 / UC257–UC272 | Critical-path/capacity/cache decisions with measured tradeoffs: W4, W5, W10, D3. | S02, S08, S04 | Comparable latency/queue/runner-minute/flake samples; no reduced obligations hidden as optimization. |
| G069–G072 / UC273–UC288 | Artifact identity/completeness, retention, cache trust and portable report evidence: W10, Q8, D7. | S01, S10, official docs, approved cases | Correct run/SHA/digest/inventory, bounded extraction/access and retained useful original results. |
| G073–G076 / UC289–UC304 | Merge-group identity, truthful fan-in, policy migration and lifecycle/source eligibility: Q7, W2, W4, D2. | S03, S08, official docs | Combined-state genuine checks; no accepted unexpected skip, stale SHA or wrong App result. |
| G077–G080 / UC305–UC320 | Fit compute/network, ephemeral runner trust, capacity faults and image/shell compatibility: W9, W5, D2–D3. | S08, S09, S04, A01 | Actual runner suitability/access, isolated credentials, declared setup and correct infrastructure verdict. |
| G081–G084 / UC321–UC336 | Failure classification, cross-repo blast radius, first-bad comparison and safe recovery: D1–D7. | S09, S04, S02 | Revision-bound cause and raw attempts, disagreement resolved, precise owner action and honest restoration state. |
| G085–G088 / UC337–UC352 | Semantics-preserving migration, upgrades, evidence audit method and plugin self-application: W11, Q5–Q9, D3. | S04, S11, S30 considered, approved cases | Old/new obligation equivalence, real installed package behavior and independent protection from self-weakened CI. |

The broader cases (for example cross-repository correlation, package integrity, non-React testing, independent behavioral evidence and self-application) are owner requirements augmented with the method above; they are not claims that one upstream Skill already implemented all of them.

## Activation, tools and overlap

`SKILL.md` metadata covers create/review/debug/migrate/optimize GitHub Actions, missing tests/evaluations, selective CI, matrix/reuse/runner/artifact contracts, misleading outcomes and plugin self-application. It does not claim ownership of standalone organization governance, supply-chain policy or production release operation. CI consumes those owners' genuine contracts and statuses.

| Shared capability | Current session observation | Runtime/packaging consequence |
| --- | --- | --- |
| CAP-01 | Native reads, `rg` and Git worked; command-scoped safe.directory used. Local `main` remained at base commit. | No global Git configuration change. Consumer local state must be inspected independently. |
| CAP-02 | Existing `C:\Program Files\GitHub CLI\gh.exe` reports 2.102.0; not resolved through sandbox PATH. `gh auth status`: no logged-in host. `gh skill --help` responds. | CLI presence/command support confirmed; authenticated operations not established. Use connected capabilities where sufficient; no install/login attempted. |
| CAP-03 | Official MCP `get_me` authenticated as owner and read public Action metadata; existing GitHub connector read remote project file. Official MCP read returned remote main `09b514f344f7abfdc7a095ff156f2398e5d0991c`. | Reads/auth confirmed for exercised scope. Private repos, settings/writes and Actions execution not verified. Inspect actual exposed methods and scopes. |
| CAP-04 | Context7 resolve + targeted query responded. | Existing documentation fallback operational; not proof of runner execution. |
| CAP-05 | Web and Exa discovery returned official/community/tutorial material. | Use targeted research and attributable claims; no live transcript claim. |
| CAP-06 | Scrapling standalone HTTP requests returned 200 for specification/artifact docs. | Existing retrieval works for those pages. No persistent browser session created or service installed. |
| CAP-07 | Existing `gh aw version`: v0.93.2. `gh extension list` requested authentication and did not enumerate extensions. | Version command works; full setup/authentication/Windows execution compatibility unverified. Optional, not a deterministic-CI dependency. |
| CAP-08 | Manifest readable, selected identities match and scoped paths present as recorded above. | Build-time provenance only; do not ship machine paths or activate source inputs. |
| CAP-09 | User-selected `C:\Users\kerol\.agents\skills\skill-creator\SKILL.md` read and applied for authoring; user restricted evaluation/packaging stages. | Skill Creator is build-time tooling. Plugin Creator/host manifest work not started. |
| CAP-10 | Source metadata/example and official semantic docs inspected. | No Action, Marketplace App or paid service selected for a real consumer pipeline; validate trust/release/cost per target. |

Current overlap with installed general CI/QA Skills is resolved through ordinary host discovery and task scope. This new Skill supplies the domain workflow; it does not import duplicate tool servers or automatically call all upstream Skills. No custom router, hooks, scripts, assets or advanced retrieval infrastructure were introduced.

## Evidence levels and outstanding dependencies

| Evidence level | Status and limit |
| --- | --- |
| Authoring/source inspection | Required four runtime Markdown artifacts and this handoff created; names/references and source identity inspected. This is not an executed validator or acceptance suite. |
| Behavioral evaluation / independent case catalog | **Not run / not created in this stage.** No baseline, assertions, benchmark, variance score, trigger optimization or scenario pass-rate claim. The owner requires separate authorization. |
| Host runtime / packaging | **Not verified.** Agent Skills format was consulted; installation, discovery, activation and execution in Codex/other hosts have not been exercised. No manifest/package/activation change. |
| GitHub integration | Read capabilities observed as above; **pipeline execution and enforcement not verified**. No workflows, check/ruleset mutations, dispatches or test pushes. |
| Release/deployment | **Not started / not verified.** No target, credentials, publication, release or production operation performed. |

Plugin Creator receives the four portable runtime files, this provenance/readiness record, capability/fallback requirements and cross-domain dependencies. Keep final supported hosts, manifests, external connector setup, installation/discovery, package license/notices and runnable package acceptance with that later authorized stage. The runtime files do not depend on this repository's goal/catalog or workstation source paths.

Governance owns effective rulesets, trusted App identity/grants and check migrations. Security owns threat/scan/integrity/attestation policy. Release/Reliability owns protected environments, promotion, rollout and recovery. Domains 2–4 remain uncreated pending their approved requirements; no source-derived substitute goal was invented.

Next executable stage, **when requested**: define an independent evaluation catalog that maps individual canonical use cases and negative scenarios to variants, observed decisions/tools and acceptance evidence, then execute within approved safe environments and report structure, behavior, host runtime and GitHub integration separately. Packaging/activation follows its own authorization. No authoring blocker remains; target permissions/credentials/providers/fixtures and host support remain dependencies for those later claims.
