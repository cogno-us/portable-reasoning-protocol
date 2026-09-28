# Installing Portable Reasoning Protocol (PRP) v1.0

PRP is distributed as an open `SKILL.md`-based reasoning protocol. The exact installation method depends on the AI platform.

> **Important:** Platform capabilities change. The instructions below distinguish native Agent Skill support from compatibility methods rather than assuming every platform implements the same Skill standard.

Repository: https://github.com/cogno-us/portable-reasoning-protocol  
Developed by **[Cognous](https://cogno.us)**.

---

## 1. ChatGPT

### Recommended: upload PRP as a Skill

For eligible ChatGPT workspaces with Skills enabled:

1. Open **ChatGPT**.
2. In the sidebar, open **Plugins**.
3. Open the **Skills** tab.
4. Select **Create**.
5. Choose **Upload from your computer**.
6. Upload the packaged PRP Skill ZIP.
7. Review the Skill contents and complete the installation.
8. Start a new chat and invoke it explicitly, for example:
   - `Apply PRP to this decision.`
   - `Use PRP with deep analysis and a concise answer.`

ChatGPT can also select an installed Skill automatically when its description matches the task.

### Alternative: create from the repository

If you are building or adapting the Skill:

1. Clone or download this repository.
2. Keep the Skill directory structure intact:
   - `SKILL.md`
   - `references/prp-core.md`
   - `agents/openai.yaml`
3. Package the directory as a Skill ZIP.
4. Upload it through the Skills interface.

### Fallback when Skills are unavailable

If your ChatGPT plan or workspace does not expose Skills, use the contents of `SKILL.md` as persistent project/workspace instructions where available, or paste the instructions into the highest-priority persistent instruction surface you control.

This fallback preserves much of PRP's behavior but does **not** provide native Skill discovery or progressive loading.

---

## 2. Claude

Claude supports Agent Skills built around `SKILL.md`.

### Claude Code — project installation

To make PRP available within one project, place the PRP skill directory under:

```text
.claude/skills/portable-reasoning-protocol/
```

The resulting structure should resemble:

```text
your-project/
└── .claude/
    └── skills/
        └── portable-reasoning-protocol/
            ├── SKILL.md
            └── references/
                └── prp-core.md
```

Then restart or reload the Claude Code session as appropriate.

### Claude Code — personal installation

To make PRP available across projects, install the Skill under:

```text
~/.claude/skills/portable-reasoning-protocol/
```

Keep `SKILL.md` and its referenced resources together.

### Invocation

Claude may load relevant Agent Skills automatically based on the Skill description. You can also make the request explicit:

- `Use the Portable Reasoning Protocol for this analysis.`
- `Apply PRP at maximum rigor.`

### Claude web/app environments

Where a Claude surface does not expose direct Agent Skill installation, use the PRP instructions as project instructions or equivalent persistent instructions if that surface supports them. Treat this as a compatibility method rather than a native Skill installation.

---

## 3. Gemini

Gemini's documented end-user customization mechanism is **Gems**, not the same native `SKILL.md` installation model used by Agent Skill-compatible environments.

The recommended Gemini deployment is therefore a **PRP Gem compatibility configuration**.

### Create a PRP Gem

1. Open the Gemini web app.
2. Open **Gems**.
3. Select **New Gem**.
4. Name it:
   ```text
   Portable Reasoning Protocol
   ```
5. Copy the body of `SKILL.md` into the Gem's **Instructions** field.
6. Under **Knowledge**, add `references/prp-core.md` as a file if your Gemini configuration supports knowledge files.
7. Save the Gem.
8. Test it with:
   - `Apply PRP to this decision.`
   - `Use maximum rigor but keep the response concise.`

### Recommended Gemini configuration

Use:

- **Gem Instructions:** the contents of `SKILL.md`
- **Knowledge file:** `references/prp-core.md`
- **Gem name:** Portable Reasoning Protocol

This keeps the runtime instructions relatively compact while making the advanced PRP reference available when Gemini needs additional context.

### Limitation

A Gemini Gem is a compatibility implementation of PRP. It should not be described as native installation of this repository's Agent Skill package unless Google adds compatible `SKILL.md` support to the relevant Gemini surface.

---

## 4. GitHub Copilot

GitHub Copilot supports Agent Skills natively.

### Project-specific installation

Inside the repository where you want PRP available, create:

```text
.github/skills/portable-reasoning-protocol/
```

and copy the PRP Skill files into it:

```text
your-repository/
└── .github/
    └── skills/
        └── portable-reasoning-protocol/
            ├── SKILL.md
            └── references/
                └── prp-core.md
```

GitHub also documents `.claude/skills` and `.agents/skills` as supported project Skill locations.

Copilot will decide when to load the Skill based on its description and the current task.

### Personal installation

For a Skill available across local projects, install it under either:

```text
~/.copilot/skills/portable-reasoning-protocol/
```

or:

```text
~/.agents/skills/portable-reasoning-protocol/
```

### GitHub Copilot app

Skills configured for supported repositories or Copilot CLI environments can also be available in the GitHub Copilot app. The app's customization interface includes a **Skills** area for managing them.

### Alternative: repository custom instructions

If you want PRP to apply to essentially every Copilot interaction in a repository rather than load conditionally as a Skill, you can adapt its core rules into:

```text
.github/copilot-instructions.md
```

Use this only when you intentionally want PRP to behave as an always-on repository instruction layer. For conditional loading, the Agent Skill form is preferable.

---

## 5. Verify the installation

After installation on any platform, use a simple test prompt:

```text
Apply the Portable Reasoning Protocol to the following question.

Before answering, distinguish verified facts, assumptions, inference, and uncertainty.
Keep the final answer concise.

[insert question]
```

A working PRP installation should generally:

- preserve the actual user objective;
- distinguish evidence from inference;
- avoid fabricated support;
- expose material assumptions or uncertainty;
- increase rigor when consequences rise;
- avoid unnecessary formalism for simple tasks;
- preserve alternatives when the evidence does not resolve them.

Do not test installation merely by checking whether the model says "PRP is active." Test whether its reasoning behavior changes appropriately.

---

## 6. Updating PRP

When a new version is released:

1. Replace the existing PRP Skill directory with the new version.
2. Preserve the directory name `portable-reasoning-protocol` unless release notes explicitly require a migration.
3. Restart or reload the relevant AI environment if necessary.
4. Re-run your benchmark or test prompts.

For Gemini Gems, update both the Gem Instructions and any attached PRP reference file.

---

## 7. Security and trust

Agent Skills can contain instructions, resources, and in some ecosystems executable scripts. Review any Skill before installing it.

This PRP distribution is intentionally instruction-centric and does not require executable code for its reasoning behavior.

Use the canonical repository when possible:

https://github.com/cogno-us/portable-reasoning-protocol

---

**Portable Reasoning Protocol (PRP) v1.0**  
Developed by **[Cognous](https://cogno.us)**.
