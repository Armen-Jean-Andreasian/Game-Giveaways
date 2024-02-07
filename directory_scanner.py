from the_directory_scanner import prettify_structure, scan_directory

directory_scan = scan_directory(
    ignored_items=('.git', '.idea', 'venv', '__pycache__', '.github',
                   'chrome-win64', 'chromedriver-win64', 'selenium_webdriver_issue'),
    output_file_name='project_structure.txt',
    directory='.'
)

prettify_structure(
    output_file=directory_scan,
    lines_to_trim=1,
    spaces_to_trim=4,
)
