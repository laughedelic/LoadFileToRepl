# LoadFileToRepl Sublime Text 2 plugin

## Description

This is a companion plugin to [SublimeREPL](http://github.com/wuub/SublimeREPL) providing a command to load current source file into according REPL. It just uses a REPL command, like `:load "foo.hs"` for Haskell, or `(load-file "foo.clj")` for Clojure and etc.

At the moment it supports Haskell, Scala, Clojure, Ruby and Python REPLs load commands, but it's easy to extend this list. Welcome to suggest yours!

(Honestly, it was tested only with Haskell and Scala REPLs, so tell me please if it works fine with others).

## Content

### Command `load_file_to_repl`

* reveals REPL view or opens a new one according to the type of current file;
* always places REPL in another layout group (to see results simultaneously with code);
* optionally clears REPL before loading file;
* saves current file;
* and finally loads it into REPL, using according command.

### Two hotkeys:

* `cmd+r` — just runs `load_file_to_repl` command (mnemonic for **r** is **R**EPL or **r**eload);
* `cmd+shift+r` — same, but clears REPL before loading file.

(On Windows and Linux there is `ctrl` istead of `cmd`)

## Installation

I recommend you to use [Sublime Package Control](http://wbond.net/sublime_packages/package_control). It is very easy and convenient. See it's [usage](http://wbond.net/sublime_packages/package_control/usage) page. Just use command pallete (`super+shift+p`):
* Install package: SublimeREPL;
* Add Repository: `https://github.com/laughedelic/LoadFileToRepl/`;
* Install package: LoadFileToRepl;

## TODO

* More flexibility — through options (e.g layout) and smaller commands;
* Add support for all SublimeREPL languages;
* Submit this plugin to Community chanell.