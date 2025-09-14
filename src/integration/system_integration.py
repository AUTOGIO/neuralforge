#!/usr/bin/env python3
"""
System Integration between System_Setup and GIOVANNINI_VAULT
Connects PERSONA profiling with AI Memory System
"""
import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from ai.memory_buffer import ConfigurableMemoryBuffer
from core.neural_check import NeuralEngineMonitor

class SystemIntegration:
    """Integrates System_Setup PERSONA profiling with GIOVANNINI_VAULT AI Memory"""
    
    def __init__(self):
        self.memory = ConfigurableMemoryBuffer()
        self.neural_monitor = NeuralEngineMonitor()
        self.system_setup_path = Path("/Users/giovannini/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/Projects/System_Setup")
        self.logs_path = self.system_setup_path / "Logs"
    
    def analyze_persona_logs(self) -> Dict[str, Any]:
        """Analyze PERSONA profiling logs and extract insights"""
        try:
            if not self.logs_path.exists():
                return {'error': 'PERSONA logs directory not found'}
            
            analysis = {
                'timestamp': datetime.now().isoformat(),
                'logs_found': 0,
                'latest_logs': [],
                'system_health': {},
                'ai_models': [],
                'recommendations': []
            }
            
            # Find latest log files
            log_files = list(self.logs_path.glob("*.md"))
            analysis['logs_found'] = len(log_files)
            
            if log_files:
                # Get the most recent log files
                latest_logs = sorted(log_files, key=lambda x: x.stat().st_mtime, reverse=True)[:5]
                
                for log_file in latest_logs:
                    log_data = self._parse_log_file(log_file)
                    if log_data:
                        analysis['latest_logs'].append(log_data)
                
                # Analyze system health
                analysis['system_health'] = self._analyze_system_health(analysis['latest_logs'])
                
                # Extract AI models information
                analysis['ai_models'] = self._extract_ai_models(analysis['latest_logs'])
                
                # Generate recommendations
                analysis['recommendations'] = self._generate_recommendations(analysis)
            
            return analysis
        except Exception as e:
            return {'error': str(e)}
    
    def _parse_log_file(self, log_file: Path) -> Optional[Dict[str, Any]]:
        """Parse a single log file"""
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return {
                'file_name': log_file.name,
                'file_path': str(log_file),
                'file_size': log_file.stat().st_size,
                'modified': datetime.fromtimestamp(log_file.stat().st_mtime).isoformat(),
                'content_preview': content[:500] + "..." if len(content) > 500 else content,
                'content_length': len(content)
            }
        except Exception as e:
            return None
    
    def _analyze_system_health(self, logs: List[Dict]) -> Dict[str, Any]:
        """Analyze system health from logs"""
        health = {
            'status': 'unknown',
            'cpu_usage': 'unknown',
            'memory_usage': 'unknown',
            'neural_engine': 'unknown',
            'ai_models_loaded': 0,
            'issues_found': []
        }
        
        for log in logs:
            content = log.get('content_preview', '').lower()
            
            # Check for system health indicators
            if 'cpu' in content and '%' in content:
                health['cpu_usage'] = 'detected'
            if 'memory' in content and ('gb' in content or 'mb' in content):
                health['memory_usage'] = 'detected'
            if 'neural' in content or 'ane' in content:
                health['neural_engine'] = 'detected'
            if 'model' in content and ('qwen' in content or 'phi' in content):
                health['ai_models_loaded'] += 1
        
        # Determine overall status
        indicators = [health['cpu_usage'], health['memory_usage'], health['neural_engine']]
        if all(ind == 'detected' for ind in indicators):
            health['status'] = 'healthy'
        elif any(ind == 'detected' for ind in indicators):
            health['status'] = 'partial'
        else:
            health['status'] = 'unknown'
        
        return health
    
    def _extract_ai_models(self, logs: List[Dict]) -> List[Dict[str, Any]]:
        """Extract AI models information from logs"""
        models = []
        
        for log in logs:
            content = log.get('content_preview', '')
            
            # Look for model references
            if 'qwen' in content.lower():
                models.append({
                    'name': 'Qwen3',
                    'type': 'language_model',
                    'detected_in': log['file_name'],
                    'status': 'available'
                })
            if 'phi' in content.lower():
                models.append({
                    'name': 'Phi-4',
                    'type': 'reasoning_model',
                    'detected_in': log['file_name'],
                    'status': 'available'
                })
            if 'gemma' in content.lower():
                models.append({
                    'name': 'Gemma',
                    'type': 'language_model',
                    'detected_in': log['file_name'],
                    'status': 'available'
                })
        
        # Remove duplicates
        unique_models = []
        seen_names = set()
        for model in models:
            if model['name'] not in seen_names:
                unique_models.append(model)
                seen_names.add(model['name'])
        
        return unique_models
    
    def _generate_recommendations(self, analysis: Dict) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        # System health recommendations
        if analysis['system_health']['status'] == 'unknown':
            recommendations.append("Execute PERSONA profiling to get current system status")
        
        if analysis['system_health']['ai_models_loaded'] == 0:
            recommendations.append("Load AI models in LM Studio for optimal performance")
        
        # AI models recommendations
        if len(analysis['ai_models']) > 0:
            recommendations.append(f"Found {len(analysis['ai_models'])} AI models - consider optimizing usage")
        
        # Log management recommendations
        if analysis['logs_found'] > 10:
            recommendations.append("Consider archiving old PERSONA logs to save space")
        
        return recommendations
    
    def store_analysis_in_memory(self, analysis: Dict) -> bool:
        """Store analysis results in AI memory system"""
        try:
            # Create memory entry for the analysis
            memory_entry = {
                'agent_name': 'System-Integration',
                'task': 'PERSONA logs analysis and system health check',
                'response': f"Analyzed {analysis.get('logs_found', 0)} log files. "
                          f"System status: {analysis.get('system_health', {}).get('status', 'unknown')}. "
                          f"AI models detected: {len(analysis.get('ai_models', []))}",
                'success_rating': 5 if analysis.get('system_health', {}).get('status') == 'healthy' else 3,
                'model_used': 'system-integration',
                'tokens_used': 0,
                'metadata': {
                    'logs_analyzed': analysis.get('logs_found', 0),
                    'system_status': analysis.get('system_health', {}).get('status', 'unknown'),
                    'ai_models_count': len(analysis.get('ai_models', [])),
                    'recommendations_count': len(analysis.get('recommendations', []))
                }
            }
            
            return self.memory.add_memory_entry(**memory_entry)
        except Exception as e:
            print(f"Error storing analysis in memory: {e}")
            return False
    
    def get_integration_status(self) -> Dict[str, Any]:
        """Get current integration status"""
        try:
            # Check if System_Setup exists
            system_setup_exists = self.system_setup_path.exists()
            logs_exist = self.logs_path.exists() if system_setup_exists else False
            
            # Check memory system
            memory_stats = self.memory.get_memory_stats()
            
            # Get neural engine status
            neural_metrics = self.neural_monitor.get_system_metrics()
            
            return {
                'timestamp': datetime.now().isoformat(),
                'system_setup_available': system_setup_exists,
                'persona_logs_available': logs_exist,
                'memory_system_status': 'active' if memory_stats['total_entries'] > 0 else 'inactive',
                'neural_engine_status': 'active' if 'error' not in neural_metrics else 'inactive',
                'integration_health': 'healthy' if all([
                    system_setup_exists, 
                    logs_exist, 
                    memory_stats['total_entries'] > 0
                ]) else 'needs_attention',
                'memory_entries': memory_stats['total_entries'],
                'system_metrics': neural_metrics
            }
        except Exception as e:
            return {'error': str(e)}
    
    def run_full_integration(self) -> Dict[str, Any]:
        """Run complete integration process"""
        try:
            print("🔗 Starting System Integration...")
            
            # Step 1: Analyze PERSONA logs
            print("📊 Analyzing PERSONA logs...")
            analysis = self.analyze_persona_logs()
            
            if 'error' in analysis:
                return {'error': f"Analysis failed: {analysis['error']}"}
            
            # Step 2: Store analysis in memory
            print("💾 Storing analysis in AI memory...")
            memory_stored = self.store_analysis_in_memory(analysis)
            
            # Step 3: Get integration status
            print("📈 Checking integration status...")
            status = self.get_integration_status()
            
            return {
                'success': True,
                'analysis': analysis,
                'memory_stored': memory_stored,
                'status': status,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {'error': str(e)}

def main():
    """Main entry point for testing"""
    print("🔗 System Integration - System_Setup ↔ GIOVANNINI_VAULT")
    print("=" * 60)
    
    # Initialize integration
    integration = SystemIntegration()
    
    # Check integration status
    print("📊 Checking integration status...")
    status = integration.get_integration_status()
    
    if 'error' in status:
        print(f"❌ Status check failed: {status['error']}")
    else:
        print(f"✅ System Setup available: {status['system_setup_available']}")
        print(f"✅ PERSONA logs available: {status['persona_logs_available']}")
        print(f"✅ Memory system: {status['memory_system_status']}")
        print(f"✅ Neural Engine: {status['neural_engine_status']}")
        print(f"🎯 Integration health: {status['integration_health']}")
        print(f"💾 Memory entries: {status['memory_entries']}")
    
    # Run full integration
    print(f"\n🚀 Running full integration...")
    result = integration.run_full_integration()
    
    if 'error' in result:
        print(f"❌ Integration failed: {result['error']}")
    else:
        print(f"✅ Integration completed successfully!")
        print(f"📊 Logs analyzed: {result['analysis']['logs_found']}")
        print(f"💾 Memory stored: {result['memory_stored']}")
        print(f"🎯 System status: {result['status']['integration_health']}")

if __name__ == "__main__":
    main()
