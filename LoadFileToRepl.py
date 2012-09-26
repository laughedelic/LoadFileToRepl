import sublime, sublime_plugin

SETTINGS_FILE = 'LoadFileToRepl.sublime-settings'

def is_installed(package):
	'''Checks if `package` is installed
	'''
	settings = sublime.load_settings('Package Control.sublime-settings')
	installed_packages = settings.get('installed_packages', [])
	return package in installed_packages

def install(package):
	'''Offers to install `package`, using Package Control api
	'''
	if sublime.ok_cancel_dialog(
			'LoadFileToRepl requires installed %s plugin. \n' % package +
			'Do you want to install it automatically?',
			'Install'):
		PC = __import__('Package Control')
		thread = PC.PackageInstallerThread(PC.PackageManager(), package)
		thread.start()
		PC.ThreadProgress(thread, 
			'Installing package %s' % package,
			'Package %s successfully installed' % package)

def bug_report(message):
	'''Offers to report about problem to the github issue tracker
	'''
	if sublime.ok_cancel_dialog(message, 'Open issue tracker'):
		sublime.active_window().run_command('open_url',
			{'url': 'https://github.com/laughedelic/LoadFileToRepl/issues'})


class LoadFileToReplCommand(sublime_plugin.WindowCommand):

	def run(self, clear=None, save_focus=None, split=None):
		# check depencies
		if not is_installed('SublimeREPL'):
			install('SublimeREPL')
			return

		# import is done inside of function, because this plugin 
		# 	may be loaded before SublimeREPL
		# this is either for master  branch:
		try: from sublimerepl import manager as repl_manager
		except ImportError: # or for release branch of SublimeREPL:
			try: import sublimerepl as repl_manager
			except ImportError: # something strange...
				bug_report(
					'Looks like SublimeREPL plugin is installed, '
					'but cannot be loaded. Try to restart Sublime Text 2. '
					'If it doesn\'t help, report about this issue, please.')
				return

		# if options are not set, use defaults from settings
		settings = sublime.load_settings(SETTINGS_FILE)
		clear      = clear      or settings.get('clear')     
		save_focus = save_focus or settings.get('save_focus')
		split      = split      or settings.get('split')     

		# source is where we are right now
		source_group = self.window.active_group()
		source_view = self.window.active_view()
		if source_view == None:
			sublime.error_message('LoadFileToRepl: No file is selected.')
			return

		filename = source_view.file_name()
		filetype = source_view.scope_name(0).split(' ')[0].split('.')[1]
		if filetype == 'plain':
			sublime.error_message(
				'LoadFileToRepl: Plain text is not supported. '
				'Change file type, please.')
			return

		# if there is only one group, split window
		if self.window.num_groups() == 1:
			if split == 'vertically':
				self.window.run_command('set_layout', {
					'cols'  : [0.0, 0.5, 1.0],
					'rows'  : [0.0, 1.0],
					'cells' : [[0, 0, 1, 1], [1, 0, 2, 1]]
					})
			elif split == 'horizontally':
				self.window.run_command('set_layout', {
					'cols'  : [0.0, 1.0],
					'rows'  : [0.0, 0.5, 1.0],
					'cells' : [[0, 0, 1, 1], [0, 1, 1, 2]]
					})
			# else no any split
		next_group = (source_group + 1) % self.window.num_groups()

		# if there is no opened repl
		if repl_manager.find_repl(filetype) == None:
			# focus on another group to open repl there
			self.window.focus_group(next_group)
			# open repl according to the type of source file
			self.window.run_command('run_existing_window_command', {
				'id'   : 'repl_' + filetype,
				'file' : 'config/' + filetype.title() + '/Main.sublime-menu'
			})

		# reveal repl view, move and clear it if needed
		repl_view = repl_manager.find_repl(filetype)._view
		self.window.focus_view(repl_view)
		if source_group == repl_view.window().active_group():
			repl_view.window().run_command(
				'move_to_group', {'group': next_group})
		if clear:
			repl_view.run_command('repl_clear')

		# focus back on source file if needed
		if save_focus:
			self.window.focus_view(source_view)

		formats = {
			  'haskell' :  ':load "%s"' 
			, 'scala'   :  ':load %s'   
			, 'clojure' :  '(load "%s")'
			, 'ruby'    :  "load '%s'"  
			, 'python'  :  'execfile("%s")'
			}
		text = formats[filetype] % filename

		source_view.run_command('save')
		self.window.run_command('repl_send', {
			'external_id' :  filetype,
			'text'        :  text,    
			'file_name'   :  filename 
			})

		# just to show user that everything is ok
		sublime.status_message(filetype.title() + ' REPL > ' + text)
