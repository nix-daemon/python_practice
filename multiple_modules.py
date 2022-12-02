from users import User 
from privileges import Admin, Privileges 

user = Admin('Sharaya', 'Rutherford', 'ssruthe.sa', 101)
user.privileges.show_privileges()