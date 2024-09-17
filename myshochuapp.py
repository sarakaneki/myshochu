import csv

# create log to csv function.
def log_to_csv(filename, data): #function accepts input of filename or the data
  # with makes sure that the file closes later
  # mode = a is append mode which adds text to the end of the file. 
  # open as file opens or creates a file. 
  with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file) # part of csv module in python.takes FILE and returns as writer obkect
    writer.writerow(data) #taking the writer object and writes a single log of data

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
        if commentlower == "exit":
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

print("今日は何を飲みましたか？")

# main function
def main():
    filename = 'shochu_log.csv'
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

if __name__ == "__main__":
    main()