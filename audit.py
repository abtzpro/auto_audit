import json
import os
import schedule
import time

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from openvas_lib import VulnscanManager, VulnscanException
from zapv2 import ZAPv2

from utils import send_email, print_progress, categorize_vulnerabilities


class Audit:
    def __init__(self, config_path):
        self.config_path = config_path
        self.load_config()
        self.load_tools()
        
    def load_config(self):
        with open(self.config_path) as f:
            self.config = json.load(f)
        
    def load_tools(self):
        self.nm = nmap.PortScanner()
        self.openvas = VulnscanManager(self.config["openvas"]["host"], self.config["openvas"]["username"], self.config["openvas"]["password"], self.config["openvas"]["port"])
        self.zap = ZAPv2(apikey=self.config["zap"]["api_key"], proxies={'http': self.config["zap"]["host"] + ':' + self.config["zap"]["port"], 'https': self.config["zap"]["host"] + ':' + self.config["zap"]["port"]})
        
    def run(self):
        targets = self.config["targets"]
        webapp_targets = self.config["webapp_targets"]
        nmap_ports = self.config["nmap_ports"]
        
        vulnerabilities = self.vulnerability_assessment(targets, nmap_ports)
        webapp_vulnerabilities = self.webapp_vulnerability_assessment(webapp_targets)
        risks = self.risk_assessment(vulnerabilities + webapp_vulnerabilities)
        compliance_results = self.compliance_audit(targets)
        report = self.generate_report(risks, compliance_results)
        
        if self.config.get("email"):
            self.send_email(report)
        else:
            print(report)
    
    def vulnerability_assessment(self, targets, nmap_ports):
        print_progress("Performing vulnerability assessment...")
        
        vulnerabilities = []
        
        for target in targets:
            # Nmap scanning
            self.nm.scan(target, nmap_ports)
            vulnerabilities.append({"target": target, "nmap": self.nm.csv()})
            
            # OpenVAS scanning
            try:
                openvas_id, openvas_results = self.openvas.launch_scan(target)
                vulnerabilities.append({"target": target, "openvas": openvas_results})
            except VulnscanException as e:
                print("Error in OpenVAS scanning:", e)
        
        print_progress("Vulnerability assessment complete")
        print()
        return vulnerabilities
    
    def webapp_vulnerability_assessment(self, webapp_targets):
        print_progress("Performing web application vulnerability assessment...")
        
        webapp_vulnerabilities = []
        
        for target in webapp_targets:
            self.zap.urlopen(target)
            scan_id = self.zap.spider.scan(target)
            while int(self.zap.spider.status(scan_id)) < 100:
                time.sleep(0.5)
                
            self.zap.ascan.scan(target)
            while int(self.zap.ascan.status) < 100:
                time.sleep(0.5)
                
            vulnerabilities = self.zap.core.alerts(baseurl=target)
            webapp_vulnerabilities.append({"target": target, "vulnerabilities": vulnerabilities})
        
        print_progress("Web application vulnerability assessment complete")
        print()
        return webapp_vulnerabilities
    
    def risk_assessment(self, vulnerabilities):
        print_progress("Performing risk assessment...")
        
        ranked_vulnerabilities = []
        
        class Audit:
    # ... (previous code) ...
    
    def risk_assessment(self, vulnerabilities):
        print_progress("Performing risk assessment...")
        
        ranked_vulnerabilities = []
        
        for vulnerability in vulnerabilities:
            if "vulnerabilities" in vulnerability:
                for vuln in vulnerability["vulnerabilities"]:
                    if "risk" in vuln and "cvss" in vuln:
                        cvss_score = float(vuln["cvss"])
                        risk_category = categorize_vulnerabilities(cvss_score)
                        vuln["risk_category"] = risk_category
            ranked_vulnerabilities.append(vulnerability)
        
        print_progress("Risk assessment complete")
        print()
        return ranked_vulnerabilities
    
    def compliance_audit(self, targets):
        print_progress("Performing compliance audit...")
        
        compliance_results = []
        
        for target in targets:
            # Example: check for secure configurations using OpenSCAP
            # Replace the command below with the appropriate scan command for your environment
            # You can use different compliance scanning tools as needed
            cmd = ["oscap", "ssh", target, "xccdf", "eval", "--profile", "your_profile", "your_scap_file"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            compliance_results.append({"target": target, "result": result.stdout})
            
        print_progress("Compliance audit complete")
        print()
        return compliance_results
    
    def generate_report(self, vulnerabilities, compliance_results):
        print_progress("Generating audit report...")
        
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template(self.config["template"])
        html_report = template.render(vulnerabilities=vulnerabilities, compliance_results=compliance_results)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        report_path = os.path.join(self.config["report_dir"], f"audit_report_{timestamp}.html")
        
        with open(report_path, "w") as f:
            f.write(html_report)
            
        print_progress("Audit report generated")
        print()
        
        return report_path
    
    def send_email(self, report_path):
        print_progress("Sending email notification...")
        
        subject = self.config["email"]["subject"]
        body = self.config["email"]["body"]
        attachments = [report_path]
        
        send_email(self.config["email"], subject, body, attachments)
        
        print_progress("Email notification sent")
        print()

