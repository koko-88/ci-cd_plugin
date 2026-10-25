# Workflow design and execution

Load the matching section for the current decision. This is an engineering method, not a ready-to-run template. Recheck current syntax, Action releases and target GitHub/GHES support before implementation. Official sources below were retrieved on 2026-10-25.

## W1. Repository topology and acceptance

Build a small execution inventory from actual manifests, scripts, workspace/module declarations, lockfiles, workflows and tests. Identify each maintained component, generated/vendor exclusions, supported runtime/OS/architecture, command owner, service dependency, result producer and current required status. Read wrapper scripts far enough to find hidden commands, swallowed exit codes and nested suites. A file named `test` or an existing report is not evidence it runs.

When documents and implementation disagree, identify the conflicting path and consequence. Approved product/support decisions govern the intended result; code reveals the existing behavior. Do not silently use whichever version is newest. Separate inherited baseline failures from introduced changes and identify missing licenses, registry access, external artifacts, network paths and secrets by name/scope without reading their values.

Use this inventory to define real obligations. A library may require install/import and consumer compatibility; an app may require a running service and user journey; an agent plugin needs discovery and behavior in addition to valid files. Preserve the existing accepted checks while resolving omissions. Establish timing/queue/flake baselines only from comparable observations; unknown cost stays unknown.

## W2. Events, refs and lifecycle

For each event, identify workflow revision, code-under-test revision, permission context, expected activity types and consumer of the result. A PR head, PR merge ref, default branch and merge-group SHA are different test inputs. Do not credit a report for the wrong one. Include ready-for-review, reopen and synchronization behavior where required; inspect the intended draft policy rather than assuming drafts should skip.

For merge queue checks, use `merge_group` / `checks_requested` in addition to relevant PR events and test the combined synthetic revision. Do not substitute an individual PR head. Distinguish tag pushes from published-release events and nominate one authoritative release handoff to avoid duplicates; publication itself belongs to the approved release stage.

Scheduled and dispatch workflows have event-specific default-branch/ref behavior. Read the current event documentation before choosing the checkout ref or assuming a manual result is eligible for merge policy. Validate dispatch inputs as data with bounded schemas; an environment string is not authorization. Correlate external request IDs/revisions, reject stale or duplicate requests according to an established persistence/identity mechanism, and expose missing durable deduplication rather than inventing it.

Token-originated events have special recursion behavior. Current GitHub.com documentation permits `workflow_dispatch` and `repository_dispatch` with `GITHUB_TOKEN`, and PR `opened`/`synchronize`/`reopened` events can create approval-required runs; other token-triggered events generally do not start new runs. App/PAT events can behave differently. Inspect actual identity, supported platform and approval state before diagnosing an absent run or proposing a different credential. Guard bot loops with actor/request/ref boundaries and scoped permissions.

Sources: [events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [triggering workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

## W3. Untrusted code and credentials

Separate two questions: who can trigger the job, and which code/data can execute with its privileges? An apparently trusted event can still execute dependency lifecycle scripts or PR-controlled setup. Model the actual token defaults, job overrides, secret availability, repository/fork policy, runner group and external network access. Avoid categorical claims such as “fork validation is safe”: a read-only token does not isolate an internal runner, its files or its network.

Keep fork/Dependabot validation available without privileged secrets where possible. Do not change to `pull_request_target` to make secrets available to PR code. Restrict privileged metadata/reporting to trusted implementation; do not check out and execute untrusted heads, scripts, action paths or artifacts in that context. A `workflow_run` success and a matching artifact name do not establish artifact trust. Check source repository, workflow, event, SHA, run and attempt, then parse bounded data without executing it.

Declare the permissions each job needs. Keep write/reporting/publication and OIDC consumers separate from tests; add a grant only for an identified authorized operation. `id-token: write` requires a real configured federation consumer, not a hypothetical deployment. Omit persistence of checkout credentials when later Git operations do not require them, after checking Action behavior.

Pass PR titles, branch names, dispatch values, matrix data and other untrusted strings through safely quoted data channels instead of expression interpolation into shell/script source. Quote shell variables, validate JSON and multiline output encoding, and use the actual Bash/PowerShell semantics. Redact secret-bearing diagnostics; avoid dumping contexts or environment variables. Protect token-scoped report uploaders and annotation jobs. Missing permissions remain blockers; do not broaden scopes reflexively.

Sources: [secure use](https://docs.github.com/en/actions/reference/security/secure-use), [workflow syntax permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions).

## W4. DAG, conditions, concurrency and cancellation

Draw the relevant dependency graph: producers, shared setup, independent work, fan-in and side effects. Validate every `needs` edge and missing/cyclic/impossible dependency before writing jobs. Keep unrelated fast feedback independent of long suites. Define the mandatory producer set explicitly so failure, unexpected skip or cancellation cannot disappear at the join.

Dependent jobs normally skip after an upstream failure/skip. A bounded verdict/reporting job can use a status condition such as `always()` to remain eligible and explicitly reduce required results; `always()` does not calculate correctness. For ordinary failure-path work that should honor cancellation, consider `!cancelled()`. Avoid unconditional source acquisition or long execution that can hang during cancellation. Set appropriate job/process/test timeouts and preserve partial diagnostics.

Distinguish expected optional skip from absent mandatory execution. A cancelled job is incomplete, not a pass. Workflow cancellation, runner loss or a platform outage can prevent any finalizer from executing; never promise an in-workflow terminal report in all conditions. Required policy must not reinterpret missing evidence as success.

Choose concurrency from work semantics:

| Intent | Decision |
| --- | --- |
| Superseded PR validation | Scope group by workflow and change/ref identity; cancel stale work only when side effects and required-check behavior allow it. |
| Distinct workflows or environments | Namespace keys to avoid unrelated cancellation; inspect inherited caller/callee group values. |
| Stateful work that must all execute | Default concurrency is not a full FIFO: it allows one running and one pending item, replacing the older pending item. Current GitHub.com syntax supports `queue: max` for up to 100 pending items; it cannot combine with `cancel-in-progress: true`. Verify target support, ordering and overflow behavior before adopting it. |
| External exactly-once operation | Concurrency alone does not prove deduplication/idempotence; require operation IDs and the external system's contract. |

Keep run ID, attempt and tested SHA on reruns. Retry only classified transient, idempotent work with bounds. Avoid repeating external mutation as part of a whole-job retry. Invalidate partial downloads and stale authorization; do not treat a later green attempt as evidence the original failure never occurred.

Sources: [jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs), [expressions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions), [concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency), [cancellation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation).

## W5. Runtime, OS, architecture and feature matrices

Derive supported combinations from product contracts, manifests and runtime/toolchain configuration. Distinguish supported customer configurations from forward-compatibility experiments. Removing an awkward required leg is a support-policy change. An obsolete contractual runtime needs an owner decision, not silent removal.

Map shell, filesystem/case sensitivity, locale/timezone, native ABI, browser/font and architecture dependencies to the relevant jobs. Record resolved versions and runner/image details; a versioned hosted-image label still changes over time. An OS label alone does not pin every dependency. Check Action JavaScript/container runtime and minimum runner requirements independently of the application's runtime.

Bound fanout by supported risk and capacity. Choose include/exclude combinations deliberately and explain residual coverage; do not reduce ordinary PRs to one arbitrary platform merely because an upstream template does. Decide `fail-fast` based on required coverage and diagnostic needs. Optional experimental legs need explicit classification and cannot hide required failures with broad `continue-on-error`.

Make artifact names unique by configuration/shard/attempt. Do not depend on concurrent matrix outputs resolving in a useful order. Reduce structured per-leg results with an expected configuration inventory and a stable final status; missing, cancelled or duplicate mandatory records invalidate completeness.

Source: [matrix execution](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations).

## W6. Reusable workflows and composite actions

Choose inline steps for local simple work, a composite action for reusable step behavior within a caller job, or a reusable workflow for shared multi-job interfaces and execution policy. A reusable workflow is called at job level, not as an ordinary step. Avoid making every tiny shell command a separate workflow or imposing one central policy on incompatible consumers.

Define typed `workflow_call` inputs, named secrets, outputs, supported runners, source revisions and failure semantics. Trace each nested edge. Caller workflow-level `env` is not automatic callee configuration; pass intended values explicitly. Nested permissions cannot exceed the caller's ceiling and every workflow must be accessible to the original caller. Prefer named secret forwarding; inspect permitted scope before using `inherit`.

Check the current platform's environment-secret passing rules and precedence, plus actual environment protections. Do not assume a declaration or `required: true` proves a nonempty secret exists. Validate availability without printing values. The callee's environment choice and a same-named environment secret can change the effective input; resolve that contract explicitly.

Pin reviewed external revisions and inspect transitively used Actions. Preserve status names and caller ownership when introducing inputs, defaults, outputs, privileges or job-name changes. Stage compatibility changes and enumerate known consumers before removal. Diagnose composite failures using the real working directory, shell and fetched action revision, including private nested access.

Sources: [reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows), [reusable configuration reference](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

## W7. Monorepo impact and stable selective CI

Compute affected scope from workspace/package/module ownership and dependency edges, including reverse consumers, shared compiler/test configuration, schema/protobuf inputs, codegen and lockfile boundaries. Reconcile root/nested lockfiles, renames and deletions. Verify graph freshness before trusting Nx/Bazel or similar outputs; do not hardcode paths from an old inventory.

Selection needs a complete diff and the correct base/event revision. Shallow history, sparse checkout and changed-file API truncation can hide impact. Inspect current platform/tool limits and fetched history; when incomplete, use a justified conservative execution scope or mark selection unresolved. Keep root configuration and transitive workspace files in the checkout closure.

Use a stable required gate that starts on every required event, with expensive work selected inside the workflow. Do not filter the entire required workflow out for docs-only changes. The selector's own failure must fail the verdict. Carry an explicit expected producer list and reasons for intentional skips. Treat deleted-package work as an intentional no-longer-applicable scope only when current topology confirms it.

Balance fanout with capacity without losing mandatory tests. Include multiple owners' obligations and assert generated tracked files remain consistent. Path-only optimizations require evidence that dependencies, shared configuration and non-source assets cannot invalidate them.

Sources: [workflow syntax filters](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [required-check troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).

## W8. Cross-repository compatibility and orchestration

Identify producer and consumers, candidate artifact/schema/workflow versions, supported compatibility combinations and authorized identity. Test the candidate revision, not mutable `latest` or a consumer's unrelated main build. Record all participating revisions when branches evolve concurrently.

Define request ID, target/source repository, tested SHA, run/attempt, result schema, expiry and authentication. Bind returned status to that tuple and expected check source. Missing, late, duplicated, out-of-order or inaccessible results remain incomplete. Preserve raw reports when normalizing formats. Make deadlines and retention explicit; refresh expired candidates through their genuine producer rather than relabelling old evidence.

Repository-scoped `GITHUB_TOKEN` access is not a cross-repository grant. Reuse an approved least-privilege App/credential where the operation requires it; report exact missing access and owner. Do not send cross-repository dispatches or mutate consumers merely to explore capability. Regional mirrors and external artifacts need content identity, not name/version equality alone.

## W9. Reproducible environment and runner boundaries

Use the project's declared toolchain, lockfile installation semantics and approved dependency sources. Provision required tools explicitly on runners; do not assume an image still includes them. Record resolved versions, environment fingerprint and differences that explain platform-specific bytes or snapshots. Preserve a working cold path when caches are absent.

Select hosted compute for supported public requirements; choose authorized network-capable compute when private dependencies demand it. Inspect OS/architecture, service/container support, licenses, disk/memory, runner versions and capacity. A private runner label does not establish isolation or accessibility. Keep public/untrusted contributions off privileged internal runners; use ephemeral isolation and credential/workspace hygiene where required. A workspace cleanup cannot by itself undo a malicious persistent runner compromise.

Use controlled integration services and readiness probes, isolated ports/namespaces and scoped test identities. Air-gapped builds need approved mirrors; missing proprietary licenses, registry grants or certificates remain specific blockers. Never repurpose production signing keys for ordinary CI. Diagnose runner startup/queue/network/disk faults separately from application defects.

Sources: [self-hosted runners](https://docs.github.com/en/actions/reference/runners/self-hosted-runners), [secure use](https://docs.github.com/en/actions/reference/security/secure-use), [Actions policies](https://docs.github.com/en/actions/concepts/about-actions-policies).

## W10. Caches, artifacts and performance

Key caches by dependency lock/configuration, runtime/toolchain, OS/architecture/ABI and relevant build inputs. Separate dependency downloads from generated binaries. Bound fallback keys; broad restores can return incompatible state. Respect cache access/trust boundaries, exclude tokens/decrypted configuration, and do not feed low-trust executable caches into privileged jobs. Prove correctness without a cache when verification is authorized.

Use artifacts for tested deliverables and reports, with source/run/content identity and retention suitable for their consumers. Caches are disposable acceleration, not release storage. Security and Release owners define provenance/signing/promotion policy; CI carries genuine evidence into the handoff.

Measure comparable samples: queue time, first actionable feedback, end-to-end critical path, total runner minutes, upload/download time and retry/flake rates. Avoid declaring success from a fastest run or unmeasured estimate. Compare like events/configurations and separate image/provider variance from a code change.

Prioritize evidenced waste: redundant equivalent work, unnecessary serial dependencies, repeated downloads, obsolete work and excessive supported fanout. Preserve checks with different targets despite similar names. Optimize expensive artifact compression/retention and reuse granularity when data supports it. Capacity/budget changes need actual allocation constraints; do not invent a percentage or silently trade coverage for cost.

Source: [dependency caching](https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching).

## W11. Migration, upgrades and self-application

Inventory old pipeline behavior, including Jenkins/GitLab post-build checks, external status producers, environments, test collection, artifact contracts and cancellation behavior. Map each obligation to its new producer before retiring the old path. Compare representative success/failure evidence only in an authorized verification stage. No baseline means equivalence is not established.

For Action/runner upgrades, inspect current metadata, vendor release notes, support/runtime requirements, permissions, inputs/defaults and artifact protocol compatibility. Resolve the reviewed release to a real commit; record what changed and what remains unverified. Keep unrelated behavior stable and isolate changes sufficiently for diagnosis without imposing an unauthorized commit strategy.

Apply the same method to this plugin when requested: inspect the actual plugin/host contract, then package completeness, discovery, behavior and GitHub enforcement as separate obligations. Do not create this repository's CI, installation configuration or release process merely because its CI Skill has been authored. Domain-specific runtime dependencies must be declared by the later packaging owner.

## W12. Source interpretation

The method synthesizes source-selection ideas from manifest S07/S11, execution variants from S08/S10/A01/I01, efficiency from S02 and upgrade discipline from S04. Pinned provenance and rejected advice are recorded in the build-time domain handoff. Upstream scripts, fixed stacks/thresholds, broad deployment defaults and automatic writebacks are not runtime dependencies.

Source review exposed unsafe simplifications: fork jobs are not automatically safe, a fixed hosted OS label does not freeze an image, path filtering can abandon required checks, `cancel-in-progress: false` is not a durable queue, and old runtime/Action examples are not current release recommendations. Prefer the current official sources cited above and actual target evidence.
