# CI/CD & Quality Engineering — Goals & Real-Production Use Cases

**Parent:** GitHub Operations Engineering Plugin  
**Domain:** CI/CD & Quality Engineering (first of four domain skills)  
**Created:** 2026-10-23  
**Stage:** goal and scenario requirements for later Skill Creator/Augmentation; not an implemented skill or passing test report.

## Domain goal

Make a compatible coding agent capable of inspecting any target repository, identifying its actual integration and quality needs, selecting maintained GitHub Actions/workflows and Marketplace integrations on demand, building and maintaining CI pipelines, implementing missing relevant tests/evaluations and quality gates, diagnosing production-scale failure cases, and delivering truthful GitHub-run evidence. This skill integrates with but does not replace the separate GitHub Platform & Governance, Security & Supply Chain, and Release/Deployment & Reliability domains.

**Non-negotiable execution model:** GitHub CLI/MCP and authoritative documentation supply live context. Reference repositories and Actions are discovered, not bulk cloned. Security scanners, testing frameworks, and packaging tools required in target pipelines execute in GitHub Actions runners instead of being installed into the user's shared local tooling repository. No fabricated checks, tokens, approvals, deployment targets, or verified outcomes.

## Use-case acceptance contract

Each UC below describes a realistic failure, conflicting constraint, or enterprise-scale need. Successful future agent behavior must: detect the issue from repository or run evidence; make a justified engineering decision; implement an appropriate workflow/test/configuration change; preserve permissions and required-check semantics; verify against actual GitHub statuses and artifacts where authorized; and declare Pass, Fail, Blocked, or Not Verified with exact missing prerequisites. An independent evaluation catalog must later map every UC to loaded skill variants, decision traces, negative cases and acceptance evidence.

## Goals and incident-driven use cases

### 01 Repository intelligence and requirements

#### G001 — Map real build and test topology

**Goal:** Map real build and test topology across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC001:** Multi-language repo has hidden test commands: derive them from manifests and workflows.
- **UC002:** Vendored sources inflate test discovery: distinguish maintained from generated code.
- **UC003:** README runtime conflicts with lockfile and workflows: report exact contract discrepancy.
- **UC004:** Test files exist but package scripts never execute them: expose missing suites.

#### G002 — Capture repository quality obligations

**Goal:** Capture repository quality obligations across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC005:** Branch rules require check names not present: reconcile actual status producers.
- **UC006:** Compliance constraints contradict inherited workflow defaults: surface decision owners before edits.
- **UC007:** Existing green workflow does not assert behavior: identify fake confidence.
- **UC008:** CI should apply to libraries and apps differently: detect package and deployment boundaries.

#### G003 — Inventory external execution requirements

**Goal:** Inventory external execution requirements across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC009:** DB tests require undocumented broker and schema: identify ownership and readiness.
- **UC010:** Runner needs private-network access: do not assume GitHub-hosted connectivity.
- **UC011:** Workflows reference removed secrets and outdated actions: classify blockers.
- **UC012:** Cross-repo test needs external artifact: identify producing commit and access requirements.

#### G004 — Define credible baseline and acceptance

**Goal:** Define credible baseline and acceptance across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC013:** Existing main branch already fails tests: separate inherited from introduced failures.
- **UC014:** Historical check name is no longer stable: define deterministic merge gate.
- **UC015:** CI cost is unknown: capture runtime, queue and flake baseline.
- **UC016:** Missing credentials prevent verification: mark blocked rather than green.

### 02 Trigger and event engineering

#### G005 — Cover workflow lifecycle events

**Goal:** Cover workflow lifecycle events across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC017:** PR passes but merge-group event never triggers: validate queued synthetic commit.
- **UC018:** Release fires twice from tag push and release event: select authoritative source.
- **UC019:** Fork PR requests privileged trigger: keep safe validation available without secrets.
- **UC020:** Deletion or unrelated dispatch triggers CI: narrow event types.

#### G006 — Reconcile paths and required checks

**Goal:** Reconcile paths and required checks across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC021:** Required workflow path-filtered to zero jobs: prevent permanently pending check.
- **UC022:** Docs-only PR must avoid expensive stages yet emit stable required verdict.
- **UC023:** Negated path pattern excludes shared config change: restore correct impact selection.
- **UC024:** Workflow schedule reads default branch instead of feature ref: document semantics.

#### G007 — Govern manual and external triggers

**Goal:** Govern manual and external triggers across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC025:** Manual run takes arbitrary environment input: constrain values and authorizations.
- **UC026:** External system sends duplicate repository_dispatch events: deduplicate request IDs.
- **UC027:** Daily maintenance overlaps urgent PR queue: partition capacity deliberately.
- **UC028:** Bot-written commit retriggers itself forever: stop automation loops.

#### G008 — Handle event race and revision identity

**Goal:** Handle event race and revision identity across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC029:** Force-push occurs during CI: do not credit stale commit results.
- **UC030:** Draft PR becomes ready after old check: require current lifecycle validation.
- **UC031:** Merge queue groups multiple PR heads: test combined state, not individuals.
- **UC032:** New upstream event subtype starts unexpected workflow: pin intended activity.

### 03 CI trust boundaries and job credentials

#### G009 — Safely validate untrusted contributions

**Goal:** Safely validate untrusted contributions across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC033:** Fork can edit setup scripts: run checks without privileged credentials.
- **UC034:** Privileged PR comment workflow executes PR head code: split trusted and untrusted steps.
- **UC035:** workflow_run downloads lower-trust artifact: inspect trust and never execute unverified input.
- **UC036:** Dependabot PR lacks regular secrets: provide supported safe route.

#### G010 — Enforce least-privilege CI permissions

**Goal:** Enforce least-privilege CI permissions across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC037:** Unit test job requests contents write for unrelated publishing: separate scopes.
- **UC038:** Action upgrade adds packages write requirement: review risk before escalation.
- **UC039:** id-token write granted without OIDC consumer: remove needless capability.
- **UC040:** Org changes default GITHUB_TOKEN permissions: explicitly scope jobs.

#### G011 — Protect context and output channels

**Goal:** Protect context and output channels across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC041:** PR title interpolated into shell command: pass untrusted text as data.
- **UC042:** Failure diagnostic leaks environment variables: redact without losing root cause.
- **UC043:** Untrusted multiline output breaks GITHUB_OUTPUT parsing: encode safely.
- **UC044:** Third-party test uploader sees excessive repo scope: minimize authorization.

#### G012 — Respect contributor and runner boundaries

**Goal:** Respect contributor and runner boundaries across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC045:** First-time contributor needs approval for expensive jobs: enforce entry policy.
- **UC046:** Public fork scheduled onto internal runner: block unsafe runner group.
- **UC047:** Bot needs to write PR annotation: separate reporting identity from tests.
- **UC048:** New event policy blocks pull_request_target: redesign instead of bypass.

### 04 Workflow DAG and failure semantics

#### G013 — Construct correct job dependency graphs

**Goal:** Construct correct job dependency graphs across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC049:** Test fan-in starts before every matrix leg completes: model explicit needs.
- **UC050:** Matrix failure causes required aggregator to skip: force truthful terminal verdict.
- **UC051:** Unrelated lint waits on browser suite: parallelize safe independent stages.
- **UC052:** Circular dependency or impossible needs graph: detect before commit.

#### G014 — Model conditional execution honestly

**Goal:** Model conditional execution honestly across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC053:** Log upload skipped after failed test: retain diagnostics on failure.
- **UC054:** Advisory benchmark blocks mandatory unit tests: distinguish gate classes.
- **UC055:** Cancelled run appears as passed check: propagate cancellations.
- **UC056:** Dependent check skipped on upstream failure: avoid false-green aggregator.

#### G015 — Control concurrency by workflow intent

**Goal:** Control concurrency by workflow intent across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC057:** Old PR head consumes expensive work: cancel stale run only.
- **UC058:** Different workflows share same group key: prevent accidental cross-cancellation.
- **UC059:** Stateful validation needs queueing not last-pending replacement: choose semantics.
- **UC060:** Queue contains outdated SHA after force-push: reject stale authorization.

#### G016 — Keep reruns safe and attributable

**Goal:** Keep reruns safe and attributable across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC061:** Registry transient failure leads to unsafe retries: bound only idempotent operations.
- **UC062:** Job rerun repeats external mutation: isolate side effects.
- **UC063:** Download interruption leaves partial artifact: fail integrity validation.
- **UC064:** Retried run reports on wrong head SHA: correlate event and run.

### 05 Runtime and OS matrix coverage

#### G017 — Enforce supported language versions

**Goal:** Enforce supported language versions across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC065:** Package supports multiple Node versions but tests latest only: cover supported set.
- **UC066:** Deprecated Python version is contractual: surface support decision.
- **UC067:** Latest runtime fails while stable passes: separate future compatibility from required.
- **UC068:** Runtime resolves mutable patch: record exact tested version.

#### G018 — Verify cross-platform compatibility

**Goal:** Verify cross-platform compatibility across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC069:** Windows case-insensitive paths hide Linux bugs: test relevant platforms.
- **UC070:** Native dependency fails ARM64: cover architecture or explicitly block claim.
- **UC071:** macOS build uses unavailable Ubuntu tool: map platform-only job.
- **UC072:** PowerShell quoting differs from Bash: retain equivalent assertions.

#### G019 — Bound matrix combinations intelligently

**Goal:** Bound matrix combinations intelligently across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC073:** OS times runtime times feature flags creates unsustainable jobs: use risk-driven matrix.
- **UC074:** Required supported customer combination was excluded: detect coverage violation.
- **UC075:** fail-fast hides remaining platform failures: choose diagnosable strategy.
- **UC076:** Expensive browser suites need representative matrix: document residual risk.

#### G020 — Aggregate matrix outcomes correctly

**Goal:** Aggregate matrix outcomes correctly across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC077:** Concurrent shards upload same artifact name: isolate names.
- **UC078:** Dynamic job names cannot be set as required checks: expose stable summary.
- **UC079:** One OS job cancelled among passes: block mandatory quality verdict.
- **UC080:** Matrix output resolves arbitrary last writer: implement deterministic reduction.

### 06 Reusable workflows and action composition

#### G021 — Specify reusable workflow interfaces

**Goal:** Specify reusable workflow interfaces across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC081:** Caller sends unsupported workflow_call input: validate schema.
- **UC082:** Nested callee requests privilege caller lacks: detect permission ceiling.
- **UC083:** Caller environment variable vanishes in callee: pass contract explicitly.
- **UC084:** Secret inheritance crosses unintended trust domain: constrain propagation.

#### G022 — Choose reusable component boundaries

**Goal:** Choose reusable component boundaries across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC085:** Three repos copy divergent test setup: consolidate verified shared logic.
- **UC086:** Tiny shell helper adds full reusable-workflow overhead: use suitable component kind.
- **UC087:** Monolithic template lacks required extension point: define bounded variant interface.
- **UC088:** Central workflow overwrites local test policy: preserve caller ownership.

#### G023 — Version reusable workflows safely

**Goal:** Version reusable workflows safely across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC089:** New mandatory input breaks all callers: stage compatible version.
- **UC090:** Consumer pins vulnerable old workflow revision: plan evidence-backed upgrade.
- **UC091:** Central job rename breaks branch protection: maintain status migration.
- **UC092:** Nested dependency upgrade changes effective permissions: trace full call chain.

#### G024 — Troubleshoot nested and composite actions

**Goal:** Troubleshoot nested and composite actions across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC093:** Third-level callee fails mysteriously: trace inputs, commit SHA and needs.
- **UC094:** Composite shell uses Bash on Windows: account for executor semantics.
- **UC095:** Reusable workflow reports green after silent internal skip: verify child coverage.
- **UC096:** Caller cannot access private nested workflow: detect scope and accessibility.

### 07 Monorepo impact and selective CI

#### G025 — Build change-impact dependency graph

**Goal:** Build change-impact dependency graph across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC097:** API package change breaks sibling consumers yet filters skip them: include reverse dependents.
- **UC098:** Shared toolchain config change affects all services: fan out mandatory checks.
- **UC099:** Package rename invalidates path map: rebuild inventory from current manifests.
- **UC100:** Monorepo PR touches independent apps: avoid full suite with proven graph.

#### G026 — Preserve stable gates under selective execution

**Goal:** Preserve stable gates under selective execution across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC101:** Filter skips required status entirely: provide always-running completion check.
- **UC102:** Package deleted and test command no longer exists: report scope-aware result.
- **UC103:** Dynamic matrix job names break required status: keep deterministic gateway.
- **UC104:** Sparse checkout omits root config and fails incorrectly: preserve workspace closure.

#### G027 — Support heterogeneous monorepo tooling

**Goal:** Support heterogeneous monorepo tooling across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC105:** pnpm workspaces and Python services share one CI policy: detect proper commands.
- **UC106:** Protobuf change affects consumers outside changed paths: include generated-contract users.
- **UC107:** Nested lockfiles contradict root version: select authoritative dependency scope.
- **UC108:** Nx or Bazel dependency graph is stale: validate graph before trusting selection.

#### G028 — Scale monorepo contributor feedback

**Goal:** Scale monorepo contributor feedback across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC109:** Large change launches hundreds of shards: balance bounded cost and complete checks.
- **UC110:** Rename-only PR evades static checks: classify real impact.
- **UC111:** Multi-owner PR misses team-specific suites: map coverage to touched subsystems.
- **UC112:** Codegen modifies tracked source inside CI: fail with reproducible diff.

### 08 Cross-repository CI contracts

#### G029 — Validate producer and consumer compatibility

**Goal:** Validate producer and consumer compatibility across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC113:** Shared library PR passes but app consumer breaks: exercise candidate artifact downstream.
- **UC114:** Schema changed but generated client still old: run contract compatibility.
- **UC115:** Central Action changes output used by consumers: verify representative callers.
- **UC116:** Consumer tests latest main artifact instead of candidate SHA: bind immutable identity.

#### G030 — Orchestrate external repository checks

**Goal:** Orchestrate external repository checks across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC117:** repository_dispatch delivered out of order: correlate IDs and revisions.
- **UC118:** Repo A requires Repo B status but sees no result: classify pending not passed.
- **UC119:** Central test service is unavailable: distinguish dependency outage from green test.
- **UC120:** Cross-repo write needs elevated token: request scoped GitHub App grant.

#### G031 — Exchange cross-repo artifacts and evidence

**Goal:** Exchange cross-repo artifacts and evidence across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC121:** Consumer downloads mutable latest artifact: verify digest and source commit.
- **UC122:** Repos produce different result formats: normalize without discarding originals.
- **UC123:** Source artifact expires before rerun: define refresh or retention.
- **UC124:** External badge shows success for wrong revision: require immutable check identity.

#### G032 — Scale multi-repo compatibility verification

**Goal:** Scale multi-repo compatibility verification across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC125:** API change impacts 20 clients: select documented risk-based breadth.
- **UC126:** Consumers disagree on required library version: test compatibility matrix.
- **UC127:** Concurrent producer and consumer feature branches race: validate combined revisions.
- **UC128:** Regional build mirrors publish unequal bytes: verify immutable content at handoff.

### 09 Deterministic build environments

#### G033 — Control toolchain and dependency resolution

**Goal:** Control toolchain and dependency resolution across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC129:** Floating compiler release changes behavior overnight: record and govern exact build environment.
- **UC130:** Runner image changes preinstalled tools: declare dependencies explicitly.
- **UC131:** Workflow uses npm install while repo mandates npm ci: preserve lockfile semantics.
- **UC132:** Workspace build tools disagree on version: honor repo contract.

#### G034 — Make tests reproducible across runner images

**Goal:** Make tests reproducible across runner images across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC133:** Test depends on local timezone: normalize clock and locale conditions.
- **UC134:** Build downloads unverified latest binary: enforce stable source and integrity.
- **UC135:** External service outage makes unit suite flaky: isolate deterministic tests.
- **UC136:** Persistent runner leaks previous build outputs: start from clean isolation.

#### G035 — Explain build divergence

**Goal:** Explain build divergence across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC137:** Same commit yields differing binaries per runner: capture environment fingerprint.
- **UC138:** Code generator produces nondeterministic diffs: compare reproducible outputs.
- **UC139:** Lockfile resolves architecture-specific assets: declare target differences.
- **UC140:** Golden snapshots change with font/image upgrade: surface intended deltas.

#### G036 — Respect restricted build prerequisites

**Goal:** Respect restricted build prerequisites across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC141:** Proprietary test license absent for forks: separate available and blocked coverage.
- **UC142:** Private package registry token missing: name exact prerequisite and owner.
- **UC143:** Air-gapped runner lacks public dependencies: use approved mirrored source.
- **UC144:** Ordinary CI attempts signing with production key: keep privilege out of test context.

### 10 Package and installable artifact verification

#### G037 — Build complete deliverable packages

**Goal:** Build complete deliverable packages across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC145:** Wheel or npm tarball omits runtime data: test installed package contents.
- **UC146:** ZIP includes absolute user-machine paths: validate portable archive manifest.
- **UC147:** Compiled executable lacks runtime assets: perform install-and-start smoke test.
- **UC148:** Multi-target build outputs only host binary: enforce expected artifacts.

#### G038 — Keep package metadata consistent

**Goal:** Keep package metadata consistent across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC149:** Tag and package version disagree: stop invalid release handoff.
- **UC150:** Generated schema bundled from previous revision: rebuild and compare input IDs.
- **UC151:** Lockfile disagrees with manifest: reject undisclosed resolution change.
- **UC152:** Packaging script edits tracked files silently: assert clean tree.

#### G039 — Validate artifact handoff integrity

**Goal:** Validate artifact handoff integrity across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC153:** Smoke stage rebuilds different bytes instead of packaged artifact: consume real candidate.
- **UC154:** One platform artifact is absent but upload step green: enforce manifest completeness.
- **UC155:** Concurrent jobs clobber artifact names: isolate output identity.
- **UC156:** Archived binary corrupts during transfer: verify extraction and digest.

#### G040 — Validate agent plugin package contracts

**Goal:** Validate agent plugin package contracts across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC157:** Packaged Skill missing SKILL.md or nested references: verify required paths.
- **UC158:** Plugin ZIP contains unsafe symlink or path traversal: reject archive.
- **UC159:** Plugin requires undeclared external tool: verify installation contract.
- **UC160:** Installed plugin uses stale source copy: reconcile package and reviewed SHA.

### 11 Unit and component test gates

#### G041 — Ensure unit test execution is truthful

**Goal:** Ensure unit test execution is truthful across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC161:** Wrapper ignores nonzero test exit code: propagate actual failure.
- **UC162:** Test only passes on developer machine globals: run on clean host.
- **UC163:** Parallel tests mutate global state: isolate fixtures.
- **UC164:** Hanging tests never terminate: bound and diagnose execution.

#### G042 — Check meaningful component behavior

**Goal:** Check meaningful component behavior across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC165:** API mock hides actual input validation: test contract boundary.
- **UC166:** Frontend renders but component accessibility fails: include applicable a11y assertions.
- **UC167:** Parser handles valid data but breaks adversarial edge inputs: require regression cases.
- **UC168:** Feature flag disabled path has no coverage: validate each supported configuration.

#### G043 — Support language-specific testing practices

**Goal:** Support language-specific testing practices across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC169:** Pytest collects no tests due to config: assert discovery count.
- **UC170:** Jest project globs exclude workspace: validate suite inventory.
- **UC171:** Go nested modules are missed by root test command: enumerate modules.
- **UC172:** Maven phases exclude integration tests by default: set explicit task contract.

#### G044 — Preserve useful unit test evidence

**Goal:** Preserve useful unit test evidence across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC173:** XML reports absent on failure: publish whatever partial results exist.
- **UC174:** Snapshot mismatch has no readable diff: attach expected and actual evidence.
- **UC175:** Retried green run hides first failure: preserve attempts.
- **UC176:** Dashboard shows stale counts: bind report to commit and run ID.

### 12 Integration and data-dependent CI

#### G045 — Provision realistic integration dependencies

**Goal:** Provision realistic integration dependencies across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC177:** SQLite substitute masks Postgres incompatibility: test real supported engine.
- **UC178:** Broker starts after tests launch: await health not arbitrary delay.
- **UC179:** Concurrent suites collide on fixed service ports: isolate execution.
- **UC180:** TLS integration lacks test certificate provisioning: name secure prerequisites.

#### G046 — Verify database migration behavior

**Goal:** Verify database migration behavior across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC181:** Migration succeeds on empty DB but fails existing data: test upgrade fixtures.
- **UC182:** Migration rollback corrupts prior state: validate supported reversibility constraints.
- **UC183:** Parallel migrations deadlock during boot: test locking and transaction boundaries.
- **UC184:** ORM update changes schema unintentionally: compare schema contract.

#### G047 — Validate inter-service compatibility

**Goal:** Validate inter-service compatibility across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC185:** Provider breaks older API clients: run consumer contracts.
- **UC186:** Gateway changes error envelope: verify routed integration behavior.
- **UC187:** gRPC field removal breaks published consumers: detect compatibility violation.
- **UC188:** Mocked auth passes but real IdP rejects claims: test controlled integration.

#### G048 — Manage integration test data safely

**Goal:** Manage integration test data safely across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC189:** Shared database leaks state across runs: isolate namespaces and cleanup.
- **UC190:** Test fixture mutates shared staging data: require scoped identities and restore.
- **UC191:** Expiring tokens fail in different timezones: use controllable clock assumptions.
- **UC192:** Third-party sandbox outage looks like app bug: report external failure separately.

### 13 Browser E2E and customer journeys

#### G049 — Test critical cross-service user flows

**Goal:** Test critical cross-service user flows across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC193:** Unit tests pass while signup fails end-to-end: exercise journey.
- **UC194:** Browser launches before preview readiness: check health and revision.
- **UC195:** Preview site is stale after PR update: confirm exact commit served.
- **UC196:** Feature flag differs from target environment: test declared modes.

#### G050 — Cover realistic browsers and devices

**Goal:** Cover realistic browsers and devices across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC197:** Chrome-only pass hides Firefox cookie issue: select compatibility browsers.
- **UC198:** Narrow viewport hides required action: assert accessible interaction.
- **UC199:** Locale and timezone change checkout behavior: test supported regions.
- **UC200:** Browser runner animation causes timing flake: use stable readiness.

#### G051 — Retain actionable browser diagnostics

**Goal:** Retain actionable browser diagnostics across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC201:** Browser test times out without trace: capture trace/screenshots/logs.
- **UC202:** Auth flow fails but logs include secrets: redact while preserving network metadata.
- **UC203:** Visual snapshot passes but semantic accessibility fails: combine complementary checks.
- **UC204:** Headless rendering differs with fonts: pin environment and review deltas.

#### G052 — Control preview environments and fixtures

**Goal:** Control preview environments and fixtures across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC205:** Shared test account locks under parallel shards: isolate identity.
- **UC206:** Fork PR cannot access preview secret: provide safe alternate check.
- **UC207:** Payment sandbox retries charge twice: ensure idempotent fake transactions.
- **UC208:** Cancelled PR leaves preview resources running: clean safely on lifecycle events.

### 14 Flaky tests sharding and execution reliability

#### G053 — Shard suites without omission

**Goal:** Shard suites without omission across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC209:** Shard glob silently drops test file: verify union equals collected suite.
- **UC210:** One shard takes 40 minutes while others finish: rebalance based on timings.
- **UC211:** Rerun selects different shard membership: preserve deterministic partition.
- **UC212:** fail-fast hides multiple independent defects: retain diagnostic coverage.

#### G054 — Track and contain flaky tests

**Goal:** Track and contain flaky tests across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC213:** Third-attempt green masks two failures: report flake and original attempts.
- **UC214:** Quarantined suite has no owner or expiry: require review and restoration policy.
- **UC215:** Network-caused flakes mixed with assertion regressions: classify separately.
- **UC216:** Flake occurs only on Windows: compute platform-specific signal.

#### G055 — Diagnose runner and test-process failures

**Goal:** Diagnose runner and test-process failures across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC217:** OOM kills tests without JUnit report: classify process crash.
- **UC218:** Integration shards contend on same database schema: isolate resources.
- **UC219:** Disk fills with browser screenshots: bound artifacts and surface diagnostics.
- **UC220:** Hung test consumes all workers: use per-test timeout and identifiers.

#### G056 — Protect aggregate test completeness

**Goal:** Protect aggregate test completeness across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC221:** Retries cover deterministic failures and waste hours: bound by failure category.
- **UC222:** Test collection returns zero after path filter: fail missing expected scope.
- **UC223:** Required child suite skipped while umbrella green: calculate all outcomes.
- **UC224:** Tests executed from stale generated code: verify workspace SHA.

### 15 Code coverage regression and quality policy

#### G057 — Make coverage metrics meaningful

**Goal:** Make coverage metrics meaningful across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC225:** Global line score hides untested changed critical logic: gate meaningful diff coverage.
- **UC226:** Coverage merged across different commits: validate consistent revision.
- **UC227:** Vendored/generated code inflates coverage: use reviewed exclusions.
- **UC228:** Branch coverage drops while line coverage rises: preserve risk-appropriate metric.

#### G058 — Prevent regression-test removal

**Goal:** Prevent regression-test removal across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC229:** PR deletes tests yet aggregate ratio stable: detect assertion erosion.
- **UC230:** Mass snapshot updates hide API contract break: require reviewable deltas.
- **UC231:** Incident regression case exists but pipeline never executes it: verify suite routing.
- **UC232:** Renamed tests move outside discovery globs: track collected test inventory.

#### G059 — Integrate diverse quality signals

**Goal:** Integrate diverse quality signals across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC233:** Typecheck ignores app subdirectory: enforce intended source coverage.
- **UC234:** Lint warning threshold silently softened: detect rule changes.
- **UC235:** Separate reporters disagree about readiness: nominate authoritative gate.
- **UC236:** External SAST is owned by another domain: consume its genuine check, not fake success.

#### G060 — Govern policy evolution

**Goal:** Govern policy evolution across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC237:** Team requests temporary quality exception: require owner and expiry.
- **UC238:** continue-on-error is added to critical gate: flag bypass.
- **UC239:** Tightened threshold blocks all PRs without rollout: stage documented policy change.
- **UC240:** Different protected branches need different checks: map contract by branch.

### 16 AI plugin and agent behavioral evaluations

#### G061 — Gate actual agent behavior

**Goal:** Gate actual agent behavior across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC241:** Skill package valid but agent gives unsafe privileged advice: evaluate scenarios.
- **UC242:** Promptfoo cases pass because assertions only check keywords: require observable outcomes.
- **UC243:** Agent invents missing deployment secret rather than blocking: enforce blocker behavior.
- **UC244:** New skill guidance regresses existing scenario: test held-out cross-skill corpus.

#### G062 — Assert tool use and decision traces

**Goal:** Assert tool use and decision traces across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC245:** Agent says it searched Marketplace but no retrieval call exists: inspect trace.
- **UC246:** Agent attempts to write protected main without permission: evaluate boundary.
- **UC247:** Agent installs local scanner despite GitHub-hosted availability: inspect selection.
- **UC248:** Agent claims GitHub run passed without access: reconcile actual status.

#### G063 — Protect evaluation integrity and reproducibility

**Goal:** Protect evaluation integrity and reproducibility across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC249:** Fixture contains secret-bearing logs: sanitize without losing failure signal.
- **UC250:** Golden test answer is embedded in Skill instructions: maintain held-out suite.
- **UC251:** LLM judge drifts after model upgrade: record rubric and versions.
- **UC252:** Stochastic responses vary but security decision must not: assert invariants.

#### G064 — Make behavioral quality a real gate

**Goal:** Make behavioral quality a real gate across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC253:** Eval config changed to reduce thresholds in same PR: require controlled review.
- **UC254:** Overall pass hides failing individual use case: publish case-level evidence.
- **UC255:** One worker crashes and evaluator silently drops cases: verify expected count.
- **UC256:** Prompt-only eval passes but packaged skill cannot execute: require runtime smoke test.

### 17 CI performance capacity and cost

#### G065 — Shorten critical path without weakening checks

**Goal:** Shorten critical path without weakening checks across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC257:** CI runs independent suites serially: parallelize verified DAG.
- **UC258:** Lint waits for slow E2E unnecessarily: prioritize early feedback.
- **UC259:** Documentation PR triggers full expensive integration matrix: scope by impact.
- **UC260:** Fast suite runs but slow required suites never finish: guarantee completion.

#### G066 — Control expensive fanout and saturation

**Goal:** Control expensive fanout and saturation across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC261:** Multiple pushes run identical costly E2E jobs: cancel stale work.
- **UC262:** Matrix multiplies with runtime variants beyond budget: prioritize supported combinations.
- **UC263:** Shared runners are saturated by nightly checks: reserve urgent merge capacity.
- **UC264:** CI spend exceeds monthly allocation: expose spend and optional stages.

#### G067 — Use safe performance optimizations

**Goal:** Use safe performance optimizations across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC265:** Dependencies download for every job: configure supported cache.
- **UC266:** Binary cache reused across incompatible ABI: key by arch/toolchain.
- **UC267:** Broad fallback cache returns stale generated artifacts: split cache types.
- **UC268:** CI only works if cache exists: enforce cold-build correctness.

#### G068 — Measure optimization empirically

**Goal:** Measure optimization empirically across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC269:** Claimed speedup based on fastest run only: compare median and queue.
- **UC270:** Test sharding helps but artifact upload dominates: optimize total path.
- **UC271:** Reusable workflow call overhead explodes at scale: quantify granularity.
- **UC272:** Hosted image upgrade slows tests: distinguish provider variance.

### 18 Cache artifact and reporting contracts

#### G069 — Protect artifact identity and completeness

**Goal:** Protect artifact identity and completeness across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC273:** Two jobs upload same artifact name: enforce namespaced manifest.
- **UC274:** Consumer reads artifact from wrong run: bind SHA and run ID.
- **UC275:** Untrusted archive contains path traversal: validate extraction input.
- **UC276:** HTML result misses failed shards: assert expected reports received.

#### G070 — Set appropriate evidence retention

**Goal:** Set appropriate evidence retention across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC277:** Browser videos fill quota: tune retention with incident needs.
- **UC278:** CI artifacts expose personal data: minimize and scope access.
- **UC279:** Failure evidence expires before postmortem: align preservation policy.
- **UC280:** Release artifact incorrectly stored only as cache: distinguish durable handoff.

#### G071 — Constrain cache poisoning risk

**Goal:** Constrain cache poisoning risk across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC281:** Fork workflow tries to overwrite default cache: preserve low-trust restrictions.
- **UC282:** Privileged job restores low-trust executable cache: reject unsafe origin.
- **UC283:** Same cache key yields different dependencies: validate integrity inputs.
- **UC284:** Cached files include decrypted token: prevent sensitive cache content.

#### G072 — Produce portable CI evidence

**Goal:** Produce portable CI evidence across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC285:** External dashboard results vanish: retain structured essential report.
- **UC286:** JUnit format differs across projects: normalize without deleting original.
- **UC287:** Summary omits failing test IDs: publish actionable diagnostics.
- **UC288:** Step log truncation hides root cause: save bounded structured evidence.

### 19 Required checks and merge queue correctness

#### G073 — Support merge-group execution

**Goal:** Support merge-group execution across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC289:** Merge queue waits forever because workflow lacks merge_group trigger: add correct status.
- **UC290:** Individually green PRs fail together: validate synthetic combined state.
- **UC291:** Dynamic check names differ between PR and queue: stable gate contract.
- **UC292:** Merge group infrastructure failure retries: distinguish retryable and code failures.

#### G074 — Aggregate all mandatory quality verdicts

**Goal:** Aggregate all mandatory quality verdicts across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC293:** Summary returns success despite failed child: fold complete required results.
- **UC294:** Optional skip confused with unexpected mandatory skip: distinguish states.
- **UC295:** Path-filtered required workflow never starts: preserve non-skippable report.
- **UC296:** Another GitHub App uses same status name: bind trusted check source.

#### G075 — Migrate required rules without outages

**Goal:** Migrate required rules without outages across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC297:** Renamed workflow status blocks every PR: coordinate ruleset transition.
- **UC298:** Merge queue policy contradicts branch protection: inspect effective enforcement.
- **UC299:** New protected branch inherits weaker checks: verify branch policy applicability.
- **UC300:** Emergency fix needs quick pass: keep minimum enforceable safety gates.

#### G076 — Handle unusual PR lifecycle states

**Goal:** Handle unusual PR lifecycle states across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC301:** Draft becomes ready without fresh run: trigger correct validation.
- **UC302:** Force-push leaves stale green commit status: require current SHA.
- **UC303:** Cancelled workflow leaves required check pending: produce truthful final verdict.
- **UC304:** Bot status tied to wrong source app: validate check provenance.

### 20 Runners execution and infrastructure

#### G077 — Choose fit-for-purpose compute

**Goal:** Choose fit-for-purpose compute across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC305:** ARM-only test accidentally scheduled on x64: map platform support.
- **UC306:** Integration needs private service access: choose authorized network-capable runner.
- **UC307:** macOS tool invoked on Ubuntu: split platform steps.
- **UC308:** Self-hosted capacity cannot handle matrix load: plan queue and fallback.

#### G078 — Isolate self-hosted runners

**Goal:** Isolate self-hosted runners across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC309:** Runner retains previous job secrets: require ephemeral environment hygiene.
- **UC310:** Fork PR lands on privileged internal runner: enforce group access.
- **UC311:** Package cache persists registry tokens: clean credentials per run.
- **UC312:** Runner has stale unmanaged build directory: avoid implicit reuse.

#### G079 — Handle infrastructure failures

**Goal:** Handle infrastructure failures across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC313:** Hosted runner startup repeatedly times out: classify capacity outage.
- **UC314:** Job runs out of ephemeral disk: surface metrics and mitigation.
- **UC315:** Runner network drops during suite: retain partial evidence.
- **UC316:** Jobs queued because all self-hosted runners offline: name capacity blocker.

#### G080 — Manage runner image compatibility

**Goal:** Manage runner image compatibility across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC317:** Hosted image removes required runtime: declare supported setup.
- **UC318:** Build assumes preinstalled binary now missing: provision explicitly.
- **UC319:** Docker action depends on unsupported base/runtime: select maintained variant.
- **UC320:** Windows runner shell update breaks quoting: test platform-specific behavior.

### 21 Incident diagnosis and recovery

#### G081 — Classify workflow failures accurately

**Goal:** Classify workflow failures accurately across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC321:** Checkout fails before tests: distinguish access from code quality.
- **UC322:** Only one OS matrix leg fails: correlate version and environment.
- **UC323:** Rerun green but original logs missing: preserve uncertainty and raw run.
- **UC324:** Skipped or neutral conclusion counted as success: normalize correctly.

#### G082 — Investigate multi-repo CI incidents

**Goal:** Investigate multi-repo CI incidents across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC325:** Shared reusable workflow breaks dozens of consumers: map blast radius.
- **UC326:** Third-party Action tag removed unexpectedly: identify affected refs.
- **UC327:** GitHub outage blocks urgent release handoff: state dependency and fallback.
- **UC328:** Artifact outage follows green build: invalidate incomplete readiness evidence.

#### G083 — Find first-bad CI change

**Goal:** Find first-bad CI change across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC329:** Workflow modification adds 20 minutes: compare critical-path steps.
- **UC330:** Action upgrade breaks Windows only: find changed revision and runner context.
- **UC331:** Dependency update silently loses test collection: compare suite inventory.
- **UC332:** Ruleset change suddenly blocks healthy PRs: distinguish policy incident.

#### G084 — Produce actionable recovery instructions

**Goal:** Produce actionable recovery instructions across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC333:** Run fails due to missing secret or scope: specify precise blocker and owner.
- **UC334:** Queue job cancellation leaves no runbook: document recoverable sequence.
- **UC335:** Failure not reproducible locally due to private resources: provide safe remote evidence.
- **UC336:** Several quality tools disagree: issue explicit passed/failed/blocked assessment.

### 22 Migration lifecycle and self-application

#### G085 — Migrate CI platforms without loss of guarantees

**Goal:** Migrate CI platforms without loss of guarantees across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC337:** Jenkins pipeline hides post-build quality checks: inventory semantics before migration.
- **UC338:** Migrated suite environment differs materially: compare behavioral equivalence.
- **UC339:** Duplicate workflows appear similar but test different targets: preserve full coverage.
- **UC340:** Migration drops security status produced by external system: retain its genuine signal.

#### G086 — Evolve workflow contracts safely

**Goal:** Evolve workflow contracts safely across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC341:** Action major upgrade changes inputs and defaults: inspect release notes.
- **UC342:** Deprecated workflow syntax still passes temporarily: plan compatible upgrade.
- **UC343:** New shared CI standard conflicts with local needs: document exceptions.
- **UC344:** Central reusable workflow breaks one consumer: restore compatibility path.

#### G087 — Audit engineering quality evidence

**Goal:** Audit engineering quality evidence across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC345:** User counts YAML jobs as proof of correctness: demand scenario-to-evidence mapping.
- **UC346:** Passing dashboard hides skipped tests: validate expected suite count.
- **UC347:** CI migrated without baseline runs: compare before/after gates and durations.
- **UC348:** Repository permissions prevent required change: mark blocked rather than inventing access.

#### G088 — Apply plugin CI to itself

**Goal:** Apply plugin CI to itself across unfamiliar real repositories while preserving validated behavior, explicit constraints, and observable evidence.

- **UC349:** Packaged GitHub Operations Skill valid but Codex cannot discover it: gate runtime discovery.
- **UC350:** Behavioral eval passes while ZIP omits references: enforce package plus behavior checks.
- **UC351:** Plugin needs scanners only within hosted workflows: do not install locally.
- **UC352:** Plugin edits its own CI and weakens mandatory checks: require independent policy verification.

## Source-based research references

These use cases are synthesized engineering challenge scenarios, **not verbatim incidents or claims of deployment success**. Sources are for traceability and future on-demand retrieval, not for cloning whole repositories or copying Actions indiscriminately. Each implementation must refresh current version and syntax.

### Official GitHub semantics

- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Workflow triggering events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Merge queue requirements](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
- [Required status troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)
- [Concurrency and queueing](https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency)
- [Reusable workflow permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations)
- [Job matrix](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)
- [Caching and cache security](https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching)
- [Workflow artifact contracts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts)
- [Secure use of pull_request_target](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)
- [Self-hosted runner management](https://docs.github.com/en/actions/reference/runners/self-hosted-runners)
- [Actions execution policies](https://docs.github.com/en/actions/concepts/about-actions-policies)

### Representative real repositories and integrations

- [GitHub CLI workflows](https://github.com/cli/cli/tree/trunk/.github/workflows) — acceptance, Go tests, lint, CodeQL, release workflow references.
- [GitHub Actions runner workflows](https://github.com/actions/runner/tree/main/.github/workflows) — build, security, dependency checks, runner publishing.
- [Renovate workflows](https://github.com/renovatebot/renovate/tree/main/.github/workflows) — merge queue, test, dependency and package automation.
- [Kubernetes test-infra](https://github.com/kubernetes/test-infra) — scaled CI operations (uses Prow; do not equate it with GitHub Actions).
- [GitHub starter workflows](https://github.com/actions/starter-workflows) — discover suitable baseline actions only when relevant.
- [Promptfoo GitHub Action](https://github.com/promptfoo/promptfoo-action) — hosted PR/CI behavioral evaluations with real reports.

### Community/tutorial discovery context

- [r/devops discussion of real CI migration and platform tradeoffs](https://www.reddit.com/r/devops/comments/1bmn7ie/why_do_some_companies_use_other_tooling_for_cicd/)
- [GitHub Actions tutorials](https://docs.github.com/en/actions/tutorials) — use as learning/discovery index, not sole normative evidence.

## Skill Creator / Augmentation handoff boundary

- Map every G/UC to imported Skill and Agent source variants and evidence of activation.
- Include both expected-success and adversarial/incident counterexamples in later evaluations; measure task-level success, tool traces, and actual GitHub outcome separately.
- A repository-specific CI design may require skills from other GitHub Operations domains. Route across domains; do not duplicate their knowledge wholesale.
- **No augmentation, final Skill packaging, runner installation, or deployment is authorized by this documentation commit.**
- A separate future knowledge-retrieval layer is intentionally deferred until domain Skills are complete.
- CI and security scanning implementation for any target repo belongs inside GitHub Actions or approved remote infrastructure, **not a new inventory of local scanner binaries**.
