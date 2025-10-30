import json
import os

def get_markdown(markdown, page, config):
    title, content = split_title_content(markdown)
    # agregar titulo si no existe
    if not page.meta.get("title"):
        page.title = title.lstrip('#').replace(':', '')

    current_lang = os.path.basename(page.file.abs_src_path)[6:8]
    default_lang = get_default_lang(config)
    breadcrumbs = get_breadcrumbs(page, current_lang, default_lang)
    categories = get_categories(page, current_lang)
    ans = f'''{title}

{breadcrumbs}

{categories}

{content}

---

{breadcrumbs}
    '''
    return ans 

def get_breadcrumbs(page, current_lang, default_lang):
    path_lang = ''
    if current_lang != default_lang:
        path_lang = current_lang + '/'
    ans = f'[DJC](https://www.djc.pe/{path_lang}) >\n'
    ans += f'[Tutorial](https://tutorial-hub.djc.pe/{path_lang})'
    return ans

def get_categories(page, current_lang):
    ans = ''
    keywords = page.meta.get('keywords')
    if keywords:
        data = get_categories_data()
        for keyword in keywords.split(','):
            keyword_path = keyword.strip().lower().replace(" ", "-")
            keyword_lang = get_categories_element(keyword_path, current_lang, data)
            if keyword_lang:
                ans += f'[{keyword_lang}](../../c/{keyword_path}/index.md) |\n'
    if ans:
        ans = '| ' + ans
    return ans

def get_categories_element(category, current_lang, data):
    if current_lang in data:
        if category in data[current_lang]:
            return data[current_lang][category]
    return ''

def get_categories_data():
    filepath = os.path.join('data', 'categories.json')
    try:
        with open('data/categories.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def split_title_content(markdown_text: str):
    # Remove leading/trailing whitespace
    markdown_text = markdown_text.strip()
    
    # Split the text into lines
    lines = markdown_text.splitlines()
    
    if not lines:
        return "", ""  # empty text
    
    first_line = lines[0].strip()
    
    # If the first line starts with "#", it’s the title
    if first_line.startswith("#"):
        title = first_line.strip()
        content = "\n".join(lines[1:]).strip()
    else:
        title = ""
        content = markdown_text  # everything is content
    
    return title, content

def get_default_lang(config):
    default_lang = None
    i18n_plugin = config.plugins['i18n']
    for lang in i18n_plugin.config['languages']:
        if lang.get('default', False):
            default_lang = lang['locale']
            break
    return default_lang
