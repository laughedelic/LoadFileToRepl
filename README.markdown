# LoadFileToRepl Sublime Text 2/3 plugin

[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/laughedelic/LoadFileToRepl?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## Description

This is a companion plugin for [SublimeREPL](http://github.com/wuub/SublimeREPL) providing a command to load current source file into according REPL. It just uses a REPL command, like `:load "foo.hs"` for Haskell, or `(load-file "foo.clj")` for Clojure and etc.

At the moment it supports load command for REPLs of the following languages (in alphabetic order):

| Language      | REPL       | Contributor                                        |                                                                |
|:--------------|:-----------|:---------------------------------------------------|:---------------------------------------------------------------|
| Clojure       | Leiningen  | [@chrisalbright](https://github.com/chrisalbright) | [#6](https://github.com/laughedelic/LoadFileToRepl/pull/6)     |
| Common Lisp   |            | [@cfmeyers](https://github.com/cfmeyers)           | [#12](https://github.com/laughedelic/LoadFileToRepl/issues/12) |
| Elixir/Erlang | iex        | [@yitzhakbg](https://github.com/yitzhakbg)         | [#23](https://github.com/laughedelic/LoadFileToRepl/issues/23) |
| F#            | fsi        | [@garystanford](https://github.com/garystanford)   | [#31](https://github.com/laughedelic/LoadFileToRepl/pull/31)   |
| Groovy        | groovysh   | [@rcavalcanti](https://github.com/rcavalcanti)     | [#15](https://github.com/laughedelic/LoadFileToRepl/pull/15)   |
| Haskell       | GHCi       |                                                    |                                                                |
| Idris         |            |                                                    |                                                                |
| JavaScript    | Node       | [@jkroso](https://github.com/jkroso)               | [#9](https://github.com/laughedelic/LoadFileToRepl/pull/9)     |
| Lua           |            | [@mkottman](https://github.com/mkottman)           | [#5](https://github.com/laughedelic/LoadFileToRepl/issues/5)   |
| Matlab        |            | [@rowanc1](https://github.com/rowanc1)             | [#17](https://github.com/laughedelic/LoadFileToRepl/pull/17)   |
| OCaml         |            | [@himito](https://github.com/himito)               | [#36](https://github.com/laughedelic/LoadFileToRepl/issues/36) |
| PowerShell    |            | [@mvoidex](https://github.com/mvoidex)             | [#7](https://github.com/laughedelic/LoadFileToRepl/issues/7)   |
| Prolog        | SICStus    | [@pedrokost](https://github.com/pedrokost)         | [#21](https://github.com/laughedelic/LoadFileToRepl/pull/21)   |
| Python        |            |                                                    |                                                                |
| R             |            |                                                    |                                                                |
| Racket        | XREPL      | [@keyanzhang](https://github.com/keyanzhang)       | [#30](https://github.com/laughedelic/LoadFileToRepl/pull/30)   |
| Ruby          |            |                                                    |                                                                |
| Scala         |            |                                                    |                                                                |
| Scheme        | MIT Scheme | [@cyberzlex](https://github.com/cyberzlex)         | [#19](https://github.com/laughedelic/LoadFileToRepl/pull/19)   |
| Standard ML   | SML        | [@ActiveObject](https://github.com/ActiveObject)   | [#8](https://github.com/laughedelic/LoadFileToRepl/pull/8)     |

It's easy to extend this list. Pull-requests are welcome!


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

You can find these options and their default values in the menu:

	Sublime Text  ➤  Preferences  ➤  Package Settings  ➤  LoadFileToRepl  ➤  Open Settings

or in Command Palette:

	Preferences: LoadFileToRepl Settings



### Key Bindings:

There are two hotkeys predefined:

* `alt+enter` — runs `load_file_to_repl` command with default options:

```json
	{ "keys": ["super+enter"], 		 "command": "load_file_to_repl"},
```

* `alt+shift+enter` — same, but clears REPL before loading file and moves cursor to REPL:

```json
	{ "keys": ["super+shift+enter"], "command": "load_file_to_repl",
	  "args": {
	  	"clear": true,
	  	"save_focus": false
	  }
	}
```

You can find these bindings at

	Sublime Text  ➤  Preferences  ➤  Package Settings  ➤  LoadFileToRepl  ➤  Default Key Bindings

> **Note**: if you don't like them and want to turn off or make your own just set the `use_load_file_to_repl_keybindings` setting to false and reload Sublime.


## Installation

Using [Sublime Package Control](http://wbond.net/sublime_packages/package_control):

> **Note**: you should install first [SublimeREPL](http://github.com/wuub/SublimeREPL) plugin.

	⌘⇧P  ➤  Package Control: Install package  ➤  LoadFileToRepl

Now restart Sublime Text to load the plugin settings. That's it!
