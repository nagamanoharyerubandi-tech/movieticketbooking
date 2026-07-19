movies = ['og', 'peddi', 'spirit', 'dragon', 'fauzi']

shows = ["8.00 am", "11.30 am", "2.30 pm", "5.30 pm", "9.00 pm"]
seats = [40, 40, 40, 40, 40]
prices = [100, 120, 180, 190, 120]

user_name = []
selected_movie = []
tickets_qty = []
show_time = []
total_amount = []

while True:
    print("1.User")
    print("2.Admin")
    print("3.Exit")
    role = int(input("select option:"))

    if role == 3:
        print("Thank You")
        break

    elif role == 1:
        while True:
            print("AVAILABLE MOVIES")
            print("-" * 60)
            print(f"{'Movie':<15}{'Show':<10}{'Price':<10}{'Seats'}")

            for i in range(len(movies)):
                print(f"{movies[i]:<15}{shows[i]:<10}{prices[i]:<10}{seats[i]}")

            m_name = input("Enter movie name : ").lower()

            if m_name in movies:
                idx = movies.index(m_name)
                print("Show Time :", shows[idx])
                time = input("Enter show time : ")

                if time == shows[idx]:
                    print("Available Seats :", seats[idx])
                    qty = int(input("How many tickets : "))

                    if qty <= seats[idx]:
                        name = input("Enter your name : ")
                        amount = qty * prices[idx]
                        seats[idx] -= qty

                        user_name.append(name)
                        selected_movie.append(m_name)
                        tickets_qty.append(qty)
                        show_time.append(time)
                        total_amount.append(amount)

                        print("BOOKING SUCCESSFUL")
                        print("-" * 75)
                        print(f"{'User':<15}{'Movie':<15}{'Show':<10}{'Qty':<10}{'Price':<10}{'Amount'}")
                        print("-" * 75)
                        print(f"{name:<15}{m_name:<15}{time:<10}{qty:<10}{prices[idx]:<10}{amount}")

                    else:
                        print("Only", seats[idx], "tickets available.")

                else:
                    print("Invalid show time.")

            else:
                print("Movie not available.")

            ch = input("Book another ticket (yes/no): ").lower()

            if ch != "yes":
                break

    elif role == 2:
        password = "manohar@4"
        c = 0

        while c < 3:
            passwd = input("enter the password:")

            if passwd == password:
                while True:
                    print("\nADMIN MENU")
                    print("1. Add Movie")
                    print("2. Update Show")
                    print("3. Update Seats")
                    print("4. Delete Show/Movie")
                    print("5. View Bookings")
                    print("6 for view available movies")
                    print("7. Exit")

                    ch = int(input("Enter choice : "))

                    if ch == 1:
                        m_name = input("Enter movie name : ").lower()

                        if m_name in movies:
                            print("Movie already exists.")
                        else:
                            show = input("Enter show time : ")
                            price = int(input("Enter ticket price : "))
                            seat = int(input("Enter total seats : "))

                            movies.append(m_name)
                            shows.append(show)
                            prices.append(price)
                            seats.append(seat)

                            print("Movie added successfully.")

                    elif ch == 2:
                        m_name = input("Enter movie name : ").lower()

                        if m_name in movies:
                            idx = movies.index(m_name)
                            new_show = input("Enter new show time : ")
                            shows[idx] = new_show
                            print("Show updated successfully.")
                        else:
                            print("Movie not found.")

                    elif ch == 3:
                        m_name = input("Enter movie name : ").lower()

                        if m_name in movies:
                            idx = movies.index(m_name)
                            new_seats = int(input("Enter seats : "))
                            seats[idx] = new_seats
                            print("Seats updated.")
                        else:
                            print("Movie not available.")

                    elif ch == 4:
                        print("1.delete show")
                        print("2.delete movie")
                        choice = int(input("select option from above:"))

                        if choice == 1:
                            for i in range(len(movies)):
                                print(movies[i], "-", shows[i])

                            time = input("Enter show time : ")

                            if time in shows:
                                idx = shows.index(time)

                                shows.pop(idx)
                                movies.pop(idx)
                                prices.pop(idx)
                                seats.pop(idx)

                                print("Show deleted successfully.")
                            else:
                                print("Invalid show time.")

                        elif choice == 2:
                            m_name = input("Enter movie name : ").lower()

                            if m_name in movies:
                                idx = movies.index(m_name)

                                movies.pop(idx)
                                shows.pop(idx)
                                prices.pop(idx)
                                seats.pop(idx)

                                print("Movie deleted successfully.")
                            else:
                                print("Movie not found.")

                        else:
                            print("Invalid choice.")

                    elif ch == 5:
                        if len(user_name) == 0:
                            print("No bookings found.")
                        else:
                            print("-" * 75)
                            print(f"{'User':<15}{'Movie':<15}{'Show':<10}{'Qty':<10}{'Amount'}")
                            print("-" * 75)

                            for i in range(len(user_name)):
                                print(f"{user_name[i]:<15}{selected_movie[i]:<15}{show_time[i]:<10}{tickets_qty[i]:<10}{total_amount[i]}")

                    elif ch == 6:
                        print("-" * 60)
                        print(f"{'Movie':<15}{'Show':<10}{'Price':<10}{'Seats'}")

                        for i in range(len(movies)):
                            print(f"{movies[i]:<15}{shows[i]:<10}{prices[i]:<10}{seats[i]}")

                    elif ch == 7:
                        c = 3
                        break

                    else:
                        print("Invalid choice.")

            else:
                print("Invalid password")
                c = c + 1

    else:
        print("Invalid role.")

