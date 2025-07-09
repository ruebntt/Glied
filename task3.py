import sys
import json

def fill_values(tests, values):
    if isinstance(tests, dict):
        if 'id' in tests:
            test_id = str(tests['id'])
            tests['value'] = values.get(test_id, None)
        for key, val in tests.items():
            if isinstance(val, (dict, list)):
                fill_values(val, values)
    elif isinstance(tests, list):
        for item in tests:
            fill_values(item, values)

def main(values_path, tests_path, report_path):
    with open(values_path, 'r', encoding='utf-8') as f:
        values = json.load(f)

    with open(tests_path, 'r', encoding='utf-8') as f:
        tests_structure = json.load(f)

    fill_values(tests_structure, values)

    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(tests_structure, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    main(values_path, tests_path, report_path)

