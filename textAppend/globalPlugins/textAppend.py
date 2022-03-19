import globalPluginHandler, api, ui

words = []

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = ("textAppend")

	def script_text_append(self, gesture):
		text = api.getClipData()
		words.append(text)
		api.copyToClip('\n'.join(words))
		ui.message("appended.")
	script_text_append.__doc__ = _("""appends text to each other.""")

	def script_text_clear(self, gesture):
		words.clear()
		api.copyToClip('\n')
		ui.message('clipboard cleared.')
	script_text_clear.__doc__ = _("""clears clipboard.""")

	def script_text_read_clipboard(self, gesture):
		if '\n'.join(words) == '':
			ui.message('clipboard is empty.')
		else:
			ui.message('\n'.join(words))
	script_text_read_clipboard.__doc__ = _("""reads clipboard.""")

	__gestures = {
		"kb:control+shift+c": "text_append",
		"kb:control+shift+r": "text_clear",
		"kb:control+shift+alt+r": "text_read_clipboard"
	}
