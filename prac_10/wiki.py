import wikipedia

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary.split("\n")[0])
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            print(e.options)

        except

        title = input("\nEnter page title: ").strip()

    print("Thank you.")


main()
