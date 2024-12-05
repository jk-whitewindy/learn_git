class Dispatcher:
	cmds = {}
	def reg(self, cmd, fn):
		self.cmds[cmd] = fn

	def run(self):
		pass

	def defalutfn(self):
		print('Unknown Command')
