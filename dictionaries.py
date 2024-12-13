def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def count_words(text):
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def print_most_common_words(word_counts, num_words=5):
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words[:num_words]:
        print(f'{word}: {count}')

if __name__ == "__main__":
    file_path = 'C:/path/to/example.txt' 
    text = read_file(file_path)
    word_counts = count_words(text)
    print_most_common_words(word_counts)


 
