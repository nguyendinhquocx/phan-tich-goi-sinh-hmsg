import pandas as pd
import sys

def analyze_excel_file(file_path):
    try:
        # Đọc tất cả các sheet trong file Excel
        excel_file = pd.ExcelFile(file_path)
        
        print(f"📊 PHÂN TÍCH FILE: {file_path}")
        print(f"📋 Số lượng sheet: {len(excel_file.sheet_names)}")
        print(f"📝 Tên các sheet: {excel_file.sheet_names}")
        print("\n" + "="*60 + "\n")
        
        # Phân tích từng sheet
        for i, sheet_name in enumerate(excel_file.sheet_names, 1):
            print(f"🔍 SHEET {i}: {sheet_name}")
            print("-" * 40)
            
            try:
                # Đọc sheet
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                
                print(f"📏 Kích thước: {df.shape[0]} hàng x {df.shape[1]} cột")
                
                if not df.empty:
                    print(f"📋 Tên các cột:")
                    for j, col in enumerate(df.columns, 1):
                        print(f"   {j}. {col}")
                    
                    print(f"\n📄 Dữ liệu mẫu (5 hàng đầu):")
                    print(df.head().to_string(index=False))
                    
                    # Thống kê cơ bản
                    print(f"\n📊 Thống kê:")
                    print(f"   - Số hàng có dữ liệu: {df.dropna(how='all').shape[0]}")
                    print(f"   - Số cột có dữ liệu: {df.dropna(axis=1, how='all').shape[1]}")
                    
                    # Kiểm tra các cột số
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    if len(numeric_cols) > 0:
                        print(f"   - Các cột số: {list(numeric_cols)}")
                    
                    # Kiểm tra các từ khóa quan trọng
                    text_content = df.to_string().lower()
                    keywords = ['gói sinh', 'bệnh viện', 'giá', 'chi phí', 'dịch vụ', 'so sánh']
                    found_keywords = [kw for kw in keywords if kw in text_content]
                    if found_keywords:
                        print(f"   - Từ khóa tìm thấy: {found_keywords}")
                        
                else:
                    print("   ⚠️ Sheet này không có dữ liệu")
                    
            except Exception as e:
                print(f"   ❌ Lỗi khi đọc sheet: {str(e)}")
            
            print("\n" + "="*60 + "\n")
        
        # Tóm tắt nội dung
        print("📝 TÓM TẮT PHÂN TÍCH:")
        print("-" * 40)
        
        all_data = []
        for sheet_name in excel_file.sheet_names:
            try:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                if not df.empty:
                    all_data.append(df)
            except:
                continue
        
        if all_data:
            combined_text = ' '.join([df.to_string() for df in all_data]).lower()
            
            # Phân tích chủ đề
            if 'gói sinh' in combined_text:
                print("🏥 Chủ đề: So sánh các gói sinh tại bệnh viện")
            
            if any(word in combined_text for word in ['giá', 'chi phí', 'tiền']):
                print("💰 Có thông tin về giá cả/chi phí")
            
            if any(word in combined_text for word in ['bệnh viện', 'phòng khám']):
                print("🏥 Có thông tin về cơ sở y tế")
            
            if any(word in combined_text for word in ['dịch vụ', 'tiện ích']):
                print("🛎️ Có thông tin về dịch vụ")
                
        print("\n✅ Phân tích hoàn tất!")
        
    except Exception as e:
        print(f"❌ Lỗi khi phân tích file: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    file_path = "d:\\pcloud\\hmsg\\package\\goi sanh\\so sanh goi sinh.xlsx"
    analyze_excel_file(file_path)