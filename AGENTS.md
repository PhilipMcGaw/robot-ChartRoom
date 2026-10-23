# Chartroom working rules

## Purpose

Chartroom is the cross-project engineering knowledge base for the Robots project. It records shared architecture, engineering rationale, significant decisions, development guidance, deployment and commissioning procedures, hardware documentation references, simulation and test knowledge, tutorials, troubleshooting guidance, and the project roadmap.

Chartroom is not the implementation authority for CuttleOS, SquidLink, or NautiPi. Those repositories remain authoritative for their own code, simulation, hardware, and repository-specific implementation details.

## Repository structure

- source/ — DokuWiki page text (`.txt`) and retained media for the `sites:chartroom` namespace; nested directories map to namespaces.
- source/architecture/ — cross-project architecture, communications, NATS, robot profiles, and system boundaries.
- source/cuttleos/, source/cockpit/, source/datalogger/ — cross-project knowledge for the robot software areas.
- source/hil-sil/ — hardware-in-the-loop and software-in-the-loop knowledge.
- source/ros2/ — ROS 2 and Gazebo learning and integration material.
- source/development/ — development, testing, deployment, hardware documentation, and documentation standards.
- source/tutorials/ — reusable engineering and development tutorials.
- source/decisions/ — significant engineering decisions and their rationale.
- source/research/ — research and reference notes; distinguish these from validated decisions.
- README.md — repository orientation and contribution guidance.

Project architecture, repository authority, and current build/deployment facts are maintained in MASTER_CONTEXT.md. These working rules define agent behaviour and editing discipline; they are not a second project-status document.

## Unavailable reference projects

The former TermiSoc reference project is not part of the current workspace. Do not recreate or add TermiSoc pages or reference content to Chartroom unless explicitly requested and supported by an available source.

## Source-of-truth rules

1. source/ is the canonical source for Chartroom content.
2. The implementation repositories are authoritative for repository-specific behaviour: CuttleOS for robot-side software, SquidLink for ROS 2/Gazebo/simulation, and NautiPi for physical hardware and embedded projects.
3. Do not duplicate implementation documentation in Chartroom unless the cross-project view adds clear value.
4. When duplicating a fact for cross-project context, link to the authoritative repository or document.
5. Engineering decisions MUST distinguish proposed, designed, implemented, simulated, bench-tested, validated, and production-proven states.
6. Do not present an assumption or unverified research note as implemented or validated behaviour.
7. Preserve existing documentation unless the task explicitly requests correction, removal, or restructuring.
8. Keep source/ as the canonical content until the DokuWiki import and rendered pages have been checked.
9. Do not add credentials, private keys, tokens, passwords, or private operational data.

## DokuWiki destination

The intended DokuWiki destination for Chartroom is the `sites:chartroom` namespace at
<https://labbook.skippy.org.uk/doku.php/sites/chartroom/>. The migration has not yet been
completed. Until it is complete and confirmed, `source/` remains the canonical Chartroom
content source. Quartz, its Node.js/npm build, deployment scripts, and generated static output have been removed from this repository.

When preparing or carrying out the migration:

- Preserve the directory hierarchy as DokuWiki namespaces. Use each `start.txt` as the corresponding namespace start page.
- Keep page content in core DokuWiki syntax and use namespace IDs for internal links. Check rendered pages and links after import; do not assume optional plugins are installed.
- Use the Labbook connector with an API token configured in its authentication settings. Do not
  store or repeat tokens, passwords, or other credentials in this repository or its documentation.
  Verify access by reading the target namespace before writing pages.
- The DokuWiki XML-RPC endpoint is <https://labbook.skippy.org.uk/lib/exe/xmlrpc.php>. Use it only
  when the server has remote API access enabled and the account is permitted. Use a client that
  retains authentication cookies, and verify the API version and a read of the target namespace
  before writing pages.
- A successful login through one interface does not prove that another interface is authenticated.
  Verify access with a read operation through the same interface that will be used for migration.

## Documentation and evidence

New technical claims SHOULD identify their source where practical: repository path, issue, decision record, standard, manufacturer document, test result, or stable external reference.

When sources disagree, preserve the disagreement, identify the authoritative source, explain the decision or uncertainty, and do not silently choose a convenient interpretation.

When recording engineering evidence, distinguish retained source material from recollection, inference, proposed wording, and unresolved claims. Do not fill gaps with plausible assumptions or present a question, draft, or general engineering explanation as evidence that a particular design, action, test, or result occurred. Attribute work to an individual only when the source or an explicit account supports that attribution. Keep numerical claims traceable to a source or clearly label them as approximate or recalled. Record material conflicts and unknowns plainly, and prefer a narrower supported claim over a broader unsupported one.

Hardware documentation SHOULD identify the manufacturer, model or part number, document type, revision/date where known, and an official source link where available. Do not redistribute third-party manuals when a stable official link is sufficient.

Use Markdown footnotes for citations when source criticism or provenance matters. Use ordinary Markdown links for project navigation and external documentation.

## Markdown and house style

All newly authored project prose, comments, commit messages, and documentation MUST use British English, clear technical language, and consistent terminology.

Define an unfamiliar abbreviation or acronym at first use on each page, then use it consistently. Avoid introducing an abbreviation that is used only once. Preserve official names and identifiers as written.

For technical explanations and procedures, use relevant ASD-STE100 principles: choose familiar, specific words; keep terminology consistent; and use clear sentence structure. Do not force controlled vocabulary into established technical terms, quotations, code, or natural narrative. Do not claim full ASD-STE100 compliance unless requested and checked against the current official specification, including its applicable rules and dictionary.

Use gender-neutral wording for roles and groups when gender is irrelevant. Use a person's stated name and pronouns; do not infer gender or pronouns. If they are unknown, repeat the person's name or role, or use singular `they`. Preserve gendered wording in quotations and historical source material, and distinguish it from editorial wording.

Use British spellings such as organisation, behaviour, colour, centre, and licence; Oxford commas where useful; ISO dates (YYYY-MM-DD); and SI symbols with a non-breaking space between values and units, such as 10 mm, 5 V, and 25 °C.

Use `program` for computer software and `programme` for an organised activity or series. Use `licence` as a noun and `license` as a verb. For month-and-year references in prose, write `April 2025`; retain ISO dates for full dates and numeric formats where filenames, code, data, or external conventions require them.

When reporting an imperial measurement from a source, retain the source value and give an approximate SI equivalent in parentheses where useful. Round conversions to a precision supported by the source, and keep conversions outside verbatim quotations. Use Unicode characters where they are semantically correct and readable.

Use precise status terms such as designed, planned, implemented, simulated, bench-tested, validated, and production-proven. Preserve quotations, code, identifiers, URLs, product names, and official third-party spellings exactly.

Use RFC 2119 terms (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY`) only when deliberately stating a requirement or recommendation; do not use them casually.

Keep front matter consistent with nearby pages. Do not invent dates, test results, or implementation details.

## Multi-agent collaboration

The repository is shared project memory and is model-agnostic. Agents MUST read applicable AGENTS.md files, inspect current files before changing them, preserve unrelated work, avoid copying private reasoning into project files, record concise conclusions and uncertainty, prefer small reviewable changes, and use Git history as the audit trail.

Do not overwrite another contributor's work. If a shared file has changed during the task, re-read it and reconcile the update before writing.

## Publishing

This repository no longer contains a static-site build or publishing workflow. The DokuWiki
import is still incomplete; retain `source/` until the destination pages and links have been
checked. Do not claim that the previous static site URL redirects to DokuWiki unless that change
has been verified outside this repository.

## Editing workflow

Before editing: inspect relevant source files and conventions; decide whether the change belongs in source/ or repository guidance; check links, front matter, diagrams, and repository paths; and consult the authoritative implementation repository for repository-specific claims.

After editing: validate Markdown/front matter; check affected links and media. When DokuWiki access is available, check the rendered destination pages. Summarise changes, validation, and uncertainty.

## Git workflow

On Windows, use GitHub Desktop as the default interface for repository status, reviewing diffs, staging selected files, committing, fetching, integrating remote changes, and pushing. Do not assume Git is unavailable because `git` is not on PowerShell's `PATH`.

Use command-line Git only when GitHub Desktop cannot perform a required operation, is unavailable, or repeatable automation is materially more appropriate. On Windows, use a repository helper such as `tools/github-desktop-git.cmd` when present. If no helper is available, use the documented GitHub Desktop bundled Git executable for the current host; recheck its path and version after GitHub Desktop upgrades. On macOS, use command-line Git from this repository's working directory and the machine's configured authentication.

On Windows host `GBR-3N87GR3`, the documented GitHub Desktop 3.6.7 executable is `C:\Users\philip.mcgaw\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd\git.exe` (`git version 2.53.0.windows.4`, checked 2026-10-09). Use it when the Desktop interface cannot perform a required operation; recheck after upgrades.

Before pushing, fetch the configured remote and integrate its latest branch into the task branch. Resolve divergence while preserving unrelated work, then review the final diff and push. Do not expose credentials or tokens.

Use focused changes with clear commit messages. After a requested change has been validated, create the focused commit and push it to the configured remote and current working branch as part of the normal workflow, unless the user explicitly asks to stop before committing or pushing, or a concrete blocker prevents it. Before staging, inspect the complete status and diff so that unrelated work is not included. Do not rewrite history, force-push, reset unrelated work, or include unrelated changes. The default branch is main unless the repository states otherwise.
