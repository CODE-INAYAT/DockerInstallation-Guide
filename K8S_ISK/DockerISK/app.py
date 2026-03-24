from flask import Flask
from colorama import Fore, init
import socket
import os

init(autoreset=True)
app = Flask(__name__)

@app.route('/')
def home():
    # Get pod details for K8s display
    hostname = socket.gethostname()
    pod_ip = socket.gethostbyname(hostname)

    print(Fore.CYAN + f">>> [K8s POD: {hostname}] Web request received!")
    return f"""
    <div style="background-color: #f5f5f5; padding: 60px; text-align: center; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; font-family: 'Segoe UI', sans-serif;">

      <!-- Main Title -->
      <h1 style="font-weight: bold; font-size: 3.5rem; color: #222; letter-spacing: 0.2em; text-transform: uppercase; margin: 0;">
        <span style="color: #326CE5;">Kubernetes</span> on Island
      </h1>

      <p style="font-weight: 300; font-size: 1rem; color: #666; letter-spacing: 0.3em; text-transform: uppercase; margin-top: 20px;">
        Orchestrated Python &middot; <span style="color: #326CE5;">Container Pods</span>
      </p>

      <!-- K8s Info Card -->
      <div style="margin-top: 50px; background: #ffffff; border: 1px solid #ddd; border-radius: 12px; padding: 30px 50px; display: inline-block; margin-left: auto; margin-right: auto; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <p style="color: #326CE5; font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 20px;">
          &#9781; Live Pod Information
        </p>
        <table style="color: #444; font-size: 1rem; text-align: left; border-collapse: collapse;">
          <tr>
            <td style="padding: 8px 20px; color: #888;">Pod Name</td>
            <td style="padding: 8px 20px; color: #1565C0; font-family: monospace;">{hostname}</td>
          </tr>
          <tr>
            <td style="padding: 8px 20px; color: #888;">Pod IP</td>
            <td style="padding: 8px 20px; color: #1565C0; font-family: monospace;">{pod_ip}</td>
          </tr>
          <tr>
            <td style="padding: 8px 20px; color: #888;">Node</td>
            <td style="padding: 8px 20px; color: #1565C0; font-family: monospace;">docker-desktop</td>
          </tr>
          <tr>
            <td style="padding: 8px 20px; color: #888;">Replicas</td>
            <td style="padding: 8px 20px; color: #1565C0; font-family: monospace;">2 Pods Running</td>
          </tr>
          <tr>
            <td style="padding: 8px 20px; color: #888;">Platform</td>
            <td style="padding: 8px 20px; color: #1565C0; font-family: monospace;">Kubernetes (Docker Desktop)</td>
          </tr>
        </table>
      </div>

      <!-- Refresh hint -->
      <p style="color: #999; font-size: 0.8rem; margin-top: 30px; letter-spacing: 0.1em;">
        &#8635; Refresh the page — if the Pod Name changes, K8s load balancing is working!
      </p>

      <!-- Footer -->
      <p style="color: #bbb; font-size: 0.75rem; margin-top: 40px; letter-spacing: 0.15em;">
        DEPLOYED VIA KUBECTL &middot; KUBERNETES v1.x &middot; LOCAL CLUSTER
      </p>
    </div>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)