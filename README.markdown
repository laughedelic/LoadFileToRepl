# LoadFileToRepl Sublime Text 2 plugin

## Description

This is a companion plugin to [SublimeREPL](http://github.com/wuub/SublimeREPL) providing a command to load current source file into according REPL. It just uses a REPL command, like `:load "foo.hs"` for Haskell, or `(load-file "foo.clj")` for Clojure and etc.

At the moment it supports Haskell, Scala, Clojure, Ruby and Python REPLs load commands, but it's easy to extend this list. Welcome to suggest yours!

(Honestly, it was tested only with Haskell and Scala REPLs only on Mac OS X, so tell me please if it works good or bad with others).

## Content

### Command `load_file_to_repl`

* reveals REPL view or opens a new one according to the type of current file;
* optionally places REPL in another layout group (to see results simultaneously with code);
* optionally clears REPL before loading file;
* saves current file;
* and finally loads it into REPL, using according command;
* optionally moves cursor to the REPL.

You can call it from command palette.

### Options:

* `clear` — if `true`, clears REPL before loading file (`false` by default);
* `save_focus` — if `true`, saves focus on the sourse file, else moves cursor to REPL (`true` by default).
* `split` —  if it has `"horizontally"` or `"vertically"` (default) value, it determines how window is splitted to show REPL in a new layout group. If it doesn't have one of these two values, or if window was already splitted, this option doesn't take effect — REPL is placed in a new tab or in the next layout group.

   > **Note**: if you want another splitting behavior or more flexibility, take a look at the [Origamy plugin](https://github.com/SublimeText/Origami/).

You can use these options in hotkeys:

### Hotkeys:

* `⌘R` — runs `load_file_to_repl` command (mnemonic for `R` is **R**EPL or **R**eload) and moves cursor to it;

```json
	{ "keys": ["super+r"], 		 "command": "load_file_to_repl", "args": {"save_focus": false}}
```

* `⌘⇧R` — same, but clears REPL before loading file and doesn't move cursor (saves focus on sourse).

```json
	{ "keys": ["super+shift+r"], "command": "load_file_to_repl", "args": {"clear": true}}
```

(On Windows and Linux there is `ctrl` instead of `⌘`)

## Installation

First of all, you _need_ [Sublime Package Control](http://wbond.net/sublime_packages/package_control) — it is extremely useful. If you have it, the rest is really simple:

	⌘⇧P  ➤  Package Control: Install package  ➤  LoadFileToRepl

> **Note**: if you have no SublimeREPL plugin yet, it will be automatically installed at the first time you use LoadFileToRepl command.
