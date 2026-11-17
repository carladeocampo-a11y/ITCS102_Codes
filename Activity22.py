anime_type = ["Isekai", "Adventure", "Scifi", "Mahnwa"]
anime_title = []

while True:
    ans = input("Do you know any anime? ---> (yes/no)")

    if ans.lower() == 'yes':
        print("What type of anime is it? ---> select from the list")
        for x in anime_type:
           print(x)
        a_type = input("type ---> ")

        title = input("What is the title of the anime? ---> ")
        anime_title.append(title)
        continue
    else:
        print("Thank you!")
        break
