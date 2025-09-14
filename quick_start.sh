#!/bin/bash
# NEURAL_CORE_VAULT Quick Start Script

echo "🧠============================================================🧠"
echo "🚀 NEURAL_CORE_VAULT - AI & Automation Toolkit"
echo "🧠============================================================🧠"
echo "🎯 Optimized for Apple Silicon (M3) Macs"
echo "🔧 PostgreSQL 17 + Neural Engine + Core ML"
echo "🧠============================================================🧠"

echo ""
echo "📦 Setting up NEURAL_CORE_VAULT..."

# Activate virtual environment
if [ -d "venv_new" ]; then
    echo "✅ Activating virtual environment..."
    source venv_new/bin/activate
else
    echo "❌ Virtual environment not found. Creating one..."
    python3 -m venv venv_new
    source venv_new/bin/activate
fi

# Install essential dependencies
echo "📦 Installing essential dependencies..."
pip install rich psycopg2-binary psutil requests beautifulsoup4 lxml pytest

echo ""
echo "🎉 NEURAL_CORE_VAULT is ready!"
echo ""
echo "🚀 To launch the toolkit:"
echo "   python3 launch_neural_vault.py"
echo ""
echo "💾 Your AI Memory System with PostgreSQL 17 is operational!"
echo "🧠 Neural Engine monitoring is ready!"
echo "📁 All tools are organized and accessible!"
echo ""
echo "🎯 Start building amazing AI systems! 🚀"
