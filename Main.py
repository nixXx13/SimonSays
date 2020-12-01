import User
from Simon import Simon


def main():
    cmd_user = User.CmdUser()
    simon = Simon(cmd_user)
    simon.play()

if __name__ == '__main__':
    main()