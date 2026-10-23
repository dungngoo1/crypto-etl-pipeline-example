from binance_client import get_price,get_all_tickers_raw
from storage import save_raw,read_file
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
   
    output_dir = os.environ.get("OUTPUT_DIR")
    symbols = os.environ.get("SYMBOLS").split(',')
    
    if not output_dir:
        print("Thiếu biến OUTPUT_DIR trong file .env")
        return
    
    text = get_all_tickers_raw()
    
    if text is None:
        print("Dừng hàm tại đây")
        return   
    
    path = save_raw(text,output_dir)
    
    loaded_json = read_file(path)
    
    print("Đường dẫn lưu file:",path)
    print("Số phần tử",len(loaded_json))
    
    for s in symbols:
        price = get_price(s)
        if price is not None:
            print(f"{s}: {price}")
        
if __name__ == "__main__":
    main()