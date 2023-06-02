import time
import openai

openai.api_key = ''


def translate_text(text):
    translation = ""
    while translation == "":
        time.sleep(6)
        print(f'循环翻译: {text}')
        try:
            prompt = f"""translate text to English：“{text}”"""

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that translates text."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.5,
            )

            translation = response.choices[0].message.content.strip()
        except:
            translation = ""
    return translation


with open('./result.txt', mode='w', encoding='utf-8') as f:
    f.write('')

with open('./list.txt', mode='r', encoding='utf-8') as f:
    content = f.read()
    for line in content.split('\n'):
        result = translate_text(line)
        result = result.replace('\n', '{placeholder}')
        print(f'结果: {result}')
        time.sleep(6)
        with open('./result.txt', mode='a+', encoding='utf-8') as a:
            a.write(f'{line}\t{result}\n')
        print('-'*80)