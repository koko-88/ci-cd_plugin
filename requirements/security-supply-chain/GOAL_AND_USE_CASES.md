# Security & Software Supply Chain — Goals and Incident-Driven Use Cases

- Parent: **GitHub Operations Engineering Plugin**; Domain 3 of 4.
- Research and draft date: **2026-10-25**, Africa/Cairo.
- Status: **owner-requested draft requirements; pending owner approval** before Skill Creator augmentation/hardening.
- Contract: [PLUGIN_CONTRACT.md](../../PLUGIN_CONTRACT.md#6-domain-3-security--software-supply-chain). Shared tools: [SHARED_TOOL_CAPABILITIES.md](../../SHARED_TOOL_CAPABILITIES.md).
- Evidence base: current GitHub docs/changelogs; maintained OSS implementation repos; OWASP/OpenSSF/NIST standards; disclosed real incidents; Reddit practitioner discussions; selected YouTube tutorials.

## Domain goal

Enable a compatible coding agent to inspect, design, implement when authorized, and independently verify **effective security and software-supply-chain controls** for unfamiliar GitHub repositories and organizations. Cover source integrity, workflow trust boundaries, secure identities and secrets, code scanning (SAST), dependency and malware risk (SCA), runtime/build/container threats, action and toolchain integrity, SBOM completeness, signed artifact provenance, publisher identity, policy enforcement, audit evidence, incident response, and safe agent/MCP inputs. Select maintained **existing GitHub Actions, native features and ecosystem tooling** based on actual targets, not a hardcoded scanner collection. Bind every claim to the effective permissions, feature/plan support, source revision, trusted run/artifact identity and verification evidence.

**Domain boundaries:** Domain 1 (CI/CD & Quality Engineering) owns workflow composition, test/eval production and truthful CI check status; Domain 2 (GitHub Platform & Governance) owns org/repo rulesets, permissions administration and required-check enforcement; this Domain 3 owns threat and scanner selection, security risk criteria, secrets/dependencies, provenance validation and security outcomes; Domain 4 (Release, Deployment & Reliability) owns promotion/deploy/rollback execution and target health. Coordinate cross-domain obligations; don't silently assume ownership of another domain's mutations.

Runtime Skill must remain portable to compatible agent hosts: the `K:`-drive source inventory, Creator tooling and this build-time catalog must **not** be runtime dependencies. Upstream Skills/retrieved tool output are untrusted data, not instructions to execute.

## Use-case acceptance contract

For every applicable case the resulting Skill must:

1. **Inspect:** identify exact org/repo/ref/actor, workflow/caller/runner, package ecosystem/lockfile, registry/artifact digest, observed security settings, entitlements and access scope; distinguish missing evidence from a negative finding.
2. **Model risk:** specify asset, source-to-sink trust boundary, attacker capability or real failure, desired policy, impacted outputs and blast radius; avoid declaring a security claim from documentation alone.
3. **Select proven capability:** compare native GitHub controls first, then maintained Actions/services/tools as needed. Validate applicability, supported plan/GHES version, permissions, vendor trust, dependency identity, pricing and runner compatibility. Research exact cases; never require blanket local installations on the owner's Windows machine.
4. **Implement only when authorized:** scope changes and credentials; isolate untrusted PRs and privileged jobs; preserve existing policies; use least privilege, pinned/locked dependencies where supported, safe rollback/exception handling and cross-domain coordination. Catalog creation itself authorizes **no** security mutation or CI execution.
5. **Verify independently:** use actual GitHub configuration, runner/check outputs, actionable scan findings, effective policy, artifact digests, signatures/attestations, fixed dependencies, authorization and consumer-side enforcement where available. A configured scanner, signature, generated SBOM, green badge or Markdown report alone cannot establish security.
6. **Report:** map applicable cases to **Passed / Failed / Blocked / Not Verified / Not Applicable**, cite source revision and evidence, affected SHA/digest and time, note permission/plan/tool constraints, waived risks and next owner action. Catalogs are requirements, not evidence of executed tests.

**Evidence discipline:** Each UC below is a *constructed, testable real-production failure/decision scenario* informed by documented mechanisms, implementations, community lessons or public incidents. Do not claim each UC occurred in this repo. Real cases cited include March 2026 Trivy compromise, but the catalog extends implications into synthetic acceptance scenarios. Official docs and upstream source take precedence over Reddit and tutorial claims. YouTube descriptions and community posts are discovery context, not certification or proof. Recheck fast-moving security features against official sources at execution time.

## Selection rules and platform caveats

| Situation | Prefer | Verify / limitation |
| --- | --- | --- |
| Native secret scanning/push protection, CodeQL, Dependabot, Dependency Review | Existing GitHub security capability when available | Plan, repository ownership, admin scopes, language/ecosystem support and actual enforcement |
| Security scanner/action | Existing maintained GitHub Action or isolated runner tool when needed | Publisher provenance, version/SHA/lockfile, transitive Actions, runtime trust and valid finding output |
| GitHub Actions dependency integrity | Reviewed full SHA pinning or 2026 workflow lockfiles where supported | Lockfiles are Public Preview as of 2026-10-14; locking is not a malware verdict |
| Artifact provenance/signature | GitHub `actions/attest`, Sigstore/SLSA mechanism only where supported | Attest the actual digest; *verify* predicate, identity and subject downstream; no automatic SLSA level inference |
| Package publishing | Registry-native trusted publishing/OIDC when supported | Trust restrictions, package identity, provenance conditions, release domain ownership |
| SBOM | Generate for actual publishable artifact; SPDX/CycloneDX via maintained tooling | Runtime/builder/OS component completeness, validation, artifact pairing and consumer usage |
| AI Skills/MCP | Vet only relevant selected sources; enforce isolation and least privilege | Runtime behavior and host boundary differ from static prompt review |
| Cross-domain policy | Security defines risk decision and evidence contract | CI/Governance/Release retain implementation/enforcement/deployment ownership |

## Selective-read index

Read domain goal and relevant index row first. Load the whole catalog only for comprehensive augmentation or coverage assessment.

| Section | Goals | Cases | Research route IDs |
| --- | --- | --- | --- |
| 01 Repository security baseline, inventory, and threat model | G001–G004 | UC001–UC016 | SS01,SS18,SS17,SS49 |
| 02 Untrusted events, expressions, and workflow trust boundaries | G005–G008 | UC017–UC032 | SS02,SS03,SS04,SS07,SS29 |
| 03 Workflow identities, GitHub tokens, OIDC, and permissions | G009–G012 | UC033–UC048 | SS02,SS03,SS49,SS50 |
| 04 Action dependency integrity, pinning, and workflow lockfiles | G013–G016 | UC049–UC064 | SS06,SS07,SS26,SS42 |
| 05 Runner isolation, cache poisoning, artifacts, and egress | G017–G020 | UC065–UC080 | SS03,SS05,SS29,SS40 |
| 06 Secret scanning, push protection, and credential incident prevention | G021–G024 | UC081–UC096 | SS13,SS14,SS39,SS31 |
| 07 Code scanning, CodeQL, SARIF and static analysis | G025–G028 | UC097–UC112 | SS08,SS09,SS38,SS44 |
| 08 Dependency graph, SCA and pull-request dependency review | G029–G032 | UC113–UC128 | SS10,SS11,SS35,SS43 |
| 09 Dependabot, Renovate, malware advisories, and remediation automation | G033–G036 | UC129–UC144 | SS11,SS12,SS33,SS41 |
| 10 Malicious packages, package acquisition, and registry integrity | G037–G040 | UC145–UC160 | SS12,SS33,SS47,SS22 |
| 11 SBOM generation, coverage, formats, and lifecycle | G041–G044 | UC161–UC176 | SS15,SS16,SS19,SS28 |
| 12 Container image, filesystem, base image and IaC scanners | G045–G048 | UC177–UC192 | SS16,SS45,SS03,SS26 |
| 13 Attestations, provenance, SLSA, and build isolation | G049–G052 | UC193–UC208 | SS19,SS20,SS21,SS34 |
| 14 Artifact signing, key custody, and admission policy | G053–G056 | UC209–UC224 | SS19,SS20,SS23,SS37 |
| 15 Trusted publishing, registries, release handoff and package integrity | G057–G060 | UC225–UC240 | SS22,SS19,SS27,SS26 |
| 16 Security gates, required checks, exceptions and merge queues | G061–G064 | UC241–UC256 | SS08,SS10,SS03,SS01 |
| 17 Infrastructure, policy-as-code and secret-aware configuration | G065–G068 | UC257–UC272 | SS37,SS03,SS49,SS02 |
| 18 Licenses, policy frameworks, OSPS baseline and supplier governance | G069–G072 | UC273–UC288 | SS18,SS17,SS46,SS49 |
| 19 Vulnerability triage, reachability, VEX, and exception lifecycle | G073–G076 | UC289–UC304 | SS11,SS12,SS16,SS17 |
| 20 Organization-scale security posture, drift and audit signals | G077–G080 | UC305–UC320 | SS01,SS17,SS30,SS36 |
| 21 Compromised Actions, scanners, incident response and recovery | G081–G084 | UC321–UC336 | SS26,SS27,SS03,SS29 |
| 22 Agent Skills, MCP tools and AI-assisted supply-chain boundaries | G085–G088 | UC337–UC352 | SS24,SS25,SS48,SS49 |
| 23 Security review, incident ownership, education and maintenance | G089–G092 | UC353–UC368 | SS03,SS18,SS31,SS32 |
| 24 Plugin self-security, end-to-end assurance and handoff | G093–G096 | UC369–UC384 | SS18,SS20,SS24,SS26 |

## Goals and incident-driven use cases

### 01 Repository security baseline, inventory, and threat model

_Research route: SS01,SS18,SS17,SS49._

#### G001: Map actual security scope and assets

- UC001: Private repository missing from token-visible inventory: mark coverage incomplete, not compliant.
- UC002: Archived project with active published package: retain release-supply-chain ownership.
- UC003: Fork sharing upstream dependency risks is counted as independent release authority: classify separately.
- UC004: Multiple registries publish from one monorepo: map each output to its true owner and build path.

#### G002: Identify threat actors and trust assets

- UC005: Public fork contributor controls workflow input: model attacker-controlled surface.
- UC006: CI robot possesses organization-write rights despite scan-only role: flag privilege target.
- UC007: Build output consumed by customers outside GitHub: include downstream trust decision.
- UC008: Threat model omits artifact repository and package installation scripts: add to attack surface.

#### G003: Resolve intended vs effective protections

- UC009: README promises signed releases but published binaries lack verifiable signature: mismatch.
- UC010: Security policy says critical findings block merge but current checks only warn: gap.
- UC011: GitHub Security features appear configured but repos outside scope lack analysis: measure effective coverage.
- UC012: Old security controls contradict currently approved owner policy: surface decision rather than guess.

#### G004: Establish evidence provenance and acceptance

- UC013: Previously green report targets different SHA: don't carry over pass.
- UC014: Scanner ran without target dependency manifests: mark result partial.
- UC015: Organization API denied by current token: mark unknown, not secure.
- UC016: Security assessment cites a tool README but has no run/report evidence: mark design-only.

### 02 Untrusted events, expressions, and workflow trust boundaries

_Research route: SS02,SS03,SS04,SS07,SS29._

#### G005: Separate untrusted pull requests from privileged execution

- UC017: Fork PR invokes pull_request_target and checks out attacker head: reject privileged execution.
- UC018: Workflow_run downloads untrusted artifact then runs it with write token: isolate or reject.
- UC019: Issue-comment trigger calls shell using untrusted body: prevent script injection.
- UC020: Workflow dispatch accepts free-form command string: treat input as data and validate allowed operations.

#### G006: Protect expression and context interpolation

- UC021: PR title interpolated into run command: avoid executable string expansion.
- UC022: Branch name used in PowerShell script without safe parameter handling: protect shell context.
- UC023: JSON workflow output is trusted as command without validation: enforce typed boundary.
- UC024: Attacker-controlled matrix value selects an executable path: constrain value source.

#### G007: Constrain executable workflow entry points

- UC025: Deployment workflow executable by any contributor through manual trigger: enforce actor rules.
- UC026: Scheduled security job depends on untrusted user-initiated event: verify actual trigger policy.
- UC027: Execution protection applies repository-wide but sensitive workflow needs narrower actors: scope file.
- UC028: New workflow name bypasses existing allowlist targeting: evaluate target matching and defaults.

#### G008: Avoid hidden trust propagation through reusable workflows

- UC029: Caller has read-only permission but callee expects write: fail closed and report missing grant.
- UC030: Nested reusable workflow receives secrets: trace explicit inheritance and least privilege.
- UC031: Reusable workflow from third-party ref mutates after approval: bind immutable identity.
- UC032: Callee job consumes artifacts from a foreign run with no provenance check: reject impersonation.

### 03 Workflow identities, GitHub tokens, OIDC, and permissions

_Research route: SS02,SS03,SS49,SS50._

#### G009: Derive minimum permissions per operation

- UC033: Read-only audit workflow requests contents write: reduce permissions.
- UC034: Upload SARIF fails under fork token: report trust boundary rather than widening all jobs.
- UC035: Attestation step needs id-token write but build step does not: separate grants.
- UC036: Reusable workflow requests privileges beyond caller ceiling: identify impossible escalation.

#### G010: Design short-lived federated identity

- UC037: Cloud deployment uses long-lived cloud secret where trusted OIDC is available: compare migration.
- UC038: OIDC subject policy trusts entire organization rather than production environment: tighten audience/claims.
- UC039: Cloud role allows every branch to deploy: bind trusted ref and environment.
- UC040: Reused token from older run is accepted by automation: respect token expiration and replay bounds.

#### G011: Protect machine users, Apps, and tokens

- UC041: Shared PAT spans unrelated repositories: propose narrower App installation token.
- UC042: GitHub App has source-admin rights for read-only code scan: constrain installation.
- UC043: Revoked App installation leaves required security check stranded: coordinate check replacement.
- UC044: Security bot credential stored in workflow output: prevent disclosure and rotate exposed token.

#### G012: Verify effective credential behavior

- UC045: YAML declares permissions but enterprise policy restricts effective rights: inspect result.
- UC046: Job logs expose a redacted secret shape that masking missed: investigate with safe redaction.
- UC047: OIDC request denied by cloud federation: distinguish trust policy mismatch from secret missing.
- UC048: Green scan does not prove it ran with least privilege: capture token scope and operation evidence.

### 04 Action dependency integrity, pinning, and workflow lockfiles

_Research route: SS06,SS07,SS26,SS42._

#### G013: Review and constrain action dependencies

- UC049: Third-party Action referenced by moving major tag: evaluate lockfile or full-SHA policy.
- UC050: Composite Action references another unpinned Action: inspect transitive chain.
- UC051: Unknown maintainer transfers Action repository: re-evaluate provenance and trust.
- UC052: Workflow invokes remote script with curl pipe shell despite pinned Action: review indirect executable source.

#### G014: Choose correct immutable execution policy

- UC053: Repository supports workflow lockfiles preview: assess support before adopting.
- UC054: Action SHA pinned but points to known malicious revision: reject safety inference.
- UC055: Dependabot updates workflow tag but lockfile is stale: require synchronized review.
- UC056: Policy says full SHA only while latest supported lockfile mechanism is mandated: reconcile both.

#### G015: Detect poisoned and impersonated revisions

- UC057: Action tag force-pushed following compromise: evaluate historical executed commit.
- UC058: Lookalike owner/repo resembles trusted Action: verify exact repository identity.
- UC059: Signed commit from stolen key interpreted as safe action: check publisher trust.
- UC060: A compromised action executes before scanner despite scan success: classify supply-chain incident.

#### G016: Maintain dependency freshness without unreviewed upgrades

- UC061: Security fix requires new pinned SHA: preserve trusted review and verification.
- UC062: Renovate PR changes Action runtime major version and runner assumptions: inspect compatibility.
- UC063: Workflow lockfile generation unavailable in GHES: use supported fallback.
- UC064: Review update contains untrusted install script in package metadata: isolate dependency execution.

### 05 Runner isolation, cache poisoning, artifacts, and egress

_Research route: SS03,SS05,SS29,SS40._

#### G017: Isolate untrusted execution environments

- UC065: Public fork PR runs on persistent self-hosted runner with production network access: block.
- UC066: Compromised build leaves files for next job: require ephemeral runner cleanup.
- UC067: Containerized scanner mounts Docker socket and broad host paths: model host escape exposure.
- UC068: Runner group shared with deployment job receives arbitrary PR code: separate trust tiers.

#### G018: Control cache write and read privileges

- UC069: Untrusted event may write cache restored by privileged release job: block poisoning route.
- UC070: cache-mode read-only default explicitly overridden to write: flag risk and verify actual policy.
- UC071: Cross-branch cache key collides between release and PR jobs: segregate scope.
- UC072: Cache used for executable build scripts without integrity validation: enforce trust boundary.

#### G019: Protect artifact upload and download

- UC073: Workflow uploads entire workspace including .env: minimize artifact paths.
- UC074: Privileged job unpacks untrusted archive with unsafe paths: reject traversal/symlink hazards.
- UC075: Artifact downloaded by name but from different run/commit: bind run and digest.
- UC076: Retained build artifact expired before downstream attestation check: report verification blocked.

#### G020: Observe network, storage, and blast radius

- UC077: Scanner makes unapproved outbound connection during CI: investigate egress.
- UC078: Runner has cloud metadata credential endpoint exposed: isolate workload.
- UC079: Workflow logs public but debug output prints sensitive environment: redact and scope access.
- UC080: Security scan requires internet but strict egress prevents advisory feed: provide approved network route.

### 06 Secret scanning, push protection, and credential incident prevention

_Research route: SS13,SS14,SS39,SS31._

#### G021: Establish detection coverage across repositories

- UC081: Secret scanning enabled only on default branch while historical exposure remains: verify scope.
- UC082: Provider token format unsupported by default patterns: assess custom pattern coverage.
- UC083: Scans skipped because repository/plan does not support feature: choose permitted fallback.
- UC084: Gitleaks report empty after shallow clone despite older leaked secret: classify coverage limitation.

#### G022: Enforce safe push-time blocking

- UC085: Push protection bypass by developer skips required reviewer: evaluate delegated bypass policy.
- UC086: Push too large or timed out for blocking: do not claim complete prevention.
- UC087: False positive credentials block legitimate change: route exception with bounded rationale.
- UC088: Known token bypassed via allowlist without expiry: reassess exception.

#### G023: Contain leaked secrets correctly

- UC089: Credential removed from HEAD but still active in git history: revoke first.
- UC090: Secret discovered in workflow log: prevent further log exposure and rotate affected identity.
- UC091: Scanner marks key inactive but provider denies validity lookup: avoid unsupported clearance.
- UC092: Leaked organization token spans repositories: evaluate entire accessible blast radius.

#### G024: Keep remediation auditable without disclosure

- UC093: Alert ticket copies raw token value: sanitize evidence.
- UC094: Push protection exception approved without actor/time: preserve reviewer decision.
- UC095: Developer rotates cloud key but old key remains allowed: verify revocation.
- UC096: Alert dismissed as false positive despite exact validated active secret: reopen/escalate.

### 07 Code scanning, CodeQL, SARIF and static analysis

_Research route: SS08,SS09,SS38,SS44._

#### G025: Select fit-for-repository SAST approach

- UC097: CodeQL default setup misses nonstandard build generation: decide advanced setup.
- UC098: Unsupported language claimed covered by CodeQL: choose supported complementary engine.
- UC099: Monorepo code scanning ignores nested service due incorrect matrix: verify inventory.
- UC100: Tool requires paid private-repository feature: report licensing block or supported alternative.

#### G026: Configure meaningful analysis contexts

- UC101: PR scan succeeds but default branch baseline never scanned: repair event coverage.
- UC102: CodeQL autobuild fails native dependency setup: choose audited manual build.
- UC103: Query suite skips relevant security family after configuration change: inspect effective queries.
- UC104: Generated code excluded from scanner without policy basis: record intentional scope.

#### G027: Integrate third-party findings correctly

- UC105: Semgrep SARIF uploaded to wrong ref: preserve commit association.
- UC106: Multiple SARIF tools reuse same category and override expected results: separate category.
- UC107: Security-events write missing but tool exits zero: detect upload failure.
- UC108: SARIF schema incompatible with GitHub ingestion: validate report format and support.

#### G028: Interpret findings and enforce evidence-backed thresholds

- UC109: Alert dismissed because scanner status green: inspect alert state and severity.
- UC110: Existing accepted debt confused with newly introduced vulnerability: apply baseline policy.
- UC111: SAST false positive suppressed globally after one case: scope exception.
- UC112: Required security status points to wrong provider App: coordinate Governance check source.

### 08 Dependency graph, SCA and pull-request dependency review

_Research route: SS10,SS11,SS35,SS43._

#### G029: Build accurate transitive dependency scope

- UC113: Manifest exists but lockfile missing and graph under-resolves transitive risk: flag.
- UC114: Workspace service excluded from dependency scan: trace module boundaries.
- UC115: Vendored binary not represented by package manifest: include artifact inspection.
- UC116: Dependency graph shows stale results after lockfile change: confirm ref/freshness.

#### G030: Prevent vulnerable dependency introductions

- UC117: PR adds known vulnerable transitive package: fail review according to policy.
- UC118: Dependabot alert exists only on default branch but PR introduces distinct vulnerable version: scan diff.
- UC119: Private registry dependency cannot be resolved by GitHub action: report access requirement.
- UC120: Dependency Review action skipped on non-PR event yet declared required on push: fix trigger/gate mismatch.

#### G031: Interpret advisories and version resolution

- UC121: Advisory affects range not installed final resolved version: avoid false positive.
- UC122: Backport patched version has alternate identifier: verify package ecosystem evidence.
- UC123: Development-only dependency treated as reachable production exploit without analysis: classify context.
- UC124: Known vulnerability has no patch: document mitigation and authorized exception.

#### G032: Keep SCA results coupled to exact revision

- UC125: Scanner uses cached dependency graph from another SHA: invalidate result.
- UC126: Dependency review status exists but action lacked API permission: mark blocked.
- UC127: Split matrix passes one ecosystem and ignores another: no complete pass.
- UC128: Critical advisory published after previous green check: rescan before release as policy requires.

### 09 Dependabot, Renovate, malware advisories, and remediation automation

_Research route: SS11,SS12,SS33,SS41._

#### G033: Automate safe dependency updates

- UC129: Bot opens breaking major update and auto-merges without tests: block.
- UC130: Security PR stalled behind unrelated version churn: prioritize policy-driven update.
- UC131: Private package credential unavailable to Dependabot: separate bot access and runner access.
- UC132: Bot updates lockfile but not generated runtime artifact: verify final resolution.

#### G034: Handle malware distinct from vulnerability alerts

- UC133: New malware advisory exists but CVE scanner has no record: classify malicious package separately.
- UC134: Package version marked malware already executed during CI: investigate credentials as well as upgrade.
- UC135: Internal package collides by name/version with public malware alert: investigate false positive carefully.
- UC136: Auto-triage assumes malware alert triggers Dependabot fix PR: report unsupported behavior.

#### G035: Manage risk-based triage and exceptions

- UC137: Auto-dismiss rule suppresses runtime critical incident: revise rule scope.
- UC138: EPSS-driven priority contradicts exploit observed in production: prioritize actual exploitation.
- UC139: Temporary advisory waiver never expires: enforce owner and review date.
- UC140: Organization rule overrides repository auto-triage: report effective rule precedence.

#### G036: Verify remediation across lockfiles and jobs

- UC141: Bot PR merges but vulnerable version remains transitively pinned: re-resolve.
- UC142: Rebase bot PR reuses stale green checks: require fresh verification.
- UC143: Security update introduces compiler/runtime regression: return actionable failure and bounded retry.
- UC144: Merge of bot PR removes test fixture and appears green due skip: detect missing actual gate.

### 10 Malicious packages, package acquisition, and registry integrity

_Research route: SS12,SS33,SS47,SS22._

#### G037: Assess install-time execution and upstream trust

- UC145: npm install script requests production secret: isolate execution.
- UC146: Typosquatted package differs by one character from approved internal dependency: verify identity.
- UC147: Dependency maintainer ownership changes immediately before release: escalate supplier review.
- UC148: Malicious version published after benign earlier versions: pin and assess affected execution window.

#### G038: Control package source and mirror semantics

- UC149: Public registry shadows internal package name: require explicit namespace/resolution.
- UC150: Internal proxy mirrors malicious package before advisory: quarantine affected digest.
- UC151: Offline build unexpectedly falls back to public registry: detect source drift.
- UC152: Base image references floating latest while release requires immutability: pin resolved digest.

#### G039: Validate checksums, signatures, and lockfiles

- UC153: Lockfile contains checksum but downloaded package differs: fail extraction.
- UC154: Package metadata signature verifies but publisher identity unapproved: enforce identity policy.
- UC155: Mirror rewrites tarball while keeping version: compare digest and provenance.
- UC156: Registry endpoint returns expired cert and insecure fallback is proposed: stop unsafe bypass.

#### G040: Respond to discovered malicious dependencies

- UC157: Affected version already installed by CI: map executed jobs and secrets.
- UC158: Update removes package but attacker-added postinstall artifact persists in cache: clear compromised state.
- UC159: New advisory lacks fixed version: isolate impact and pursue vetted substitute.
- UC160: Downstream project consumed poisoned transitive package: trace all affected outputs.

### 11 SBOM generation, coverage, formats, and lifecycle

_Research route: SS15,SS16,SS19,SS28._

#### G041: Generate SBOM from actual built deliverables

- UC161: Source-only SBOM misses OS packages inside published container: capture built image.
- UC162: Multi-stage Docker build runtime inventory differs from builder: distinguish artifact surfaces.
- UC163: Static executable embeds dependencies invisible to lockfile: record coverage gap.
- UC164: Monorepo publishes multiple packages but shares one ambiguous SBOM: bind per artifact.

#### G042: Preserve machine-readable SBOM integrity

- UC165: CycloneDX output missing version identities: fail quality check.
- UC166: SPDX document references unresolvable package IDs: validate graph.
- UC167: Combined SBOM duplicates component identities and drops relationships: deduplicate correctly.
- UC168: SBOM digest does not match attached release image: reject pairing.

#### G043: Use SBOM for ongoing vulnerability management

- UC169: New advisory lands after release without rebuild: re-evaluate retained SBOM.
- UC170: Security tool rescans mutable tag not released digest: anchor subject.
- UC171: Third-party components marked unknown origin: retain uncertainty.
- UC172: Package removed from new SBOM but remains deployed in prior environment: distinguish versions.

#### G044: Track ownership, distribution, and lifecycle

- UC173: SBOM includes private infrastructure paths in public release: redact sensitive metadata.
- UC174: Customer requires SBOM but release assets omit it: coordinate Release domain.
- UC175: SBOM retention shorter than supported product life: adjust evidence preservation.
- UC176: SBOM generated but never consumed or verified: avoid claiming risk reduction.

### 12 Container image, filesystem, base image and IaC scanners

_Research route: SS16,SS45,SS03,SS26._

#### G045: Select scanner targets and safe execution

- UC177: Trivy scans repository root but misses published container OS layer: correct target.
- UC178: Built image architecture differs from scan architecture: audit scope.
- UC179: Scanner binary downloaded at runtime from mutable tag: verify tool provenance.
- UC180: Container scan executes on privileged host with production secret mounts: isolate.

#### G046: Detect and prioritize runtime-image risks

- UC181: Minimal distroless image yields no package metadata for scanner: report blind spot.
- UC182: Critical CVE fixed in rebuilt base image but deployed digest unchanged: verify promotion.
- UC183: Image contains embedded credentials outside packages: add appropriate secret scan.
- UC184: Vulnerability claimed exploitable only on unreachable optional feature: record context.

#### G047: Treat scanner databases and results as evidence

- UC185: Scanner database update failed offline while run exits zero: mark stale.
- UC186: Multiple scanners disagree on vendor backport: resolve advisory/version provenance.
- UC187: SARIF image findings uploaded without artifact digest: fail correlation.
- UC188: Scanner excluded package layer to reduce noise without owner approval: surface.

#### G048: Constrain configuration and infrastructure risk

- UC189: Dockerfile adds privileged runtime despite passing CVE scan: apply policy.
- UC190: Terraform plan exposes public database despite SAST pass: validate IaC checks.
- UC191: Kubernetes manifest uses wildcard RBAC and insecure hostPath: raise IaC control.
- UC192: Policy scanner is configured but its failure cannot block release: coordinate gate.

### 13 Attestations, provenance, SLSA, and build isolation

_Research route: SS19,SS20,SS21,SS34._

#### G049: Produce verifiable source-to-artifact provenance

- UC193: Artifact has release label but no source SHA/runner identity evidence: require attestation.
- UC194: Attestation subject digest differs from promoted package: reject.
- UC195: Attestation produced for intermediate zip while consumer installs different bundle: fix subject.
- UC196: Attestation generated on untrusted fork job: do not confer trusted publisher identity.

#### G050: Choose realistic SLSA trust level and mechanism

- UC197: Plain attestation claimed to prove SLSA Build Level 3: verify builder isolation requirements.
- UC198: Project promises SLSA level without qualifying runner trust: downgrade claim.
- UC199: Reusable workflow provenance references mutable builder version: bind trusted revision.
- UC200: Platform lacks GitHub attestations for target private repo plan: report alternative/prerequisite.

#### G051: Protect build inputs and reproducibility signals

- UC201: Build pulls branch HEAD during release: replace with audited immutable source.
- UC202: Build dependency installed without lock despite reproducible claim: correct.
- UC203: Rebuild yields different digest due timestamp and claims byte equivalence: investigate.
- UC204: Nested build step downloads unreviewed binary unavailable in build manifest: trace input.

#### G052: Verify provenance at the consumer boundary

- UC205: CI emits signed statement but release never verifies it: no security gate.
- UC206: Attestation certificate identity belongs to unexpected repo or workflow: reject.
- UC207: Offline verification lacks needed trust material: mark blocked not passed.
- UC208: Consumer validates signature but ignores subject digest or predicate: enforce full policy.

### 14 Artifact signing, key custody, and admission policy

_Research route: SS19,SS20,SS23,SS37._

#### G053: Choose supported signing and trust roots

- UC209: Long-lived signing key exposed in build job: consider keyless or isolated signing.
- UC210: Signing certificate valid but issuer and audience differ from policy: reject.
- UC211: Private Sigstore attestation assumed in public transparency log: clarify trust mode.
- UC212: Signing service unavailable on target registry/platform: report prerequisite.

#### G054: Bind signature verification to artifact identity

- UC213: cosign verifies tag after tag moved: resolve immutable digest.
- UC214: Signature for image A reused with image B: fail subject check.
- UC215: SBOM attested for binary but delivery publishes rebuilt binary: require match.
- UC216: Registry accepts unsigned manifest while policy says signed: identify enforcement point.

#### G055: Enforce admission and deployment boundaries

- UC217: Kubernetes admission controller configured audit-only yet release claims enforcement: correct.
- UC218: High-privilege override bypasses signature policy without exception record: block.
- UC219: Admission failure causes fallback unsigned deploy: fail closed.
- UC220: Cross-cluster policy differs and image passes only staging: verify target cluster.

#### G056: Manage key rotation and compromised signers

- UC221: Signing identity revoked but past signatures still accepted without time policy: review.
- UC222: Certificate trust root changed with no pinned policy update: stage migration.
- UC223: Compromised key used to sign malicious artifact: revoke trust and assess affected digests.
- UC224: Ephemeral keyless token mis-scoped to untrusted branch: tighten issuer claim.

### 15 Trusted publishing, registries, release handoff and package integrity

_Research route: SS22,SS19,SS27,SS26._

#### G057: Secure publication identities and package ownership

- UC225: npm trusted publisher accepts unintended workflow file: correct mapping.
- UC226: Package publishing credential shared with PR scans: isolate jobs.
- UC227: Registry maintainer grants outsider publish role unnoticed: audit collaborator change.
- UC228: Publishing bot may overwrite stable version without approval: enforce immutable policy.

#### G058: Verify registry identity and provenance semantics

- UC229: OIDC trusted publishing succeeded but provenance unsupported due private source: state limitation.
- UC230: Artifact attestation subject differs from uploaded registry archive: stop release.
- UC231: Registry index resolves package name to spoofed namespace: validate exact owner.
- UC232: Provenance points to workflow path but run not approved: inspect ref/event trust.

#### G059: Prevent promotion of unverified release artifacts

- UC233: Release rebuilds after security scan instead of promoting same digest: reject.
- UC234: Security gate only scanned source, not packaged dependency set: request artifact check.
- UC235: Multiple registries publish divergent binaries under same version: compare digests.
- UC236: Delayed security advisory makes previously approved artifact blocked under new policy: re-evaluate.

#### G060: Preserve Release domain boundary and response

- UC237: Publishing incident requires rollback: Security scopes compromise, Release owns deployment action.
- UC238: Malicious package already downloaded by consumers: publish advisory with approval.
- UC239: Credential rotation interrupts publisher identity: coordinate phased migration.
- UC240: Self-application plugin package lacks license/source tracking: require package evidence.

### 16 Security gates, required checks, exceptions and merge queues

_Research route: SS08,SS10,SS03,SS01._

#### G061: Make security checks truly enforceable

- UC241: Scanner errors but workflow uses continue-on-error and green status: fail closed.
- UC242: Required check is optional/skipped for fork PRs: reconcile gate design.
- UC243: Security scanner runs after merge rather than before protected merge: move meaningful boundary.
- UC244: Required check points to outdated check name from deleted workflow: repair governance integration.

#### G062: Preserve truthful result and status producers

- UC245: SARIF upload succeeds but scanner fails: preserve failure verdict.
- UC246: Matrix security job missing one language while aggregator passes: validate total set.
- UC247: Timeout cancels scan but aggregate reports success: distinguish incomplete run.
- UC248: Merge queue uses merge_group without scanning merged commit: coordinate correct event.

#### G063: Define risk-based policy and authorized waivers

- UC249: Critical reachable vulnerability found and blanket ignore applied: require scoped exception.
- UC250: Exception approved for one package but applied to all repositories: constrain scope.
- UC251: Waiver expiry passes yet blocking check remains suppressed: re-enable gate.
- UC252: Emergency release explicitly approved despite risk: retain authority and audit evidence.

#### G064: Cross-check CI/Governance/Release ownership

- UC253: CI owns job wiring, Security owns rejection criteria: emit interface.
- UC254: Governance owns required status enforcement but scanner defines no stable output: coordinate.
- UC255: Release consumes unsigned artifact despite Security verified other digest: block handoff.
- UC256: Security outcome claimed passed from configuration alone: require run-specific evidence.

### 17 Infrastructure, policy-as-code and secret-aware configuration

_Research route: SS37,SS03,SS49,SS02._

#### G065: Choose fit-for-target policy scanners

- UC257: CloudFormation not supported by chosen scanner rule pack: choose compatible checker.
- UC258: OPA policy assumes Terraform JSON when provided plan lacks resolved values: mark unknown.
- UC259: Container baseline policy checks Dockerfile but runtime manifest grants privilege: extend scope.
- UC260: Security checks duplicate existing organization enforcement without added value: reuse existing policy.

#### G066: Protect infrastructure secrets and service identities

- UC261: Terraform state artifact uploaded publicly with credentials: block exposure.
- UC262: CI creates cloud key then stores it in logs: prefer scoped OIDC and redact.
- UC263: Secret accessed during pull_request_target from fork: separate environment.
- UC264: Kubernetes secret manifests committed despite encryption claim: inspect encryption and access.

#### G067: Control policy updates and rule ownership

- UC265: Security policy file changed in same untrusted PR as failing config: use trusted baseline.
- UC266: Regulatory policy check auto-disabled to unblock pipeline: require owner approval.
- UC267: Conftest rules fetched by floating branch at runtime: pin reviewed revision.
- UC268: Conflicting organization and repository policy definitions yield different verdicts: resolve authority.

#### G068: Verify plan/apply and actual infrastructure

- UC269: IaC scan passes but current cloud state drifted to public exposure: report boundary.
- UC270: Terraform plan references resources unavailable to scanner: don't assume secure.
- UC271: Policy-as-code ran in audit mode and was described as blocking: correct evidence.
- UC272: IaC remediation requires destructive apply outside current authorization: propose safe bounded change.

### 18 Licenses, policy frameworks, OSPS baseline and supplier governance

_Research route: SS18,SS17,SS46,SS49._

#### G069: Apply versioned security baselines realistically

- UC273: OSPS baseline claims compliance without checking required level: identify applicable maturity.
- UC274: Scorecard score mapped to full security certification: reject equivalence.
- UC275: NIST SSDF mapped to GitHub check without owner evidence: mark manual controls.
- UC276: Compliance report built using outdated framework revision: bind version and effective date.

#### G070: Inspect component licenses and obligations

- UC277: Transitive copyleft license introduced into distributable plugin: require policy review.
- UC278: License metadata missing for bundled Skill sources: flag provenance.
- UC279: Dependency waiver permits excluded license across unrelated packages: narrow.
- UC280: SBOM labels all dependencies permissive though two packages have unknown license: report ambiguity.

#### G071: Evaluate third-party provider integrity

- UC281: Maintainer account compromised on critical dependency: escalate supplier trust.
- UC282: OSS dependency unmaintained yet referenced by critical workflow: compare maintained alternatives.
- UC283: Tool download from unsigned mirror with no checksums: reject.
- UC284: Security tool reports compliant but its own update channel unverified: evaluate supply chain.

#### G072: Generate defensible audit evidence

- UC285: Security control marked green from stale screenshot: capture fresh evidence.
- UC286: Audit package omits repository/ref/actor timestamps: repair traceability.
- UC287: Control verified only on public repositories but compliance claims include private fleet: scope result.
- UC288: Third-party assessor requests evidence beyond current API permissions: state blocker.

### 19 Vulnerability triage, reachability, VEX, and exception lifecycle

_Research route: SS11,SS12,SS16,SS17._

#### G073: Correlate findings without losing risk signals

- UC289: Same CVE from CodeQL, OSV, and image scanner creates three tickets: deduplicate by asset.
- UC290: Alert references package alias not exact installed component: resolve.
- UC291: Multiple services depend on one vulnerable base image: identify common root cause.
- UC292: Risk register references severity only, missing asset exposure and exploitability: enrich.

#### G074: Prioritize exploits and environment impact

- UC293: Medium CVE actively exploited on internet-facing service: elevate priority.
- UC294: Critical CVE in unused build-only tool assumed exposed in runtime: evaluate reachability.
- UC295: VEX states not affected without supporting SBOM and runtime evidence: reject unsupported.
- UC296: EPSS score low but observed exploitation in logs: trust incident evidence.

#### G075: Manage waivers, suppressions and remediation SLAs

- UC297: Security ticket suppressed indefinitely with no approver: require expiry.
- UC298: Exemption references old digest after rebuild: invalidate association.
- UC299: False positive reported by vendor but tool still failing: require policy-compliant suppression.
- UC300: Unpatched vulnerability accepted temporarily: document compensating controls and recheck date.

#### G076: Prove fixed state rather than PR closure

- UC301: Fix PR merged but deploy uses old image: compare published/deployed digest.
- UC302: Dependency patch updates manifest but lockfile resolves vulnerable version: verify actual tree.
- UC303: CodeQL alert auto-closed after path rename without real remediation: inspect code.
- UC304: Owner closes ticket while upstream advisory remains and no scan rerun exists: status unverified.

### 20 Organization-scale security posture, drift and audit signals

_Research route: SS01,SS17,SS30,SS36._

#### G077: Map actual fleet security enrollment

- UC305: Repository newly transferred out of org security configuration: mark coverage change.
- UC306: CodeQL enabled org-wide but one repo opted out: report exception.
- UC307: Org list pagination misses repositories and reports 100 percent coverage: fail census.
- UC308: Private repo inaccessible to audit token: separate unknown from compliant.

#### G078: Detect controls being silently weakened

- UC309: Secret scanning disabled after initial policy rollout: alert on drift.
- UC310: Dependabot security updates off while baseline requires them: determine owner.
- UC311: Ruleset security check enforcement changed to Evaluate: coordinate Governance domain.
- UC312: App installation revoked causing scanner results to stop: detect stale signals.

#### G079: Scope safe remediation across fleets

- UC313: Proposed bulk enablement exceeds token admin rights: stage authorized operators.
- UC314: Existing Terraform controller manages security settings: don't fight desired state.
- UC315: Enforcement on new repos requires approved org-level configuration: prefer native policy.
- UC316: Bulk remediation risks changing excluded research repos: respect classification.

#### G080: Retain auditable snapshots and change evidence

- UC317: Audit observes security posture during ongoing migration: bind temporal snapshot.
- UC318: Scan finds stale check on archived repo and counts it as active failure: classify.
- UC319: Security event was deleted from retention window: document missing evidence.
- UC320: Monitoring workflow succeeds but never compares actual effective configuration: no compliance claim.

### 21 Compromised Actions, scanners, incident response and recovery

_Research route: SS26,SS27,SS03,SS29._

#### G081: Recognize compromised CI tooling

- UC321: Trivy-style force-pushed tag loads malware despite unchanged workflow: resolve executed commit.
- UC322: Security scanner returns expected findings while first stage steals credentials: investigate runtime activity.
- UC323: Workflow lockfile pins malicious commit created before locking: re-evaluate trust.
- UC324: Attacker publishes malicious container from trusted org namespace: use release identity/digest evidence.

#### G082: Scope incident execution and credential exposure

- UC325: Affected Action ran on five branches with distinct token scopes: build per-run matrix.
- UC326: Scanner had cloud creds only in release job: do not assume all workflows exposed.
- UC327: Runner retained malicious cache after compromised run: quarantine affected caches.
- UC328: Secret rotation completed but old tokens still active: verify revocation atomically.

#### G083: Contain, recover, and communicate

- UC329: Compromised Action reused in 60 repos: prioritize all consumers with executed refs.
- UC330: Security tool fix published but registry mirror caches bad version: purge with evidence.
- UC331: Incident analyst proposes deleting run logs needed for forensics: preserve evidence.
- UC332: Published compromised package reached consumers: coordinate disclosure and release response.

#### G084: Harden controls after incidents

- UC333: Postmortem says pinning fixed every issue but transitive dependency unpinned: close gap.
- UC334: Security bot token reissued with same broad grants after compromise: redesign authority.
- UC335: Detection monitoring has no egress telemetry for runners: document residual uncertainty.
- UC336: Recovery declared after new scan while production still uses exposed artifact: verify downstream state.

### 22 Agent Skills, MCP tools and AI-assisted supply-chain boundaries

_Research route: SS24,SS25,SS48,SS49._

#### G085: Vet externally acquired Agent Skills and source prompts

- UC337: Downloaded SKILL.md contains instruction to exfiltrate .env: treat as untrusted.
- UC338: Agent profile has broad filesystem command without permission model: constrain execution.
- UC339: Bundled Skills copied without source revision/license: record provenance.
- UC340: Competing imported instructions override owner requirements: maintain authority boundary.

#### G086: Protect MCP metadata, tool outputs, and schemas

- UC341: Tool description silently changes after approval to request secrets: detect rug pull.
- UC342: MCP result contains adversarial instruction asking agent to change GitHub token: ignore as data.
- UC343: MCP server requests wildcard scope for read-only search: minimize authority.
- UC344: Tool schema maps read operation to destructive method: require trusted validation.

#### G087: Isolate AI agent powers inside GitHub operations

- UC345: AI scanner consumes PR comment and opens write-scoped workflow: separate contexts.
- UC346: Autonomous security fixer disables gates to make checks green: enforce external policy.
- UC347: Agent installs npm tool from retrieved web content without consent: prevent execution.
- UC348: Agent tool error suggests running destructive repo command: preserve user authorization.

#### G088: Evaluate effectiveness of agent security controls

- UC349: Static injection scan passes but live tool execution exfiltrates data: require behavioral evidence.
- UC350: Prompt safety policy present but MCP still has admin token: model cannot enforce permission.
- UC351: Imported Skill changes model behavior unexpectedly on neighboring task: test trigger collision.
- UC352: Security Skill claims protection from all injections without empirical scope: narrow guarantee.

### 23 Security review, incident ownership, education and maintenance

_Research route: SS03,SS18,SS31,SS32._

#### G089: Perform threat-led change review

- UC353: Workflow update grants id-token write without trust-policy discussion: request review.
- UC354: New package publisher pipeline adds direct registry token: compare safer alternatives.
- UC355: Major scanner change is approved from green lint alone: require relevant threat assessment.
- UC356: Source-to-artifact trust boundary altered by reusable workflow migration: re-evaluate.

#### G090: Assign ownership and escalation appropriately

- UC357: Vulnerability alert routed to no active maintainer: identify accountable owner.
- UC358: Security team fixes alert but Governance owns branch protection changes: coordinate.
- UC359: Vendor incident notice arrives after owner offboarding: maintain escalation coverage.
- UC360: Critical finding has no triage SLA: identify policy gap without fabricating deadline.

#### G091: Manage secure exceptions and developer usability

- UC361: False positive blocks all PRs without supported exception path: design bounded waiver.
- UC362: Developer bypasses security scan for speed after long runtime: optimize without weakening gate.
- UC363: Security dashboard shows raw CVE counts but cannot identify introduced risk: improve signal.
- UC364: Emergency remediation needs restricted access approval: expose operator dependency.

#### G092: Keep references and expertise current

- UC365: GitHub feature moved from preview to GA but Skill still calls it unsupported: refresh docs.
- UC366: Scanner repository archived while Skill recommends it as maintained: reassess.
- UC367: Outdated YouTube workflow example uses deprecated token behavior: defer to current official docs.
- UC368: Training demonstrates enabling security but not verifying effective control: mark tutorial limitations.

### 24 Plugin self-security, end-to-end assurance and handoff

_Research route: SS18,SS20,SS24,SS26._

#### G093: Apply security design to this plugin itself

- UC369: Plugin installs but source Skills lack license and pinned provenance: block packaging.
- UC370: Plugin Security Skill calls scanner that isn't present on target runner: report dependency.
- UC371: Agent profile inherits workstation K drive path as runtime prerequisite: reject portability.
- UC372: Plugin can run CI for others but lacks verified self-security gate: make gap visible.

#### G094: Turn constructed cases into meaningful verification

- UC373: Use-case text exists but no observable security assertion: classify design-only.
- UC374: Promptfoo eval grades explanation not actual revoked token or verified attestation: avoid pass.
- UC375: Test fixture for malicious Action would execute real payload on sensitive runner: use inert simulation.
- UC376: Security evaluation runs without host-specific permissions and claims universal coverage: scope results.

#### G095: Produce cross-domain security contracts

- UC377: Security says scan passed but CI check is skipped: require actual run evidence.
- UC378: Governance required check points at unmatched producer: return stable check identity.
- UC379: Release needs attestation before promotion but no trusted verification interface exists: block.
- UC380: Security incident demands rollback but Release domain owns target state: hand off signed assessment.

#### G096: Report exact outcome and remaining dependencies

- UC381: All 384 cases described in catalog but none behavior-tested: label authored only.
- UC382: Feature requires paid plan or admin permissions not present: state blocked.
- UC383: Action unavailable on GitHub Enterprise Server deployment: state supported alternative.
- UC384: Domain hardening complete in Markdown but independent controls untested: do not claim release-ready.

## Research route / source register

These are **source candidates and evidence routes**, not proof that each scenario was observed in an external project. Use the latest official documentation and inspect source revisions before adopting patterns. `community`/`tutorial` entries inform realistic variants but do not override official product semantics.

| ID | Source | Type | URL |
| --- | --- | --- | --- |
| SS01 | GitHub code security product docs | official | https://docs.github.com/en/code-security/concepts |
| SS02 | GitHub Actions security documentation | official | https://docs.github.com/en/actions/how-tos/secure-your-work |
| SS03 | OWASP GitHub Actions Security Cheat Sheet | standard | https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html |
| SS04 | Workflow execution protections, Sep 2026 | official | https://github.blog/changelog/2026-09-17-workflow-execution-protections-in-github-actions-generally-available/ |
| SS05 | cache-mode security, Sep 2026 | official | https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode/ |
| SS06 | Workflow lockfile preview, Oct 2026 | official/preview | https://github.blog/changelog/2026-10-14-github-actions-workflow-lockfiles-in-public-preview/ |
| SS07 | zizmor CI security analyzer | upstream | https://github.com/zizmorcore/zizmor |
| SS08 | GitHub CodeQL advanced setup | official | https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning |
| SS09 | Third-party SARIF upload semantics | official | https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/integrate-with-existing-tools/upload-sarif-file |
| SS10 | GitHub Dependency Review | official | https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request |
| SS11 | GitHub dependency security management | official | https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security |
| SS12 | Dependabot malicious package alerts | official | https://docs.github.com/en/code-security/concepts/supply-chain-security/malware-alerts |
| SS13 | GitHub secret scanning | official | https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning |
| SS14 | GitHub push protection | official | https://docs.github.com/en/code-security/concepts/secret-security/push-protection |
| SS15 | Syft SBOM tool | upstream | https://github.com/anchore/syft |
| SS16 | Grype vulnerability scanner | upstream | https://github.com/anchore/grype |
| SS17 | OpenSSF Scorecard | upstream | https://github.com/ossf/scorecard |
| SS18 | OpenSSF OSPS Baseline v2026.08.28 | standard | https://baseline.openssf.org/versions/2026-08-28 |
| SS19 | GitHub artifact attestations | official | https://docs.github.com/en/actions/concepts/security/artifact-attestations |
| SS20 | actions/attest | upstream | https://github.com/actions/attest |
| SS21 | SLSA GitHub generator | upstream | https://github.com/slsa-framework/slsa-github-generator |
| SS22 | npm trusted publishing / provenance | official | https://docs.npmjs.com/trusted-publishers/ |
| SS23 | Sigstore cosign | upstream | https://github.com/sigstore/cosign |
| SS24 | OWASP MCP Top 10 | standard | https://owasp.org/projects/mcp-top-10 |
| SS25 | OWASP MCP Security Cheat Sheet | standard | https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html |
| SS26 | Trivy upstream March 2026 compromise advisory | incident | https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23 |
| SS27 | Microsoft Trivy compromise incident investigation | incident | https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/ |
| SS28 | Reddit DevSecOps SBOM tool practitioner discussion | community | https://www.reddit.com/r/devsecops/comments/1qky5fq/what_sbom_tools_are_you_actually_using_day_to_day/ |
| SS29 | Reddit DevSecOps GitHub Actions security checklist | community | https://www.reddit.com/r/devsecops/comments/1tdb5eb/how_to_secure_your_github_actions_against_supply/ |
| SS30 | Reddit DevSecOps GitHub security posture drift | community | https://www.reddit.com/r/devsecops/comments/1s4djo5/any_automations_on_tracking_github_security/ |
| SS31 | freeCodeCamp GitHub Advanced Security walkthrough | tutorial | https://www.youtube.com/watch?v=i740xlsqxEM |
| SS32 | GitHub official beginner security tutorial, Mar 2026 | tutorial | https://www.youtube.com/watch?v=zhxXaFzzJYA |
| SS33 | GitHub malware advisories beyond npm, Aug 2026 | official | https://github.blog/security/supply-chain-security/how-we-took-malware-advisories-beyond-npm/ |
| SS34 | GitHub attestation generation & verification | official | https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations |
| SS35 | OpenSSF OSV Scanner | upstream | https://github.com/google/osv-scanner |
| SS36 | OpenSSF Allstar | upstream | https://github.com/ossf/allstar |
| SS37 | OPA Conftest | upstream | https://github.com/open-policy-agent/conftest |
| SS38 | Semgrep | upstream | https://github.com/semgrep/semgrep |
| SS39 | Gitleaks | upstream | https://github.com/gitleaks/gitleaks |
| SS40 | Harden Runner | upstream | https://github.com/step-security/harden-runner |
| SS41 | Renovate | upstream | https://github.com/renovatebot/renovate |
| SS42 | GitHub actions-lock | upstream/preview | https://github.com/github/gh-actions-lock |
| SS43 | GitHub dependency-review-action | upstream | https://github.com/actions/dependency-review-action |
| SS44 | GitHub CodeQL Action | upstream | https://github.com/github/codeql-action |
| SS45 | Trivy upstream | upstream | https://github.com/aquasecurity/trivy |
| SS46 | Anchore Grant license policy | upstream | https://github.com/anchore/grant |
| SS47 | OpenSSF malicious-packages database | upstream | https://github.com/ossf/malicious-packages |
| SS48 | GitHub Awesome Copilot hardening Skill | source-skill | https://github.com/github/awesome-copilot/tree/main/skills/github-actions-hardening |
| SS49 | NIST SSDF SP 800-218 | standard | https://csrc.nist.gov/pubs/sp/800/218/final |
| SS50 | GitHub Actions trusted publishing and supply-chain documentation | official | https://docs.github.com/en/actions/concepts/security |

## Authoring handoff — Domain 3 Skill Creator

- **Inputs:** this owner-reviewed catalog, Domain 3 of `PLUGIN_CONTRACT.md`, `SHARED_TOOL_CAPABILITIES.md`, source-manifest IDs/selected versions/licenses, real GitHub docs and target-specific threat assumptions.
- **Selected augmentation source candidates from contract:** `github-actions-hardening`, `agent-supply-chain`, `pinact`, `senior-security`, `senior-secops`, `threat-model-analyst`, CodeQL/Dependabot/secret-scanning/security-review expertise and official standards; confirm that each upstream source actually exists and is suitable before relying on it.
- **Required runtime deliverables:** `skills/security-supply-chain/SKILL.md`; `references/threat-model-and-trust-boundaries.md`; `references/dependencies-build-artifacts-and-provenance.md`; `references/security-gates-and-audit-evidence.md`; `docs/domain-handoffs/security-supply-chain.md`.
- **Coverage matrix:** map each G/UC to precise skill sections/reference anchors/tool capabilities; label covered, partial, missing, infeasible or intentionally out of domain with reason. Explicitly retain trust-boundary failure modes and source evidence.
- **Validation separate from authoring:** structure and source review are not behavior verified; test security behavior with safe/inert fixtures on isolated runners when separately authorized, including failure and bypass cases; preserve run evidence and fixed digests.
- **Lifecycle:** Security coordinates with CI/CD, Governance and Release without bundling preselected workflows, local scanners or a custom framework unnecessarily. Self-application to this plugin occurs only under separately authorized plugin CI/release stages.
- **Outstanding preconditions:** catalog owner approval; supported GitHub plan/feature level for each consumer; identity/admin scopes; package/registry targets; safe non-production testing fixtures; runnable hosts and evidence retention.

## Catalog verification (authored scope only)

- 24 topic areas; 96 goals (G001–G096); 384 incident/decision cases (UC001–UC384).
- A passing catalog count proves only numbering and authored coverage *intent*, not effectiveness of the eventual Skill or successful GitHub scanning.
- Research performed 2026-10-25; external links are revision-sensitive; verify at runtime. No infrastructure settings, Actions runs, installations or GitHub secrets were changed by this catalog.
