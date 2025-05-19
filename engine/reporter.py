# engine/reporter.py
import json
import csv
from datetime import datetime
import os

class Reporter:
    def __init__(self, report_dir="reports"):
        self.report_dir = report_dir
        os.makedirs(self.report_dir, exist_ok=True)

    def generate_report_name(self, prefix="report"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{prefix}_{timestamp}"

    def save_json_report(self, results, report_name=None):
        if not report_name:
            report_name = self.generate_report_name(prefix="json_report")
        report_path = os.path.join(self.report_dir, f"{report_name}.json")
        with open(report_path, "w") as f:
            json.dump(results, f, indent=4)
        print(f"JSON report saved to: {report_path}")

    def save_csv_report(self, results, report_name=None):
        if not report_name:
            report_name = self.generate_report_name(prefix="csv_report")
        report_path = os.path.join(self.report_dir, f"{report_name}.csv")
        fieldnames = ["Task", "Status", "Details"]

        with open(report_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for task, result in results:
                writer.writerow({
                    "Task": task,
                    "Status": result.get("status", "unknown"),
                    "Details": result.get("details", "No details provided")
                })
        print(f"CSV report saved to: {report_path}")

    def save_html_report(self, results, report_name=None):
        if not report_name:
            report_name = self.generate_report_name(prefix="html_report")
        report_path = os.path.join(self.report_dir, f"{report_name}.html")

        # Generate HTML content
        html_content = """
        <html>
        <head>
            <title>Test Report</title>
            <style>
                body { font-family: Arial, sans-serif; }
                table { width: 100%; border-collapse: collapse; }
                th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
                th { background-color: #f2f2f2; }
                .pass { color: green; }
                .fail { color: red; }
            </style>
        </head>
        <body>
            <h1>Test Report</h1>
            <table>
                <tr>
                    <th>Task</th>
                    <th>Status</th>
                    <th>Details</th>
                </tr>
        """

        for task, result in results:
            status_class = "pass" if result.get("status") == "success" else "fail"
            html_content += f"""
                <tr>
                    <td>{task}</td>
                    <td class="{status_class}">{result.get("status", "unknown")}</td>
                    <td>{result.get("details", "No details provided")}</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        with open(report_path, "w") as f:
            f.write(html_content)
        print(f"HTML report saved to: {report_path}")