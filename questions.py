questions_list = [
    # --- EASY (50 Questions) ---
    # Database Definitions & Basics
    {"difficulty": "easy", "question": "SQL viết tắt của từ gì?", "options": ["Structured Query Language", "Strong Question Language", "Structured Question List", "Simple Query Language"], "answer": "Structured Query Language", "explanation": "SQL là viết tắt của Structured Query Language (Ngôn ngữ truy vấn có cấu trúc)."},
    {"difficulty": "easy", "question": "Câu lệnh nào dùng để lấy dữ liệu từ cơ sở dữ liệu?", "options": ["SELECT", "GET", "OPEN", "EXTRACT"], "answer": "SELECT", "explanation": "SELECT là câu lệnh dùng để truy vấn dữ liệu."},
    {"difficulty": "easy", "question": "Câu lệnh nào dùng để cập nhật dữ liệu trong bảng?", "options": ["UPDATE", "SAVE", "MODIFY", "SAVE AS"], "answer": "UPDATE", "explanation": "UPDATE được dùng để thay đổi dữ liệu đã tồn tại."},
    {"difficulty": "easy", "question": "Câu lệnh nào dùng để xóa dữ liệu ra khỏi bảng?", "options": ["DELETE", "REMOVE", "COLLAPSE", "DROP"], "answer": "DELETE", "explanation": "DELETE dùng để xóa các hàng dữ liệu."},
    {"difficulty": "easy", "question": "Câu lệnh nào dùng để thêm dữ liệu mới vào bảng?", "options": ["INSERT INTO", "ADD RECORD", "ADD NEW", "INSERT NEW"], "answer": "INSERT INTO", "explanation": "INSERT INTO dùng để chèn hàng mới vào bảng."},
    {"difficulty": "easy", "question": "Câu lệnh nào dùng để tạo một bảng mới?", "options": ["CREATE TABLE", "MAKE TABLE", "NEW TABLE", "ADD TABLE"], "answer": "CREATE TABLE", "explanation": "CREATE TABLE dùng để định nghĩa một bảng mới."},
    {"difficulty": "easy", "question": "Câu lệnh nào dùng để xóa hoàn toàn một bảng?", "options": ["DROP TABLE", "DELETE TABLE", "REMOVE TABLE", "CLEAR TABLE"], "answer": "DROP TABLE", "explanation": "DROP TABLE xóa cả cấu trúc và dữ liệu của bảng."},
    {"difficulty": "easy", "question": "Mệnh đề nào trong SELECT dùng để lọc điều kiện?", "options": ["WHERE", "HAVING", "FILTER", "WHEN"], "answer": "WHERE", "explanation": "WHERE dùng để lọc các bản ghi thỏa mãn điều kiện."},
    {"difficulty": "easy", "question": "Toán tử nào so sánh bằng trong SQL?", "options": ["=", "==", "===", "EQUALS"], "answer": "=", "explanation": "Trong SQL chuẩn, dấu = dùng để so sánh bằng."},
    {"difficulty": "easy", "question": "Từ khóa nào trả về các giá trị không trùng lặp?", "options": ["DISTINCT", "UNIQUE", "DIFFERENT", "SINGLE"], "answer": "DISTINCT", "explanation": "SELECT DISTINCT trả về các giá trị duy nhất."},
    
    # Data Types & Constraints
    {"difficulty": "easy", "question": "Kiểu dữ liệu nào lưu trữ số nguyên?", "options": ["INT", "CHAR", "VARCHAR", "DATE"], "answer": "INT", "explanation": "INT (Integer) dùng lưu số nguyên."},
    {"difficulty": "easy", "question": "Kiểu dữ liệu VARCHAR(255) nghĩa là gì?", "options": ["Chuỗi ký tự độ dài tối đa 255", "Chuỗi ký tự độ dài cố định 255", "Số nguyên tối đa 255", "Ngày tháng năm"], "answer": "Chuỗi ký tự độ dài tối đa 255", "explanation": "VARCHAR là chuỗi ký tự độ dài thay đổi, tối đa là tham số truyền vào."},
    {"difficulty": "easy", "question": "Ràng buộc nào đảm bảo cột không được để trống?", "options": ["NOT NULL", "UNIQUE", "PRIMARY KEY", "CHECK"], "answer": "NOT NULL", "explanation": "NOT NULL bắt buộc cột phải có giá trị."},
    {"difficulty": "easy", "question": "Khóa chính (Primary Key) có đặc điểm gì?", "options": ["Duy nhất và không NULL", "Có thể trùng lặp", "Có thể NULL", "Chỉ là số nguyên"], "answer": "Duy nhất và không NULL", "explanation": "Primary Key định danh duy nhất mỗi hàng và không được NULL."},
    {"difficulty": "easy", "question": "Để chọn tất cả các cột trong bảng, ta dùng ký tự nào?", "options": ["*", "%", "ALL", "#"], "answer": "*", "explanation": "SELECT * FROM ... lấy tất cả các cột."},
    
    # More Basic Operations
    {"difficulty": "easy", "question": "Câu lệnh nào dùng để sắp xếp kết quả?", "options": ["ORDER BY", "SORT BY", "ARRANGE BY", "GROUP BY"], "answer": "ORDER BY", "explanation": "ORDER BY dùng để sắp xếp kết quả truy vấn."},
    {"difficulty": "easy", "question": "Mặc định ORDER BY sắp xếp theo thứ tự nào?", "options": ["Tăng dần (ASC)", "Giảm dần (DESC)", "Ngẫu nhiên", "Theo ID"], "answer": "Tăng dần (ASC)", "explanation": "Mặc định là ASC (Ascending)."},
    {"difficulty": "easy", "question": "Để sắp xếp giảm dần, ta dùng từ khóa nào?", "options": ["DESC", "ASC", "DOWN", "DEC"], "answer": "DESC", "explanation": "DESC viết tắt của Descending."},
    {"difficulty": "easy", "question": "Toán tử nào dùng kiểm tra giá trị nằm trong danh sách?", "options": ["IN", "BETWEEN", "LIKE", "EXISTS"], "answer": "IN", "explanation": "IN (a, b, c) kiểm tra giá trị có nằm trong tập hợp không."},
    {"difficulty": "easy", "question": "Toán tử nào dùng kiểm tra giá trị trong khoảng?", "options": ["BETWEEN", "IN", "AHONG", "WITHIN"], "answer": "BETWEEN", "explanation": "BETWEEN val1 AND val2."},

    # Logic & Syntax
    {"difficulty": "easy", "question": "Điều kiện nào đúng khi cả A và B đều đúng?", "options": ["AND", "OR", "XOR", "NOT"], "answer": "AND", "explanation": "AND yêu cầu cả 2 vế đều đúng."},
    {"difficulty": "easy", "question": "Điều kiện nào đúng khi A hoặc B đúng?", "options": ["OR", "AND", "NOR", "NOT"], "answer": "OR", "explanation": "OR chỉ cần ít nhất 1 vế đúng."},
    {"difficulty": "easy", "question": "Để tìm tên bắt đầu bằng 'A', ta dùng LIKE như thế nào?", "options": ["LIKE 'A%'", "LIKE '%A'", "LIKE 'A_'", "LIKE '%A%'"], "answer": "LIKE 'A%'", "explanation": "% đại diện cho chuỗi ký tự bất kỳ phía sau."},
    {"difficulty": "easy", "question": "Ký tự đại diện cho 1 ký tự đơn lẻ trong LIKE là gì?", "options": ["_", "%", "?", "*"], "answer": "_", "explanation": "Dấu gạch dưới (_) đại diện cho đúng 1 ký tự."},
    {"difficulty": "easy", "question": "SQL comment một dòng bắt đầu bằng ký tự nào (thông dụng)?", "options": ["--", "//", "/*", "#"], "answer": "--", "explanation": "-- là chuẩn comment 1 dòng trong SQL."},
    
    # More Easy Questions
    {"difficulty": "easy", "question": "Hàm COUNT() dùng để làm gì?", "options": ["Đếm số lượng hàng", "Tính tổng", "Tính trung bình", "Tìm max"], "answer": "Đếm số lượng hàng", "explanation": "COUNT đếm số bản ghi."},
    {"difficulty": "easy", "question": "Hàm SUM() dùng để làm gì?", "options": ["Tính tổng giá trị", "Đếm số dòng", "Tính trung bình", "Nối chuỗi"], "answer": "Tính tổng giá trị", "explanation": "SUM tính tổng giá trị của cột số."},
    {"difficulty": "easy", "question": "Hàm MAX() trả về cái gì?", "options": ["Giá trị lớn nhất", "Giá trị nhỏ nhất", "Giá trị trung bình", "Số lượng"], "answer": "Giá trị lớn nhất", "explanation": "MAX tìm giá trị lớn nhất."},
    {"difficulty": "easy", "question": "Hàm MIN() trả về cái gì?", "options": ["Giá trị nhỏ nhất", "Giá trị lớn nhất", "Tổng", "Trung bình"], "answer": "Giá trị nhỏ nhất", "explanation": "MIN tìm giá trị nhỏ nhất."},
    {"difficulty": "easy", "question": "Hàm AVG() dùng để làm gì?", "options": ["Tính trung bình cộng", "Tính tổng", "Đếm số lượng", "Làm tròn"], "answer": "Tính trung bình cộng", "explanation": "AVG viết tắt của Average."},

    # Tables & Databases
    {"difficulty": "easy", "question": "Lệnh TRUNCATE TABLE làm gì?", "options": ["Xóa hết dữ liệu nhưng giữ cấu trúc", "Xóa bảng hoàn toàn", "Xóa cột", "Sao chép bảng"], "answer": "Xóa hết dữ liệu nhưng giữ cấu trúc", "explanation": "TRUNCATE nhanh hơn DELETE và reset lại bảng."},
    {"difficulty": "easy", "question": "Lệnh ALTER TABLE dùng để làm gì?", "options": ["Sửa đổi cấu trúc bảng", "Thêm dữ liệu", "Xóa bảng", "Tạo database"], "answer": "Sửa đổi cấu trúc bảng", "explanation": "ALTER TABLE dùng để thêm/sửa/xóa cột."},
    {"difficulty": "easy", "question": "Để thêm cột mới vào bảng, dùng lệnh nào?", "options": ["ALTER TABLE ... ADD", "UPDATE TABLE ... ADD", "INSERT COLUMN", "MODIFY TABLE"], "answer": "ALTER TABLE ... ADD", "explanation": "Cú pháp: ALTER TABLE table_name ADD column_name type."},
    {"difficulty": "easy", "question": "Để xóa cột khỏi bảng, dùng lệnh nào?", "options": ["ALTER TABLE ... DROP COLUMN", "DELETE COLUMN", "REMOVE COLUMN", "DROP COLUMN"], "answer": "ALTER TABLE ... DROP COLUMN", "explanation": "Cú pháp xóa cột trong bảng."},
    {"difficulty": "easy", "question": "Khóa ngoại (Foreign Key) dùng để làm gì?", "options": ["Liên kết các bảng với nhau", "Tăng tốc độ tìm kiếm", "Đảm bảo dữ liệu duy nhất", "Đặt tên cột"], "answer": "Liên kết các bảng với nhau", "explanation": "Foreign Key tham chiếu đến Primary Key của bảng khác."},

    # Misc Easy
    {"difficulty": "easy", "question": "NULL trong SQL nghĩa là gì?", "options": ["Giá trị rỗng hoặc không xác định", "Số 0", "Chuỗi rỗng", "False"], "answer": "Giá trị rỗng hoặc không xác định", "explanation": "NULL đại diện cho thiếu dữ liệu."},
    {"difficulty": "easy", "question": "Để kiểm tra giá trị NULL, dùng toán tử nào?", "options": ["IS NULL", "= NULL", "== NULL", "HAS NULL"], "answer": "IS NULL", "explanation": "Không thể dùng = với NULL, phải dùng IS NULL."},
    {"difficulty": "easy", "question": "Cú pháp đúng để chọn cột 'Name' từ bảng 'Users'?", "options": ["SELECT Name FROM Users", "EXTRACT Name FROM Users", "GET Name Users", "SELECT Users.Name"], "answer": "SELECT Name FROM Users", "explanation": "Cú pháp chuẩn SELECT column FROM table."},
    {"difficulty": "easy", "question": "AS trong SQL dùng để làm gì?", "options": ["Đặt bí danh (ALIAS)", "So sánh", "Gán giá trị", "Tạo bảng"], "answer": "Đặt bí danh (ALIAS)", "explanation": "AS dùng đặt tên tạm thời cho cột hoặc bảng."},
    {"difficulty": "easy", "question": "Dấu ; cuối câu lệnh SQL có ý nghĩa gì?", "options": ["Kết thúc câu lệnh", "Bắt đầu câu lệnh", "Comment", "Không có ý nghĩa"], "answer": "Kết thúc câu lệnh", "explanation": "Dấu chấm phẩy ngăn cách các câu lệnh."},

    # Finishing Easy (41-50)
    {"difficulty": "easy", "question": "Cơ sở dữ liệu quan hệ (RDBMS) tổ chức dữ liệu dưới dạng nào?", "options": ["Bảng (Table)", "Cây (Tree)", "Đồ thị (Graph)", "Danh sách (List)"], "answer": "Bảng (Table)", "explanation": "RDBMS lưu dữ liệu trong các bảng có hàng và cột."},
    {"difficulty": "easy", "question": "SQL có phân biệt chữ hoa thường với từ khóa không?", "options": ["Không (thường là vậy)", "Có", "Tùy hệ điều hành", "Chỉ với tên bảng"], "answer": "Không (thường là vậy)", "explanation": "Từ khóa như SELECT, FROM thường không phân biệt hoa thường."},
    {"difficulty": "easy", "question": "Để chọn tất cả bản ghi mà cột City là 'Hanoi' hoặc 'HCM'?", "options": ["WHERE City IN ('Hanoi', 'HCM')", "WHERE City = 'Hanoi' AND City = 'HCM'", "WHERE City LIKE 'H%'", "WHERE City BETWEEN 'Hanoi' AND 'HCM'"], "answer": "WHERE City IN ('Hanoi', 'HCM')", "explanation": "IN dùng để chọn giá trị trong danh sách liệt kê."},
    {"difficulty": "easy", "question": "NOT trong SQL dùng để làm gì?", "options": ["Đảo ngược điều kiện logic", "Xóa bảng", "Tạo bảng", "Thêm dữ liệu"], "answer": "Đảo ngược điều kiện logic", "explanation": "Ví dụ WHERE NOT condition."},
    {"difficulty": "easy", "question": "Mệnh đề FROM xác định điều gì?", "options": ["Bảng chứa dữ liệu cần lấy", "Cột cần lấy", "Điều kiện lọc", "Thứ tự sắp xếp"], "answer": "Bảng chứa dữ liệu cần lấy", "explanation": "FROM table_name."},
    {"difficulty": "easy", "question": "LIKE '%a' sẽ khớp với chuỗi nào?", "options": ["Banana", "Apple", "Bread", "Car"], "answer": "Banana", "explanation": "%a nghĩa là kết thúc bằng 'a'."},
    {"difficulty": "easy", "question": "LIKE 'a%' sẽ khớp với chuỗi nào?", "options": ["Apple", "Banana", "Bread", "Car"], "answer": "Apple", "explanation": "a% nghĩa là bắt đầu bằng 'a'."},
    {"difficulty": "easy", "question": "Mệnh đề SET dùng trong câu lệnh nào?", "options": ["UPDATE", "INSERT", "SELECT", "DELETE"], "answer": "UPDATE", "explanation": "UPDATE table SET col=val."},
    {"difficulty": "easy", "question": "Mệnh đề VALUES dùng trong câu lệnh nào?", "options": ["INSERT INTO", "UPDATE", "SELECT", "ALTER"], "answer": "INSERT INTO", "explanation": "INSERT INTO table VALUES (...)."},
    {"difficulty": "easy", "question": "Câu lệnh tạo cơ sở dữ liệu mới?", "options": ["CREATE DATABASE dbname", "NEW DATABASE dbname", "ADD DATABASE dbname", "INIT DATABASE dbname"], "answer": "CREATE DATABASE dbname", "explanation": "Cú pháp chuẩn để tạo DB."},

    # --- MEDIUM (30 Questions) ---
    # Joins
    {"difficulty": "medium", "question": "Loại JOIN trả về dữ liệu khớp ở cả 2 bảng?", "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"], "answer": "INNER JOIN", "explanation": "INNER JOIN chỉ lấy các bản ghi có khóa tương ứng ở cả hai bảng."},
    {"difficulty": "medium", "question": "LEFT JOIN trả về gì?", "options": ["Tất cả từ bảng trái, và khớp từ bảng phải", "Tất cả từ bảng phải", "Chỉ phần giao nhau", "Tất cả 2 bảng"], "answer": "Tất cả từ bảng trái, và khớp từ bảng phải", "explanation": "LEFT JOIN ưu tiên bảng bên trái (bảng FROM)."},
    {"difficulty": "medium", "question": "RIGHT JOIN trả về gì?", "options": ["Tất cả từ bảng phải, và khớp từ bảng trái", "Tất cả từ bảng trái", "Chỉ phần giao nhau", "Tất cả 2 bảng"], "answer": "Tất cả từ bảng phải, và khớp từ bảng trái", "explanation": "RIGHT JOIN ưu tiên bảng bên phải (bảng sau từ khóa JOIN)."},
    {"difficulty": "medium", "question": "FULL OUTER JOIN trả về gì?", "options": ["Tất cả dữ liệu từ cả 2 bảng", "Chỉ dữ liệu khớp", "Dữ liệu bên trái", "Dữ liệu bên phải"], "answer": "Tất cả dữ liệu từ cả 2 bảng", "explanation": "Kết hợp kết quả của cả LEFT và RIGHT JOIN."},
    {"difficulty": "medium", "question": "Khi JOIN mà không có điều kiện ON, chuyện gì xảy ra?", "options": ["Tích Đề-các (Cartesian Product)", "Lỗi cú pháp", "Inner Join", "Không có dữ liệu trả về"], "answer": "Tích Đề-các (Cartesian Product)", "explanation": "Mỗi hàng bảng A sẽ ghép với mọi hàng bảng B."},

    # Group By & Aggregation
    {"difficulty": "medium", "question": "Mệnh đề GROUP BY thường dùng với các hàm nào?", "options": ["Hàm tổng hợp (COUNT, MAX, SUM)", "Hàm xử lý chuỗi", "Hàm ngày tháng", "Toán tử logic"], "answer": "Hàm tổng hợp (COUNT, MAX, SUM)", "explanation": "GROUP BY gom nhóm dữ liệu để tính toán tổng hợp."},
    {"difficulty": "medium", "question": "Để lọc dữ liệu SAU khi đã GROUP BY, ta dùng mệnh đề nào?", "options": ["HAVING", "WHERE", "FILTER", "LIMIT"], "answer": "HAVING", "explanation": "WHERE lọc trước khi gom nhóm, HAVING lọc sau khi gom nhóm."},
    {"difficulty": "medium", "question": "SELECT Department, COUNT(*) FROM Employees ... cần thêm gì?", "options": ["GROUP BY Department", "ORDER BY Department", "WHERE Department", "HAVING Count"], "answer": "GROUP BY Department", "explanation": "Mọi cột không phải hàm tổng hợp trong SELECT đều phải có trong GROUP BY."},
    
    # Text & Date Functions
    {"difficulty": "medium", "question": "Hàm nào dùng để nối chuỗi trong SQL Server/Standard?", "options": ["CONCAT()", "JOIN()", "MERGE()", "ADD()"], "answer": "CONCAT()", "explanation": "CONCAT(str1, str2) nối các chuỗi lại."},
    {"difficulty": "medium", "question": "Để lấy ngày giờ hiện tại trong SQL Server, dùng hàm nào?", "options": ["GETDATE()", "NOW()", "CURDATE()", "TODAY()"], "answer": "GETDATE()", "explanation": "GETDATE() trả về ngày giờ hiện tại hệ thống."},
    {"difficulty": "medium", "question": "Hàm LEN() (hoặc LENGTH) trả về gì?", "options": ["Độ dài của chuỗi ký tự", "Số từ trong chuỗi", "Kích thước byte", "Số cột"], "answer": "Độ dài của chuỗi ký tự", "explanation": "Trả về số ký tự trong chuỗi."},
    {"difficulty": "medium", "question": "Hàm UPPER() làm gì?", "options": ["Chuyển chuỗi thành chữ hoa", "Chuyển chuỗi thành chữ thường", "Viết hoa chữ cái đầu", "Cắt chuỗi"], "answer": "Chuyển chuỗi thành chữ hoa", "explanation": "UPPER('text') -> 'TEXT'."},

    # Contraints & Logic
    {"difficulty": "medium", "question": "Ràng buộc CHECK dùng để làm gì?", "options": ["Giới hạn giá trị của cột theo điều kiện", "Kiểm tra khóa chính", "Kiểm tra bảng tồn tại", "Kiểm tra quyền truy cập"], "answer": "Giới hạn giá trị của cột theo điều kiện", "explanation": "Ví dụ: CHECK (Age >= 18)."},
    {"difficulty": "medium", "question": "Ràng buộc DEFAULT dùng để làm gì?", "options": ["Gán giá trị mặc định nếu không nhập", "Bắt buộc nhập", "Tạo khóa chính", "Tạo index"], "answer": "Gán giá trị mặc định nếu không nhập", "explanation": "Nếu INSERT không có giá trị, DEFAULT sẽ được dùng."},
    {"difficulty": "medium", "question": "Câu lệnh DROP khác DELETE ở điểm nào quan trọng?", "options": ["DROP không thể rollback (trong một số ngữ cảnh) và xóa cấu trúc", "DELETE nhanh hơn", "DROP có mệnh đề WHERE", "DELETE xóa bảng"], "answer": "DROP không thể rollback (trong một số ngữ cảnh) và xóa cấu trúc", "explanation": "DROP là DDL, DELETE là DML. DELETE có thể rollback trong transaction."},
    {"difficulty": "medium", "question": "Để lấy 5 dòng đầu tiên trong SQL Server, dùng từ khóa nào?", "options": ["TOP 5", "LIMIT 5", "ROWNUM <= 5", "HEAD 5"], "answer": "TOP 5", "explanation": "SELECT TOP 5 * FROM ... (SQL Server). MySQL dùng LIMIT."},
    
    # Subqueries and Logic
    {"difficulty": "medium", "question": "Subquery (truy vấn con) là gì?", "options": ["Một câu lệnh SELECT lồng trong câu lệnh khác", "Một bảng phụ", "Một stored procedure", "Một view"], "answer": "Một câu lệnh SELECT lồng trong câu lệnh khác", "explanation": "Subquery thường nằm trong mệnh đề WHERE hoặc FROM."},
    {"difficulty": "medium", "question": "Kết quả của subquery trong mệnh đề WHERE col = (...) phải trả về gì?", "options": ["Một giá trị đơn", "Một bảng", "Nhiều cột", "Không trả về gì"], "answer": "Một giá trị đơn", "explanation": "Nếu dùng dấu '=', subquery chỉ được trả về 1 giá trị duy nhất."},

    # Logic Priority
    {"difficulty": "medium", "question": "Thứ tự thực hiện logic: NOT, AND, OR?", "options": ["NOT -> AND -> OR", "AND -> OR -> NOT", "OR -> AND -> NOT", "Ngang hàng nhau"], "answer": "NOT -> AND -> OR", "explanation": "Độ ưu tiên: NOT cao nhất, sau đó đến AND, cuối cùng là OR."},
    {"difficulty": "medium", "question": "SELECT * FROM A WHERE x=1 AND y=2 OR z=3 được hiểu là?", "options": ["(x=1 AND y=2) OR z=3", "x=1 AND (y=2 OR z=3)", "Tùy trình biên dịch", "Lỗi"], "answer": "(x=1 AND y=2) OR z=3", "explanation": "Do AND có độ ưu tiên cao hơn OR."},
    
    # Updates & Misc
    {"difficulty": "medium", "question": "Nếu UPDATE không có WHERE, điều gì xảy ra?", "options": ["Tất cả các hàng trong bảng đều bị cập nhật", "Lỗi cú pháp", "Chỉ hàng đầu tiên bị cập nhật", "Không có gì xảy ra"], "answer": "Tất cả các hàng trong bảng đều bị cập nhật", "explanation": "Rất nguy hiểm, toàn bộ dữ liệu sẽ bị ghi đè."},
    {"difficulty": "medium", "question": "Nếu DELETE không có WHERE, điều gì xảy ra?", "options": ["Tất cả dữ liệu trong bảng bị xóa", "Lỗi cú pháp", "Xóa bảng", "Bảng bị khóa"], "answer": "Tất cả dữ liệu trong bảng bị xóa", "explanation": "Bảng sẽ trở thành bảng rỗng."},
    {"difficulty": "medium", "question": "UNION khác UNION ALL như thế nào?", "options": ["UNION loại bỏ trùng lặp, UNION ALL lấy tất cả", "UNION nhanh hơn", "UNION ALL loại bỏ trùng lặp", "Không khác nhau"], "answer": "UNION loại bỏ trùng lặp, UNION ALL lấy tất cả", "explanation": "UNION thực hiện bước khử trùng lặp nên chậm hơn UNION ALL."},
    {"difficulty": "medium", "question": "Bảng 'Employees' có cột 'Salary'. Tìm lương cao thứ nhì?", "options": ["Dùng Subquery hoặc Order By Offset", "MAX(Salary)-1", "TOP 2 Salary", "SECOND(Salary)"], "answer": "Dùng Subquery hoặc Order By Offset", "explanation": "Ví dụ: SELECT MAX(Salary) FROM Table WHERE Salary < (SELECT MAX(Salary)...)."},
    {"difficulty": "medium", "question": "Cú pháp INSERT thông dụng nào cho phép chèn nhiều dòng?", "options": ["INSERT INTO ... VALUES (), (), ()", "INSERT MULTIPLE ...", "ADD LINES ...", "Không thể chèn nhiều dòng"], "answer": "INSERT INTO ... VALUES (), (), ()", "explanation": "Các bộ giá trị cách nhau bởi dấu phẩy."},
    {"difficulty": "medium", "question": "Self Join là gì?", "options": ["Một bảng tự join với chính nó", "Join bảng tạm", "Join tự động", "Join không điều kiện"], "answer": "Một bảng tự join với chính nó", "explanation": "Thường dùng để so sánh các dòng trong cùng 1 bảng."},
    {"difficulty": "medium", "question": "Dạng chuẩn 1NF yêu cầu gì?", "options": ["Giá trị trong cột là nguyên tố (atomic), không lặp nhóm", "Có khóa chính", "Không phụ thuộc bắc cầu", "Mọi cột phụ thuộc khóa chính"], "answer": "Giá trị trong cột là nguyên tố (atomic), không lặp nhóm", "explanation": "Mỗi ô chỉ chứa 1 giá trị duy nhất."},
    {"difficulty": "medium", "question": "Dạng chuẩn 2NF yêu cầu gì?", "options": ["Đạt 1NF và các thuộc tính không khóa phụ thuộc hoàn toàn vào khóa chính", "Không có cột null", "Đạt 3NF", "Không có quan hệ n-n"], "answer": "Đạt 1NF và các thuộc tính không khóa phụ thuộc hoàn toàn vào khóa chính", "explanation": "Loại bỏ phụ thuộc một phần vào khóa chính."},
    {"difficulty": "medium", "question": "Dạng chuẩn 3NF yêu cầu gì?", "options": ["Đạt 2NF và không có phụ thuộc bắc cầu", "Đạt BCNF", "Có khóa ngoại", "Tối ưu hiệu suất"], "answer": "Đạt 2NF và không có phụ thuộc bắc cầu", "explanation": "Thuộc tính không khóa không được phụ thuộc vào thuộc tính không khóa khác."},

    # --- HARD (20 Questions) ---
    # Advanced Objects
    {"difficulty": "hard", "question": "Stored Procedure có lợi ích gì chính?", "options": ["Tái sử dụng code, bảo mật, hiệu suất (pre-compiled)", "Lưu trữ dữ liệu rẻ hơn", "Tạo giao diện người dùng", "Tự động backup"], "answer": "Tái sử dụng code, bảo mật, hiệu suất (pre-compiled)", "explanation": "Giảm traffic mạng và tận dụng kế hoạch thực thi cache."},
    {"difficulty": "hard", "question": "View được cập nhật dữ liệu khi nào?", "options": ["Khi truy vấn View (nếu là view thường) hoặc khi bảng gốc đổi (nếu materialized)", "Chỉ khi admin chạy lệnh", "Mỗi 24h", "Không bao giờ cập nhật"], "answer": "Khi truy vấn View (nếu là view thường) hoặc khi bảng gốc đổi (nếu materialized)", "explanation": "View thường là bảng ảo, truy vấn view thực chất là chạy câu lệnh SELECT định nghĩa nó."},
    {"difficulty": "hard", "question": "Trigger là gì?", "options": ["Thủ tục tự động chạy khi có sự kiện Insert/Update/Delete", "Một loại khóa ngoại", "Công cụ lập lịch", "Hàm tính toán"], "answer": "Thủ tục tự động chạy khi có sự kiện Insert/Update/Delete", "explanation": "Dùng để kiểm soát toàn vẹn dữ liệu tự động."},
    {"difficulty": "hard", "question": "Trong Trigger, bảng 'INSERTED' (hoặc NEW) chứa gì?", "options": ["Dữ liệu vừa mới được chèn hoặc cập nhật", "Dữ liệu cũ trước khi xóa", "Toàn bộ bảng", "Không chứa gì"], "answer": "Dữ liệu vừa mới được chèn hoặc cập nhật", "explanation": "Dùng để truy cập giá trị mới trong trigger."},
    {"difficulty": "hard", "question": "Trong Trigger, bảng 'DELETED' (hoặc OLD) chứa gì?", "options": ["Dữ liệu trước khi bị xóa hoặc cập nhật", "Dữ liệu mới", "File backup", "Log hệ thống"], "answer": "Dữ liệu trước khi bị xóa hoặc cập nhật", "explanation": "Dùng để truy cập giá trị cũ."},
    
    # Transactions
    {"difficulty": "hard", "question": "ACID trong Transaction là viết tắt của?", "options": ["Atomicity, Consistency, Isolation, Durability", "Auto, Check, Index, Data", "Add, Create, Insert, Delete", "Access, Control, Interface, Design"], "answer": "Atomicity, Consistency, Isolation, Durability", "explanation": "4 tính chất đảm bảo độ tin cậy của giao dịch."},
    {"difficulty": "hard", "question": "Lệnh ROLLBACK dùng để làm gì?", "options": ["Hủy bỏ transaction, quay về trạng thái trước đó", "Lưu thay đổi vĩnh viễn", "Xóa database", "Tạo bản sao lưu"], "answer": "Hủy bỏ transaction, quay về trạng thái trước đó", "explanation": "Phục hồi dữ liệu nếu transaction gặp lỗi."},
    {"difficulty": "hard", "question": "Lệnh COMMIT dùng để làm gì?", "options": ["Lưu các thay đổi của transaction vĩnh viễn", "Bắt đầu transaction mới", "Hủy bỏ transaction", "Khóa bảng"], "answer": "Lưu các thay đổi của transaction vĩnh viễn", "explanation": "Xác nhận transaction thành công."},
    {"difficulty": "hard", "question": "Transaction giúp đảm bảo tính chất nào của dữ liệu là quan trọng nhất?", "options": ["Tính toàn vẹn (Integrity)", "Tính bảo mật", "Tốc độ", "Dung lượng"], "answer": "Tính toàn vẹn (Integrity)", "explanation": "Đảm bảo dữ liệu không bị lỗi khi có sự cố xảy ra giữa chừng."},
    
    # Indexes
    {"difficulty": "hard", "question": "Index (Chỉ mục) thường được tạo trên các cột nào?", "options": ["Cột thường xuyên dùng trong WHERE hoặc JOIN", "Cột ít khi truy vấn", "Tất cả các cột", "Chỉ cột ký tự"], "answer": "Cột thường xuyên dùng trong WHERE hoặc JOIN", "explanation": "Giúp tăng tốc độ tìm kiếm."},
    {"difficulty": "hard", "question": "Lợi ích chính của Index là gì?", "options": ["Tăng tốc độ truy vấn (SELECT)", "Tăng tốc độ INSERT", "Tiết kiệm dung lượng", "Bảo mật dữ liệu"], "answer": "Tăng tốc độ truy vấn (SELECT)", "explanation": "Giúp tìm kiếm nhanh hơn nhưng làm chậm INSERT/UPDATE/DELETE."},
    
    # Advanced Queries (Replacements)
    {"difficulty": "hard", "question": "Câu lệnh CASE WHEN dùng để làm gì?", "options": ["Thực hiện logic rẽ nhánh (IF-ELSE) trong câu lệnh SQL", "Tạo vòng lặp", "Tạo bảng mới", "Xóa dữ liệu"], "answer": "Thực hiện logic rẽ nhánh (IF-ELSE) trong câu lệnh SQL", "explanation": "Giúp trả về giá trị khác nhau tùy điều kiện."},
    {"difficulty": "hard", "question": "Để lấy dữ liệu từ bảng A nhưng KHÔNG có trong bảng B, ta dùng?", "options": ["LEFT JOIN vói WHERE B.id IS NULL hoặc NOT EXISTS", "INNER JOIN", "CROSS JOIN", "UNION"], "answer": "LEFT JOIN vói WHERE B.id IS NULL hoặc NOT EXISTS", "explanation": "Kỹ thuật tìm bản ghi mồ côi (orphaned records)."},
    {"difficulty": "hard", "question": "Hàm EXISTS trả về giá trị gì?", "options": ["True/False (Có hoặc Không có kết quả)", "Số lượng bản ghi", "Bảng kết quả", "NULL"], "answer": "True/False (Có hoặc Không có kết quả)", "explanation": "Dùng để kiểm tra sự tồn tại của dữ liệu trong subquery."},
    {"difficulty": "hard", "question": "Câu lệnh HAVING khác WHERE ở điểm nào?", "options": ["HAVING lọc trên kết quả tổng hợp (Aggregate), WHERE lọc trên từng dòng", "HAVING chạy trước WHERE", "HAVING chỉ dùng cho UPDATE", "Không khác nhau"], "answer": "HAVING lọc trên kết quả tổng hợp (Aggregate), WHERE lọc trên từng dòng", "explanation": "HAVING đi kèm với GROUP BY."},
    {"difficulty": "hard", "question": "Ràng buộc ON DELETE CASCADE có ý nghĩa gì?", "options": ["Khi xóa cha thì tự động xóa con", "Không cho phép xóa cha", "Xóa cha thì set con về NULL", "Báo lỗi khi xóa"], "answer": "Khi xóa cha thì tự động xóa con", "explanation": "Tự động dọn dẹp dữ liệu liên quan."},
    {"difficulty": "hard", "question": "SELECT * FROM (SELECT ... ) AS T gọi là gì?", "options": ["Derived Table (Bảng dẫn xuất)", "View", "CTE", "Temp Table"], "answer": "Derived Table (Bảng dẫn xuất)", "explanation": "Subquery nằm trong mệnh đề FROM."},
    
    # Logic & Theory
    {"difficulty": "hard", "question": "Vấn đề SQL Injection là gì?", "options": ["Kỹ thuật tấn công chèn mã SQL độc hại vào input", "Lỗi tràn bộ nhớ", "Lỗi kết nối mạng", "Tối ưu hóa sai"], "answer": "Kỹ thuật tấn công chèn mã SQL độc hại vào input", "explanation": "Xảy ra khi nối chuỗi trực tiếp trong ứng dụng thay vì dùng Parameter."},
    {"difficulty": "hard", "question": "Prepared Statement giúp phòng chống lỗi gì?", "options": ["SQL Injection", "Deadlock", "Timeout", "Syntax Error"], "answer": "SQL Injection", "explanation": "Tách biệt mã SQL và dữ liệu."},
    {"difficulty": "hard", "question": "Khóa Composite Key là gì?", "options": ["Khóa chính được tạo thành từ 2 cột trở lên", "Khóa ngoại", "Khóa phụ", "Khóa số nguyên"], "answer": "Khóa chính được tạo thành từ 2 cột trở lên", "explanation": "Dùng khi một cột không đủ để định danh duy nhất."},
    {"difficulty": "hard", "question": "Deadlock là hiện tượng gì?", "options": ["Hai transaction chờ nhau giải phóng tài nguyên, gây tắc nghẽn", "Server bị sập", "Ổ cứng đầy", "Mất kết nối"], "answer": "Hai transaction chờ nhau giải phóng tài nguyên, gây tắc nghẽn", "explanation": "Hệ quản trị CSDL thường sẽ chọn 1 transaction làm nạn nhân (victim) để kill."},
    {"difficulty": "hard", "question": "Câu lệnh REVOKE dùng để làm gì?", "options": ["Thu hồi quyền truy cập", "Cấp quyền", "Xóa user", "Tạo role"], "answer": "Thu hồi quyền truy cập", "explanation": "Ngược lại với GRANT."}
]

questions = questions_list
