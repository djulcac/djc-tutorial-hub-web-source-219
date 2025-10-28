# v1.1.4 202509022253
import xml.etree.ElementTree as ET
import os
import datetime
import gzip
import shutil
import subprocess

def get_default_lang(config):
    default_lang = None
    i18n_plugin = config.plugins['i18n']
    for lang in i18n_plugin.config['languages']:
        if lang.get('default', False):
            default_lang = lang['locale']
            break
    return default_lang

def get_datefile(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"El archivo '{file_path}' no existe.")
    # Obtiene la fecha del último commit que modificó el archivo
    result = subprocess.run(
        ["git", "log", "-1", "--format=%ct", file_path],
        capture_output=True,
        text=True,
        check=True
    )
    string_value = result.stdout.strip()
    timestamp = int(string_value) if string_value not in (None, "") else 0
    fecha = datetime.datetime.fromtimestamp(timestamp)
    return fecha.strftime("%Y-%m-%d")

def get_path(url: str, default_lang: str, supported_langs=None) -> str:
    if supported_langs is None:
        supported_langs = ['en', 'es', 'fr']

    # Eliminamos el dominio si está presente
    path = url.split("://")[-1].split("/", 1)[-1]
    path = path.strip("/")

    # Detectamos idioma
    parts = path.split("/", 1)
    lang = default_lang
    remaining_path = path

    if parts[0] in supported_langs:
        lang = parts[0]
        remaining_path = parts[1] if len(parts) > 1 else ""

    # Construimos la ruta de forma portable
    md_path = os.path.join("docs", remaining_path, f"index.{lang}.md") if remaining_path else os.path.join("docs", f"index.{lang}.md")
    
    # Normalizamos la ruta para el OS actual
    return os.path.normpath(md_path)

def update_file_sitemap(file_path, default_lang='en'):
    namespaces = {
        "sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xhtml": "http://www.w3.org/1999/xhtml"
    }

    # Registrar namespaces para mantenerlos al escribir
    ET.register_namespace("", namespaces["sm"])
    ET.register_namespace("xhtml", namespaces["xhtml"])

    # Cargar el XML
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Actualizar todos los <lastmod>
    for url in root.findall("sm:url", namespaces):
        try:
            lastmod = url.find("sm:lastmod", namespaces)
            loc = url.find("sm:loc", namespaces)
            path = get_path(loc.text, default_lang=default_lang)
            datefile = get_datefile(path)
            if lastmod is not None:
                lastmod.text = datefile
        except Exception as e:
            print("Warning:", e)

    # Guardar los cambios
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

def compress_sitemap(xml_file, gz_file):
    with open(xml_file, 'rb') as f_in:
        with gzip.open(gz_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def update_sitemap(config):
    default_lang = get_default_lang(config)
    if not os.path.isfile('site/sitemap.xml'):
        print("Warning: Don't exist 'site/sitemap.xml'")
        return
    update_file_sitemap('site/sitemap.xml', default_lang)
    compress_sitemap('site/sitemap.xml', 'site/sitemap.xml.gz')
