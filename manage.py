import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manage = Manager(app)
migrate = Migrate(app, db)

def make_Shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

@manage.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manage.add_command("shell", Shell(make_context=make_Shell_context))
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()