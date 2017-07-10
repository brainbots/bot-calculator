from .abstract_bot import AbstractBot
from bots.action import Action

class CalculatorBot(AbstractBot):
	def __init__(self, id):
		# TODO: Improve the manually-added calculator.calculate intent 
		actions = ['calculator.calculate']
		super().__init__(id, actions)
		# REQUIRED
		self.expr = None
		self.num = None
		self.op = None

	def extract_attr(self, intent):
		# TODO: Handle binary operations
		self.expr = intent.query_string
		self.num = intent.parameters.get('number')
		self.op = intent.parameters.get('op')

	def execute(self):
	    result = None
	    try:
	        result = eval(self.expr)
	    except Exception as e:
	        # Try to form the expression using
	        # the num and op lists
	        if len(self.op) == len(self.num)-1:
	            ex = []
	            ex.append(str(self.num.pop(0)))
	            for op in self.op:
	                ex.append(op)
	                ex.append(str(self.num.pop(0)))
	            result = eval(''.join(ex))

	    return Action(
	        action_type = 'message',
	        body = result if not None else
	            'Please enter a valid (simple) expression',
	        bot = self.id,
	        keep_context = False)

	def request_missing_attr(self):
	    #TODO: Check for missing attr
	    return

	def has_missing_attr(self):
	    return False

	def is_long_running(self):
	    return False
