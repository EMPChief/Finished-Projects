with open("bear.txt", 'r') as f:
    content = f.read()
    print(content)

    with open("essay.txt", 'r') as f:
        content = f.read()
        converted_content = ' '.join(word.capitalize() for word in content.split())
        print(converted_content)
with open('essay.txt', 'r') as f:
    content = f.read()
    convert_content = ' '.join(word.capitalize() for word in content.split())
    print(convert_content)
    
    with open("essay.txt", 'r') as f:
        content = f.read()
        num_characters = len(content)
        print(num_characters)
