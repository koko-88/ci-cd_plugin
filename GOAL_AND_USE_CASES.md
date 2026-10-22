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
