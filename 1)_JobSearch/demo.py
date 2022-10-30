from bs4 import BeautifulSoup

with open("index.html","r") as file:
    content = file.read()
    soup = BeautifulSoup(content,"html.parser")

    # Course headings
    course_headings = soup.find_all("h5")
    for course in course_headings:
        print(course.text)

    print("=========================")

    # Course cards
    course_cards = soup.find_all("div",class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

    