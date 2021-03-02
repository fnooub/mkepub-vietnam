# -*- coding: utf-8 -*-
import mkepub

book = mkepub.Book(title='Advanced Example', author='The Author', subjects=['Văn học', 'Công nghệ'])
# multiple authors can be specified as a list:
# mkepub.Book(title='Advanced Example', authors=['The First Author', 'The Second Author'])
with open('cover.jpg', 'rb') as file:
    book.set_cover(file.read())
with open('style.css') as file:
    book.set_stylesheet(file.read())

first = book.add_page('Chapter 1', 'And so the book begins.')

child = book.add_page('Chapter 1.1', 'Nested TOC is supported.', parent=first)
book.add_page('Chapter 1.1.1', 'Infinite nesting levels', parent=child)
book.add_page('Chapter 1.2', 'In any order you wish.', parent=first)

book.add_page('Chapter 2', 'Use <b>html</b> to make your text <span class="pink">prettier</span>')

book.add_page('Chapter 3: Images', '<p>Chúng ta vẫn biết rằng, làm việc với một đoạn văn bản dễ đọc và rõ nghĩa dễ gây rối trí và cản trở việc tập trung vào yếu tố trình bày văn bản. Lorem Ipsum có ưu điểm hơn so với đoạn văn bản chỉ gồm nội dung kiểu "Nội dung, nội dung, nội dung" là nó khiến văn bản giống thật hơn, bình thường hơn. Nhiều phần mềm thiết kế giao diện web và dàn trang ngày nay đã sử dụng Lorem Ipsum làm đoạn văn bản giả, và nếu bạn thử tìm các đoạn "Lorem ipsum" trên mạng thì sẽ khám phá ra nhiều trang web hiện vẫn đang trong quá trình xây dựng. Có nhiều phiên bản khác nhau đã xuất hiện, đôi khi do vô tình, nhiều khi do cố ý (xen thêm vào những câu hài hước hay thông tục).</p><img src="images/chapter3.jpg" alt="You can use images as well" /><p>Lorem Ipsum chỉ đơn giản là một đoạn văn bản giả, được dùng vào việc trình bày và dàn trang phục vụ cho in ấn. Lorem Ipsum đã được sử dụng như một văn bản chuẩn cho ngành công nghiệp in ấn từ những năm 1500, khi một họa sĩ vô danh ghép nhiều đoạn văn bản với nhau để tạo thành một bản mẫu văn bản. Đoạn văn bản này không những đã tồn tại năm thế kỉ, mà khi được áp dụng vào tin học văn phòng, nội dung của nó vẫn không hề bị thay đổi. Nó đã được phổ biến trong những năm 1960 nhờ việc bán những bản giấy Letraset in những đoạn Lorem Ipsum, và gần đây hơn, được sử dụng trong các ứng dụng dàn trang, như Aldus PageMaker.</p>')
# as long as you add them to the book:
with open('chapter3.jpg', 'rb') as file:
    book.add_image('chapter3.jpg', file.read())

book.save('advanced.epub')