import sublime, sublime_plugin

class LoadFileToReplCommand(sublime_plugin.TextCommand):
	def run(self, edit, clear=False, save_focus=True):
		import sublimerepl

		filename = self.view.file_name()
		filetype = self.view.scope_name(0).split(" ")[0].split(".")[1]

		source_view = self.view
		source_group = source_view.window().active_group()

		# if there is only one group change layout to 2 columns
		if self.view.window().num_groups() == 1:
			self.view.window().run_command("set_layout", {
				"cols"  :  [0.0, 0.5, 1.0],            
				"rows"  :  [0.0, 1.0],                 
				"cells" :  [[0, 0, 1, 1], [1, 0, 2, 1]]
				})
		next_group = (source_group + 1) % self.view.window().num_groups()

		if sublimerepl.find_repl(filetype) == None:
			# focus on another group to open repl there
			self.view.window().focus_group(next_group)
			# open repl according to the type of source file
			self.view.window().run_command("run_existing_window_command", {
				"id"   :  "repl_" + filetype,
				"file" :  "config/" + filetype.title() + "/Main.sublime-menu"
			})

		# reveal repl view, move and clear it if needed
		repl_view = sublimerepl.find_repl(filetype)._view
		self.view.window().focus_view(repl_view)
		if source_group == repl_view.window().active_group():
			repl_view.window().run_command("move_to_group", {"group": next_group})
		if clear:
			repl_view.run_command("repl_clear")

		# focus back on source file if needed
		if save_focus:
			self.view.window().focus_view(source_view)

		formats = {
			  'haskell' :  ':load "%s"' 
			, 'scala'   :  ':load %s'   
			, 'clojure' :  '(load "%s")'
			, 'ruby'    :  "load '%s'"  
			, 'python'  :  'execfile("%s")'
			}
		text = formats[filetype] % filename

		source_view.run_command("save")
		self.view.window().run_command("repl_send", {
			"external_id" :  filetype,
			"text"        :  text,    
			"file_name"   :  filename 
			})

		# just to show user that everything is ok
		sublime.status_message(filetype.title() + " REPL > " + text)
