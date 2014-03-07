openerp-rpc-cli
===============

A simple wrapper around openerp-client-lib that provides you with various argparse CLI arguments so you don't have to re-type them each time you write a script that needs an OpenERP RPC connection.

Usage
-----

Simple usage example:

```
from openerp_rpc_cli import openerp_rpc_cli

class my_oe_cli(openerp_rpc_cli):

    description = "Description shown in argparse help message"

	def set_arguments(self, parser):
		""" Manually add parameters to the argparse object """
		parser.add_argument('my_awsome_parameter', type=str)

	def do(self, arguments, connection):
		""" Do some stuff """
		pass # but I am le tired

my_oe_cli()
```

In the above example we add an additional CLI argument to the existing OE RPC ones specified by the openerp\_rpc\_cli class. Then we put the bulk of our actual code in the do function, making use of the arguments and connection properties. Don't forget to instantiate your class afterwards! do() will be called automatically in the \__init__ function of the openerp-rpc-cli class.
