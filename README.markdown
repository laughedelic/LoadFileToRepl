# LoadFileToRepl Sublime Text 2 plugin

## Description

This is a companion plugin to [SublimeREPL](http://github.com/wuub/SublimeREPL) providing a command to load current source file into according REPL. It just uses a REPL command, like `:load "foo.hs"` for Haskell, or `(load-file "foo.clj")` for Clojure and etc.

At the moment it supports Haskell, Scala, Clojure, Ruby and Python REPLs load commands, but it's easy to extend this list. Welcome to suggest yours!

(Honestly, it was tested only with Haskell and Scala REPLs, so tell me please if it works fine with others).

## Features (or just how it works)

- Command `load_file_to_repl`
	* reveals REPL view or opens a new one according to the type of current file;
	* always places REPL in another layout group (to see results simultaneously with code);
	* optionally clears REPL before loading file;
	* saves current file;
	* and finally loads it into REPL, using according command.
- Two hotkeys:
	* `super+r` — just runs `load_file_to_repl` command;
	* `super+shift+r` — same, but clears REPL before loading file.

## Installation

I recommend you to use [Sublime Package Control](http://wbond.net/sublime_packages/package_control).
* Install [SublimeREPL](http://github.com/wuub/SublimeREPL) plugin;
* Add this repo as a new channel to Package Control and install this package.

## TODO

* More flexibility — through options (e.g layout) and smaller commands;
* Add support for all SublimeREPL languages;
* Submit this plugin to Community chanell.