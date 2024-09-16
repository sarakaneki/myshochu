import csv

# create log to csv function.
def log_to_csv(filename, data): #function accepts input of filename or the data
  # with makes sure that the file cloess later
  # mode = a is append mode which adds text to the end of the file. 
  # open as file opens or creates a file. 
  with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file) # part of csv module in python.takes FILE and returns as writer obkect
    writer.writerow(data) #taking the writer object and writes a single log of data

def get_rating(): # input validation for rating
   while True: #continue if true. start loop
      rating = input("評価をしてください (1-10): ")
      #validation
      if rating.isdigit() and 1 <= int(rating) <= 10: #checks if input is digit AND checks if it is between 1 and 10
            return int(rating)  # This returns the valid rating to the calling function. Otherwise the program juts keeps on going.
      else:
          print("無効な入力です。1から10の間の数字を入力してください。")

print("今日は何を飲みましたか？")

# main function
def main():
    # CSV file to log the data
    filename = 'shochu_log.csv'

    # Ask the user for the 3 parameters
    shochu_name = input("焼酎の名前を入力してください： ")
    rating = get_rating()
    comment = input("感想を入れてください: ")

    # Create a list with the input data
    data = [shochu_name, rating, comment]

    # Log the data into the CSV file
    log_to_csv(filename, data)
    
    print(f"{data}　を入力しました。")

if __name__ == "__main__":
    main()