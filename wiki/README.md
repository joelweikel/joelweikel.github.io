# MMORP Wiki

The wiki is a static part of the website. Its articles, navigation, search index, and HTML pages do not need a server or database.

## Updating articles

Edit content.py, then run this from the website root:

    python wiki/build.py

The build regenerates wiki/index.html, the individual article pages, and wiki/search-data.js. Edit content.py rather than the generated HTML so changes survive the next build. Python's standard library is the only build requirement.

Each add(...) entry defines an article. Its slug becomes the HTML filename; category controls where it appears in the index; facts, sections, related, and gallery fill out the article. Use [[article-slug|link text]] for links between articles. Images and other files referenced by entries belong in wiki/assets/. The builder checks that referenced assets and related articles exist.

wiki.css controls the wiki layout, and wiki.js provides search, category filters, and the mobile menu. The pages and article links remain available without JavaScript.
