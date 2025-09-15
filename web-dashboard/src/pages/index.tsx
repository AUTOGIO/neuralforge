import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { 
  Brain, 
  Cpu, 
  HardDrive, 
  Globe, 
  Mail, 
  Clock, 
  BarChart3, 
  Settings,
  Activity,
  Zap,
  Database,
  FileText
} from 'lucide-react';

interface SystemMetrics {
  cpu: number;
  memory: number;
  neuralEngine: number;
  temperature: number;
  power: number;
}

interface ToolStatus {
  name: string;
  status: 'active' | 'inactive' | 'error';
  icon: React.ReactNode;
  description: string;
  lastRun?: string;
}

const NeuralForgeDashboard: React.FC = () => {
  const [metrics, setMetrics] = useState<SystemMetrics>({
    cpu: 0,
    memory: 0,
    neuralEngine: 0,
    temperature: 0,
    power: 0
  });

  const [tools] = useState<ToolStatus[]>([
    {
      name: 'Neural Engine Monitor',
      status: 'active',
      icon: <Brain className="w-6 h-6" />,
      description: 'Real-time Apple Neural Engine monitoring',
      lastRun: '2 minutes ago'
    },
    {
      name: 'AI Memory System',
      status: 'active',
      icon: <Database className="w-6 h-6" />,
      description: 'PostgreSQL-powered conversation storage',
      lastRun: '5 minutes ago'
    },
    {
      name: 'File Organizer',
      status: 'inactive',
      icon: <HardDrive className="w-6 h-6" />,
      description: 'Intelligent file management',
      lastRun: '1 hour ago'
    },
    {
      name: 'Web Scraper',
      status: 'inactive',
      icon: <Globe className="w-6 h-6" />,
      description: 'Advanced web data extraction',
      lastRun: 'Never'
    },
    {
      name: 'Email Automation',
      status: 'inactive',
      icon: <Mail className="w-6 h-6" />,
      description: 'Automated email workflows',
      lastRun: 'Never'
    },
    {
      name: 'Schedule Automation',
      status: 'active',
      icon: <Clock className="w-6 h-6" />,
      description: 'Task scheduling and automation',
      lastRun: 'Running'
    }
  ]);

  // Simulate real-time metrics update
  useEffect(() => {
    const interval = setInterval(() => {
      setMetrics({
        cpu: Math.random() * 100,
        memory: Math.random() * 100,
        neuralEngine: Math.random() * 100,
        temperature: 35 + Math.random() * 15,
        power: 10 + Math.random() * 20
      });
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'text-green-500 bg-green-100';
      case 'inactive': return 'text-gray-500 bg-gray-100';
      case 'error': return 'text-red-500 bg-red-100';
      default: return 'text-gray-500 bg-gray-100';
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white shadow-lg border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <div className="flex items-center space-x-3">
              <div className="bg-gradient-to-r from-blue-600 to-purple-600 p-3 rounded-xl">
                <Brain className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-3xl font-bold text-gray-900">NeuralForge</h1>
                <p className="text-gray-600">AI & Automation Toolkit for Apple Silicon</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2 text-sm text-gray-600">
                <Activity className="w-4 h-4" />
                <span>M3 iMac • 16GB RAM</span>
              </div>
              <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
                <Settings className="w-4 h-4 inline mr-2" />
                Settings
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* System Metrics */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 mb-8"
        >
          <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">CPU Usage</p>
                <p className="text-2xl font-bold text-gray-900">{metrics.cpu.toFixed(1)}%</p>
              </div>
              <Cpu className="w-8 h-8 text-blue-600" />
            </div>
            <div className="mt-4">
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div 
                  className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${metrics.cpu}%` }}
                ></div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Memory</p>
                <p className="text-2xl font-bold text-gray-900">{metrics.memory.toFixed(1)}%</p>
              </div>
              <HardDrive className="w-8 h-8 text-green-600" />
            </div>
            <div className="mt-4">
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div 
                  className="bg-green-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${metrics.memory}%` }}
                ></div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Neural Engine</p>
                <p className="text-2xl font-bold text-gray-900">{metrics.neuralEngine.toFixed(1)}%</p>
              </div>
              <Zap className="w-8 h-8 text-purple-600" />
            </div>
            <div className="mt-4">
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div 
                  className="bg-purple-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${metrics.neuralEngine}%` }}
                ></div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Temperature</p>
                <p className="text-2xl font-bold text-gray-900">{metrics.temperature.toFixed(1)}°C</p>
              </div>
              <Activity className="w-8 h-8 text-orange-600" />
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Power</p>
                <p className="text-2xl font-bold text-gray-900">{metrics.power.toFixed(1)}W</p>
              </div>
              <Zap className="w-8 h-8 text-yellow-600" />
            </div>
          </div>
        </motion.div>

        {/* Tools Grid */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          {tools.map((tool, index) => (
            <motion.div
              key={tool.name}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className="bg-white rounded-xl shadow-lg p-6 border border-gray-200 hover:shadow-xl transition-shadow cursor-pointer"
            >
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center space-x-3">
                  <div className="text-gray-600">
                    {tool.icon}
                  </div>
                  <h3 className="text-lg font-semibold text-gray-900">{tool.name}</h3>
                </div>
                <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(tool.status)}`}>
                  {tool.status}
                </span>
              </div>
              
              <p className="text-gray-600 text-sm mb-4">{tool.description}</p>
              
              <div className="flex items-center justify-between text-sm text-gray-500">
                <span>Last run: {tool.lastRun}</span>
                <button className="text-blue-600 hover:text-blue-800 font-medium">
                  Launch →
                </button>
              </div>
            </motion.div>
          ))}
        </motion.div>

        {/* Quick Actions */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="mt-8 bg-white rounded-xl shadow-lg p-6 border border-gray-200"
        >
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Actions</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <button className="flex items-center justify-center space-x-2 bg-blue-50 text-blue-700 px-4 py-3 rounded-lg hover:bg-blue-100 transition-colors">
              <FileText className="w-5 h-5" />
              <span>Organize Files</span>
            </button>
            <button className="flex items-center justify-center space-x-2 bg-green-50 text-green-700 px-4 py-3 rounded-lg hover:bg-green-100 transition-colors">
              <BarChart3 className="w-5 h-5" />
              <span>View Analytics</span>
            </button>
            <button className="flex items-center justify-center space-x-2 bg-purple-50 text-purple-700 px-4 py-3 rounded-lg hover:bg-purple-100 transition-colors">
              <Globe className="w-5 h-5" />
              <span>Start Scraping</span>
            </button>
            <button className="flex items-center justify-center space-x-2 bg-orange-50 text-orange-700 px-4 py-3 rounded-lg hover:bg-orange-100 transition-colors">
              <Settings className="w-5 h-5" />
              <span>Configure</span>
            </button>
          </div>
        </motion.div>
      </main>
    </div>
  );
};

export default NeuralForgeDashboard;
