# skill-test

Learning how skills work with claude, codex, vscode (when it is released soon).

## Skills

### cli

Create a CLI with `typer`, and a package to match around it if it hasn't been created already.

## Installation

### codex

After entering `codex`, use the command:

```bash
$skill-installer please list the skills at <https://github.com/gordonwatts/skill-test/tree/main/.codex/skills>
```

And given the list, add "all of them". Once done you'll have to exit and restart codex. Entering `$` in the terminal will show everything. You can tne try out the below prompt.

### claude

The installation process isn't automated (but probably could be using the `skill-installer` skill!). In the meantime:

```bash
git clone https://github.com/gordonwatts/skill-test.git /tmp/skills
mkdir -p ~/.claude/skills
cp -R /tmp/skills/.codex/skills/* ~/.claude/skills
```

Start up `claude` and us the `/skills` command to make sure they all showed up.

### Sample Prompt

This prompt works well to get a parquet file.

```text
I'd like to create a stand-alone script called `atlas-jetpt.py` that takes one argument, `<dataset>`. The script will use servicex to get the jet pT's for that rucio dataset and save them to a parquet file called "<dataset>_jetpt.parquet" in the current working directory. Once you have the code, please run it against the dataset "mc23_13p6TeV:mc23_13p6TeV.801167.Py8EG_A14NNPDF23LO_jj_JZ2.deriv.DAOD_PHYSLITE.e8514_e8528_a911_s4114_r15224_r15225_p6697" to fix any bugs.
```

This prompt works well to get a png file of a plot.

```text
I'd like to create a stand-alone script called `atlas-jetpt-plot.py` that takes one argument, `<dataset>`. The script will use servicex to plot the jet pT's for that rucio dataset and save them to a png file called "<dataset>_jetpt.png" in the current working directory. Once you have the code, please run it against the dataset "mc23_13p6TeV:mc23_13p6TeV.801167.Py8EG_A14NNPDF23LO_jj_JZ2.deriv.DAOD_PHYSLITE.e8514_e8528_a911_s4114_r15224_r15225_p6697" to fix any bugs.
```

While you can mention skills individually, and explicitly, for this example so few skills were installed it made no difference.
