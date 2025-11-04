from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

@app.route('/')
def serve_dashboard():
    """Serve the professional AINEXUS dashboard"""
    return send_file('../dashboard.html')

@app.route('/api/health')
def health_check():
    """Health check endpoint for Render"""
    return jsonify({
        'status': 'healthy',
        'service': 'ainexus-industrial-dashboard',
        'dashboard': 'professional'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
