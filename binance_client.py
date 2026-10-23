import requests


# Bài 1: Tách module
# Tạo binance_client.py và chuyển vào đó hàm get_price (bản đã sửa bài 5). Tạo main.py, import hàm này (thử cả hai kiểu: import binance_client và from binance_client import get_price), rồi in giá BTCUSDT.
# -> Đã hoàn thành
# Bài 2: Thấy tác dụng của __main__
# Trong binance_client.py, thêm ở tầng ngoài dòng print("Đang chạy binance_client"). Chạy python main.py và quan sát. Sau đó sửa lại: đưa dòng in vào hàm main() và gọi nó trong khối if __name__ == "__main__":. Chạy lại main.py, rồi chạy trực tiếp python binance_client.py, so sánh hai lần.
# Câu hỏi: vì sao lần đầu dòng in xuất hiện khi bạn chỉ chạy main.py? -> Vì khi import thì file code luôn chạy tầng ngoài cùng của file

def get_price(symbol):
    try:
        res = requests.get('https://api.binance.com/api/v3/ticker/price',
                           params={"symbol": symbol}, timeout=10)
        res.raise_for_status()
        data = res.json()
        price = float(data['price'])
        return price
    except requests.HTTPError as e:
        print(f"Lỗi HTTP khi lấy giá {symbol}: {e}")
        return None

    except requests.ConnectTimeout:
        print(f"Request lấy giá {symbol} bị timeout.")
        return None

    except requests.ConnectionError:
        print(f"Không thể kết nối mạng khi lấy giá {symbol}.")
        return None


# Bài 3: Thêm hàm lấy toàn bộ ticker
# Trong binance_client.py, viết hàm get_all_tickers_raw() gọi https://api.binance.com/api/v3/ticker/price và trả về chuỗi thô (res.text),
# có timeout và xử lý lỗi như bài 5 (lỗi thì in thông báo và trả None).


def get_all_tickers_raw():
    try:
        res = requests.get(
            "https://api.binance.com/api/v3/ticker/price", timeout=10)
        res.raise_for_status()
        text = res.text
        return text
    except requests.HTTPError as e:
        print("Lỗi HTTP khi gọi API:", e)
        return None
    except requests.ConnectTimeout as e:
        print("Lỗi Timeout:", e)
        return None
    except requests.ConnectionError as e:
        print("Lỗi connection lỗi mạng:", e)
        return None
    except (KeyError, ValueError) as e:
        print("Dữ liệu không hợp lệ", e)
        return None


def main():
    print("Đang chạy binance_client.py")
    text = get_all_tickers_raw()
    print(text)


if __name__ == "__main__":
    main()
