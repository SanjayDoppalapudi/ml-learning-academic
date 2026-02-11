#!/bin/bash
# Local build test script

echo "🧪 Testing JupyterBook Build Locally"
echo ""

# Check if jupyter-book is installed
if ! command -v jupyter-book &> /dev/null; then
    echo "❌ jupyter-book not found. Installing..."
    pip install jupyter-book
fi

echo "📦 Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "🔨 Building JupyterBook..."
cd book

# Clean previous build
rm -rf _build

# Build the book
jupyter-book build . 2>&1 | tee ../build.log

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build successful!"
    echo ""
    echo "📂 Build location: book/_build/html/"
    echo "🌐 To preview locally:"
    echo "   cd book/_build/html && python -m http.server 8000"
    echo "   Then open: http://localhost:8000"
else
    echo ""
    echo "❌ Build failed!"
    echo "📄 Check build.log for errors"
    echo ""
    echo "Common issues:"
    echo "  - Missing files referenced in _toc.yml"
    echo "  - Syntax errors in notebooks"
    echo "  - Missing dependencies"
fi