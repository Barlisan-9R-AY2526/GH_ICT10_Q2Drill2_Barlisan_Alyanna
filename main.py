# getting data from a textbox
from pyscript import display, document


def get_name(e):
    document.getElementById("div1").innerHTML = ''
    club_members = ['carina jimenez', 'nancy milante', 'daphne mariano', 'alyanna barlisan', 'aj darimbang', 'jm piansay']
    first_name = document.getElementById("fname").value.lower().strip()
    last_name = document.getElementById("lname").value.lower().strip()
    full_name = first_name + ' ' + last_name
    name_checker = full_name in club_members
    display_message = (
        f'Sorry {full_name}, your name is not on the list of members. Try again next year!',
        f'Congratulations {full_name}! You are now part of the Rainbow Catering Club.'
    )
    display(display_message[name_checker], target='div1')