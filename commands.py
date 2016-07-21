import sublime_plugin
import os

class ShowSimilar(sublime_plugin.WindowCommand):
  def run(self):
    text = self._getFileName()
    self.window.run_command('show_overlay', {'overlay': 'goto', 'text': text,
      "show_files": True})

  def _getFileName(self):
    view = self.window.active_view()
    if view == None:
      return None
    filename = view.file_name()
    basename = os.path.basename(filename)
    return os.path.splitext(basename)[0]
