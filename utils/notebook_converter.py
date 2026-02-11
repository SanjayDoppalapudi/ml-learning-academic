"""
Notebook conversion utilities
Export Jupyter notebooks to PDF, Python scripts, and HTML
"""

import json
import os
import subprocess
from pathlib import Path
from typing import Optional, List
import nbformat
from nbconvert import PDFExporter, PythonExporter, HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor


class NotebookConverter:
    """
    Convert Jupyter notebooks to various formats.
    """
    
    def __init__(self, base_path: str = "."):
        """
        Initialize converter.
        
        Args:
            base_path: Base directory for the learning platform
        """
        self.base_path = Path(base_path)
        self.exports_dir = self.base_path / "exports"
        self.exports_dir.mkdir(exist_ok=True)
        
        # Create subdirectories
        (self.exports_dir / "pdf").mkdir(exist_ok=True)
        (self.exports_dir / "scripts").mkdir(exist_ok=True)
        (self.exports_dir / "html").mkdir(exist_ok=True)
    
    def export_notebook(self, notebook_path: str, 
                       format: str = "pdf",
                       execute: bool = False) -> str:
        """
        Export a notebook to specified format.
        
        Args:
            notebook_path: Path to .ipynb file
            format: 'pdf', 'py', or 'html'
            execute: Whether to execute notebook before export
            
        Returns:
            Path to exported file
        """
        notebook_path = Path(notebook_path)
        
        if not notebook_path.exists():
            raise FileNotFoundError(f"Notebook not found: {notebook_path}")
        
        # Read notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Execute if requested
        if execute:
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': notebook_path.parent}})
        
        # Export based on format
        if format == "pdf":
            return self._export_pdf(nb, notebook_path)
        elif format == "py" or format == "python":
            return self._export_python(nb, notebook_path)
        elif format == "html":
            return self._export_html(nb, notebook_path)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _export_pdf(self, nb, notebook_path: Path) -> str:
        """Export notebook to PDF."""
        pdf_exporter = PDFExporter()
        pdf_exporter.exclude_input_prompt = True
        pdf_exporter.exclude_output_prompt = True
        
        pdf_data, resources = pdf_exporter.from_notebook_node(nb)
        
        # Create output path
        output_path = self.exports_dir / "pdf" / f"{notebook_path.stem}.pdf"
        
        with open(output_path, 'wb') as f:
            f.write(pdf_data)
        
        return str(output_path)
    
    def _export_python(self, nb, notebook_path: Path) -> str:
        """Export notebook to Python script."""
        py_exporter = PythonExporter()
        py_exporter.exclude_markdown = False
        
        py_data, resources = py_exporter.from_notebook_node(nb)
        
        # Create output path
        output_path = self.exports_dir / "scripts" / f"{notebook_path.stem}.py"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(py_data)
        
        return str(output_path)
    
    def _export_html(self, nb, notebook_path: Path) -> str:
        """Export notebook to HTML."""
        html_exporter = HTMLExporter()
        html_exporter.exclude_input_prompt = True
        html_exporter.exclude_output_prompt = True
        
        html_data, resources = html_exporter.from_notebook_node(nb)
        
        # Create output path
        output_path = self.exports_dir / "html" / f"{notebook_path.stem}.html"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_data)
        
        return str(output_path)
    
    def batch_export(self, module_dir: str, 
                    format: str = "pdf",
                    execute: bool = False) -> List[str]:
        """
        Export all notebooks in a module directory.
        
        Args:
            module_dir: Path to module directory
            format: Export format
            execute: Whether to execute notebooks
            
        Returns:
            List of exported file paths
        """
        module_path = Path(module_dir)
        exported_files = []
        
        # Find all notebooks
        notebooks = list(module_path.rglob("*.ipynb"))
        
        for nb_path in notebooks:
            try:
                output_path = self.export_notebook(nb_path, format, execute)
                exported_files.append(output_path)
                print(f"✓ Exported: {nb_path.name} → {output_path}")
            except Exception as e:
                print(f"✗ Failed to export {nb_path.name}: {e}")
        
        return exported_files
    
    def create_study_guide(self, module_dir: str) -> str:
        """
        Create a combined study guide PDF from all module notebooks.
        
        Args:
            module_dir: Path to module directory
            
        Returns:
            Path to combined PDF
        """
        module_path = Path(module_dir)
        module_name = module_path.name
        
        # Find all notebooks
        notebooks = sorted(module_path.rglob("*.ipynb"))
        
        if not notebooks:
            raise ValueError(f"No notebooks found in {module_dir}")
        
        # Combine notebooks
        combined_nb = nbformat.v4.new_notebook()
        
        # Add title
        title_cell = nbformat.v4.new_markdown_cell(
            f"# {module_name.replace('_', ' ').title()}\n\n"
            f"Complete Study Guide\n\n"
            f"Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}"
        )
        combined_nb.cells.append(title_cell)
        
        for nb_path in notebooks:
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Add section header
            section_cell = nbformat.v4.new_markdown_cell(
                f"---\n\n## {nb_path.stem.replace('_', ' ').title()}"
            )
            combined_nb.cells.append(section_cell)
            
            # Add cells from notebook
            for cell in nb.cells:
                combined_nb.cells.append(cell)
        
        # Export combined notebook
        output_path = self.exports_dir / "pdf" / f"{module_name}_study_guide.pdf"
        
        pdf_exporter = PDFExporter()
        pdf_exporter.exclude_input_prompt = True
        pdf_exporter.exclude_output_prompt = True
        
        pdf_data, resources = pdf_exporter.from_notebook_node(combined_nb)
        
        with open(output_path, 'wb') as f:
            f.write(pdf_data)
        
        return str(output_path)


def export_notebook(notebook_path: str, format: str = "pdf", execute: bool = False) -> str:
    """
    Convenience function to export a single notebook.
    
    Args:
        notebook_path: Path to notebook
        format: 'pdf', 'py', or 'html'
        execute: Whether to execute before export
        
    Returns:
        Path to exported file
    """
    converter = NotebookConverter()
    return converter.export_notebook(notebook_path, format, execute)


def batch_export_module(module_dir: str, format: str = "pdf") -> List[str]:
    """
    Convenience function to export all notebooks in a module.
    
    Args:
        module_dir: Path to module directory
        format: Export format
        
    Returns:
        List of exported file paths
    """
    converter = NotebookConverter()
    return converter.batch_export(module_dir, format)