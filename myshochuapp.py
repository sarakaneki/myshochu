import csv

# create log to csv function.
def log_to_csv(filename, data): #function accepts input of filename or the data
  # with makes sure that the file closes later
  # mode = a is append mode which adds text to the end of the file. 
  # open as file opens or creates a file. 
  with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file) # part of csv module in python.takes FILE and returns as writer obkect
    writer.writerow(data) #taking the writer object and writes a single log of data

# Function to read the CSV file and return the list of entries. 
def read_csv(filename): #filename is just a placeholder
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file) #csv module in python creates a reader object that will read the contents of the file as rows of data. every row is a list
        return list(reader) # converts object into rows. for example ShochuA,8,Good ShochuB,7,Average - > [['ShochuA', '8', 'Good'], ['ShochuB', '7', 'Average']

# Function to write the list of entries back to the CSV file (after editing).
def write_csv(filename, entries):
    with open(filename, mode="w", newline="", encoding="utf-8") as file: # mode="w" will overwrite 
        writer = csv.writer(file) # creates a writer object, part of the csv module
        writer.writerows(entries)  # takes all the data and writes as lists of lists

# Display all entries to the user.
def display_entries(entries):
    print("\n現在のログ:") #\n is to make a new line and make sure that the data is printed on a new line afterwards
    for index, entry in enumerate(entries): # enumerate puts a number to every entry. , is an example of tuple unpacking.
        print(f"{index}: 焼酎 = {entry[0]}, 評価 = {entry[1]}, 感想 = {entry[2]}") #f string is to print variables in string. entry 0 is shochu name.

# Function to edit an existing entry
def edit_entry(entries):
    display_entries(entries)
    try:
        index_to_edit = input("編集するログの番号を入力してください ('exit' で戻る): ").strip()
        if index_to_edit.lower() == "exit":
            print("編集をキャンセルしてメインメニューに戻ります。")
            return  # Return to main menu
        
        index_to_edit = int(index_to_edit)  # Convert the input to an integer if it's not "exit"
        
        if 0 <= index_to_edit < len(entries):
            print(f"選択されたログ: {entries[index_to_edit]}")
            new_drink_name = input("新しい焼酎の名前を入力してください (空欄のままにすると変更なし): ").strip()
            new_drink_rating = input("新しい評価を入力してください (空欄のままにすると変更なし): ").strip()
            new_comment = input("新しい感想を入力してください (空欄のままにすると変更なし): ").strip()

            # Update only if the input is not empty
            if new_drink_name:
                entries[index_to_edit][0] = new_drink_name
            if new_drink_rating.isdigit() and 1 <= int(new_drink_rating) <= 10:
                entries[index_to_edit][1] = new_drink_rating
            if new_comment:
                entries[index_to_edit][2] = new_comment

            print(f"ログが更新されました: {entries[index_to_edit]}")
        else:
            print("無効な番号です。")
    except ValueError:
        print("番号を正しく入力してください。")


def get_name():
    while True:
        shochu_name = input("焼酎の名前を入力してください：　").strip()
        if shochu_name.lower() == "exit":
            print("プログラムを終了します。")
            break
        # Check if the input is not empty and doesn't consist of only numbers.
        # if shochu_name just checks if it is empty or not. Empty string is false. So if shochu_name = True.
        # char.isalpha() checks if there are alphabetic characters. Loop to iterate over every input. any() looks at the whole expression to find a true.
        if shochu_name and not shochu_name.isdigit() and any(char.isalpha() for char in shochu_name):
            return shochu_name
        else:
            print("無効な入力です。名前に数字を含めず、文字を入力してください。")

def get_comment():
    while True:
        comment = input("感想を入れてください：　").strip()
        if comment.lower == "exit":
            print("プログラムを終了します。")
            return None
        # Check if the input is not empty and doesn't consist of only numbers.
        # if shochu_name just checks if it is empty or not. Empty string is false. So if shochu_name = True.
        # char.isalpha() checks if there are alphabetic characters. Loop to iterate over every input. any() looks at the whole expression to find a true.
        if comment and not comment.isdigit() and any(char.isalpha() for char in comment):
            return comment
        else:
            print("無効な入力です。名前に数字を含めず、文字を入力してください。")   

def get_rating(): # input validation for rating
   while True: #continue if true. start loop
    rating = input("評価をしてください (1-10)：　").strip()
    if rating.lower() == "exit":
        print("プログラムを終了します。")
        break
      #validation
    if rating.isdigit() and 1 <= int(rating) <= 10: #checks if input is digit AND checks if it is between 1 and 10
        return int(rating)  # This returns the valid rating to the calling function. Otherwise the program juts keeps on going.
    else:
        print("無効な入力です。1から10の間の数字を入力してください。")

def more_drink():
    while True:
        moredrink = input("あと何か飲みましたか？ Y/N：　").strip().upper()  # Use strip() to remove any leading/trailing whitespace and upper() to handle case insensitivity
        if moredrink == "Y":
            return True  # Indicate that more drinks will be entered
        elif moredrink == "N":
            return None  # Indicate that the user does not want to enter more drinks
        else:
            print("無効な入力です。'Y' または 'N' を入力してください。")

# Main function
def main():
    filename = 'shochu_log.csv'
    print("今日は何を飲みましたか？")

    while True:
        choice = input("\n1: 新しいログを追加\n2: 既存のログを編集\n3: 現在のログを見る\n'exit'でプログラムを終了します。\n選択肢を入力してください: ").strip()
        
        if choice.lower() == "exit":
            print("プログラムを終了します。")
            break

        elif choice == "1":
            while True:
                shochu_name = get_name()
                if shochu_name is None:
                    break

                rating = get_rating()
                if rating is None:
                    break

                comment = get_comment()
                if comment is None:
                    break

                # Create a list with the input data
                data = [shochu_name, rating, comment]
                # Log the data into the CSV file
                log_to_csv(filename, data)
                print(f"{data} を入力しました。")

                if more_drink() is None:
                    print("終了します")
                    break

        elif choice == "2":
            # Read the current entries
            entries = read_csv(filename)
            if entries:
                edit_entry(entries)
                write_csv(filename, entries)
            else:
                print("ログが見つかりません。")
        elif choice == "3":
            #just view the current entries
            entries = read_csv(filename)
            if entries: #if there are logs. otherwise break the program
                while True: #create an infinite loop
                    display_entries(entries) #display function from earlier
                    exit_choice = input("\n'exit'でメインメニューに戻ります: ").strip().lower() # and then ask user what they want to do
                    if exit_choice == "exit":
                        break
        else:
            print("無効な選択です。もう一度選択してください。")

if __name__ == "__main__":
    main()