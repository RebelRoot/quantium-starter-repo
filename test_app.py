import os
from webdriver_manager.chrome import ChromeDriverManager
from app import app

# Automatically download and configure the ChromeDriver matching the local Google Chrome browser version
# Then inject its folder path into the system PATH so that dash_duo can locate it
driver_path = ChromeDriverManager().install()
driver_dir = os.path.dirname(driver_path)
os.environ["PATH"] += os.pathsep + driver_dir

# Test 1: The header is present in the application layout and has the correct text
def test_header_present(dash_duo):
    dash_duo.start_server(app)
    # Locate the header element using its CSS class
    header = dash_duo.find_element('.dashboard-title')
    assert header is not None
    assert "Soul Foods: Pink Morsel Visualizer" in header.text

# Test 2: The visualization graph is present on the page
def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    # Locate the Plotly graph using its ID selector
    graph = dash_duo.find_element('#sales-line-chart')
    assert graph is not None

# Test 3: The region selector (radio buttons) is present on the page
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    # Locate the RadioItems component using its ID selector
    picker = dash_duo.find_element('#region-selector')
    assert picker is not None
