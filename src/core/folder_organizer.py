#!/usr/bin/env python3
"""
Intelligent File Organizer with wxPython GUI
Smart file organization and management
"""
import os
import sys
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import hashlib

class FileOrganizer:
    """Core file organization logic"""
    
    def __init__(self):
        self.organize_rules = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
            'data': ['.csv', '.json', '.xml', '.yaml', '.yml'],
            'presentations': ['.ppt', '.pptx', '.odp'],
            'spreadsheets': ['.xls', '.xlsx', '.ods', '.csv']
        }
    
    def analyze_directory(self, directory: str) -> Dict[str, Any]:
        """Analyze directory structure and file types"""
        try:
            path = Path(directory)
            if not path.exists():
                return {'error': 'Directory does not exist'}
            
            analysis = {
                'directory': str(path),
                'total_files': 0,
                'total_size_mb': 0,
                'file_types': {},
                'duplicates': [],
                'large_files': [],
                'recent_files': [],
                'analysis_time': datetime.now().isoformat()
            }
            
            for file_path in path.rglob('*'):
                if file_path.is_file():
                    analysis['total_files'] += 1
                    file_size = file_path.stat().st_size
                    analysis['total_size_mb'] += file_size / (1024 * 1024)
                    
                    # File type analysis
                    ext = file_path.suffix.lower()
                    if ext in analysis['file_types']:
                        analysis['file_types'][ext] += 1
                    else:
                        analysis['file_types'][ext] = 1
                    
                    # Large files (>100MB)
                    if file_size > 100 * 1024 * 1024:
                        analysis['large_files'].append({
                            'path': str(file_path),
                            'size_mb': file_size / (1024 * 1024)
                        })
                    
                    # Recent files (last 7 days)
                    file_mtime = file_path.stat().st_mtime
                    if (datetime.now().timestamp() - file_mtime) < 7 * 24 * 3600:
                        analysis['recent_files'].append({
                            'path': str(file_path),
                            'modified': datetime.fromtimestamp(file_mtime).isoformat()
                        })
            
            # Find duplicates by size and name
            analysis['duplicates'] = self._find_duplicates(directory)
            
            return analysis
        except Exception as e:
            return {'error': str(e)}
    
    def _find_duplicates(self, directory: str) -> List[Dict[str, Any]]:
        """Find duplicate files"""
        try:
            file_hashes = {}
            duplicates = []
            
            for file_path in Path(directory).rglob('*'):
                if file_path.is_file():
                    try:
                        # Simple hash by file size and name
                        file_hash = hashlib.md5(
                            f"{file_path.name}{file_path.stat().st_size}".encode()
                        ).hexdigest()
                        
                        if file_hash in file_hashes:
                            duplicates.append({
                                'hash': file_hash,
                                'files': [str(file_hashes[file_hash]), str(file_path)],
                                'size_mb': file_path.stat().st_size / (1024 * 1024)
                            })
                        else:
                            file_hashes[file_hash] = file_path
                    except:
                        continue
            
            return duplicates
        except:
            return []
    
    def organize_files(self, source_dir: str, target_dir: str, 
                      dry_run: bool = True) -> Dict[str, Any]:
        """Organize files according to rules"""
        try:
            source_path = Path(source_dir)
            target_path = Path(target_dir)
            
            if not source_path.exists():
                return {'error': 'Source directory does not exist'}
            
            if not target_path.exists():
                target_path.mkdir(parents=True, exist_ok=True)
            
            results = {
                'source': str(source_path),
                'target': str(target_path),
                'dry_run': dry_run,
                'files_processed': 0,
                'files_moved': 0,
                'files_skipped': 0,
                'errors': [],
                'operations': []
            }
            
            for file_path in source_path.iterdir():
                if file_path.is_file():
                    results['files_processed'] += 1
                    
                    # Determine category
                    category = self._get_file_category(file_path)
                    if category:
                        target_category_dir = target_path / category
                        target_category_dir.mkdir(exist_ok=True)
                        
                        target_file_path = target_category_dir / file_path.name
                        
                        # Handle name conflicts
                        counter = 1
                        original_target = target_file_path
                        while target_file_path.exists():
                            stem = original_target.stem
                            suffix = original_target.suffix
                            target_file_path = target_category_dir / f"{stem}_{counter}{suffix}"
                            counter += 1
                        
                        operation = {
                            'source': str(file_path),
                            'target': str(target_file_path),
                            'category': category
                        }
                        
                        if not dry_run:
                            try:
                                shutil.move(str(file_path), str(target_file_path))
                                results['files_moved'] += 1
                                operation['status'] = 'moved'
                            except Exception as e:
                                results['files_skipped'] += 1
                                operation['status'] = 'error'
                                operation['error'] = str(e)
                                results['errors'].append(str(e))
                        else:
                            results['files_moved'] += 1
                            operation['status'] = 'would_move'
                        
                        results['operations'].append(operation)
                    else:
                        results['files_skipped'] += 1
            
            return results
        except Exception as e:
            return {'error': str(e)}
    
    def _get_file_category(self, file_path: Path) -> Optional[str]:
        """Get file category based on extension"""
        ext = file_path.suffix.lower()
        
        for category, extensions in self.organize_rules.items():
            if ext in extensions:
                return category
        
        return None
    
    def create_organization_plan(self, directory: str) -> Dict[str, Any]:
        """Create a plan for organizing files"""
        analysis = self.analyze_directory(directory)
        if 'error' in analysis:
            return analysis
        
        plan = {
            'directory': directory,
            'total_files': analysis['total_files'],
            'total_size_mb': round(analysis['total_size_mb'], 2),
            'categories': {},
            'recommendations': [],
            'estimated_time_minutes': 0
        }
        
        # Categorize files
        for file_path in Path(directory).iterdir():
            if file_path.is_file():
                category = self._get_file_category(file_path)
                if category:
                    if category not in plan['categories']:
                        plan['categories'][category] = {'count': 0, 'size_mb': 0}
                    plan['categories'][category]['count'] += 1
                    plan['categories'][category]['size_mb'] += file_path.stat().st_size / (1024 * 1024)
        
        # Generate recommendations
        if analysis['duplicates']:
            plan['recommendations'].append(f"Found {len(analysis['duplicates'])} duplicate files")
        
        if analysis['large_files']:
            plan['recommendations'].append(f"Found {len(analysis['large_files'])} large files (>100MB)")
        
        plan['estimated_time_minutes'] = max(1, analysis['total_files'] // 100)
        
        return plan

def main():
    """Main entry point for testing"""
    print("📁 Intelligent File Organizer")
    print("=" * 40)
    
    # Initialize organizer
    organizer = FileOrganizer()
    
    # Test directory analysis
    test_dir = os.path.expanduser("~/Downloads")
    print(f"🔍 Analyzing directory: {test_dir}")
    
    analysis = organizer.analyze_directory(test_dir)
    if 'error' in analysis:
        print(f"❌ Analysis failed: {analysis['error']}")
    else:
        print(f"✅ Found {analysis['total_files']} files")
        print(f"📊 Total size: {analysis['total_size_mb']:.2f} MB")
        print(f"📁 File types: {len(analysis['file_types'])} different extensions")
        print(f"🔄 Duplicates: {len(analysis['duplicates'])} found")
        print(f"📈 Large files: {len(analysis['large_files'])} found")
    
    # Test organization plan
    print(f"\n📋 Creating organization plan...")
    plan = organizer.create_organization_plan(test_dir)
    if 'error' in plan:
        print(f"❌ Plan creation failed: {plan['error']}")
    else:
        print(f"✅ Plan created for {plan['total_files']} files")
        print(f"📊 Categories: {list(plan['categories'].keys())}")
        print(f"⏱️ Estimated time: {plan['estimated_time_minutes']} minutes")
        print(f"💡 Recommendations: {len(plan['recommendations'])} items")

if __name__ == "__main__":
    main()
