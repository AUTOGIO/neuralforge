#!/usr/bin/env python3
"""
Document Tagger and Processor
Intelligent document processing and tagging using NLTK
"""
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

class DocumentTagger:
    """Document processing and tagging system"""
    
    def __init__(self):
        self.tag_patterns = {
            'technical': ['api', 'code', 'programming', 'development', 'software', 'system'],
            'business': ['meeting', 'report', 'analysis', 'strategy', 'planning', 'budget'],
            'personal': ['note', 'reminder', 'todo', 'idea', 'journal', 'diary'],
            'academic': ['research', 'study', 'paper', 'thesis', 'education', 'learning'],
            'creative': ['design', 'art', 'creative', 'writing', 'story', 'poem']
        }
    
    def extract_keywords(self, text: str, max_keywords: int = 10) -> List[str]:
        """Extract keywords from text"""
        try:
            # Simple keyword extraction
            # Remove common words and extract meaningful terms
            common_words = {
                'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
                'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these',
                'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him',
                'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their'
            }
            
            # Clean and split text
            text_clean = re.sub(r'[^\w\s]', ' ', text.lower())
            words = text_clean.split()
            
            # Filter and count words
            word_count = {}
            for word in words:
                if len(word) > 2 and word not in common_words:
                    word_count[word] = word_count.get(word, 0) + 1
            
            # Sort by frequency and return top keywords
            sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
            return [word for word, count in sorted_words[:max_keywords]]
        except Exception as e:
            return []
    
    def generate_tags(self, text: str, title: str = "") -> List[str]:
        """Generate relevant tags for document"""
        try:
            tags = []
            text_lower = text.lower()
            title_lower = title.lower()
            
            # Check against tag patterns
            for category, keywords in self.tag_patterns.items():
                for keyword in keywords:
                    if keyword in text_lower or keyword in title_lower:
                        if category not in tags:
                            tags.append(category)
            
            # Add extracted keywords as tags
            keywords = self.extract_keywords(text, 5)
            tags.extend(keywords[:3])  # Add top 3 keywords
            
            # Remove duplicates and return
            return list(set(tags))
        except Exception as e:
            return []
    
    def process_document(self, file_path: str) -> Dict[str, Any]:
        """Process a document and extract metadata"""
        try:
            path = Path(file_path)
            if not path.exists():
                return {'error': 'File does not exist'}
            
            # Read file content
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(path, 'r', encoding='latin-1') as f:
                    content = f.read()
            
            # Get file stats
            stat = path.stat()
            
            # Extract metadata
            title = path.stem
            keywords = self.extract_keywords(content)
            tags = self.generate_tags(content, title)
            
            # Calculate readability score (simplified)
            word_count = len(content.split())
            sentence_count = len(re.findall(r'[.!?]+', content))
            avg_words_per_sentence = word_count / max(sentence_count, 1)
            
            readability = "easy" if avg_words_per_sentence < 15 else "medium" if avg_words_per_sentence < 25 else "hard"
            
            return {
                'file_path': str(path),
                'file_name': path.name,
                'title': title,
                'file_size_bytes': stat.st_size,
                'file_size_mb': round(stat.st_size / (1024 * 1024), 2),
                'word_count': word_count,
                'sentence_count': sentence_count,
                'avg_words_per_sentence': round(avg_words_per_sentence, 1),
                'readability': readability,
                'keywords': keywords,
                'tags': tags,
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'processed_at': datetime.now().isoformat()
            }
        except Exception as e:
            return {'error': str(e)}
    
    def process_directory(self, directory: str, file_extensions: List[str] = None) -> Dict[str, Any]:
        """Process all documents in a directory"""
        try:
            if file_extensions is None:
                file_extensions = ['.txt', '.md', '.py', '.js', '.html', '.css', '.json']
            
            directory_path = Path(directory)
            if not directory_path.exists():
                return {'error': 'Directory does not exist'}
            
            results = {
                'directory': str(directory_path),
                'total_files': 0,
                'processed_files': 0,
                'failed_files': 0,
                'documents': [],
                'summary': {
                    'total_words': 0,
                    'total_tags': set(),
                    'file_types': {},
                    'readability_distribution': {'easy': 0, 'medium': 0, 'hard': 0}
                },
                'processed_at': datetime.now().isoformat()
            }
            
            # Process files
            for file_path in directory_path.rglob('*'):
                if file_path.is_file() and file_path.suffix.lower() in file_extensions:
                    results['total_files'] += 1
                    
                    doc_result = self.process_document(str(file_path))
                    if 'error' in doc_result:
                        results['failed_files'] += 1
                    else:
                        results['processed_files'] += 1
                        results['documents'].append(doc_result)
                        
                        # Update summary
                        results['summary']['total_words'] += doc_result['word_count']
                        results['summary']['total_tags'].update(doc_result['tags'])
                        
                        # File type distribution
                        ext = file_path.suffix.lower()
                        if ext in results['summary']['file_types']:
                            results['summary']['file_types'][ext] += 1
                        else:
                            results['summary']['file_types'][ext] = 1
                        
                        # Readability distribution
                        readability = doc_result['readability']
                        results['summary']['readability_distribution'][readability] += 1
            
            # Convert set to list for JSON serialization
            results['summary']['total_tags'] = list(results['summary']['total_tags'])
            
            return results
        except Exception as e:
            return {'error': str(e)}
    
    def search_documents(self, documents: List[Dict], query: str) -> List[Dict]:
        """Search through processed documents"""
        try:
            query_lower = query.lower()
            results = []
            
            for doc in documents:
                score = 0
                
                # Search in title
                if query_lower in doc.get('title', '').lower():
                    score += 3
                
                # Search in keywords
                for keyword in doc.get('keywords', []):
                    if query_lower in keyword.lower():
                        score += 2
                
                # Search in tags
                for tag in doc.get('tags', []):
                    if query_lower in tag.lower():
                        score += 1
                
                if score > 0:
                    doc['relevance_score'] = score
                    results.append(doc)
            
            # Sort by relevance score
            results.sort(key=lambda x: x['relevance_score'], reverse=True)
            return results
        except Exception as e:
            return []

def main():
    """Main entry point for testing"""
    print("📄 Document Tagger and Processor")
    print("=" * 40)
    
    # Initialize tagger
    tagger = DocumentTagger()
    
    # Test with sample text
    sample_text = """
    This is a Python programming document about machine learning and AI.
    It covers topics like neural networks, deep learning, and data analysis.
    The document discusses various algorithms and their applications in business.
    """
    
    print("🔍 Testing keyword extraction...")
    keywords = tagger.extract_keywords(sample_text)
    print(f"Keywords: {keywords}")
    
    print("\n🏷️ Testing tag generation...")
    tags = tagger.generate_tags(sample_text, "Python AI Guide")
    print(f"Tags: {tags}")
    
    print("\n📊 Testing document processing...")
    # Create a test file
    test_file = "test_document.txt"
    with open(test_file, 'w') as f:
        f.write(sample_text)
    
    doc_result = tagger.process_document(test_file)
    if 'error' in doc_result:
        print(f"❌ Processing failed: {doc_result['error']}")
    else:
        print(f"✅ Document processed successfully")
        print(f"📄 Title: {doc_result['title']}")
        print(f"📊 Word count: {doc_result['word_count']}")
        print(f"🏷️ Tags: {doc_result['tags']}")
        print(f"📈 Readability: {doc_result['readability']}")
    
    # Clean up test file
    if os.path.exists(test_file):
        os.remove(test_file)

if __name__ == "__main__":
    main()
