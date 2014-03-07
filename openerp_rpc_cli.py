import argparse
import openerplib

class OpenErpRpcCli(object):
	"""
	Wrapper around openerp-client-lib (openerplib) to provide argparse command line
	arguments to CLI programs that use an OE RPC connections.

	To use, inherit this class and override the do(arguments,  connection) function.
	You can also override the set_arguments(parser) function to set your own argparse
	arguments. self.description provides the argparse CLI description. 
	"""

	description = """
	YOUR AD HERE! Override the description attribute in your child class to change this message.
	"""

	def __init__(self):
		"""
		Setup RPC cli arguments 
		"""
		# setup argparse RPC arguments
		self.parser = argparse.ArgumentParser(self.description)

		self.parser.add_argument('database', type=str, help='Name of database to connect to')
		self.parser.add_argument('--hostname', type=str, help='Hostname of the OpenERP server', default='localhost')
		self.parser.add_argument('--port', type=int, help='RPC port of the OpenERP server', default=0)
		self.parser.add_argument('--protocol', type=str, help='The protocol used by the RPC connection', default='xmlrpc')
		self.parser.add_argument('--username', type=str, help='Username to connect to the OpenERP server', default='admin')
		self.parser.add_argument('--password', type=str, help='Password to connect to the OpenERP server', default='admin')
		self.parser.add_argument('--saas', type=bool, help="If connecting to SaaS, automatically set appropriate port and protocol", default=False)

		# call set_arguments to let user define their own cli arguments
		self.set_arguments(self.parser)

		# parse args
		self.args = self.parser.parse_args()
		
		# The saas option sets up some params to be used with OE SaaS instances
		if self.args.saas:
			self.args.protocol = 'xmlrpcs'
			self.args.port = 443

		# Open the connection and check the login
		self.conn = openerplib.get_connection(hostname=self.args.hostname, database=self.args.database, login=self.args.username, password=self.args.password, port=self.args.port or 'auto', protocol=self.args.protocol)
		self.conn.check_login()

		# Call self.do to run the users code
		self.do(self.args, self.conn)

	def set_arguments(self, parser):
		"""
		Override me and use parser to manually set your own CLI arguments. No need to call super.
		@param parser: instance of argparse.ArgumentParser
		"""
		pass

	def do(self, arguments, connection):
		"""
		Override me and do something with arguments and connection! No need to call super.
		@param arguments: argparse arguments as returned by argparse.ArgumentParser().parse_args()
		@param connection: openerplib RPC connection
		"""
		pass
