# Quality gates and evaluations

Use this reference to turn repository obligations into observable quality signals. Its instructions describe runtime engineering when authorized; authoring this skill does not authorize creating or running an evaluation suite. Recheck selected framework/Action APIs against current official sources.

## Q1. Define the behavior and its real producer

For each relevant component or change, connect the intended behavior to its tests, actual collection/execution command, runner environment, report and merge verdict. Read assertions and fixtures rather than judging test names or file counts. Separate confirmed missing coverage from inferred gaps. Inspect direct and indirect coverage before declaring a module untested.

Choose the lowest practical level that proves the behavior. Use unit/component tests for isolated logic and interaction, integration/contract tests for service/data boundaries and E2E for critical journeys across the actual system. Do not impose a framework, testing-pyramid ratio or coverage percentage on every repository. Derive support combinations and thresholds from approved policy, risk and baseline. Reuse nearby test conventions and existing accepted services.

When missing-test implementation is authorized, add concrete assertions for applicable successful, failure, edge, data-validation, permission and regression behavior. Generated stubs, rendering alone, keyword checks and snapshot mass updates do not prove the intended contract. Mocks are useful only when they preserve the boundary being claimed; use a real supported engine/provider in controlled integration where a substitute would conceal incompatibility.

Keep scoped review scoped. Do not turn a CI question into an unbounded general audit. New suites, tools, report categories or shared policy changes follow the consumer's approval rules. Do not import upstream audit scripts or scaffolding just because they exist.

## Q2. Truthful unit and component execution

Inspect wrappers, working directories, runner flags, configuration inheritance, glob patterns and module/workspace discovery. Root commands can omit nested Go modules, Maven integration phases, Jest projects or Python directories. Enumerate the intended execution units rather than assuming one root invocation reaches everything.

Preserve nonzero exits through shell pipelines, reporters and process wrappers using the actual shell's supported error handling. Avoid `|| true`, unconditional success exits or permissive test flags in mandatory paths. Decide explicitly whether zero tests is valid for the selected scope; zero collection for an expected suite is incomplete validation.

Use isolated fixtures, controlled clocks/locale and supported feature-flag states. Cover parser boundaries and hostile inputs where behavior demands it; assert accessibility/semantic interaction when appropriate. Bound hung tests/processes and capture identifiers. A clean environment should not depend on developer globals, stale generated files or a previous runner's build output.

Keep test counts, suite IDs, failed assertions and useful diffs. Emit partial JUnit/other reports on failure where possible without masking the original exit. Bind reports to the tested SHA, configuration and attempt; an old XML file in a persistent workspace is not current evidence.

## Q3. Integration, migrations and E2E

Declare the required database/broker/API/IdP/certificate/network prerequisites, owners and readiness signals. Use service health checks and bounded readiness probes instead of arbitrary sleeps. Isolate ports, schemas, data namespaces and identities across parallel jobs. A private dependency with no runner route is a named infrastructure blocker.

Validate migrations against representative existing-data upgrade fixtures as well as fresh databases. Test only supported rollback behavior; do not assume destructive migrations are reversible. Cover transaction/locking/concurrent startup risks and schema drift. Validate provider/consumer and routed error contracts, generated clients and protocol compatibility against the intended versions.

Use synthetic or approved sanitized data, scoped identities and safe cleanup. Do not point fixtures at shared staging data by default. Make time-based expiry assumptions controllable. Separate external sandbox outages from deterministic application assertions, and make repeated simulated transactions idempotent.

For E2E, identify the deployed/preview revision and readiness before launching a browser. Exercise critical behavior such as signup/checkout across service boundaries, not merely a loaded page. Cover supported browsers/devices, region/timezone/locale and feature modes according to requirements. Pin relevant test-environment dependencies, then review visual changes rather than blindly updating snapshots.

Retain useful traces, screenshots, browser/server logs and sanitized network metadata on failure. Keep accessibility and semantic assertions complementary to visual comparisons. Isolate test accounts across shards. If fork secrets or preview access are unavailable, provide the feasible unprivileged checks and report the missing journey coverage. Coordinate lifecycle cleanup for cancelled previews with the environment owner, without granting PR code privileged cleanup credentials.

## Q4. Shards, retries, flakes and completeness

Define an expected test inventory and deterministic shard membership for the tested revision. Check the union matches intended collection, account for duplicates, and ensure reruns retain traceable membership. Balance by representative timings without silently omitting long or platform-specific tests. Decide `fail-fast` based on evidence needs and capacity.

For every mandatory shard, require a result record and distinguish assertion failure, timeout, OOM/process crash, infrastructure failure, cancellation and no collection. Missing XML after a crash is not a zero-failure report. Guard report merging against duplicates and missing producers. Do not merge results from different SHAs or incompatible environments as one coverage claim.

Bound retries by failure class and operation idempotence. Retain original failures, attempt counts and final outcomes so eventual success does not erase flakiness. Track OS/configuration-specific flake rates separately from deterministic failures. Quarantine requires an approved owner, reason, scope, expiry and restoration condition; keep quarantined signal visible. Do not create a permanent silent exclusion to make the pipeline green.

Contain shared-resource collisions and runaway evidence volume. Set per-test/job timeouts, disk/artifact budgets and cleanup around isolated resources. Report incomplete diagnostic evidence when a runner disappears rather than fabricating a root cause.

## Q5. Coverage, regression and quality policy

Assess behavior and changed critical paths alongside applicable line/branch/diff coverage. Review generated/vendor exclusions, merged report revision and discovery scope. A higher global ratio can hide lost branch coverage, deleted regression assertions or a renamed test outside collection.

Inspect policy/configuration diffs as well as production/test code. Flag reduced lint severity, narrower typecheck scope, disabled assertions, `continue-on-error` on required work, snapshot replacement and altered evaluation thresholds. Temporary exceptions need the authorized owner, reason, expiry and explicit remaining risk. Stage tighter policy with owners when necessary; do not choose a lower threshold to conceal an existing failure.

Choose an authoritative result when multiple reporters disagree, preserving original evidence. Integrate the target's accepted SonarQube, coverage, lint/typecheck or security service rather than recreating it locally. Verify actual project/configuration, analyzed revision, gate computation and check source. A dashboard badge or report upload success does not establish the gate passed.

Security scans and supply-chain policy belong to their owners; CI configures the approved runner integration and consumes its genuine verdict. Never impersonate another App's status or replace an inaccessible scanner with a fabricated success. Record unsupported repository visibility, license/plan, permissions or external-service access as prerequisites.

## Q6. Agent and plugin behavioral evaluations

First establish authorization, the intended behavior, protected policy and existing evaluator/host. Use the approved use-case catalog and actual failures to select scenarios. Keep an independent held-out set outside the skill's instructions; do not place golden answers into runtime guidance. A source-to-case map is design traceability, not a passed evaluation.

Prefer assertions on observable outcomes and trace evidence: repository findings, selected tools, actual retrieved sources, changed artifacts, respected permissions, genuine blockers and absence of invented results. Keyword matching alone cannot establish safe engineering. Include negative/adversarial boundaries such as untrusted log instructions, missing credentials, conflicting policy and stale revision; use isolated safe fixtures, not a production privilege experiment.

When selected for a real target, inspect an existing evaluation integration such as Promptfoo through its official documentation/source, runner/runtime support, model/provider availability, cost, secrets and output contract. Do not require one provider or install its CLI in shared workstation tools. Deterministic structural checks complement scenario execution; neither replaces it.

For stochastic or judged cases, record the skill/package revision, case dataset revision, model/provider/version, available tools, environment, judge/rubric/version and repeated observations appropriate to the risk. Calibrate subjective judgment against human-reviewed examples; separate hard security/permission invariants from weighted quality scores. Pinning a model name alone does not prove reproducibility.

Make missing/crashed/timeout cases explicit and compare completed count with the expected set. Preserve per-case outcomes and tool traces so an aggregate mean cannot hide a critical failure. Report variance and baseline comparison only when actually measured under comparable conditions. Keep provider failures distinct from behavior failures. Redact sensitive fixtures/logs and retain useful evidence under the consumer's policy.

Threshold, fixture and grader changes need independent policy review when the same change could weaken its own gate. Verify the installed/packaged skill in the intended host as well as prompt-level behavior; stale source copies, missing references or undiscoverable packages invalidate the runtime claim. Establish the supported host/packaging contract first rather than inventing a manifest.

Sources: [Promptfoo Action source](https://github.com/promptfoo/promptfoo-action), [Agent Skills specification](https://agentskills.io/specification). The former is a candidate integration, not an executed or mandatory dependency.

## Q7. Required checks, aggregate verdicts and merge queue

Inspect the effective branch/ruleset configuration, exact check contexts and trusted producing App/source where available. Workflow display names, job names, matrix names and check contexts are not interchangeable. Avoid duplicate ambiguous producers. Keep a stable aggregate name when dynamic matrices or selective CI feed a required verdict.

GitHub can accept skipped/neutral checks in circumstances where the project's mandatory behavior never executed. A workflow excluded by event/path/branch/commit filtering may leave a required check pending, while a job condition can produce an accepted skip. Define the stronger engineering contract explicitly rather than relying on the UI's color.

The aggregate needs an authoritative expected producer set, selection result and revision/run identity. Treat outcome reduction as a contract, implemented with the target's established tools:

| Evidence | Engineering treatment |
| --- | --- |
| All expected mandatory producers ran successfully with required reports | Eligible to pass for this event/revision, subject to other policy. |
| Intentional non-applicability established by a successful trusted selector | Accept the documented skip only for that scope; report what was excluded. |
| Selector failure, invalid selection data or unknown impact | Fail/incomplete; do not create an empty successful matrix. |
| Any mandatory failure, timeout, cancellation, unexplained skip or absent producer | Do not pass. Preserve cause and incomplete coverage. |
| Success report for another SHA, attempt, event or source App | Reject as evidence for this verdict. |
| Report download succeeded but expected cases/shards/artifacts are missing | Incomplete; uploader success is insufficient. |

Use explicit `needs` for all mandatory jobs and a suitable terminal condition so upstream failure does not silently skip the verdict job. Verify each branch of that reduction when authorized. Cancellation or runner loss may prevent the verdict from executing; retain incomplete status, not a promise of guaranteed finalization.

For merge queues, trigger the required validation on `merge_group: checks_requested`, compute scope for the combined revision and publish stable checks against its SHA. Reuse PR support obligations but do not substitute PR-only results. Include the relevant draft/ready/reopen/force-push lifecycle; old green checks must not credit a newer revision.

Verify required-check eligibility for the actual event. Current GitHub.com troubleshooting documentation states that a passing `workflow_dispatch` run does not satisfy a PR's required workflow check simply because it uses the same head SHA. An authorized manual run is useful execution evidence, not automatically evidence of merge enforcement. Check target-platform behavior rather than assuming all check origins are equivalent.

For check-name or App-source migration, coordinate with Governance: establish the new producer, observe genuine eligible results, update the authorized rule and retire the old producer in a compatible sequence. Do not remove protections or bypass required work to resolve a pending check. Inspect ruleset/merge-queue interactions and protected branch applicability; emergency paths still need the owner's enforceable minimum contract.

Sources: [required-status troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks), [merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue), [job conditions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-jobs-with-conditions). Retrieved 2026-10-25; GHES feature/version applicability remains target-specific.

## Q8. Package, artifact and evidence contracts

Build deliverables from the tested source and verify the actual packaged bytes rather than rebuilding a replacement during smoke checks. For libraries/executables, inspect expected assets, metadata/versions, supported platform outputs and installation/start/import behavior in a clean supported environment. Assert packaging/codegen does not silently mutate tracked source or use stale schemas. A successful upload with no expected files is not a complete package.

For plugins, inspect the approved host contract, required `SKILL.md`, referenced resources, manifest/dependency declarations and portable archive layout. Reject unsafe paths, traversal, escaping symlinks and unintended workstation/secret material. Compare installed package identity with the reviewed source. Do not claim host compatibility from valid YAML or correct file names alone.

Identify artifacts with repository, workflow, tested SHA, run ID, attempt, configuration/shard, expected file inventory and content digest. Validate extraction boundaries, expected producers and report schemas before consuming untrusted archives. Do not execute a lower-trust artifact in a privileged job. Preserve raw reports alongside normalized essentials when the existing evidence system supports it.

Current GitHub artifact documentation describes automatic digest comparison on download, with a mismatch reported as a warning. When integrity is mandatory, enforce an explicit rejecting comparison or verification step; do not assume the warning blocks the job. Digest equality proves content identity, not trusted origin. Security owns additional attestation/signature policy, and Release owns promotion of the accepted artifact.

Set retention/access to incident response, rerun and consumer needs while minimizing personal data, secret-bearing logs and oversized browser media. A cache is not durable release storage. Record expired/unavailable evidence as a gap; an external dashboard that has disappeared cannot support a present pass claim.

Sources: [artifacts concepts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts), [artifact tutorial and digest behavior](https://docs.github.com/en/actions/tutorials/store-and-share-data). Retrieved 2026-10-25.

## Q9. Separate evidence levels

| Level | Can establish | Cannot establish by itself |
| --- | --- | --- |
| Structure/source inspection | Declared commands, layout, syntax or intended gate policy | Executed behavior, complete reports or enforcement. |
| Local/unit execution | Observed behavior in that local environment | Remote runner access, GitHub event or merge policy. |
| Scenario/evaluation execution | Observed outcomes/traces for the cases and configuration exercised | Unrun cases, other hosts, packaging or production safety. |
| Packaged host execution | Installation/discovery and observed installed behavior | Authentic GitHub statuses or deployment. |
| GitHub integration | Actual event/revision jobs, checks, artifacts and observed policy | Untested events/platforms or successful deployment. |
| Deployment/operational evidence | The particular authorized rollout and observed health | Universal correctness or future reliability. |

For each relevant claim, return Passed / Failed / Blocked / Not Verified with its supporting command, path or immutable run/check evidence. A review of this reference is authoring work, not a behavioral evaluation. Maintain no success counters for unexecuted scenarios.

## Q10. Augmentation choices

This method uses S07 quality-gate sequencing, S19 risk/behavior-oriented testing, S27 test-gap investigation and S22 outcome/rubric/trace concepts. S19's React/Next.js examples, 80% sample threshold and framework-specific scaffolding are not general defaults. S22's self-reflection and generated tests are not independent evidence of correctness. S27's blanket full-repository audit/report workflow is not automatically authorized by a scoped CI request. No source scripts or evaluator loops are bundled.
