from datetime import datetime


def main():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(current_time)


if __name__ == '__main__':
    main()
