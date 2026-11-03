---
id: note.simulations.setting-laying-out-files
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
  line: 742
  subsection: Laying out the files
---

## formal
Open the supplement's top folder, \file{T14b\_supplement}, as the project in the IDE and keep its layout:
{ \begin{verbatim}
T14b_supplement/          open this folder as the project
  README.md
  requirements.txt
  code/                   every script and library; nothing is run from here
  outputs/                the deposited results the note quotes
  films/                  the deposited films
  work/                   created by reproduce.py
    bin/tpsim               the compiled simulation code
    tests/                  the two code tests
    sims/                   runs/<tag>/ (mergers) and halos/<tag>/ (assembly)
    films/                  runs/<tag>/ (film re-runs, compact frames)
    galaxy/                 the Galaxy model's outputs
    outputs/                regenerated results, named as in outputs/
    figures/                regenerated figures
  work_quick/             created by reproduce.py --quick, laid out as work/
\end{verbatim}}
Two rules follow from how the scripts are written. First, every file in \file{code/} must stay in that one folder: the scripts import one another by module name (\file{ics}, \file{render\_lib}, \file{sam2} and so on), and Python finds them because they sit beside the script being run. Second, the working directory matters. The simulation and measurement scripts read and write paths relative to the folder they are run from (\file{runs/}, \file{halos/}, \file{./tpsim}), so they must be run from \file{work/sims} (mergers, assembly, measurements) or \file{work/films} (film re-runs), never from \file{code/}. \file{reproduce.py} sets the working directory for each stage and copies \file{tpsim} into place, so the simplest course is to run everything through it.

## technical
pending

## lay
pending

## one-liner
pending
