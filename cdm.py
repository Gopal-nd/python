
def hello(name,lang):
    greeting= {
        "english":"Hello",
        "spanish":"halo",
        "German":"Hallo"
    }
    msg= f"{greeting[lang]} {name}"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personal greeeting"

    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True ,help="The name of Person to greet"
    )
    parser.add_argument(
        "-l","--lang",metavar="language",
        required=True , choices=["english","spanish","German"],
        help="The name of Person to greet"
    )

    args = parser.parse_args()

    msg = f"Hello {args.name}"
    hello(args.name,args.lang)