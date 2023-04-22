import pdfplumber
from pdfrw import PdfReader, PdfWriter

def file_name(i, main_patch, mode):
    print("тута крч тип - "+mode)
    with pdfplumber.open(main_patch) as pdf:
        student_name = ""
        date = ""
        previous_word = ""
        key = 0

        page = pdf.pages[i]
        text = page.extract_text()

        splited_text = text.split()
        if mode == "report":
            for word in splited_text:
                print(previous_word)
                if previous_word == "NAME:":
                    key = 1

                if word == "ATTENDANCE:":
                    break

                if key == 1:
                    student_name += word+" "

                if word == "YEAR":
                    date += "Y"
                elif key == 0 and word != "NAME:":
                    date += word[0] + word[1:].lower()+" "
                previous_word = word

        if mode == "mok":
            print("Оно сюда пришло")
            for word in splited_text:
                print(previous_word)
                if previous_word == "Name:":
                    key = 1

                if word == "Below":
                    break

                if key == 1:
                    student_name += word + " "

                previous_word = word

            for word in splited_text:
                print(previous_word)
                if previous_word == "school3@bismoscow.com":
                    key = 1

                if word == "Name:":
                    break

                if key == 1:
                    date += word + " "

                previous_word = word


        file_final_name = student_name + date
        print("student name - "+student_name)
        print("date - "+date)
        print(file_final_name,"\n\n\n\n")
        return(file_final_name)

def separate_main_file(report_name, page_number, output_patch, main_path):
    output_file = r"{0}/{1}.pdf".format(output_patch,report_name)
    reader_input = PdfReader(main_path)
    writer_output = PdfWriter()

    for current_page in range(page_number, page_number+2):
        writer_output.addpage(reader_input.pages[current_page])

    writer_output.write(output_file)

def separate_all(main_patch, output_path, list_w, mode):

    i = 0
    pdf_obj = PdfReader(main_patch)
    total_pages = len(pdf_obj.pages)

    while i <= total_pages - 2:
        name = file_name(i, main_patch, mode)
        separate_main_file(name, i, output_path, main_patch)
        i += 2
        list_w.addItem("created - "+name)

    list_w.addItem("Process was sucсessfully finished")

