# LoadFileToRepl Sublime Text 2 plugin

## Description

This is a companion plugin to [SublimeREPL](http://github.com/wuub/SublimeREPL) providing a command to load current source file into according REPL. It just uses a REPL command, like `:load "foo.hs"` for Haskell, or `(load-file "foo.clj")` for Clojure and etc.

At the moment it supports load command for REPLs of the following languages:

- Haskell
- Scala
- Clojure
- Ruby
- Python
- ... it's easy to extend this list. Welcome to suggest yours!

(Honestly, it was tested only with Haskell and Scala REPLs only on Mac OS X, so tell me please if it works good or bad with others).


## Content

### Command `SublimeREPL: Load current file`

1. reveals REPL view or opens a new one according to the type of current file;
1. optionally places REPL in another layout group (to see results simultaneously with code);
1. optionally clears REPL before loading file;
1. saves current file;
1. and finally loads it into REPL, using according command;
1. optionally moves cursor to the REPL.

You can call it using 

* Command Palette: `⌘⇧P  ➤  SublimeREPL: Load current file  ↩`;
* Menu: `Tools  ➤  SublimeREPL  ➤  Load current file`;
* Hotkeys: see below.


### Settings:

Command `load_file_to_repl` has several options:

* `clear` — if `true`, clears REPL before loading file (`false` by default);
* `save_focus` — if `true`, saves focus on the source file, else moves cursor to REPL (`true` by default).
* `split` —  if it has `"horizontally"` or `"vertically"` (default) value, it determines how window is splitted to show REPL in a new layout group. If it doesn't have one of these two values, or if window was already splitted, this option doesn't take effect — REPL is placed in a new tab or in the next layout group.

   > **Note**: if you want another splitting behavior or more flexibility, take a look at the [Origamy plugin](https://github.com/SublimeText/Origami/).

You can find these options and their default values at 

	Sublime Text 2  ➤  Preferences  ➤  Package Settings  ➤  LoadFileToRepl  ➤  Settings - Default/User 

or in Command Palette. You should not edit "Default" files — use them just as a reference. Open "User" files and write (copy from "Defaults") what you need.


### Key Bindings:

There are two hotkeys predefined:

* `⌘↩` — runs `load_file_to_repl` command with default options:

```json
	{ "keys": ["super+enter"], 		 "command": "load_file_to_repl"},
```

* `⌘⇧↩` — same, but clears REPL before loading file and moves cursor to REPL:

```json
	{ "keys": ["super+shift+enter"], "command": "load_file_to_repl", 
	  "args": {
	  	"clear": true,
	  	"save_focus": false
	  }
	}
```

(On Windows and Linux there is `ctrl` instead of `⌘`)

You can find these bindings at

	Sublime Text 2  ➤  Preferences  ➤  Package Settings  ➤  LoadFileToRepl  ➤  Key Bindings - Default/User


## Installation

First of all, you _need_ [Sublime Package Control](http://wbond.net/sublime_packages/package_control) — it is extremely useful. If you have it, the rest is really simple:

	⌘⇧P  ➤  Package Control: Install package  ➤  LoadFileToRepl

> **Note**: if you have no SublimeREPL plugin yet, it will be automatically installed at the first time you use LoadFileToRepl command.
