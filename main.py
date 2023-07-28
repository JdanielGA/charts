from app.charts import generate_bar_chart, generate_pie_chart
from pkg.read_csv import read_csv
from pkg.utils import get_population, get_percentage, clean_screen
import time

def run():

    data = read_csv('./Documents/world_population.csv')
    selection = 0

    while selection not in [1, 2, 3]:
        
        clean_screen()
        selection = input('''
What do you want to do?
                    
-> 1 for consult by country.
-> 2 for consult percentages of global population
-> 3 for exit

''')
        try:
            user_selection = int(selection)

            if user_selection == 1:
                clean_screen()
                consultation = get_population(data)
                chart = generate_bar_chart(consultation)
            
            elif user_selection == 2:
                clean_screen()
                consultation = get_percentage(data)
                chart = generate_pie_chart(consultation)
            
            elif user_selection == 3:
                clean_screen()
                break
        
        except ValueError:

            clean_screen()
            print("\nInvalid input! Please enter a valid number.")
            time.sleep(2)

    

if __name__ == '__main__':

    run()