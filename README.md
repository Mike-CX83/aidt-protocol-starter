# AIDT Protocol Starter

## Project Description

AIDT is a file based workflow for coordinating AI assisted development across separate sessions. Its Handshake and Handoff Protocol gives each role a written scope, working state, reports, and decisions so a project can continue without relying on chat memory alone.

The starter includes Markdown instructions, YAML templates, JSON schemas, Python helpers, and GitHub Actions checks. It is intended for developers using tools such as Cursor who want an explicit record of what changed, what was approved, and what should happen next.

## Contents

* [Usage](#usage)
* [Installation](#installation)
* [How It Works](#how-it-works)
* [Validation and Utilities](#validation-and-utilities)
* [Known Limitations](#known-limitations)
* [Tech Stack](#tech-stack)
* [Author](#author)

## Usage

The workflow defines three roles:

* **A1, Logic:** requirements, specifications, and related planning artifacts.
* **A2, Build:** implementation, infrastructure, and tools.
* **A3, Review:** review, coordination, and recorded decisions.

Start with the included files:

1. Open the repository in your editor and describe the project in [handoff/brief.md](handoff/brief.md).
2. Read the [starter guide](start/START-HERE.md) and [A3 bootstrap prompt](prompts/agent3-autoboot.md).
3. In an AI coding session with access to the repository, use the prompt to prepare real plans and initial working states. Review the generated files.
4. Use separate A1 and A2 sessions to read their own `STATE.yaml` and carry out the listed next actions.
5. For a proposed plan change, prepare reports and responses in a new handshake folder, then record A3's decision.
6. Update the decision ledger and each affected state file so the next session can resume from written evidence.

The repository does not launch AI agents or connect to a model provider. Sessions and permissions are supplied by your chosen development tool. The prompt describes work for that session to perform; it is not a background service.

## Installation

### Requirements

* Git and a text editor.
* Python 3 for validation and utilities.
* PyYAML and jsonschema.
* Bash and optionally Make for the shell shortcuts.
* An AI enabled development environment if using the agent prompts.

```bash
git clone https://github.com/Mike-CX83/aidt-protocol-starter.git
cd aidt-protocol-starter
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pyyaml jsonschema
```

The Markdown and YAML workflow can be used directly. There is no application server, database, or model API key required by the starter itself.

On Windows, use the environment's Windows activation command and run the Python utilities directly, or use a Bash compatible environment for the shell commands.

## How It Works

Each agent folder stores its identity, procedures, requirements, build plan, and current state. The state file points to canonical project files and records next actions.

A handshake groups A1/A2 reports and responses with an A3 decision. Decisions can be summarized in `handoff/DECISIONS.md` and architecture decision records under `docs/adr/`.

The protocol asks participants to update plans only through the review process. Templates make the structure repeatable; human and agent discipline still determine the quality and legitimacy of the decisions.

## Validation and Utilities

From the repository root:

```bash
python scripts/self_test.py
python scripts/schema_validate.py
```

The self check verifies a few essential files and the size of existing A1/A2 state files. The schema utility checks state and handshake YAML against the supplied schemas, with the limitations below.

On Bash:

```bash
bash scripts/validate.sh
```

Other utilities:

```bash
python scripts/metrics.py
python scripts/export_pack.py
```

The metrics utility writes a CSV under `metrics/`, named for the current week, containing the handshake decisions it finds. It does not filter records to that week or calculate lead time.

The export utility writes a ZIP under `deliverables/` containing selected A1/A2 plans and states, handshake files, decisions, and ADRs. It is not a complete repository backup.

## Known Limitations

The source review on November 16, 2026 found:

* `scripts/aidt.py` fails Python syntax parsing at line 55 because of an escaped string delimiter. Its `new-agent`, `new-handshake`, `rollup`, and `apply-decision` commands, including Make wrappers, are not usable until repaired.
* The same helper references `re` without importing it. Its rollup implementation also writes only part of the state required by the schema. Fixing the syntax alone will not finish those commands.
* `scripts/schema_validate.py` can downgrade a schema error to a warning when basic keys exist. A passing result does not establish full schema compliance.
* The plan edit guard checks whether a decision filename is present in a diff. It does not verify that the decision approves the change or matches the edited plan.
* CI runs structure/schema checks and the plan edit guard. It does not automatically roll up agent states.
* Agent creation can overwrite an existing agent's template files once the CLI is repaired; it should not be used casually on active state.

Use the manual template workflow while the CLI is repaired. Some older guides describe intended automation more strongly than the current implementation supports.

This review parsed all five Python scripts without executing the project workflow: four parsed successfully, and `aidt.py` failed. The full CI and schema checks were not rerun.

## Tech Stack

* Markdown for instructions and decision records.
* YAML for state, plans, and reports.
* JSON Schema for document structure.
* Python, PyYAML, and jsonschema for helpers.
* Bash, Make, Git, and GitHub Actions for checks and workflow support.

## Further Reading

* [Protocol specification](docs/Spec.md)
* [Cursor guide](docs/Cursor-Guide.md)
* [New session checklist](start/New-Window-Checklist.md)
* [Why the project exists](docs/Open-Letter.md)
* [Contribution guide](CONTRIBUTING.md)
* [Historical README checkpoint](docs/README_CHECKPOINT_2026_11_16.md)

## Author

**Mike Hankins**, founder of CX83 Labs and software engineering student focused on systems design and AI assisted workflows.

[GitHub](https://github.com/Mike-CX83) · [CX83 Labs](https://cx83labs.com)

## License

[MIT License](LICENSE).
