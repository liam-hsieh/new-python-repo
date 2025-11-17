"""Generate API reference pages automatically from source code."""

from pathlib import Path
import mkdocs_gen_files

# Define the source directory
src_dir = Path("src")

# Generate documentation for each Python package/module
for path in sorted(src_dir.rglob("*.py")):
    # Skip __pycache__ and other non-source files
    if "__pycache__" in str(path) or path.name.startswith("_"):
        continue
    
    # Convert file path to module path
    module_path = path.relative_to(src_dir).with_suffix("")
    doc_path = path.relative_to(src_dir).with_suffix(".md")
    full_doc_path = Path("api") / doc_path
    
    # Convert path separators to dots for Python module names
    module_name = str(module_path).replace("/", ".")
    
    # Create the markdown content with mkdocstrings reference
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        # Get the module/package name for the title
        title = module_path.name or str(module_path)
        
        print(f"# {title.replace('_', ' ').title()}", file=fd)
        print(f"\n::: src.{module_name}", file=fd)
    
    # Set up navigation
    mkdocs_gen_files.set_edit_path(full_doc_path, path)