# v1.1.0 202509021754
from pathlib import Path
import os
import re

from jinja2 import Environment, FileSystemLoader

LANGUAGES = {
    "es": "Español",
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
}

def get_select(page, config):
    root_dir = os.path.abspath(config['docs_dir'])
    current_dir = os.path.dirname(page.file.abs_src_path)
    current_lang = os.path.basename(page.file.abs_src_path)[6:8]
    page_url = relative_url(root_dir, current_dir)
    index_list = filter_index_md(current_dir)
    default_lang = get_default_lang(config)
    if len(index_list) > 1:
        return get_render(default_lang, current_lang, index_list, page_url)
    return ""

def get_alternate_links(page, config):
    root_dir = os.path.abspath(config['docs_dir'])
    current_dir = os.path.dirname(page.file.abs_src_path)
    current_lang = os.path.basename(page.file.abs_src_path)[6:8]
    page_url = relative_url(root_dir, current_dir)
    index_list = filter_index_md(current_dir)
    default_lang = get_default_lang(config)
    site_url = config.get('site_url')
    if len(index_list) > 1:
        return build_alternate_links(index_list, site_url, page_url, default_lang)
    return ""

def relative_url(root, current):
    root = Path(root).resolve()
    current = Path(current).resolve()

    # Si son iguales, solo devolvemos "/"
    if root == current:
        return "/"

    rel_path = current.relative_to(root)
    url = "/" + str(rel_path).replace("\\", "/")
    if not url.endswith("/"):
        url += "/"
    return url

def filter_index_md(current_dir):
    """Devuelve los archivos con la forma index.<algo>.md en la ruta dada."""
    pattern = re.compile(r"^index\.[^.]+\.md$")
    return [
        f for f in os.listdir(current_dir)
        if os.path.isfile(os.path.join(current_dir, f)) and pattern.match(f)
    ]

def get_default_lang(config):
    default_lang = None
    i18n_plugin = config.plugins['i18n']
    for lang in i18n_plugin.config['languages']:
        if lang.get('default', False):
            default_lang = lang['locale']
            break
    return default_lang

def get_render(default_lang, current_lang, index_list, page_url):
    env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
    )
    template = env.get_template('language.html')
    languages = get_languages_from_index_list(index_list)
    params = {
        "languages": languages,
        "default_lang": default_lang,
        "current_lang": current_lang,
        "page_url": page_url,
    }
    html_resultado = template.render(params)
    return html_resultado

def get_languages_from_index_list(index_list):
    result = {}
    pattern = re.compile(r"\.(\w+)\.md$")

    for f in index_list:
        match = pattern.search(f)
        if match:
            lang = match.group(1)
            if lang in LANGUAGES:
                result[lang] = LANGUAGES[lang]

    return result

def build_alternate_links(index_list, base_url, slug, default_lang):
    base_url = base_url.rstrip("/")
    pattern = re.compile(r"\.(\w+)\.md$")
    links = []

    for f in index_list:
        match = pattern.search(f)
        if match:
            lang = match.group(1)
            if lang in LANGUAGES:
                if lang == default_lang:
                    url = f"{base_url}{slug}"
                else:
                    url = f"{base_url}/{lang}{slug}"
                links.append(
                    f'<link rel="alternate" hreflang="{lang}" href="{url}" />'
                )
    return "\n".join(links)


# # Ejemplo de uso
# files = ['index.es.md', 'index.en.md']
# print(build_alternate_links(files, "https://example.com", "excel/automatizar-reportes/"))
