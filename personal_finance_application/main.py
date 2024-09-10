import click
from project.app import FinanceApp


app = FinanceApp()

@click.command()
@click.option('--username', prompt='Username', help='Your username')
@click.option('--password', prompt='Password', help='Your password') #hide_input=True, confirmation_prompt=True, 
def register(username, password):
    """Register a new user"""
    try:
        app.register_user(username, password)
        click.echo('User registered successfully!')
    except ValueError as e:
        click.echo(str(e))

@click.command()
@click.option('--username', prompt='Username', help='Your username')
@click.option('--password', prompt='Password', help='Your password') #  hide_input=True,
def login(username, password):
    """Login as an existing user"""
    try:
        app.login_user(username, password)
        click.echo('Login successful!')
    except ValueError as e:
        click.echo(str(e))
        
@click.command()
@click.option('--user_id',prompt = 'User Id',type = int , help = 'The ID of user for addinf transaction')
@click.option('--transaction_type', prompt= 'Transaction Type', type = click.Choice(['income', 'expense']), help= 'The Type of Transaction')
@click.option('--category', prompt='Category', help='From where you got the money or expend it like  food, rent , dress and so on...')
@click.option('--amount',prompt= 'Amount', type= float, help = 'Type what amount u gain in income or spend in expense')
# @click.option('--date', prompt="Enter Date (optional)", default = None,help='Enter the todays date')
def add(user_id,transaction_type,category,amount):
    ''' Add transaction as income or expense'''
    try:
        app.add_records(user_id,transaction_type,category,amount)
        click.echo("Transaction added successfully")
    except ValueError:
        click.echo("efewf")


@click.command()
@click.option('--user_id',prompt = 'User Id',type = int , help = 'The ID of user for addinf transaction')
def view(user_id):
    ''' For viewing all Transaction'''
    try:
        app.all_transaction(user_id)
        click.echo("All transaction")
    except ValueError as e:
        click.echo(e)

@click.command()
@click.option('--transaction_id', prompt= 'Transaction id', help='Type the transaction id you want to update')
@click.option('--category',prompt='Category', help='Type the category')
@click.option('--amount',prompt='Amount', help= 'Type the amount if its changed')
# @click.option('--date', prompt='Date', help= 'Enter the Date')
def update(transaction_id, category, amount):
    ''' Update the Transaction'''
    app.update_records(transaction_id, category, amount)
    click.echo("Records updated successfully")

@click.command()
@click.option('--transaction_id', prompt='Transaction Id', help='Type the transaction id You want to delete')
def delete(transaction_id):
    ''' Delte the Transaction'''
    app.delete_records(transaction_id)
    click.echo("Records deleted successfully")

@click.command()
@click.option('--month', prompt = 'Month', help = 'Enter the month in YYYY-MM format')
def month_report(month):
    ''' To view the monthly report'''
    click.echo("Monthly report ")
    app.monthly_review(month)
    

@click.command()
@click.option('--year', prompt = 'Year', help = 'Enter the month in YYYY-MM format')
def year_report(year):
    ''' To view the yearly report'''
    click.echo("Yearly report ")
    app.monthly_review(year)
    click.echo("Yearly report")
    


@click.group()
def cli():
    """Personal Finance Management Application"""
    pass

cli.add_command(register)
cli.add_command(login)
cli.add_command(add)
cli.add_command(view)
cli.add_command(update)
cli.add_command(delete)
cli.add_command(month_report)
cli.add_command(year_report)

if __name__ == '__main__':
    cli()


# Username: ASDFG
# Password:
# Repeat for confirmation:
# Hashed Password (for verification): Aa12!