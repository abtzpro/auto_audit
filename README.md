# AutoAudit

AutoAudit is an automated security audit tool designed for SMB and enterprise organizations. It is built with Python and incorporates popular security tools such as Nmap, OpenVAS, and ZAP to perform vulnerability assessments, risk assessments, and compliance audits. AutoAudit generates comprehensive HTML reports and can be scheduled to run at regular intervals. The tool can also send email notifications with the latest audit reports.

## Features

- Nmap scanning for host discovery and open port detection
- OpenVAS scanning for vulnerability detection
- ZAP scanning for web application vulnerability detection
- Risk assessment based on Common Vulnerability Scoring System (CVSS) scores
- Compliance auditing with OpenSCAP or other compliance scanning tools
- HTML report generation with customizable templates
- Scheduled audits at regular intervals
- Email notifications with latest audit reports

## Getting Started

### Prerequisites

- Python 3.x
- Nmap
- OpenVAS
- ZAP
- OpenSCAP (or other compliance scanning tools)
- Jinja2
- Schedule
- Click
- Flask-Mail

### Installation

1. Clone the `auto_audit` repository:

   ```bash
   git clone https://github.com/abtzpro/auto_audit.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the `config.json` file with your desired settings.

### Usage

To run AutoAudit, use the following command:

```bash
python audit.py
```

This will perform a security audit using the settings specified in the `config.json` file.

You can also use the `--schedule` option to schedule audits at regular intervals:

```bash
python audit.py --schedule
```

This will schedule audits according to the settings specified in the `config.json` file.

## Configuration

The `config.json` file contains the settings for the `auto_audit` program. The following parameters can be configured:

- `targets`: IP addresses or IP ranges to scan with Nmap
- `webapp_targets`: URLs of web applications to scan with ZAP
- `nmap_ports`: port range to scan with Nmap
- `openvas_host`: IP address of OpenVAS server
- `openvas_port`: port number of OpenVAS server
- `openvas_username`: username for OpenVAS authentication
- `openvas_password`: password for OpenVAS authentication
- `zap_api_key`: API key for ZAP
- `zap_host`: URL of ZAP instance
- `zap_port`: port number of ZAP instance
- `report_dir`: directory to save audit reports
- `template`: path to HTML report template
- `email`: email settings for sending notifications with audit reports
- `schedule`: schedule settings for running audits at regular intervals

## Report Template

The `report.html` file is a Jinja2 template for generating HTML audit reports. The following variables are available for use in the template:

- `timestamp`: timestamp of the audit
- `nmap_results`: results of Nmap scan
- `openvas_results`: results of OpenVAS scan
- `webapp_results`: results of ZAP scan
- `compliance_results`: results of compliance audit

You can modify the `report.html` template to customize the appearance and content of the audit report.

## Scheduled Audits

You can schedule audits to run at regular intervals using the `--schedule` option. The `config.json` file contains the settings for the scheduled audits. You can specify the interval, unit, and days for the schedule. 

## Email Notifications

You can configure AutoAudit to send email notifications with the latest audit reports using the `--email` option. This option requires that you have configured the email settings in the `config.json` file. 

```bash
python audit.py --email
```

This will send an email with the latest audit report to the recipients specified in the `config.json` file.

## Contributing

Contributions to the `auto_audit` project are welcome! If you find a bug or have a suggestion for a new feature, please submit an issue or pull request on the GitHub repository.

## Developer 

@abtzpro @AdamR @HelloSecurity

## Extra Credit To

chatGPT for the awesome and informative debugging capabilities, notation capabilities, and README.md file creation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
