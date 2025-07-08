# Gói Sinh - Package Analysis Project

## Tổng quan dự án

Dự án phân tích và so sánh các gói sinh tại các bệnh viện, bao gồm việc xử lý dữ liệu Excel, tạo báo cáo và presentation để hỗ trợ quyết định lựa chọn gói sinh phù hợp.

## Cấu trúc dự án

```
goi sanh/
├── Dữ liệu Excel
│   ├── danh sach dang ki sanh.xlsx          # Danh sách đăng ký sinh
│   ├── danh sach khach hang can sinh.xlsx   # Danh sách khách hàng cần sinh
│   ├── file xu li du lieu.xlsx             # File xử lý dữ liệu
│   └── so sanh goi sinh.xlsx               # So sánh các gói sinh
│
├── Tài liệu PDF
│   ├── goi sinh hanh phuc.pdf              # Gói sinh Hạnh Phúc
│   ├── goi sinh hoan my sai gon.pdf        # Gói sinh Hoàn Mỹ Sài Gòn
│   └── goi sinh hoan my thu duc.pdf        # Gói sinh Hoàn Mỹ Thủ Đức
│
├── Presentations
│   ├── so sanh goi sinh v1.pptx            # Presentation v1
│   ├── so sanh goi sinh v2.pptx            # Presentation v2
│   └── so sanh goi sinh v2.pdf             # Presentation v2 (PDF)
│   └── so sanh goi sinh v3.pdf             # Presentation v3 (PDF)
│
├── Scripts & Tools
│   ├── read_excel.py                       # Script đọc dữ liệu Excel
│   ├── excel_data.json                     # Dữ liệu Excel đã convert
│   ├── index.html                          # Web interface
│   └── presentation.html                   # Web presentation
│
├── Documentation
│   ├── summary_report.md                   # Báo cáo tổng hợp
│   ├── user_rules.md                       # Quy tắc toàn cục
│   └── README.md                           # File này
│
└── Configuration
    ├── .vscode/launch.json                  # VS Code debug config
    └── .trae/.ignore                       # Trae ignore file
```

## Triết lý thiết kế

Dự án tuân theo nguyên tắc **"Less, but better"** của Jony Ive và Steve Jobs:

### Nguyên tắc cốt lõi
- **Tối giản nhưng hoàn hảo**: Chỉ giữ lại những gì thực sự cần thiết
- **Đơn giản là đỉnh cao**: Thiết kế không chỉ là hình thức mà là cách hoạt động
- **Lấy người dùng làm trung tâm**: Mọi quyết định thiết kế đều phục vụ trải nghiệm người dùng

### Visual Design
- **Màu sắc**: Chỉ sử dụng trắng (#FFFFFF) và đen (#000000)
- **Typography**: Inter, SF Pro Display, Helvetica Neue
- **Icons**: Đơn giản, outline style, màu trắng đen
- **Layout**: 8-point grid system, spacing nhất quán

## Tính năng chính

### Xử lý dữ liệu Excel
- Đọc và phân tích dữ liệu từ multiple Excel files
- So sánh các gói sinh khác nhau
- Tạo báo cáo tự động từ dữ liệu

### Quản lý tài liệu
- Chuyển đổi giữa các format (PDF, DOCX, HTML)
- Tạo presentation từ dữ liệu
- Export báo cáo professional

### Web Interface
- Giao diện web đơn giản, dễ sử dụng
- Hiển thị dữ liệu interactive
- Responsive design cho mọi thiết bị

## Công nghệ sử dụng

### Data Processing
- **Python**: Script xử lý dữ liệu Excel
- **Excel MCP**: Đọc/ghi dữ liệu spreadsheet
- **JSON**: Format lưu trữ dữ liệu structured

### Document Conversion
- **Pandoc MCP**: Chuyển đổi giữa các format
- **PDF Generation**: Tạo báo cáo professional
- **HTML/CSS**: Web presentation

### AI & Analysis
- **Graphlit MCP**: Knowledge base và AI conversation
- **Content Analysis**: Phân tích và insights từ documents
- **Automated Reporting**: Tạo báo cáo tự động

## Quy tắc phát triển

### Code Quality
- **Naming**: camelCase cho variables, PascalCase cho classes
- **Error Handling**: Try-catch cho tất cả external calls
- **Security**: Không hardcode secrets, sử dụng environment variables
- **Documentation**: Comments tiếng Việt hoặc English

### Workflow
1. **Planning**: Phân tích requirements chi tiết
2. **Implementation**: Core functionality trước, UI sau
3. **Testing**: Systematic testing và debugging
4. **Optimization**: Performance và polish

### Progress Tracking
- Format: `[X/Y hoàn thành] - Đang làm: [Task hiện tại]`
- Visual: `████████░░ 80%`
- Time estimate: `15 phút / 2 giờ ước tính`

## MCP Server Integration

Dự án tích hợp các MCP servers để tối ưu workflow:

### Excel MCP
- **Auto-trigger**: Khi có file .xlsx và user mentions "phân tích", "báo cáo", "dữ liệu"
- **Use cases**: Đọc/ghi Excel, tạo báo cáo, so sánh data

### Pandoc MCP
- **Auto-trigger**: Khi user requests "PDF", "DOCX", "chuyển đổi", "export"
- **Use cases**: Convert documents, tạo PDF reports, export presentations

### Graphlit MCP
- **Auto-trigger**: Khi có multiple documents và user asks "tìm kiếm", "so sánh", "phân tích nội dung"
- **Use cases**: Knowledge base, Q&A với documents, content analysis

### GitHub MCP
- **Use cases**: Backup code, version control, collaboration

## Kết quả đạt được

### Hoàn thành
- [x] Cấu trúc dự án clean và organized
- [x] Quy tắc thiết kế toàn cục (user_rules.md)
- [x] Integration MCP servers
- [x] Data processing pipeline
- [x] Web interface cơ bản
- [x] Documentation đầy đủ

### Tính năng nổi bật
- **Automated Excel Processing**: Xử lý dữ liệu Excel tự động
- **Multi-format Export**: Export sang PDF, DOCX, HTML
- **AI-powered Analysis**: Phân tích nội dung với Graphlit
- **Clean UI/UX**: Thiết kế tối giản, user-friendly

## Hướng dẫn sử dụng

### 1. Xử lý dữ liệu Excel
```bash
python read_excel.py
```

### 2. Mở web interface
```bash
# Mở index.html trong browser
# Hoặc sử dụng live server
```

### 3. Tạo báo cáo PDF
- Sử dụng Pandoc MCP để convert từ HTML/MD sang PDF
- Tự động styling với reference templates

### 4. Phân tích nội dung
- Upload documents vào Graphlit
- Sử dụng AI conversation để phân tích
- Extract insights và tạo báo cáo

## Roadmap tương lai

### Data Enhancement
- [ ] Real-time data sync
- [ ] Advanced analytics dashboard
- [ ] Automated report scheduling

### UI/UX Improvements
- [ ] Mobile-first responsive design
- [ ] Dark mode support
- [ ] Accessibility improvements

### AI Integration
- [ ] Predictive analytics
- [ ] Automated recommendations
- [ ] Natural language queries

### Technical Improvements
- [ ] Performance optimization
- [ ] Error handling enhancement
- [ ] Testing automation

## Đóng góp

Dự án tuân theo quy tắc trong `user_rules.md`:
- Thiết kế tối giản, lấy người dùng làm trung tâm
- Code quality cao với proper documentation
- Sử dụng MCP servers hiệu quả
- Progress tracking và communication rõ ràng

## Liên hệ

Mọi thắc mắc về dự án, vui lòng tham khảo:
- `user_rules.md` - Quy tắc toàn cục
- `summary_report.md` - Báo cáo chi tiết
- Code comments trong các files

---

*Dự án được phát triển theo triết lý "Less, but better" - Tối giản nhưng hoàn hảo, với focus vào user experience và code quality.*