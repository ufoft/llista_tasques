import tasca

def main():
    tasca_1 = tasca.Tasca(None, "Tasca nova 1")    # On None és persistencia i "Tasca nova 1" el nou títol.
    tasca_2 = tasca.Tasca(None, "Tasca nova 2")
    tasca_3 = tasca.Tasca(None, "Tasca nova 3")

    print(tasca_1)
    print(tasca_2)
    print(tasca_3)

if __name__ == "__main__":
    main()