#!/bin/bash
# Setup script for ML Learning Platform

echo "🚀 Setting up ML Learning Platform..."
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

# Install required packages
echo ""
echo "📦 Installing required packages..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install packages. Please check your internet connection."
    exit 1
fi

# Create necessary directories
echo ""
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p exports/pdf
mkdir -p exports/scripts
mkdir -p exports/html
mkdir -p data/raw
mkdir -p data/processed

# Setup git hooks (optional)
echo ""
echo "⚙️  Setting up Git hooks..."
if [ -d .git ]; then
    # Create pre-commit hook for auto-saving progress
    cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
echo "Saving learning progress before commit..."
python3 -c "from utils.progress_tracker import get_tracker; t = get_tracker(); t._save_progress()"
EOF
    chmod +x .git/hooks/pre-commit
    echo "✓ Git hooks configured"
fi

# Initialize progress tracking
echo ""
echo "📊 Initializing progress tracking..."
python3 -c "
from utils.progress_tracker import get_tracker
tracker = get_tracker()
print('✓ Progress tracking initialized')
print(f'  Data directory: logs/')
"

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 To get started:"
echo "   1. Launch JupyterLab: jupyter lab"
echo "   2. Navigate to module_0_python_foundation/"
echo "   3. Start with: 01_numpy_refresher.ipynb"
echo ""
echo "📚 Available modules:"
echo "   - Module 0: Python Foundation (Reference)"
echo "   - Module 1: Mathematical Foundations (4 projects)"
echo "   - Module 2: Statistical Inference (4 projects)"
echo "   - Module 3: ML Algorithms (5 projects)"
echo "   - Module 4: Deep Learning (4 projects)"
echo ""
echo "🎓 Happy Learning!"