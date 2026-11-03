---
id: note.simulations.setting-what-needed
kind: note
version: 1
title: What is needed
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
  line: 707
  subsection: What is needed
---

## formal
\begin{itemize}
\item Python 3.10 or later with numpy, scipy and matplotlib (\file{requirements.txt}).
\item A C compiler with OpenMP, to build \file{tpsim.c}: gcc on Linux. On macOS the system compiler does not accept \texttt{-fopenmp}; gcc from Homebrew should work, but this has not been tested.
\item ffmpeg with the libx264 encoder on the command path, for the two films only.
\item On Windows, the Windows Subsystem for Linux (WSL 2) with Ubuntu. The scripts call the compiled code as \texttt{./tpsim} and write a temporary file under \texttt{/tmp}, which native Windows does not provide.
\item For the full runs, about $7$ GB of disk (the merger snapshots $6$ GB, the film frames $1$ GB) and half a day to a day on two cores (Table \ref{tab:stages}).
\end{itemize}

## technical
pending

## lay
pending

## one-liner
pending
