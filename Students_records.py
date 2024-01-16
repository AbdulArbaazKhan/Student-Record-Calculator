from tkinter import *
import time


def label(frame, index1, index2, index3):
    return Label(frame, text=index1, font="lucinda 10 bold", bg="#23292E", fg="white", ).grid(row=index2, column=index3, ipadx=20, sticky="w", ipady=2, padx=5, pady=3)


def entry(frame, index1, index2, index3, bg, fg):
    # state="readonly" change entry state
    return Entry(frame, textvariable=index1, borderwidth=0, bg=bg, fg=fg, ).grid(row=index2, column=index3, ipady=2, padx=5, pady=3)


def tot(mark, out_of):
    if len(mark) == 0:
        Total_Marks.set(int(Out_Off.get()))
    else:
        Total_Marks.set(out_of * len(mark))
        return int(out_of * len(mark))


def obtained_Marks(mark):
    add = 0
    fails = 0
    for o in range(0, len(mark)):
        add += mark[o]
        if mark[o] < pass_marks():
            fails += 1
    Fail_Subjects.set(fails)
    Obtained_Marks.set(int(add))
    return add


def average(mark):
    try:
        bar_value.set("Done!!")
        status_bar.update()
        return Average.set(obtained_Marks(mark) / len(mark))
    except ZeroDivisionError as e:
        Average.set("Not divisible by zero")
        bar_value.set("By default")
        status_bar.update()


def percentage(mark):
    try:
        Percentage.set(f"{obtained_Marks(mark) / tot(mark, int(Out_Off.get())) * 100}%")
        return obtained_Marks(mark) / tot(mark, int(Out_Off.get())) * 100
    except TypeError as t:
        Percentage.set("Not divisible by zero")


def pass_marks():
    Pass_Marks.set(f"{(40 / 100) * int(Out_Off.get())}")
    return float((40 / 100) * int(Out_Off.get()))


def grade(mark):
    parc = percentage(mark)
    try:
        if parc > 89:
            Grade.set("A+")
        elif parc > 79:
            Grade.set("A1")
        elif parc > 60:
            Grade.set("A")
        elif parc > 45:
            Grade.set("B")
        elif parc > 35:
            Grade.set("C")
        elif parc > 23:
            Grade.set("D")
        else:
            Grade.set("Fail")
    except TypeError as g:
        Grade.set("At Least One")


def gets(event):
    marks = []
    if Out_Off.get() == '':
        Out_Off.set(75)
    for w in range(0, 14):
        if subject_values[w].get().isnumeric() or subject_values[w].get().replace(".", "").isnumeric():
            marks.append(float(subject_values[w].get()))
    tot(marks, int(Out_Off.get()))
    obtained_Marks(marks)
    average(marks)
    percentage(marks)
    pass_marks()
    Date.set(time.asctime())
    grade(marks)


root = Tk()
root.geometry("600x500")
root.title("Students Data")
Results = Frame(root, bg="#23292E", borderwidth=3, relief=GROOVE)
func = ["Obtained Marks", "Percentage", "Grade", "Pass Marks", "Total Marks", "Average", "Date", "Fail_Subjects"]
bar_value = StringVar()
bar_value.set("Fill the Marks boxes and Press Enter")
Obtained_Marks, Percentage, Grade, Pass_Marks, Total_Marks, Average, Date, Fail_Subjects = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
func_list = [Obtained_Marks, Percentage, Grade, Pass_Marks, Total_Marks, Average, Date, Fail_Subjects]
# Subjects and Entries for Students000
Label(text="Student Result Manager", font="lucinda 17 bold", bg="black", fg="white", pady=10).pack(fill=X, padx=1, pady=1)
subjects = Frame(root, bg="#23292E")
subject = ["English-A", "English-B", "Urdu-A", "Urdu-B", "Math", "Physics", "Chemistry", "Social Studies", "Islamiat",
           "Arabic", "Drawing", "Computer Science", "Biology", "Economics", "Out Of", "Class"]
# Entry values
English_A, English_B, Urdu_A, Urdu_B, Math, Physics, Chemistry, Social_Studies, Islamiat, Arabic, Drawing, Computer_Science, Biology, Economics, Out_Off, Class = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
# Entry values list
subject_values = [English_A, English_B, Urdu_A, Urdu_B, Math, Physics, Chemistry, Social_Studies, Islamiat, Arabic, Drawing, Computer_Science, Biology, Economics, Out_Off, Class]
i = 0
i2 = 0
i3 = 0
for i in range(0, 16):
    if i <= 3:
        label(Results, func[i], i, 0)
        func_list[i].set("")
        entry(Results, func_list[i], i, 1, "#23292E", "white")
    if 4 <= i <= 7:
        label(Results, func[i], i3, 2)
        func_list[i].set("")
        entry(Results, func_list[i], i3, 3, "#23292E", "white")
        i3 += 1
    if i <= 7:
        label(subjects, subject[i], i, 0)
        subject_values[i].set("")
        entry(subjects, subject_values[i], i, 1, "#485562", "white")
        continue
    else:
        label(subjects, subject[i], i2, 3)
        subject_values[i].set("")
        entry(subjects, subject_values[i], i2, 4, "#485562", "white")
        i2 += 1
    i += 1
subjects.pack(anchor="nw", fill=X)
bd = Button(root, text="Get Record", bg="#23292E", fg="white", highlightcolor="white", borderwidth=0)
root.bind("<Key-Return>", gets)
bd.bind("<Button-1>", gets)
bd.pack(fill=X, padx=0.5, pady=0.5)
# TODO:When using basic code completion (Ctrl+Space), you don't need to type upper-case letters in CamelHump names.
#  It is enough to type the initial letters of the camel names in lower case, and they will be smartly recognized It
#  is very easy to toggle between find and replace functionality. When you perform search and replace in a file,
#  pressing Ctrl+F shows the search pane. Pressing Ctrl+R adds field, where you can type the replace string.
Results.pack(anchor="nw", fill=X)
# Status bar
status_frame = Frame(root, relief=SUNKEN, width=600, borderwidth=3, bg="#23292E")
status_bar = Label(status_frame, textvar=bar_value, pady=8, bg="#23292E", fg="white", font="timesnewroman 8 italic")
status_bar.pack(anchor=W)
status_frame.pack(side=BOTTOM, fill=X)
root.mainloop()
