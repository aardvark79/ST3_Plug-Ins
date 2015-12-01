import sublime, sublime_plugin

class goto_definition_in_active_fileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selections = self.view.sel()
        
        if len(selections) > 1:
            return
            
        selection = selections[0]
        word = None
        
        if selection.empty():
            word = self.view.substr(self.view.word(selection))
        else:
            word = self.view.substr(selection)
        
        self.view.window().run_command("show_overlay", {"overlay": "goto", "show_files": False, "text": "@" + word})
        self.view.window().run_command("hide_overlay")
        
        self.view.window().run_command("move_to", {"to": "bol", "extend": False})
        return