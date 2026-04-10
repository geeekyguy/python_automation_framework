from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
TEST_DATA_DIR = PROJECT_ROOT / "test_data"
REPORTS_DIR = PROJECT_ROOT / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
ALLURE_RESULTS_DIR = REPORTS_DIR / "allure-results"
ALLURE_REPORT_DIR = REPORTS_DIR / "allure-report"