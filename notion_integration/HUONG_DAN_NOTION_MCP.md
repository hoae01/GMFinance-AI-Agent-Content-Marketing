# Hướng Dẫn Kết Nối Notion Database (Notion API Key & MCP Server)

Tài liệu này hướng dẫn bạn 2 cách kết nối Notion Database để Agent có thể tự động lấy dữ liệu ý tưởng/ghi chú của bạn mỗi ngày.

---

## CÁCH 1: Lấy Notion Integration Token & Database ID (Dễ nhất & Nhanh nhất)

### Bước 1: Tạo Notion Integration Token
1. Truy cập trang Notion Integrations: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Nhấn nút **"+ New integration"**.
3. Điền tên: `AI Agent Facebook Post` (chọn đúng Workspace của bạn).
4. Chọn Capabilities: Đảm bảo chọn **Read content**, **Update content**, **Read user information**.
5. Nhấn **Submit** -> **Save**.
6. Bạn sẽ nhận được 1 chuỗi **Internal Integration Secret** (dạng `ntn_...` hoặc `secret_...`). Hãy copy chuỗi này!

### Bước 2: Chia sẻ Database Notion cho Integration
1. Mở trang Database chứa ghi chú/ý tưởng bài viết của bạn trên Notion.
2. Nhấn vào dấu 3 chấm `...` ở góc trên cùng bên phải trang Notion (hoặc nút **Share**).
3. Tìm phần **Add connections** (hoặc **Connect to**).
4. Tìm và chọn `AI Agent Facebook Post` (Integration vừa tạo ở Bước 1) -> Nhấn **Confirm**.

### Bước 3: Lấy Database ID
1. Nhìn vào đường dẫn (URL) của trang Database trên trình duyệt:
   `https://www.notion.so/workspace/32 ký tự alphanumeric?v=...`
2. **Database ID** chính là chuỗi **32 ký tự** đứng ngay sau tên workspace và trước dấu `?` hoặc `/`.
   - Ví dụ URL: `https://www.notion.so/myworkspace/a1b2c3d4e5f678901234567890abcdef?v=12345`
   - Database ID: `a1b2c3d4e5f678901234567890abcdef`

### Bước 4: Lưu thông tin cấu hình
Tạo file `.env` hoặc cập nhật thông tin vào hệ thống:
```env
NOTION_TOKEN=ntn_your_secret_token_here
NOTION_DATABASE_ID=a1b2c3d4e5f678901234567890abcdef
```

---

## CÁCH 2: Cấu Hình Notion MCP Server (Model Context Protocol)

Nếu bạn sử dụng môi trường hỗ trợ MCP Server (như Claude Desktop, Antigravity Agent, Cursor, Windsurf, v.v.), bạn có thể cấu hình Notion MCP Server như sau:

### Đăng ký & Cấu hình MCP Server:
Thêm đoạn JSON sau vào cấu hình MCP (`mcpServers` trong settings):

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-notion"
      ],
      "env": {
        "NOTION_API_TOKEN": "ntn_your_secret_token_here"
      }
    }
  }
}
```

Sau khi cài đặt xong, Agent có thể trực tiếp gọi các công cụ MCP Notion như `notion_search`, `notion_query_database`, `notion_get_page` để đọc ghi chú của bạn vô cùng linh hoạt.
