---
description: Quy tắc thiết kế và phát triển tối ưu cho tất cả dự án
globs: **/*
alwaysApply: true
---

# User Rules - Quy tắc toàn cục tối ưu

## 🎨 Triết lý thiết kế (Jony Ive & Steve Jobs)

### Nguyên tắc cốt lõi
- **"Less, but better"** - Tối giản nhưng hoàn hảo
- **"Simplicity is the ultimate sophistication"** - Đơn giản là đỉnh cao của tinh tế
- **"Design is not just what it looks like - design is how it works"** - Thiết kế không chỉ là hình thức mà là cách hoạt động

### Màu sắc và Visual
- **Chỉ sử dụng**: Trắng (#FFFFFF) và Đen (#000000)
- **Không sử dụng**: Màu sắc rườm rà, gradient phức tạp, hiệu ứng không cần thiết
- **Background**: Luôn là trắng thuần khiết, không dùng xám
- **Text**: Đen (#000000) hoặc xám đậm (#333333) cho readability

## 🖼️ Giao diện người dùng (UI/UX)

### Typography
- **Font family**: Inter, SF Pro Display, Helvetica Neue, system-ui
- **Font weight**: 300 (Light), 400 (Regular), 500 (Medium), 600 (Semibold)
- **Font style**: Thanh mảnh, hiện đại, dễ đọc
- **Line height**: 1.5 cho body text, 1.2 cho headings

### Layout và Spacing
- **Grid system**: 8-point grid (8px, 16px, 24px, 32px, 48px)
- **Container**: Max-width 1200px, centered
- **Padding**: 24px cho mobile, 48px cho desktop
- **Margin**: Consistent spacing giữa các elements

### Components Design
- **Border radius**: 
  - Buttons: 8px
  - Cards: 12px
  - Modals: 16px
  - Input fields: 6px
- **Shadows**: Subtle và minimal
  - Light: `0 1px 3px rgba(0,0,0,0.1)`
  - Medium: `0 4px 12px rgba(0,0,0,0.1)`
  - Heavy: `0 8px 24px rgba(0,0,0,0.12)` (chỉ dùng cho modals)

### Interactive Elements
- **Buttons**: 
  - Primary: Đen background, trắng text
  - Secondary: Trắng background, đen border, đen text
  - Hover: Opacity 0.8 transition
- **Links**: Đen, underline on hover
- **Icons**: 
  - **Chỉ sử dụng**: Icon đơn giản màu trắng đen
  - **Không sử dụng**: Icon màu mè, phức tạp, gradient
  - **Style**: Outline style, stroke-width 1.5px, 20px-24px size
  - **Recommended**: Feather, Lucide, Material Icons Outlined
  - **Nguyên tắc**: Mọi icon đều có lý do hiện diện, không trang trí

## 📊 Progress Tracking & Communication

### Báo cáo tiến độ
- **Format**: `🔄 [X/Y hoàn thành] - Đang làm: [Task hiện tại]`
- **Visual progress**: `████████░░ 80%`
- **Time estimate**: `⏰ 15 phút / 2 giờ ước tính`
- **Next step**: `🎯 Tiếp theo: [Task sắp tới]`

### Task breakdown
- Chia nhỏ mỗi task không quá 30 phút
- Giải thích rõ từng bước đang làm
- Báo cáo vấn đề và cách giải quyết
- Cập nhật real-time trong conversation

### Feature suggestions
- Phân tích code hiện tại để hiểu context
- Đề xuất 2-3 tính năng hữu ích dựa trên:
  - User workflow hiện tại
  - Pain points có thể cải thiện
  - Best practices trong ngành
  - Performance và security improvements

## 💻 Code Quality Standards

### Code Structure
- **Naming**: camelCase cho variables/functions, PascalCase cho classes
- **Variables**: Sử dụng `const` và `let`, tránh `var` (JavaScript/TypeScript)
- **Functions**: Tách nhỏ, single responsibility principle
- **Comments**: Tiếng Việt hoặc English, giải thích logic phức tạp

### Performance & Security
- **Error handling**: Try-catch cho tất cả external calls
- **Input validation**: Validate tất cả user inputs
- **Security**: Không hardcode secrets, sử dụng environment variables
- **Optimization**: Minimize API calls, implement caching khi phù hợp

### Architecture Principles
- **Separation of concerns**: Tách riêng logic, UI, và data
- **Modular design**: Chia code thành modules/components nhỏ
- **Configuration**: Tách config ra files riêng
- **Documentation**: README rõ ràng, inline comments khi cần

## 🎯 Development Workflow

### Planning Phase
1. Phân tích requirements chi tiết
2. Chia nhỏ thành tasks cụ thể (< 30 phút/task)
3. Ước tính thời gian realistic
4. Xác định dependencies và risks

### Implementation Phase
1. Setup cấu trúc project clean
2. Implement core functionality trước
3. Thêm UI/UX với design system
4. Testing và debugging systematic
5. Optimization và polish

### Communication Standards
- Báo cáo tiến độ sau mỗi major milestone
- Giải thích technical decisions và trade-offs
- Đề xuất improvements dựa trên data
- Hỏi feedback khi có uncertainty

## 🚀 Feature Enhancement Guidelines

### Khi đề xuất tính năng mới
- **User-centric**: Tập trung vào real user needs
- **Practical**: Tính năng thực sự solve problems
- **Feasible**: Assess technical complexity và resources
- **Scalable**: Consider future growth và maintenance

### Innovation Approach
- **Automation**: Tự động hóa repetitive tasks
- **Integration**: Connect với existing tools/services
- **Analytics**: Data-driven insights và reporting
- **User Experience**: Streamline workflows
- **Performance**: Optimize speed và reliability

## 📱 Responsive Design Principles

### Mobile-first approach
- Design cho mobile trước, progressive enhancement
- Touch-friendly interactions (minimum 44px targets)
- Readable typography (minimum 16px font size)
- Adequate spacing cho touch interfaces

### Breakpoints Strategy
- Mobile: < 768px (primary focus)
- Tablet: 768px - 1024px (adaptive)
- Desktop: > 1024px (enhanced experience)

### Accessibility Standards
- **Color contrast**: Minimum WCAG AA compliance
- **Keyboard navigation**: Full keyboard accessibility
- **Screen readers**: Proper semantic HTML và ARIA labels
- **Focus indicators**: Clear visual focus states

## 🧠 Chuyên gia Thiết kế Lấy Người Dùng Làm Trung Tâm

### Triết lý thiết kế tích hợp
- **Donald A. Norman**: "Design of Everyday Things" - thiết kế trực quan
- **Jony Ive**: Chủ nghĩa tối giản, thanh lịch - ánh sáng trắng, đường nét nhẹ
- **Steve Jobs**: "Nghệ thuật là loại bỏ" - chỉ giữ lại điều cần thiết
- **Google Research**: Behavioral psychology và A/B testing insights

### Mục tiêu thiết kế
- **Đẹp - Đơn giản - Dễ dùng - Có lý do**
- Phù hợp với tâm lý hành vi và thói quen người dùng
- Làm người dùng cảm thấy thông minh, nhẹ nhàng, hứng thú
- Giảm xung đột nhận thức, tối ưu hành vi

### Quy trình thiết kế UI/UX

#### ✨ 1. Nhận diện vai trò người dùng & mục tiêu
- **Phân tích người dùng**: Ai? (bận rộn, hiểu biết công nghệ, thiết bị?)
- **Mục tiêu hành động**: Tìm kiếm nhanh, nhấn 1 nút, theo dõi tiến độ
- **Tâm lý đi kèm**: Yên tâm, hào hứng, hay kiểm soát?
- **User flow**: Mở app → hành động chính → kết quả

#### 🎨 2. Bố cục và phong cách UI
- **Grid system**: Cấu trúc logic, 8-point grid
- **Typography**: 1-2 font (Inter, SF Pro, Helvetica Neue)
- **Màu sắc tối giản**:
  - Nền: Trắng tuyệt đối (#ffffff)
  - Text: Đen mềm (#222)
  - Action: Đen đậm hoặc xanh tinh khiết
- **Components**: Bo tròn 2xl, hover nhẹ, bóng đổ tinh tế
- **Nguyên tắc**: Không trang trí, mọi thành phần có lý do

#### 🧠 3. Tâm lý học hành vi
- **F-shaped pattern**: Vị trí nút theo tầm nhìn tự nhiên
- **Progressive Disclosure**: Hiện thông tin đúng lúc
- **Paradox of Choice**: Tránh quá nhiều lựa chọn
- **Color Psychology**: Xanh tin cậy, đen quyền lực, xám thông tin phụ
- **Feedback Loop**: Phản hồi ngay lập tức
- **Navigation**: Hiểu rõ vị trí hiện tại và bước tiếp theo

#### 🔍 4. Phân tích và tối ưu
- Xác định khu vực rối, dày chữ, thừa thông tin
- Gom nhóm chức năng liên quan
- Tách phần phức tạp thành bottom sheet/modal
- Ưu tiên thông tin quan trọng ở trang chính
- So sánh với Apple/ChatGPT UI/Basecamp/Notion

### Công cụ và phương pháp
- **Design Tools**: Penpot, Figma, tldraw
- **Testing**: A/B test, user behavior analysis
- **Documentation**: Wireframe, UI specification cho dev
- **Validation**: Logic + tâm lý học cho mỗi thay đổi

### Điều KHÔNG làm
- ❌ Nhiều màu, icon động, gradient rối mắt
- ❌ Copy layout mà không hiểu ngữ cảnh
- ❌ Ưu tiên thẩm mỹ hơn chức năng
- ❌ Trang trí không có mục đích

## 🚀 MCP Server Usage Rules - Quy tắc sử dụng MCP hiệu quả

### 📋 Tổng quan MCP
Document này định nghĩa **khi nào** và **như thế nào** sử dụng từng MCP server để tối ưu hóa workflow và tránh bỏ lỡ cơ hội tận dụng các công cụ mạnh mẽ này.

### 📊 **Excel MCP** - Xử lý dữ liệu bảng tính

#### 🎯 Khi nào SỬ DỤNG:
- **File Excel (.xlsx, .xls)** xuất hiện trong project
- User yêu cầu **đọc/ghi/phân tích** dữ liệu spreadsheet
- Cần **tạo báo cáo** từ dữ liệu Excel
- **So sánh** hoặc **merge** nhiều file Excel
- Tạo **dashboard** hoặc **visualization** từ Excel data
- **Automation** các task Excel repetitive

#### 🛠️ Tools chính:
- `excel_read_sheet` - Đọc dữ liệu với pagination
- `excel_write_to_sheet` - Ghi dữ liệu mới
- `excel_describe_sheets` - Liệt kê thông tin sheets
- `excel_create_table` - Tạo bảng có cấu trúc
- `excel_screen_capture` - Screenshot Excel (Windows only)

### 🔄 **Pandoc MCP** - Chuyển đổi định dạng tài liệu

#### 🎯 Khi nào SỬ DỤNG:
- User yêu cầu **chuyển đổi** giữa các format: MD ↔ HTML ↔ PDF ↔ DOCX
- Cần tạo **PDF reports** từ markdown/HTML
- **Export presentation** sang PDF/DOCX
- Tạo **documentation** với multiple formats
- **Styling DOCX** với reference templates
- **Batch conversion** nhiều files

#### 🛠️ Tool chính:
- `convert-contents` - Chuyển đổi universal

#### ⚠️ Lưu ý quan trọng:
- **PDF conversion**: Cần cài TeX Live trước
- **File paths**: Phải specify đầy đủ path + filename + extension
- **Reference docs**: Sử dụng cho DOCX styling

### 🧠 **Graphlit MCP** - Knowledge base & AI conversation

#### 🎯 Khi nào SỬ DỤNG:
- Cần **tìm kiếm thông tin** trong large dataset
- **Chat với documents** đã upload
- **Extract structured data** từ unstructured text
- Tạo **knowledge base** từ multiple sources
- **Q&A system** cho documents
- **Content analysis** và insights

#### 🛠️ Tools chính:
- `promptConversation` - Chat với knowledge base
- `retrieveSources` - Tìm kiếm content relevant
- `extractText` - Trích xuất JSON từ text
- `queryContents` - Query metadata
- `createCollection` - Tổ chức content

### 🐙 **GitHub MCP** - Git repository management

#### 🎯 Khi nào SỬ DỤNG:
- **Deploy project** lên GitHub
- **Backup code** và version control
- **Collaborate** với team members
- Tạo **issues** và **pull requests**
- **Search code** across repositories
- **Manage releases** và documentation

#### 🛠️ Tools chính:
- `create_repository` - Tạo repo mới
- `push_files` - Upload multiple files
- `create_issue` - Tạo issue tracking
- `search_code` - Tìm kiếm code
- `create_pull_request` - Code review workflow

### 🎭 **Puppeteer MCP** - Web automation & testing

#### 🎯 Khi nào SỬ DỤNG:
- **Test web applications** tự động
- **Screenshot** websites/web apps
- **Web scraping** data từ websites
- **Automated interactions** với web forms
- **Performance testing** web pages
- **Generate reports** từ web data

#### 🛠️ Tools chính:
- `puppeteer_navigate` - Điều hướng URL
- `puppeteer_screenshot` - Chụp màn hình
- `puppeteer_click` - Click elements
- `puppeteer_fill` - Fill forms
- `puppeteer_evaluate` - Execute JavaScript

### 📚 **Context7 & TaskManager MCP**

#### Context7 - Library documentation:
- **Documentation** cho libraries/packages
- **Resolve dependencies** và compatibility
- **Best practices** cho specific libraries

#### TaskManager - Project management:
- **Complex projects** cần task breakdown
- **Team collaboration** và task assignment
- **Progress tracking** và reporting

### 🎯 **DECISION MATRIX** - Khi nào dùng MCP nào?

| Tình huống | MCP được ưu tiên | Lý do |
|------------|------------------|-------|
| File .xlsx trong project | **Excel** | Specialized Excel handling |
| Cần PDF/DOCX output | **Pandoc** | Professional document conversion |
| Multiple documents analysis | **Graphlit** | AI-powered content understanding |
| Web app testing | **Puppeteer** | Browser automation |
| Code backup/sharing | **GitHub** | Version control & collaboration |
| Complex project | **TaskManager** | Structured project management |
| Library questions | **Context7** | Technical documentation |

### 🚀 **AUTO-TRIGGER RULES** - Tự động kích hoạt

#### 📊 Excel MCP auto-triggers:
```
IF (file_extension == ".xlsx" OR file_extension == ".xls") 
   AND (user_mentions == "phân tích" OR "báo cáo" OR "dữ liệu")
THEN use Excel MCP
```

#### 🔄 Pandoc MCP auto-triggers:
```
IF user_requests == ("PDF" OR "DOCX" OR "chuyển đổi" OR "export")
   AND current_files == (".html" OR ".md" OR ".txt")
THEN use Pandoc MCP
```

#### 🧠 Graphlit MCP auto-triggers:
```
IF (multiple_documents_present == true)
   AND (user_asks == "tìm kiếm" OR "so sánh" OR "phân tích nội dung")
THEN use Graphlit MCP
```

#### 🎭 Puppeteer MCP auto-triggers:
```
IF (file_type == ".html" OR web_app_present == true)
   AND (user_requests == "test" OR "screenshot" OR "demo")
THEN use Puppeteer MCP
```

### 💡 **MCP BEST PRACTICES**

#### 🔄 Workflow optimization:
1. **Analyze context** trước khi chọn MCP
2. **Combine MCPs** khi cần (Excel → Pandoc → GitHub)
3. **Cache results** để tránh duplicate calls
4. **Error handling** cho mỗi MCP call

#### 📊 Performance tips:
1. **Excel MCP**: Sử dụng pagination cho large datasets
2. **Pandoc MCP**: Batch convert multiple files
3. **Graphlit MCP**: Create collections để organize content
4. **GitHub MCP**: Push multiple files trong 1 commit

#### 🎯 User experience:
1. **Explain** tại sao chọn MCP cụ thể
2. **Show progress** cho long-running operations
3. **Provide alternatives** nếu MCP không available
4. **Suggest improvements** dựa trên MCP capabilities

#### 🔧 **TROUBLESHOOTING**
- **Pandoc PDF**: Cần cài TeX Live
- **Excel large files**: Sử dụng pagination
- **Graphlit setup**: Cần configure project trước
- **GitHub auth**: Check permissions
- **Puppeteer timeout**: Increase wait times

---

*Những quy tắc này áp dụng cho mọi dự án, đảm bảo consistency, quality và user experience tối ưu theo triết lý "Less, but better" của Jony Ive và Steve Jobs, kết hợp với nghiên cứu behavioral psychology hiện đại và tối ưu hóa việc sử dụng MCP servers.*