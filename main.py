import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create table
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos 
        (id INTEGER PRIMARY KEY,
         name TEXT NOT NULL,
         time TEXT NOT NULL       
        )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("No videos found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Time: {row[2]}")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video added successfully!")

def update_video(index, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, index))
    conn.commit()
    print("Video updated successfully!")

def delete_video(index):
    cursor.execute("DELETE FROM videos WHERE id = ?", (index,))
    conn.commit()
    print("Video deleted successfully!")

def main():
    while True:
        print("\nYouTube Manager | Choose an Option")
        print("1. List all YT Videos")
        print("2. Add a YT Video")
        print("3. Update a YT Video Details")
        print("4. Delete a YT Video")
        print("5. Exit the App")
        choice = input("Enter the Option: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            try:
                index = int(input("Enter the Video ID to Update: "))
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                update_video(index, name, time)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter the Video ID to Delete: "))
                delete_video(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            break
        else:
            print("Invalid option! Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
