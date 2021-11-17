import pandas

student_dictionary = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dictionary)
# print(student_data_frame)

# looping through frame
# for (key, value) in student_data_frame.items():
#     print(value)
# pandas inbuilt loop
for (index, row) in student_data_frame.iterrows():
    print(row)
