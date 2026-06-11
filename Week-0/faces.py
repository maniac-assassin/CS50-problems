def main():
    text = input("Enter text: ").split()
    emojis = {":)": "🙂", ":(": "🙁"}
    result = " ".join(emojis.get(word, word) for word in text)
    print("Converted:", result)

if __name__ == "__main__":
    main()