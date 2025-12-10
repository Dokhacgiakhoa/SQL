questions = [
    # ======================================================================================
    # EASY (50 Questions)
    # Target: 25 Single Choice, 25 Multiple Choice
    # Points: 1
    # ======================================================================================

    # --- EASY SINGLE CHOICE (25) ---
    {
        "difficulty": "easy", "type": "single",
        "question": "SQL viết tắt của từ gì?",
        "options": ["Structured Query Language", "Strong Question Language", "Structured Question List", "Simple Query Language"],
        "answer": "Structured Query Language",
        "explanation": "SQL là viết tắt của Structured Query Language (Ngôn ngữ truy vấn có cấu trúc)."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Câu lệnh nào dùng để lấy dữ liệu từ bảng?",
        "options": ["SELECT", "GET", "OPEN", "EXTRACT"],
        "answer": "SELECT",
        "explanation": "SELECT là câu lệnh cơ bản để truy vấn dữ liệu."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Mệnh đề nào dùng để lọc bản ghi?",
        "options": ["WHERE", "HAVING", "FILTER", "SEARCH"],
        "answer": "WHERE",
        "explanation": "WHERE lọc các dòng thỏa mãn điều kiện cụ thể."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Từ khóa nào trả về các giá trị duy nhất?",
        "options": ["DISTINCT", "UNIQUE", "DIFFERENT", "SINGLE"],
        "answer": "DISTINCT",
        "explanation": "SELECT DISTINCT loại bỏ các dòng trùng lặp trong kết quả."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Để sắp xếp kết quả, ta dùng mệnh đề nào?",
        "options": ["ORDER BY", "SORT BY", "ARRANGE BY", "GROUP BY"],
        "answer": "ORDER BY",
        "explanation": "ORDER BY sắp xếp kết quả theo cột chỉ định."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Mặc định ORDER BY sắp xếp như thế nào?",
        "options": ["Tăng dần (ASC)", "Giảm dần (DESC)", "Ngẫu nhiên", "Theo ID"],
        "answer": "Tăng dần (ASC)",
        "explanation": "Nếu không ghi rõ, SQL mặc định sắp xếp ASC."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Toán tử nào so sánh 'khác nhau' trong SQL chuẩn?",
        "options": ["<> hoặc !=", "==", "><", "NOT"],
        "answer": "<> hoặc !=",
        "explanation": "Cả <> và != thường được chấp nhận là toán tử khác."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Để chèn dữ liệu mới, dùng lệnh nào?",
        "options": ["INSERT INTO", "ADD RECORD", "UPDATE", "MAKE NEW"],
        "answer": "INSERT INTO",
        "explanation": "INSERT INTO table VALUES ..."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Để xóa bảng hoàn toàn (cả cấu trúc), dùng lệnh nào?",
        "options": ["DROP TABLE", "DELETE TABLE", "REMOVE TABLE", "CLEAR TABLE"],
        "answer": "DROP TABLE",
        "explanation": "DROP TABLE hủy bảng khỏi CSDL."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Giá trị NULL nghĩa là gì?",
        "options": ["Giá trị chưa xác định", "Số 0", "Chuỗi rỗng", "False"],
        "answer": "Giá trị chưa xác định",
        "explanation": "NULL đại diện cho missing data hoặc unknown."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Kiểu dữ liệu INT dùng lưu chữ gì?",
        "options": ["Số nguyên", "Số thực", "Chuỗi", "Ngày tháng"],
        "answer": "Số nguyên",
        "explanation": "INT là Integer."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Hàm COUNT(*) trả về gì?",
        "options": ["Tổng số dòng", "Tổng giá trị", "Giá trị lớn nhất", "Giá trị trung bình"],
        "answer": "Tổng số dòng",
        "explanation": "Đếm tất cả các dòng, kể cả dòng có chứa NULL."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Mệnh đề FROM đứng sau mệnh đề nào trog cú pháp chuẩn?",
        "options": ["SELECT", "WHERE", "ORDER BY", "GROUP BY"],
        "answer": "SELECT",
        "explanation": "SELECT ... FROM ..."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Để tìm tên bắt đầu bằng chữ 'A', dùng mẫu nào?",
        "options": ["LIKE 'A%'", "LIKE '%A'", "LIKE 'A_'", "LIKE '_A'"],
        "answer": "LIKE 'A%'",
        "explanation": "% đại diện cho chuỗi bất kỳ phía sau."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Toán tử nào kiểm tra giá trị nằm trong danh sách?",
        "options": ["IN", "BETWEEN", "LIKE", "EXISTS"],
        "answer": "IN",
        "explanation": "IN ('a', 'b', 'c')."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Ràng buộc PRIMARY KEY yêu cầu gì?",
        "options": ["Không NULL và Duy Nhất", "Chỉ cần Duy Nhất", "Có thể NULL", "Là số nguyên"],
        "answer": "Không NULL và Duy Nhất",
        "explanation": "Khóa chính định danh dòng nên không được trùng và không được rỗng."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Lệnh UPDATE dùng để làm gì?",
        "options": ["Sửa đổi dữ liệu đã có", "Thêm dữ liệu mới", "Xóa dữ liệu", "Xem dữ liệu"],
        "answer": "Sửa đổi dữ liệu đã có",
        "explanation": "UPDATE table SET col = new_val."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Dấu comment 1 dòng trong SQL là gì?",
        "options": ["--", "//", "#", "/*"],
        "answer": "--",
        "explanation": "Hai dấu gạch nối (--) là chuẩn SQL."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Để lấy tất cả các cột, dùng ký hiệu nào?",
        "options": ["*", "ALL", "%", "&"],
        "answer": "*",
        "explanation": "SELECT * FROM ..."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Phép AND trả về TRUE khi nào?",
        "options": ["Cả hai điều kiện đều đúng", "Một trong hai đúng", "Cả hai sai", "Không bao giờ"],
        "answer": "Cả hai điều kiện đều đúng",
        "explanation": "Logic AND yêu cầu tất cả vế phải True."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Phép OR trả về TRUE khi nào?",
        "options": ["Ít nhất một điều kiện đúng", "Cả hai phải đúng", "Cả hai phải sai", "Chỉ khi vế đầu đúng"],
        "answer": "Ít nhất một điều kiện đúng",
        "explanation": "Logic OR chỉ cần 1 vế True là kết quả True."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Hàm MAX() dùng để làm gì?",
        "options": ["Tìm giá trị lớn nhất", "Đếm số dòng", "Tính tổng", "Làm tròn"],
        "answer": "Tìm giá trị lớn nhất",
        "explanation": "MAX(column) trả về giá trị cao nhất."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Kiểu dữ liệu nào lưu chuỗi có độ dài thay đổi?",
        "options": ["VARCHAR", "CHAR", "TEXT", "INT"],
        "answer": "VARCHAR",
        "explanation": "Variable Character."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Để xóa các dòng dữ liệu, dùng mệnh đề nào?",
        "options": ["DELETE FROM", "REMOVE FROM", "DROP FROM", "CLEAR"],
        "answer": "DELETE FROM",
        "explanation": "DELETE FROM table WHERE ..."
    },
    {
        "difficulty": "easy", "type": "single",
        "question": "Hàm NOW() hoặc GETDATE() thường trả về gì?",
        "options": ["Ngày giờ hiện tại", "Ngày hôm qua", "Giờ UTC", "Năm hiện tại"],
        "answer": "Ngày giờ hiện tại",
        "explanation": "Trả về timestamp hiện tại của hệ thống."
    },

    # --- EASY MULTIPLE CHOICE (25) ---
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các lệnh thuộc nhóm DML (Data Manipulation Language)?",
        "options": ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP"],
        "answer": ["SELECT", "INSERT", "UPDATE", "DELETE"],
        "explanation": "DML thao tác dữ liệu. CREATE/DROP là DDL."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các lệnh thuộc nhóm DDL (Data Definition Language)?",
        "options": ["CREATE", "ALTER", "DROP", "TRUNCATE", "SELECT", "INSERT"],
        "answer": ["CREATE", "ALTER", "DROP", "TRUNCATE"],
        "explanation": "DDL định nghĩa và sửa đổi cấu trúc bảng."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Những toán tử nào dùng để so sánh trong mệnh đề WHERE?",
        "options": ["=", ">", "<", "LIKE", "PLUS", "MINUS"],
        "answer": ["=", ">", "<", "LIKE"],
        "explanation": "PLUS/MINUS là toán tử số học, không phải so sánh logic."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Các hàm nào là hàm tổng hợp (Aggregate Functions)?",
        "options": ["SUM", "COUNT", "AVG", "MIN", "MAX", "LEN", "MID"],
        "answer": ["SUM", "COUNT", "AVG", "MIN", "MAX"],
        "explanation": "Các hàm này tính toán trên một tập hợp dòng."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các kiểu dữ liệu số trong SQL?",
        "options": ["INT", "FLOAT", "DECIMAL", "VARCHAR", "DATE"],
        "answer": ["INT", "FLOAT", "DECIMAL"],
        "explanation": "VARCHAR là chuỗi, DATE là ngày tháng."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Thành phần nào là bắt buộc trong câu lệnh SELECT cơ bản?",
        "options": ["SELECT", "FROM", "WHERE", "GROUP BY"],
        "answer": ["SELECT", "FROM"],
        "explanation": "Tối thiểu phải có SELECT và FROM (đối với hầu hết các hệ quản trị)."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các từ khóa dùng trong mệnh đề ORDER BY?",
        "options": ["ASC", "DESC", "TOP", "BOTTOM"],
        "answer": ["ASC", "DESC"],
        "explanation": "Tăng dần và Giảm dần."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Những ký tự đại diện (wildcards) nào dùng với LIKE?",
        "options": ["%", "_", "*", "?"],
        "answer": ["%", "_"],
        "explanation": "% (chuỗi bất kỳ), _ (1 ký tự). * và ? thường dùng trong DOS/Shell."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các ràng buộc (Constraints) hợp lệ?",
        "options": ["PRIMARY KEY", "FOREIGN KEY", "NOT NULL", "UNIQUE", "SUPER KEY"],
        "answer": ["PRIMARY KEY", "FOREIGN KEY", "NOT NULL", "UNIQUE"],
        "explanation": "SUPER KEY là khái niệm lý thuyết, không phải từ khóa khai báo."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Để thêm một cột mới vào bảng, dùng các từ khóa nào?",
        "options": ["ALTER TABLE", "ADD COLUMN", "UPDATE TABLE", "INSERT COLUMN"],
        "answer": ["ALTER TABLE", "ADD COLUMN"], # Chấp nhận syntax phổ biến
        "explanation": "Cú pháp: ALTER TABLE ... ADD column/ADD ..."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Những giá trị nào KHÔNG thỏa mãn điều kiện 'WHERE age > 18'?",
        "options": ["18", "10", "15", "19", "20"],
        "answer": ["18", "10", "15"],
        "explanation": "> 18 nghĩa là phải từ 19 trở lên."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các phép toán logic trong SQL?",
        "options": ["AND", "OR", "NOT", "XOR", "IF"],
        "answer": ["AND", "OR", "NOT"],
        "explanation": "IF thường là hàm hoặc luồng điều khiển, không phải toán tử logic mệnh đề WHERE cơ bản (tùy ngữ cảnh nhưng ở mức basic là AND/OR/NOT)."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Cú pháp INSERT nào hợp lệ (tùy hệ)?",
        "options": ["INSERT INTO t VALUES (1, 'A')", "INSERT INTO t (col1) VALUES (1)", "INSERT t SET col1=1", "INSERT NEW (1)"],
        "answer": ["INSERT INTO t VALUES (1, 'A')", "INSERT INTO t (col1) VALUES (1)"],
        "explanation": "Hai dạng đầu là chuẩn ANSI SQL."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các kiểu dữ liệu chuỗi?",
        "options": ["CHAR", "VARCHAR", "TEXT", "INT", "BIT"],
        "answer": ["CHAR", "VARCHAR", "TEXT"],
        "explanation": "Dùng lưu ký tự."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Những lệnh nào không trả về dữ liệu (Result Set)?",
        "options": ["UPDATE", "DELETE", "INSERT", "SELECT"],
        "answer": ["UPDATE", "DELETE", "INSERT"],
        "explanation": "Chúng trả về số dòng bị ảnh hưởng, không phải bảng dữ liệu (trừ khi dùng RETURNING)."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Các lỗi cú pháp thường gặp?",
        "options": ["Thiếu FROM", "Thiếu dấu ; (ở một số tool)", "Viết sai chính tả SELECT", "Dùng nháy kép cho chuỗi (tùy hệ)"],
        "answer": ["Thiếu FROM", "Viết sai chính tả SELECT"],
        "explanation": "Đây là các lỗi cơ bản làm câu lệnh không chạy."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Thuộc tính của PRIMARY KEY?",
        "options": ["Unique", "Not Null", "Auto Increment (thường dùng)", "Cho phép trùng lắp"],
        "answer": ["Unique", "Not Null"],
        "explanation": "Bản chất là duy nhất và không rỗng."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Những cách viết comment đúng trong SQL (tùy hệ)?",
        "options": ["-- comment", "/* comment */", "# comment", "// comment"],
        "answer": ["-- comment", "/* comment */"],
        "explanation": "-- và /* */ là chuẩn ANSI."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Phần nào giúp tăng tốc độ tìm kiếm?",
        "options": ["INDEX", "PRIMARY KEY (tạo index ngầm)", "COMMENT", "ALIAS"],
        "answer": ["INDEX", "PRIMARY KEY (tạo index ngầm)"],
        "explanation": "Index giúp scan nhanh hơn."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Từ khóa nào dùng để đặt tên giả (Alias)?",
        "options": ["AS", "Space (khoảng trắng)", "ALIAS", "NAME"],
        "answer": ["AS", "Space (khoảng trắng)"],
        "explanation": "SELECT col AS c hoặc SELECT col c đều được."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn các hàm xử lý chuỗi?",
        "options": ["LOWER", "UPPER", "SUBSTRING", "SQRT", "ABS"],
        "answer": ["LOWER", "UPPER", "SUBSTRING"],
        "explanation": "SQRT, ABS là hàm toán học."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "NULL khác với?",
        "options": ["Chuỗi rỗng ''", "Số 0", "Dấu cách ' '", "Giá trị không xác định"],
        "answer": ["Chuỗi rỗng ''", "Số 0", "Dấu cách ' '"],
        "explanation": "NULL không bằng bất kỳ giá trị cụ thể nào."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Mệnh đề GROUP BY thường đi kèm với?",
        "options": ["COUNT", "SUM", "AVG", "WHERE"],
        "answer": ["COUNT", "SUM", "AVG"],
        "explanation": "Gom nhóm để tính toán tổng hợp."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Những câu lệnh nào thay đổi dữ liệu trong bảng?",
        "options": ["UPDATE", "DELETE", "SELECT", "TRUNCATE"],
        "answer": ["UPDATE", "DELETE", "TRUNCATE"],
        "explanation": "SELECT chỉ đọc."
    },
    {
        "difficulty": "easy", "type": "multiple",
        "question": "Chọn đúng về câu lệnh TRUNCATE?",
        "options": ["Xóa hết dữ liệu", "Giữ lại cấu trúc bảng", "Xóa bảng khỏi database", "Chậm hơn DELETE"],
        "answer": ["Xóa hết dữ liệu", "Giữ lại cấu trúc bảng"],
        "explanation": "Nhanh hơn DELETE và reset Identity."
    },

    # ======================================================================================
    # MEDIUM (30 Questions)
    # Target: 15 Single Choice, 15 Multiple Choice
    # Points: 2
    # ======================================================================================

    # --- MEDIUM SINGLE CHOICE (15) ---
    {
        "difficulty": "medium", "type": "single",
        "question": "INNER JOIN trả về kết quả nào?",
        "options": ["Chỉ các dòng khớp ở cả 2 bảng", "Tất cả dòng bảng trái", "Tất cả dòng bảng phải", "Tích Đề-các"],
        "answer": "Chỉ các dòng khớp ở cả 2 bảng",
        "explanation": "Giao của 2 tập hợp dựa trên điều kiện ON."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "LEFT JOIN giữ lại dữ liệu của bảng nào?",
        "options": ["Bảng bên trái (FROM)", "Bảng bên phải (JOIN)", "Cả hai", "chỉ dòng khớp"],
        "answer": "Bảng bên trái (FROM)",
        "explanation": "Lấy hết bảng trái + phần khớp bảng phải."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Điều kiện trong HAVING dùng để lọc gì?",
        "options": ["Kết quả sau khi Group By", "Dữ liệu thô trước khi Group", "Tên cột", "Số trang"],
        "answer": "Kết quả sau khi Group By",
        "explanation": "HAVING lọc trên Aggregate (VD: HAVING COUNT(*) > 5)."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Hàm CONCAT() dùng để?",
        "options": ["Nối chuỗi", "Cắt chuỗi", "Tìm kiếm", "Thay thế"],
        "answer": "Nối chuỗi",
        "explanation": "Ghép các chuỗi lại với nhau."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Dạng chuẩn 1NF yêu cầu gì?",
        "options": ["Giá trị nguyên tố (Atomic)", "Có khóa ngoại", "Không phụ thuộc bắc cầu", "Tách bảng"],
        "answer": "Giá trị nguyên tố (Atomic)",
        "explanation": "Mỗi ô chỉ chứa 1 giá trị đơn."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Subquery là gì?",
        "options": ["Truy vấn lồng bên trong", "Truy vấn chính", "Thủ tục lưu trữ", "Bảng ảo"],
        "answer": "Truy vấn lồng bên trong",
        "explanation": "SELECT ... (SELECT ...)."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "UNION mặc định làm gì với các dòng trùng lặp?",
        "options": ["Loại bỏ", "Giữ lại", "Báo lỗi", "Sắp xếp"],
        "answer": "Loại bỏ",
        "explanation": "UNION lọc trùng, UNION ALL thì không."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Nếu DELETE không có WHERE?",
        "options": ["Xóa toàn bộ dữ liệu bảng", "Lỗi", "Xóa dòng đầu", "Không làm gì"],
        "answer": "Xóa toàn bộ dữ liệu bảng",
        "explanation": "Rất nguy hiểm."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "BETWEEN 10 AND 20 có bao gồm 10 và 20 không?",
        "options": ["Có (Inclusive)", "Không (Exclusive)", "Tùy database", "Chỉ gồm 10"],
        "answer": "Có (Inclusive)",
        "explanation": "Thường là bao gồm cả cận trên và dưới."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Foreign Key tham chiếu đến đâu?",
        "options": ["Primary Key (hoặc Unique) bảng khác", "Cột bất kỳ", "Index", "View"],
        "answer": "Primary Key (hoặc Unique) bảng khác",
        "explanation": "Đảm bảo toàn vẹn tham chiếu."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Self Join là kỹ thuật gì?",
        "options": ["Join bảng với chính nó", "Join tự động", "Join không cần ON", "Join bảng hệ thống"],
        "answer": "Join bảng với chính nó",
        "explanation": "Dùng Alias để giả lập 2 bảng khác nhau."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "CASE WHEN tương đương với cấu trúc nào trong lập trình?",
        "options": ["IF - ELSE", "FOR LOOP", "WHILE", "FUNCTION"],
        "answer": "IF - ELSE",
        "explanation": "Rẽ nhánh điều kiện."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Hàm lấy năm từ ngày tháng?",
        "options": ["YEAR()", "GETYEAR()", "Y()", "DATEPART() - tham số year"],
        "answer": "YEAR()",
        "explanation": "Phổ biến nhất là YEAR(date)."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "Constraint CHECK dùng để?",
        "options": ["Kiểm tra điều kiện giá trị", "Kiểm tra khóa chính", "Kiểm tra null", "Kiểm tra kiểu"],
        "answer": "Kiểm tra điều kiện giá trị",
        "explanation": "VD: CHECK (Age >= 18)."
    },
    {
        "difficulty": "medium", "type": "single",
        "question": "SELECT TOP 5 ... tương đương với gì trong MySQL?",
        "options": ["LIMIT 5", "ROWNUM 5", "HEAD 5", "FIRST 5"],
        "answer": "LIMIT 5",
        "explanation": "SQL Server dùng TOP, MySQL dùng LIMIT."
    },

    # --- MEDIUM MULTIPLE CHOICE (15) ---
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Các loại JOIN phổ biến?",
        "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN", "CROSS JOIN"],
        "answer": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN", "CROSS JOIN"],
        "explanation": "Tất cả đều là các loại Join chuẩn."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Sự khác biệt giữa WHERE và HAVING?",
        "options": ["WHERE lọc trước Group By", "HAVING lọc sau Group By", "HAVING dùng được hàm Aggregate", "WHERE dùng được hàm Aggregate"],
        "answer": ["WHERE lọc trước Group By", "HAVING lọc sau Group By", "HAVING dùng được hàm Aggregate"],
        "explanation": "WHERE không thể dùng với Aggregate (VD: SUM(x))."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Các ưu điểm của VIEW?",
        "options": ["Bảo mật (che giấu cột)", "Đơn giản hóa truy vấn phức tạp", "Lưu trữ dữ liệu vật lý (thông thường)", "Tái sử dụng code"],
        "answer": ["Bảo mật (che giấu cột)", "Đơn giản hóa truy vấn phức tạp", "Tái sử dụng code"],
        "explanation": "View thường không lưu dữ liệu (trừ Materialized View)."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Những hàm nào xử lý NULL?",
        "options": ["ISNULL()", "COALESCE()", "NVL()", "IFNULL()", "NULLIF()"],
        "answer": ["ISNULL()", "COALESCE()", "NVL()", "IFNULL()", "NULLIF()"],
        "explanation": "Tùy hệ quản trị nhưng tất cả đều liên quan xử lý NULL."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Chọn phát biểu đúng về UNION và UNION ALL?",
        "options": ["UNION chậm hơn UNION ALL", "UNION loại bỏ trùng", "UNION ALL giữ lại trùng", "UNION ALL nhanh hơn"],
        "answer": ["UNION chậm hơn UNION ALL", "UNION loại bỏ trùng", "UNION ALL giữ lại trùng", "UNION ALL nhanh hơn"],
        "explanation": "UNION tốn chi phí sort/distinct."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Các dạng chuẩn hóa thường gặp?",
        "options": ["1NF", "2NF", "3NF", "BCNF", "XML"],
        "answer": ["1NF", "2NF", "3NF", "BCNF"],
        "explanation": "XML là định dạng dữ liệu."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Subquery có thể nằm ở đâu?",
        "options": ["Trong SELECT", "Trong FROM", "Trong WHERE", "Trong GROUP BY (ít gặp nhưng có thể)"],
        "answer": ["Trong SELECT", "Trong FROM", "Trong WHERE"],
        "explanation": "Phổ biến nhất là 3 vị trí này."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Để sao chép dữ liệu từ bảng A sang bảng B?",
        "options": ["INSERT INTO B SELECT * FROM A", "SELECT * INTO B FROM A (SQL Server)", "COPY A TO B", "MOVE A TO B"],
        "answer": ["INSERT INTO B SELECT * FROM A", "SELECT * INTO B FROM A (SQL Server)"],
        "explanation": "Cấu trúc INSERT ... SELECT hoặc SELECT ... INTO."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Thuộc tính của Transaction?",
        "options": ["Atomic", "Consistent", "Isolated", "Durable"],
        "answer": ["Atomic", "Consistent", "Isolated", "Durable"],
        "explanation": "ACID."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Các hàm ngày tháng thông dụng?",
        "options": ["DATEDIFF", "DATEADD", "DAY", "MONTH", "YEAR"],
        "answer": ["DATEDIFF", "DATEADD", "DAY", "MONTH", "YEAR"],
        "explanation": "Dùng tính toán thời gian."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Lệnh nào liên quan đến quyền hạn (Security)?",
        "options": ["GRANT", "REVOKE", "DENY", "ALLOW"],
        "answer": ["GRANT", "REVOKE", "DENY"],
        "explanation": "ALLOW không phải từ khóa chuẩn (thường là GRANT)."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Ràng buộc 'Referential Integrity' liên quan đến?",
        "options": ["Foreign Key", "Primary Key", "Mối quan hệ cha-con", "Check"],
        "answer": ["Foreign Key", "Primary Key", "Mối quan hệ cha-con"],
        "explanation": "Đảm bảo tham chiếu hợp lệ giữa các bảng."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Trường hợp nào không dùng được Index?",
        "options": ["Cột có độ phân tán thấp (VD: Giới tính)", "Tìm kiếm với '%abc'", "Cột quá nhỏ", "Luôn dùng được"],
        "answer": ["Cột có độ phân tán thấp (VD: Giới tính)", "Tìm kiếm với '%abc'", "Cột quá nhỏ"],
        "explanation": "Index không hiệu quả trong các trường hợp này."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "Các kiểu dữ liệu lưu thời gian?",
        "options": ["DATE", "TIME", "DATETIME", "TIMESTAMP", "YEAR"],
        "answer": ["DATE", "TIME", "DATETIME", "TIMESTAMP"],
        "explanation": "YEAR chỉ lưu năm (MySQL)."
    },
    {
        "difficulty": "medium", "type": "multiple",
        "question": "CROSS JOIN tạo ra cái gì?",
        "options": ["Tích Đề-các", "Cartesian Product", "Mỗi dòng A ghép mọi dòng B", "Giao của A và B"],
        "answer": ["Tích Đề-các", "Cartesian Product", "Mỗi dòng A ghép mọi dòng B"],
        "explanation": "Số dòng = N(A) * N(B)."
    },

    # ======================================================================================
    # HARD (20 Questions)
    # Target: 10 Single Choice, 10 Multiple Choice
    # Points: 3
    # ======================================================================================

    # --- HARD SINGLE CHOICE (10) ---
    {
        "difficulty": "hard", "type": "single",
        "question": "Trigger được kích hoạt khi nào?",
        "options": ["Khi có sự kiện INSERT/UPDATE/DELETE", "Khi người dùng đăng nhập", "Lúc 12h đêm", "Khi tạo bảng"],
        "answer": "Khi có sự kiện INSERT/UPDATE/DELETE",
        "explanation": "Trigger gắn liền với sự kiện thay đổi dữ liệu bảng."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "Stored Procedure khác Function điểm nào cơ bản?",
        "options": ["Procedure không bắt buộc trả về giá trị, Function bắt buộc", "Procedure chậm hơn", "Function có thể gọi Execute", "Không khác"],
        "answer": "Procedure không bắt buộc trả về giá trị, Function bắt buộc",
        "explanation": "Function phải return, SP có thể không."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "Deadlock là gì?",
        "options": ["Hai tiến trình chờ nhau giải phóng tài nguyên", "Lỗi mất mạng", "Server chết", "Khóa bảng vĩnh viễn"],
        "answer": "Hai tiến trình chờ nhau giải phóng tài nguyên",
        "explanation": "Vòng tròn chờ đợi (Circular Wait)."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "Isolation Level cao nhất là gì?",
        "options": ["Serializable", "Read Committed", "Read Uncommitted", "Repeatable Read"],
        "answer": "Serializable",
        "explanation": "Đảm bảo an toàn nhất nhưng chậm nhất."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "SQL Injection là tấn công vào đâu?",
        "options": ["Lớp ứng dụng (Input đầu vào)", "Mạng", "Server vật lý", "Hệ điều hành"],
        "answer": "Lớp ứng dụng (Input đầu vào)",
        "explanation": "Chèn mã SQL vào input form."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "Bảng `INSERTED` trong Trigger chứa gì?",
        "options": ["Dữ liệu mới (New)", "Dữ liệu cũ (Old)", "Tất cả bảng", "Không có gì"],
        "answer": "Dữ liệu mới (New)",
        "explanation": "Chứa dòng vừa insert hoặc update (giá trị mới)."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "Lệnh ROLLBACK chỉ hoạt động khi nào?",
        "options": ["Trong một Transaction chưa Commit", "Bất cứ lúc nào", "Sau khi Commit", "Khi tắt máy"],
        "answer": "Trong một Transaction chưa Commit",
        "explanation": "Transaction phải đang active."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "Index Clustered khác Non-Clustered như thế nào?",
        "options": ["Clustered sắp xếp vật lý dữ liệu, Non-Clustered là con trỏ", "Clustered chậm hơn", "Non-Clustered là chính", "Giống nhau"],
        "answer": "Clustered sắp xếp vật lý dữ liệu, Non-Clustered là con trỏ",
        "explanation": "Mỗi bảng chỉ có 1 Clustered Index."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "Pivot Table trong SQL dùng để làm gì?",
        "options": ["Chuyển hàng thành cột", "Chuyển cột thành hàng", "Gom nhóm", "Sắp xếp"],
        "answer": "Chuyển hàng thành cột",
        "explanation": "Xoay dữ liệu để báo cáo."
    },
    {
        "difficulty": "hard", "type": "single",
        "question": "CTE (Common Table Expression) được định nghĩa bằng từ khóa?",
        "options": ["WITH", "LET", "DEFINE", "SET"],
        "answer": "WITH",
        "explanation": "WITH cte_name AS (...)."
    },

    # --- HARD MULTIPLE CHOICE (10) ---
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Những các phòng chống SQL Injection?",
        "options": ["Dùng Parameterized Queries (Prepared Statements)", "Validate Input", "Dùng ORM", "Tắt Database", "Nối chuỗi cẩn thận"],
        "answer": ["Dùng Parameterized Queries (Prepared Statements)", "Validate Input", "Dùng ORM"],
        "explanation": "Không bao giờ được nối chuỗi trực tiếp từ input user."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Các tính chất của ACID?",
        "options": ["Atomicity (Nguyên tử)", "Consistency (Nhất quán)", "Isolation (Cô lập)", "Durability (Bền vững)", "Availablity"],
        "answer": ["Atomicity (Nguyên tử)", "Consistency (Nhất quán)", "Isolation (Cô lập)", "Durability (Bền vững)"],
        "explanation": "Availability là của CAP theorem."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Trigger có thể dùng để làm gì?",
        "options": ["Kiểm tra ràng buộc phức tạp", "Ghi log lịch sử (Audit)", "Tự động cập nhật bảng liên quan", "Tạo giao diện"],
        "answer": ["Kiểm tra ràng buộc phức tạp", "Ghi log lịch sử (Audit)", "Tự động cập nhật bảng liên quan"],
        "explanation": "Trigger chạy ngầm trong database layer."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Các mức độ cô lập (Isolation Levels)?",
        "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable", "Read Only"],
        "answer": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
        "explanation": "Các mức chuẩn của SQL."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Lợi ích của Stored Procedure?",
        "options": ["Giảm traffic mạng", "Plan được cache (Hiệu suất)", "Bảo mật (Cấp quyền trên SP)", "Dễ debug hơn code app"],
        "answer": ["Giảm traffic mạng", "Plan được cache (Hiệu suất)", "Bảo mật (Cấp quyền trên SP)"],
        "explanation": "Debug SP thường khó hơn code App, nhưng hiệu suất tốt hơn."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Khi nào nên dùng Index?",
        "options": ["Cột hay dùng trong WHERE", "Cột hay dùng trong JOIN", "Khóa ngoại", "Bảng rất nhỏ", "Cột update liên tục"],
        "answer": ["Cột hay dùng trong WHERE", "Cột hay dùng trong JOIN", "Khóa ngoại"],
        "explanation": "Bảng nhỏ hoặc update nhiều thì Index gây chậm."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Recursive CTE dùng để làm gì?",
        "options": ["Truy vấn dữ liệu phân cấp (Cây)", "Tính giai thừa", "Quy hoạch động", "Vòng lặp vô hạn"],
        "answer": ["Truy vấn dữ liệu phân cấp (Cây)", "Tính giai thừa"],
        "explanation": "Duyệt cây cha-con."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Các loại Window Function phổ biến?",
        "options": ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "NTILE()", "GROUP()"],
        "answer": ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "NTILE()"],
        "explanation": "Dùng để xếp hạng và phân tích trượt."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Dirty Read xây ra ở mức Isolation nào?",
        "options": ["Read Uncommitted", "Read Committed", "Serializable", "Repeatable Read"],
        "answer": ["Read Uncommitted"],
        "explanation": "Đọc dữ liệu chưa được commit."
    },
    {
        "difficulty": "hard", "type": "multiple",
        "question": "Lệnh MERGE dùng để làm gì?",
        "options": ["Thực hiện đồng thời Insert/Update/Delete", "Trộn 2 bảng", "Upsert", "Xóa bảng"],
        "answer": ["Thực hiện đồng thời Insert/Update/Delete", "Upsert"],
        "explanation": "Hợp nhất dữ liệu nguồn vào đích."
    }
]
