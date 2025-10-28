# v1.2.0 202509021640
import add_languages
import add_date

def on_page_context(context, page, config, nav):
    # agregar meta_description
    if page.meta.get("description"):
        context["meta_description"] = page.meta["description"]
    else:
        context["meta_description"] = page.title
    
    # agregar links alternate_links
    alternate_links = add_languages.get_alternate_links(page, config)
    if len(alternate_links) > 0:
        context["alternate_links"] = alternate_links

    # # personalizar canonical
    if page.meta.get("canonical_url"):
        page.canonical_url = page.meta['canonical_url']

    return context

def on_page_markdown(markdown, page, config, files):
    add_lan = add_languages.get_select(page, config)
    return add_lan + "\n\n" + markdown

def on_post_build(config):
    # actualizar la fecha de sitemap
    add_date.update_sitemap(config)
