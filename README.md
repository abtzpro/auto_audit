# AutoAudit
# AutoAudit: Automated Enterprise Security Audit Tool

AutoAudit is an automated security audit tool designed to streamline the process of conducting security audits for SMBs and Enterprise organizations. The tool integrates multiple open-source tools to perform vulnerability assessments, risk assessments, and compliance audits.

## Features

- Network scanning using Nmap
- Vulnerability scanning using OpenVAS
- Web application scanning using OWASP ZAP
- Compliance auditing using OpenSCAP
- Risk assessment and ranking of vulnerabilities
- HTML report generation
- Scheduled audits
- Email notifications with audit summary and report attachments

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/abtzpro/auto_audit.git
   cd auto_audit
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Install and configure the necessary tools:

   - [Nmap](https://nmap.org/download.html)
   - [OpenVAS](https://www.openvas.org/install-source.html)
   - [OWASP ZAP](https://www.zaproxy.org/download/)
   - [OpenSCAP](https://www.open-scap.org/getting-started/)

4. Configure the `config.json` file with the required settings for each tool and email notifications.

   Example:

   ```json
   {
       "openvas": {
           "host": "127.0.0.1",
           "port": 9390,
           "username": "your_openvas_username",
           "password": "your_openvas_password"
       },
       "zap": {
           "api_key": "your_zap_api_key",
           "host": "http://127.0.0.1",
           "port": "8080"
       },
       "targets": ["192.168.1.0/24"],
       "webapp_targets": ["http://example.com"],
       "nmap_ports": "1-65535",
       "email": {
           "server": "smtp.example.com",
           "port": 587,
           "username": "your_email_username",
           "password": "your_email_password",
           "from_address": "your_email@example.com",
           "to_addresses": ["recipient1@example.com", "recipient2@example.com"],
           "subject": "AutoAudit Security Report"
       },
       "schedule": {
           "interval": 7,
           "unit": "days"
       }
   }
   ```

5. Run the `auto_audit` tool:

   ```
   python audit.py
   ```

## Usage

Once the installation is complete and the `config.json` file is configured, you can run the `auto_audit` tool with the following command:

```
python audit.py
```

The tool will perform the security audit and generate an HTML report (`audit_report.html`) in the project directory. If email notifications are configured, the tool will also send an email with the audit summary and the report attached.

You can schedule the audits to run automatically at a specified interval (e.g., every week) by configuring the `schedule` settings in the `config.json` file.

## Contributing

If you have any suggestions, bug reports, or feature requests, please open an issue on (https://github.com/abtzpro/auto_audit/issues). We appreciate your contributions and feedback!

Developed by @abtzpro @AdamR @HelloSecurity

## License

AutoAudit is released under the [MIT License](https://opensource.org/licenses/MIT).
