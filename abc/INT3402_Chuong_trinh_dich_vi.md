HỌC PHẦN: CHƯƠNG TRÌNH DỊCH
# các giảng viên học phần: chương trình dịch - compilers ngành công nghệ thông tin
Tên giảng viên: Nguyễn Phương Thái, chức danh: TS, chuyên ngành: Khoa học máy tính, đơn vị: Trường ĐHCN
Tên giảng viên: Nguyễn Văn Vinh, chức danh: TS, chuyên ngành: Khoa học máy tính, đơn vị: Trường ĐHCN
# 2. thông tin chung về học phần: chương trình dịch 
Tên học phần:
Tiếng Việt: Chương trình dịch Tiếng Anh: Compilers
Mã số học phần: INT3402 Số tín chỉ: 3 Giờ tín chỉ đối với các hoạt động (LTThHTH): 4500 Học phần tiên quyết (tên và mã số học phần): INT2210 Cấu trúc dữ liệu và giải thuật Các yêu cầu đối với học phần (nếu có): Bộ môn Khoa phụ trách học phần: Bộ môn KHMT Khoa CNTT
# 3. mục tiêu học phần: chương trình dịch
Môn học giúp sinh viên hiểu vai trò của chương trình dịch trong phát triển phần mềm. Hiểu biết về chương trình dịch giúp sinh viên có thể lựa chọn và làm chủ tốt hơn ngôn ngữ lập trình môi trường và công cụ lập trình. Sinh viên có khả năng nhận biết được các bài toán có thể giải quyết bằng kỹ thuật chương trình dịch. Sinh viên cũng có thể tự xây dựng được một chương trình dịch sử dụng các công cụ trợ giúp sẵn có.
# 5. tóm tắt nội dung học phần: chương trình dịch
Trước tiên sinh viên sẽ được giới thiệu về ý nghĩa của môn học quan hệ của nó với các môn học khác trong chương trình đào tạo và một số vị trí công việc thực tế cần kiến thức chương trình dịch. Sau đó sinh viên sẽ được học lý thuyết chung về chương trình dịch bao gồm: cấu trúc chương trình dịch các thuật toán các phương pháp cơ bản để xây dựng nên các thành phần một chương trình dịch. Cụ thể là: Biểu diễn từ vựng sử dụng biểu thức chính qui và phân tích từ vựng sử dụng otomat hữu hạn trạng thái Biểu diễn cú pháp ngôn ngữ lập trình bằng văn phạm phi ngữ cảnh và phân tích cú pháp bằng các thuật toán LL LR Kỹ thuật dịch cú pháp điều khiển Phân tích ngữ nghĩa dựa vào cú pháp điều khiển Sinh mã trung gian ở dạng biểu diễn 3 địa chỉ Một số vấn đề về sinh mã đích Sinh viên cũng được hướng dẫn để thực hành xây dựng một số thành phần của chương trình dịch như môđun phân tích từ vựng môđun phân tích cú pháp v.v. với mục tiêu là dịch một ngôn ngữ là biến thể (đơn giản hóa) của C ra ngôn ngữ máy ảo Java (JVM).
# 6. nội dung chi tiết học phần: chương trình dịch
1. Mở đầu
1. Giới thiệu môn học
2. Chương trình dịch: định nghĩa phân loại cấu trúc vị trí
3. Các bước phát triển một dự án chương trình dịch
2. Nhắc lại về ngôn ngữ hình thức
1. Một số khái niệm cơ sở
2. Văn phạm chính qui và Otomat hữu hạn trạng thái
3. Văn phạm phi ngữ cảnh
4. Lược đồ phân loại văn phạm của Chomsky
3. Phân tích từ vựng
1. Vai trò của bộ phân tích từ vựng
2. Từ vị và từ tố
3. Các bước để xây dựng bộ phân tích từ vựng
4. Xây dựng bộ phân tích từ vựng sử dụng JFlex
4. Các phương pháp phân tích cú pháp cơ bản
1. Vai trò của bộ phân tích cú pháp
2. Phân tích Topdown
3. Phân tích Bottomup
5. Các phương pháp phân tích cú pháp hiệu quả
1. Phân tích LL: thuật toán phân tích LL(1) tính FIRST và FOLLOW xây dựng bảng phân tích
2. Phân tích LR SLR: thuật toán phân tích xây dựng bảng phân tích
3. Khôi phục lỗi
4. Xây dựng bộ phân tích cú pháp sử dụng CUP
6. Biên dịch dựa cú pháp
1. Vai trò
2. Cú pháp điều khiển: định nghĩa đồ thị phụ thuộc thứ tự đánh giá thuộc tính
3. Lược đồ dịch
4. Cú pháp điều khiển trong phân tích LL và LR
7. Phân tích ngữ nghĩa
1. Vai trò của phân tích ngữ nghĩa
2. Hệ thống kiểu
3. Một số luật kiểm tra kiểu
4. Xây dựng bộ phân tích ngữ nghĩa sử dụng CUP
8. Sinh mã trung gian
1. Vai trò của sinh mã trung gian
2. Các loại mã trung gian
3. Sinh mã ba địa chỉ
4. Máy ảo Java (JVM)
5. Sinh mã máy ảo Java
9. Sinh mã đích
1. Vai trò của sinh mã đích
2. Các loại mã đối tượng
3. Giới thiệu một máy đích ảo
4. Một bộ sinh mã đơn giản
5. Một số ví dụ về tối ưu mã
# 8. hình thức tổ chức dạy học: chương trình dịch
Lịch trình dạy cụ thể: CHƯƠNG TRÌNH DỊCH Tuần Nội dung giảng dạy lý Nội dung sinh viên tự thuyếtthực hành học 1 Giới thiệu về chương Lịch sử phát triển của trình dịch chương trình dịch. 2 Nhắc lại kiến thức về ngôn ngữ hình thức 3 Phân tích từ vựng Kiến trúc một hệ sinh bộ phân tích từ vựng (ví dụ JFlex) 4 Giới thiệu bài tập lớn số Tìm hiểu cách sử dụng 1. JFlex; Viết biểu thức chính qui mô tả từ tố. Bài toán phân tích cú pháp và các phương pháp phân tích cơ bản 5 Phân tích LL 6 Phân tích LL (tiếp) Cách chuyển đổi văn phạm từ dạng EBNF sang BNF. 7 Phân tích LR 8 Phân tích LR (tiếp) Kiến trúc một hệ sinh bộ phân tích cú pháp theo phương pháp LR (ví dụ CUP). 9 Giới thiệu bài tập lớn 2 Tìm hiểu cách sử dụng CUP một công cụ giúp Biên dịch dựa cú pháp sinh bộ phân tích cú pháp tự động 10 Phân tích ngữ nghĩa tĩnh Cách tạo và quản lý bảng ký hiệu. 11 Sinh mã trung gian Một số kỹ thuật tối ưu mã. 12 Sinh mã đích Tập lệnh của một số bộ vi xử lý thực. 13 Tìm hiểu máy ảo Java Một số vấn đề liên quan đến máy ảo Java. 14 Cách viết cú pháp điều Thực hành viết cú pháp khiển sinh mã máy áo điều khiển cho một số Java. thành phần của chương trình. 15 Tổng kết 
