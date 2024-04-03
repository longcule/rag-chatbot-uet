HỌC PHẦN: CHƯƠNG TRÌNH DỊCH
1. Thông tin về các giảng viên học phần: CHƯƠNG TRÌNH DỊCH
STT   Họ và tên        Chức danh, học vị   Địa chỉ liên hệ   Điện thoại / Email                                         Ghi chú
--------- -------------------- ----------------------- --------------------- -------------------------------------------------------------- ----------------
1         Nguyễn Phương Thái   PGS.TS                  BM KHMT               [[thainp\@vnu.edu.vn]{.underline}](mailto:thainp@vnu.edu.vn)   Trưởng môn học
2         Nguyễn Văn Vinh      TS                      BM KHMT               [[vinhnv\@vnu.edu.vn]{.underline}](mailto:vinhnv@vnu.edu.vn)   Giảng viên
2. Thông tin chung về học phần: CHƯƠNG TRÌNH DỊCH
-   Tên học phần:
```{=html}
<!-- -->
```
-   Tiếng Việt: Chương trình dịch
-   Tiếng Anh: Compilers
```{=html}
<!-- -->
```
-   Mã số học phần: INT3402
-   Số tín chỉ: 3
-   Giờ tín chỉ đối với các hoạt động (LT/ThH/TH): 45/0/0
-   Học phần tiên quyết (tên và mã số học phần): INT2210 -- Cấu trúc dữ
liệu và giải thuật
-   Các yêu cầu đối với học phần (nếu có):
-   Bộ môn, Khoa phụ trách học phần: Bộ môn KHMT, Khoa CNTT
3. Mục tiêu học phần: CHƯƠNG TRÌNH DỊCH
Môn học giúp sinh viên hiểu vai trò của chương trình dịch trong phát
triển phần mềm. Hiểu biết về chương trình dịch giúp sinh viên có thể lựa
chọn và làm chủ tốt hơn ngôn ngữ lập trình, môi trường và công cụ lập
trình. Sinh viên có khả năng nhận biết được các bài toán có thể giải
quyết bằng kỹ thuật chương trình dịch. Sinh viên cũng có thể tự xây dựng
được một chương trình dịch sử dụng các công cụ trợ giúp sẵn có.
4. Chuẩn đầu ra: CHƯƠNG TRÌNH DỊCH
Chuẩn đầu ra học phần:
--------------------------------------------------------------------------------
Mã\                              Nội dung chuẩn đầu ra\
CĐR                              (Bắt đầu bằng động từ theo thang Bloom)
---------------------------------- ---------------------------------------------
Kiến thức
CLO1
CLO...
Kỹ năng
CLO...
CLO...
Mức độ tự chủ và trách nhiệm
CLO...
CLO...
--------------------------------------------------------------------------------
Ma trận liên kết giữa Chuẩn đầu ra học phần (CLO) và Chuẩn đầu ra
chương trình đào tạo (PLO):
Chuẩn đầu ra   CTĐT CNTT   CTĐT KHMT   ...
------------------ --------------- --------------- ------------ ------------ ------------ --
PLO1        PLO2        PLO...   PLO...   PLO...
CLO1               x1
CLO...                             x2
CLO...
Tổng hợp       x1          x2          ....
Ghi chú:
-   Số lượng CLO nên dưới 10
-   Mỗi CLO nên đóng góp vào 1 PLO của mỗi CTĐT. Học phần xuất hiện
> trong nhiều CTĐT thì phải đóng góp vào PLO của các CTĐT đó. Chú ý,
> với các PLO mức trường và mức chung của Khoa thì nên có sự đóng
> góp giống nhau giữa các CTĐT.
-   Chuẩn đầu ra học phần (CLO) đóng góp cho chuẩn đầu ra CTĐT (PLO)
> nào thì ghi mức của CLO theo thang Bloom (căn cứ theo động từ mô
> tả CLO) vào ô tương ứng.
-   Dòng Tổng hợp ghi đóng góp của các CLO cho PLO tương ứng (theo
> giá trị max) và phải khớp với MA TRẬN CĐR của CTĐT.
-   Có thể đặt bảng này vào phần Phụ lục ở cuối đề cương.
5. Tóm tắt nội dung học phần: CHƯƠNG TRÌNH DỊCH
Trước tiên sinh viên sẽ được giới thiệu về ý nghĩa của môn học, quan hệ
của nó với các môn học khác trong chương trình đào tạo và một số vị trí
công việc thực tế cần kiến thức chương trình dịch. Sau đó, sinh viên sẽ
được học lý thuyết chung về chương trình dịch bao gồm: cấu trúc chương
trình dịch, các thuật toán, các phương pháp cơ bản để xây dựng nên các
thành phần một chương trình dịch. Cụ thể là:
-   Biểu diễn từ vựng sử dụng biểu thức chính qui và phân tích từ vựng
> sử dụng otomat hữu hạn trạng thái
-   Biểu diễn cú pháp ngôn ngữ lập trình bằng văn phạm phi ngữ cảnh và
> phân tích cú pháp bằng các thuật toán LL, LR
-   Kỹ thuật dịch cú pháp điều khiển
-   Phân tích ngữ nghĩa dựa vào cú pháp điều khiển
-   Sinh mã trung gian ở dạng biểu diễn 3 địa chỉ
-   Một số vấn đề về sinh mã đích
Sinh viên cũng được hướng dẫn để thực hành xây dựng một số thành phần
của chương trình dịch như mô-đun phân tích từ vựng, mô-đun phân tích cú
pháp, v.v. với mục tiêu là dịch một ngôn ngữ là biến thể (đơn giản hóa)
của C++ ra ngôn ngữ máy ảo Java (JVM).
6. Nội dung chi tiết học phần: CHƯƠNG TRÌNH DỊCH
1.  Mở đầu
1.  Giới thiệu môn học
2.  Chương trình dịch: định nghĩa, phân loại, cấu trúc, vị trí
3.  Các bước phát triển một dự án chương trình dịch
2.  Nhắc lại về ngôn ngữ hình thức
1.  Một số khái niệm cơ sở
2.  Văn phạm chính qui và Otomat hữu hạn trạng thái
3.  Văn phạm phi ngữ cảnh
4.  Lược đồ phân loại văn phạm của Chomsky
3.  Phân tích từ vựng
1.  Vai trò của bộ phân tích từ vựng
2.  Từ vị và từ tố
3.  Các bước để xây dựng bộ phân tích từ vựng
4.  Xây dựng bộ phân tích từ vựng sử dụng JFlex
4.  Các phương pháp phân tích cú pháp cơ bản
1.  Vai trò của bộ phân tích cú pháp
2.  Phân tích Top-down
3.  Phân tích Bottom-up
5.  Các phương pháp phân tích cú pháp hiệu quả
1.  Phân tích LL: thuật toán phân tích LL(1), tính FIRST và FOLLOW,
> xây dựng bảng phân tích
2.  Phân tích LR, SLR: thuật toán phân tích, xây dựng bảng phân tích
3.  Khôi phục lỗi
4.  Xây dựng bộ phân tích cú pháp sử dụng CUP
6.  Biên dịch dựa cú pháp
1.  Vai trò
2.  Cú pháp điều khiển: định nghĩa, đồ thị phụ thuộc, thứ tự đánh
> giá thuộc tính
3.  Lược đồ dịch
4.  Cú pháp điều khiển trong phân tích LL và LR
7.  Phân tích ngữ nghĩa
1.  Vai trò của phân tích ngữ nghĩa
2.  Hệ thống kiểu
3.  Một số luật kiểm tra kiểu
4.  Xây dựng bộ phân tích ngữ nghĩa sử dụng CUP
8.  Sinh mã trung gian
1.  Vai trò của sinh mã trung gian
2.  Các loại mã trung gian
3.  Sinh mã ba địa chỉ
4.  Máy ảo Java (JVM)
5.  Sinh mã máy ảo Java
9.  Sinh mã đích
1.  Vai trò của sinh mã đích
2.  Các loại mã đối tượng
3.  Giới thiệu một máy đích ảo
4.  Một bộ sinh mã đơn giản
5.  Một số ví dụ về tối ưu mã
7. Học liệu (Nên dùng các tài liệu từ 2015 trở lại đây) CHƯƠNG TRÌNH DỊCH
-   ### 7.1. Học liệu bắt buộc CHƯƠNG TRÌNH DỊCH
\[1\] Alfred V. Aho, Ravi Sethi, Jeffrey D. Ullman. Compilers:
Principles, Techniques, and Tools. Prentice Hall Publisher. 2007.
\[2\] Phạm Hồng Nguyên. Giáo trình chương trình dịch. NXB ĐHQG Hà Nội.
2009.
7.2 Học liệu tham khảo
\[3\] Keith Cooper, Linda Torczon. Engineering a Compiler. Morgan
Kaufmann Publisher. 2011.
8. Hình thức tổ chức dạy học: CHƯƠNG TRÌNH DỊCH
8.1. Phân bổ lịch trình giảng dạy trong 1 học kỳ (15 tuần): CHƯƠNG TRÌNH DỊCH
-----------------------------------------------------------------------------
+----------------+----------------+----------------+----------------+
| Hình thức    | Số           | Từ tuần ...  | Địa điểm   |
| dạy          | tiết/tuần    | đến tuần ... |                |
|                |                |                | (Giảng       |
|                |                |                | đường, PM,     |
|                |                |                | online)      |
+================+================+================+================+
| Lý thuyết      | 3              | 1-15           | Giảng đường    |
+----------------+----------------+----------------+----------------+
| Thực hành      |                |                | (Vd.Phòng máy/ |
|                |                |                |                |
|                |                |                | Phòng thí      |
|                |                |                | nghiệm)        |
+----------------+----------------+----------------+----------------+
| Tự học bắt     |                |                |                |
| buộc           |                |                |                |
+----------------+----------------+----------------+----------------+
8.2. Lịch trình dạy cụ thể: CHƯƠNG TRÌNH DỊCH
---------------------------------------------
+------------+---------------------------+---------------------------+
| Tuần | Nội dung giảng dạy lý  | Nội dung sinh viên tự  |
|            | thuyết/thực hành       | học                    |
+============+===========================+===========================+
| 1          | Giới thiệu về chương      | Lịch sử phát triển của    |
|            | trình dịch                | chương trình dịch.        |
+------------+---------------------------+---------------------------+
| 2          | Nhắc lại kiến thức về     |                           |
|            | ngôn ngữ hình thức        |                           |
+------------+---------------------------+---------------------------+
| 3          | Phân tích từ vựng         | Kiến trúc một hệ sinh bộ  |
|            |                           | phân tích từ vựng (ví dụ  |
|            |                           | JFlex)                    |
+------------+---------------------------+---------------------------+
| 4          | Giới thiệu bài tập lớn số | Tìm hiểu cách sử dụng     |
|            | 1.                        | JFlex; Viết biểu thức     |
|            |                           | chính qui mô tả từ tố.    |
|            | Bài toán phân tích cú     |                           |
|            | pháp và các phương pháp   |                           |
|            | phân tích cơ bản          |                           |
+------------+---------------------------+---------------------------+
| 5          | Phân tích LL              |                           |
+------------+---------------------------+---------------------------+
| 6          | Phân tích LL (tiếp)       | Cách chuyển đổi văn phạm  |
|            |                           | từ dạng EBNF sang BNF.    |
+------------+---------------------------+---------------------------+
| 7          | Phân tích LR              |                           |
+------------+---------------------------+---------------------------+
| 8          | Phân tích LR (tiếp)       | Kiến trúc một hệ sinh bộ  |
|            |                           | phân tích cú pháp theo    |
|            |                           | phương pháp LR (ví dụ     |
|            |                           | CUP).                     |
+------------+---------------------------+---------------------------+
| 9          | Giới thiệu bài tập lớn 2  | Tìm hiểu cách sử dụng     |
|            |                           | CUP, một công cụ giúp     |
|            | Biên dịch dựa cú pháp     | sinh bộ phân tích cú pháp |
|            |                           | tự động                   |
+------------+---------------------------+---------------------------+
| 10         | Phân tích ngữ nghĩa tĩnh  | Cách tạo và quản lý bảng  |
|            |                           | ký hiệu.                  |
+------------+---------------------------+---------------------------+
| 11         | Sinh mã trung gian        | Một số kỹ thuật tối ưu    |
|            |                           | mã.                       |
+------------+---------------------------+---------------------------+
| 12         | Sinh mã đích              | Tập lệnh của một số bộ vi |
|            |                           | xử lý thực.               |
+------------+---------------------------+---------------------------+
| 13         | Tìm hiểu máy ảo Java      | Một số vấn đề liên quan   |
|            |                           | đến máy ảo Java.          |
+------------+---------------------------+---------------------------+
| 14         | Cách viết cú pháp điều    | Thực hành viết cú pháp    |
|            | khiển sinh mã máy áo      | điều khiển cho một số     |
|            | Java.                     | thành phần của chương     |
|            |                           | trình.                    |
+------------+---------------------------+---------------------------+
| 15         | Tổng kết                  |                           |
+------------+---------------------------+---------------------------+
9. Chính sách đối với học phần và các yêu cầu khác của giảng viên: CHƯƠNG TRÌNH DỊCH
-   Sinh viên nghỉ quá 20% số buổi học lý thuyết (3 buổi học) sẽ không
> được thi cuối kỳ. Mỗi buổi học sẽ có điểm danh.
-   Sinh viên tích cực làm bài tập trên lớp, tham gia thảo luận, trả lời
> câu hỏi (ở lớp hoặc trên diễn đàn của trang web môn học) sẽ được
> xem xét cộng điểm môn học.
-   Với các nội dung liên quan đến lập trình (ví dụ bài tập lớn) nếu
> sinh viên gian lận mã nguồn thì sẽ bị điểm môn học là 0.
10. Phương pháp, hình thức kiểm tra, đánh giá kết quả học tập học phần: CHƯƠNG TRÌNH DỊCH
10.1. Phương pháp, hình thức kiểm tra, đánh giá: CHƯƠNG TRÌNH DỊCH
------------------------------------------------------------------
+-------------+-------------+-------------+-------------+-------------+
| Hình      | Phương    | Mục       | CLO được  | Trọng     |
| thức      | pháp      | đích      | đánh giá  | số        |
|             |             |             |             |             |
| (Chuyên    | (Viết, vấn |             |             |             |
| cần, giữa   | đáp, thực   |             |             |             |
| kỳ, kết     | hành, bài   |             |             |             |
| thúc học    | tập lớn,    |             |             |             |
| phần, ...) | ...)       |             |             |             |
+=============+=============+=============+=============+=============+
| Bài tập lớn | Dự án nhỏ   | Đánh giá kỹ |             | 15%         |
|             | làm việc    | năng lập    |             |             |
|             | theo nhóm   | trình, xây  |             |             |
|             |             | dựng hệ     |             |             |
|             |             | thống dịch  |             |             |
|             |             | vận dụng    |             |             |
|             |             | kiến thức   |             |             |
|             |             | đã học      |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Kiểm tra    | Thi viết    | Đánh giá    |             | 25%         |
| giữa kỳ     |             | kiến thức,  |             |             |
|             |             | kỹ năng     |             |             |
|             |             | sinh viên   |             |             |
|             |             | đạt được    |             |             |
|             |             | sau nửa học |             |             |
|             |             | kỳ          |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Thi kết     | Thi viết    | Đánh giá    |             | 60%         |
| thúc môn    |             | kiến thức,  |             |             |
| học         |             | kỹ năng     |             |             |
|             |             | sinh viên   |             |             |
|             |             | đạt được    |             |             |
|             |             | khi kết     |             |             |
|             |             | thúc môn    |             |             |
|             |             | học         |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Tổng:   |             | 100%    |             |             |
+-------------+-------------+-------------+-------------+-------------+
CHƯƠNG TRÌNH DỊCH
-----------------
10.2. Tiêu chí đánh giá: CHƯƠNG TRÌNH DỊCH
------------------------------------------
\- Tiêu chí đánh giá cụ thể với từng đầu điểm của môn học:
\+ Bài tập lớn: đọc hiểu được tài liệu hệ thống CUP; viết được luật phân
tích từ tố/cú pháp/ngữ nghĩa/sinh mã (trong luật có thể bao gồm mã nguồn
Java) để dịch ngôn ngữ VC sang ngôn ngữ của JVM; biên dịch thành hệ
thống chạy được; tùy biến hệ thống theo các yêu cầu của giảng viên.
\+ Kiểm tra giữa kỳ: nắm được kiến thức đã học trong tuần 1 đến tuần 7;
khả năng vận dụng kiến thức về ngôn ngữ hình thức, thuật toán trong xây
dựng mô-đun phân tích từ vựng, phân tích cú pháp của chương trình dịch.
\+ Kết thúc môn: nắm được kiến thức, kỹ năng đã học trong cả 15 tuần của
học kỳ.
\- Cụ thể việc đánh giá kiến thức, kỹ năng của sinh viên theo các mức
đáp ứng được chuẩn đầu ra, mức khá, mức giỏi:
Tùy vào mức độ hoàn thành các bài kiểm tra trên mà sinh viên sẽ được
phân loại thành trung bình, khá, và giỏi.
-   Giỏi: hoàn thành hết các bài tập được giao với mức độ hoàn thiện cao
-   Khá: hoàn thành được các bài tập cơ bản, chưa làm được các bài tập
> nâng cao hoặc làm chưa hoàn thiện
-   Trung bình: còn một số nội dung chưa làm được.
Tiêu chí đánh giá chung:
Mức chất lượng   Thang điểm   Mô tả mức chất lượng/Yêu cầu
-------------------- ---------------- ----------------------------------------------------------------------------------------------------
Xuất sắc             9-10             Hoàn thành tốt các yêu cầu đề ra, thể hiện khả năng vận dụng thành thạo các kiến thức đã học
Khá, giỏi            7-8              Hoàn thành khoảng 70-80% các yêu cầu đề ra, thể hiện khả năng vận dụng cơ bản các kiến thức đã học
Đạt                  5-6              Hoàn thành khoảng 50-60% các yêu cầu đề ra, mới dừng lại ở mức mô tả lại kiến thức đã học
Chưa đạt             0-4              Hoàn thành dưới 50% yêu cầu đề ra, trên 50% yêu cầu quan trọng chưa đạt
10.3. Lịch thi và kiểm tra: CHƯƠNG TRÌNH DỊCH
---------------------------------------------
Hình thức kiểm tra   Thời gian   Dự kiến thời gian tiến hành
------------------------ --------------- ---------------------------------
Bài tập lớn 1                            Tuần 5
Kiểm tra giữa kỳ                         Tuần 8
Bài tập lớn 2                            Tuần 9
Thi cuối kỳ                              Theo lịch của Trường
Hà Nội, ngày tháng năm 2023
----------- -------------------- ----------------------
Duyệt   Chủ nhiệm Khoa   Chủ nhiệm Bộ môn
----------- -------------------- ----------------------
CHƯƠNG TRÌNH DỊCH
PHỤ LỤC