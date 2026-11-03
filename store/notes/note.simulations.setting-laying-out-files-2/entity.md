---
id: note.simulations.setting-laying-out-files-2
kind: note
version: 1
title: Laying out the files
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
comments_on:
- simulations.mirror-galaxy
locators:
  paper: T14b
  number: Setting
  section: Running the code
  line: 762
  subsection: Laying out the files
---

## formal
\textbf{In an IDE.} In Visual Studio Code, open \file{T14b\_supplement} with \emph{File, Open Folder} (on Windows, from inside WSL with the WSL extension's \emph{Open Folder in WSL}). Create a virtual environment in that folder, select it as the Python interpreter, and run the stages from the integrated terminal at the top folder. To run or debug one script inside the IDE, give its launch configuration the stage folder as working directory, for example \texttt{"cwd": "\$\{workspaceFolder\}/work/sims"}. In PyCharm, mark \file{code/} as a sources root and set each run configuration's working directory to \file{work/sims}, \file{work/films} or \file{work/galaxy}. No C tooling in the IDE is needed: \file{tpsim} is built once from the terminal.

## technical
pending

## lay
pending

## one-liner
pending
