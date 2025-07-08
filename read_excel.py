import pandas as pd
import json

try:
    # Đọc file Excel
    file_path = 'so sanh goi sinh.xlsx'
    
    # Đọc tất cả các sheet
    excel_file = pd.ExcelFile(file_path)
    print(f"Các sheet có sẵn: {excel_file.sheet_names}")
    
    data = {}
    for sheet_name in excel_file.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"\n=== Sheet: {sheet_name} ===")
        print(f"Kích thước: {df.shape}")
        print("Dữ liệu:")
        print(df.to_string())
        
        # Lưu vào dictionary
        data[sheet_name] = df.to_dict('records')
    
    # Lưu dữ liệu ra file JSON
    with open('excel_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    
    print("\nĐã lưu dữ liệu vào excel_data.json")
    
except Exception as e:
    print(f"Lỗi: {e}")
    import traceback
    traceback.print_exc()