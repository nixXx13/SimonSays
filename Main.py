from Entities import User
from Entities.Simon import Simon

"""
Main file to run Simon says locally
"""
def main():
    cmd_user = User.CmdUser()
    simon = Simon(cmd_user)
    simon.play()

if __name__ == '__main__':
    main()