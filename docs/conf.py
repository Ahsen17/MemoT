project = "Kortex"
copyright = "2025, Ahsen"
author = "Ahsen"


extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
    "sphinxext.opengraph",
    "sphinx_tippy",
]

# 配置autosectionlabel以避免重复标签警告
autosectionlabel_prefix_document = True
myst_enable_extensions = [
    "colon_fence",
    "html_admonition",
    "html_image",
    "deflist",
    "substitution",
]

# Mermaid配置
mermaid_version = "latest"
mermaid_init_js = """
  mermaid.initialize({
    startOnLoad: true,
    theme: 'default',
    themeVariables: {
      primaryColor: '#42b983',
      primaryTextColor: '#2c3e50',
      primaryBorderColor: '#42b983',
      lineColor: '#42b983',
      secondaryColor: '#f8f8f2',
      tertiaryColor: '#f1f1f1'
    },
    flowchart: {
      useMaxWidth: true,
      htmlLabels: true,
      curve: 'basis'
    }
  });
"""

# Open Graph配置
ogp_site_url = "https://your-username.github.io/kortex/"
ogp_description = "Kortex - An experimental memory agent demo"
ogp_image = ""

tippy_enable_auto_dark_mode = True
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "shibuya"
html_title = "kortex"
html_static_path = ["_static"]
html_css_files = ["style.css"]
