from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()
def wite_words(word_count, file_name):
    with open(file_name,'w', encoding='UTF-8') as file:
        for word in range(1, word_count +1):
            file.write(f"Какое-то слово № {word} \n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    pass
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

time_and = datetime.now()
time_result = time_and - time_start
print(f"Поток {time_result}")

time_start = datetime.now()
wite_words_one = Thread(target=wite_words,args=(10, "example5.txt"))
wite_words_two = Thread(target=wite_words,args=(30, "example6.txt"))
wite_words_three = Thread(target=wite_words,args=(200, "example7.txt"))
wite_words_four = Thread(target=wite_words,args=(100, "example8.txt"))

wite_words_one.start()
wite_words_two.start()
wite_words_three.start()
wite_words_four.start()

wite_words_one.join()
wite_words_two.join()
wite_words_three.join()
wite_words_four.join()

time_and = datetime.now()
time_result = time_and - time_start
print(f"Поток {time_result}")