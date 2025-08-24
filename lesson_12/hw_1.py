import codecs


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file, open(result_file, "w", encoding="utf-8") as result:
        in_tag = False
        for line in file:
            some_chars = []
            for char in line:
                if in_tag:
                    if char == ">":
                        in_tag = False
                    else:
                        continue
                else:
                    if char == "<":
                        in_tag = True
                    else:
                        some_chars.append(char)

            cleaned_line = ''.join(some_chars)
            if cleaned_line.strip():
                result.write(cleaned_line.lstrip())


delete_html_tags("draft.html", "cleaned.txt")