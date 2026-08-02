from core.application import GeoShieldApplication


def main():
    app = GeoShieldApplication()

    app.initialize()

    print(app.status())


if __name__ == "__main__":
    main()