from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Thiết lập các tùy chọn cho Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless") 
# chrome_options.add_argument("--disable-gpu")  

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Mở trang web
driver.get("https://www.thegioididong.com/dong-ho-deo-tay-orient")

# Tìm tất cả các phần tử chứa thông tin sản phẩm
products = driver.find_elements(By.CSS_SELECTOR, ".item.__cate_7264")

# Duyệt qua từng sản phẩm và lấy tên cùng giá
for product in products:

    try:
        # Lấy tên sản phẩm
        name = product.find_element(By.CSS_SELECTOR, "h3").text

        # Lấy giá sản phẩm
        price = product.find_element(By.CSS_SELECTOR, "strong.price").text

        # In ra tên và giá
        print(f"Tên sản phẩm: {name} - Giá: {price}")
    except Exception as e:
        # Nếu có lỗi (ví dụ: phần tử không có giá), bỏ qua sản phẩm này
        continue

# Đóng trình duyệt
driver.quit()