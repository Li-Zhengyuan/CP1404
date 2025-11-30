import wikipedia

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary.split("\n")[0])
            print(page.url)

        except

        except

        title = input("\nEnter page title: ").strip()

    print("Thank you.")


main()
