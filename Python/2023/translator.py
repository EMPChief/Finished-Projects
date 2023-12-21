from translate import Translator
import html


def read_translate(filename):
    print("Starting to read from file.....")
    translator = Translator(to_lang="no")
    translated_text = []

    try:
        with open(filename, "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                words = line.split()
                translation = ""
                for i in range(0, len(words), 400):
                    batch = words[i:i + 400]
                    batch_translation = translator.translate(" ".join(batch))
                    batch_translation = html.unescape(batch_translation)
                    print(f"Translated batch: {batch_translation}")
                    translation += batch_translation + " "
                translated_text.append(translation.strip())
    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Error while reading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Read complete.")
        return translated_text


def write_translate(translated_text, output_filename):
    try:
        print("Starting to write to file.....")
        with open(output_filename, "w", encoding='utf-8') as file:
            for line in translated_text:
                file.write(line + "\n")
        print("Finished writing to file")
    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Error while writing file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Write complete.")


filename = "./translate.txt"
translated_text = read_translate(filename)
output_filename = "./finish_translation.txt"
write_translate(translated_text, output_filename)
print("Work done!")
