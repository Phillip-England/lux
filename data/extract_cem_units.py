

from bs4 import BeautifulSoup

from util import contains_substring


def extract_cem_units(file_path):
  with open(file_path) as file:


    soup = BeautifulSoup(file, 'html.parser')

    # results stored here
    results = {
      'osat': '',
      'taste': '',
      'speed': '',
      'ace': '',
      'clean': '',
      'accuracy': '',
      'start_date': soup.select("div#__start_date")[0].text,
      'end_date': soup.select("div#__end_date")[0].text,
      'start_day_of_week': soup.select("div#__start_day_of_week")[0].text,
      'end_day_of_week': soup.select("div#__end_day_of_week")[0].text
    }

    if soup.select("div#__error_exists")[0].text == "TRUE":
      results['error'] = True
    else:
      results['error'] = False

    error_message = results['error']

    if error_message == True:
      return results

    # getting all tds with score keywords
    osat_td = soup.find("td", text="Overall Satisfaction")
    taste_td = soup.find('td', text="Taste")
    speed_td = soup.find('td', text="Fast Service")
    ace_td = soup.find('td', text="Attentive/Courteous")
    clean_td = soup.find('td', text="Cleanliness Combined")
    accuracy_td = soup.find('td', text="Order Accuracy")

    osat_table = osat_td.parent.parent
    taste_table = taste_td.parent.parent
    speed_table = speed_td.parent.parent
    ace_table = ace_td.parent.parent
    clean_table = clean_td.parent.parent
    accuracy_table = accuracy_td.parent.parent

    results['osat'] = osat_table.find(text=" Highly Satisfied").find_parent().find_next_sibling().find_next_sibling().text.strip()
    results['taste'] = taste_table.find(text=" Highly Satisfied").find_parent().find_next_sibling().find_next_sibling().text.strip()
    results['speed'] = speed_table.find(text=" Highly Satisfied").find_parent().find_next_sibling().find_next_sibling().text.strip()
    results['ace'] = ace_table.find(text=" Highly Satisfied").find_parent().find_next_sibling().find_next_sibling().text.strip()
    results['clean'] = clean_table.find(text=" Highly Satisfied").find_parent().find_next_sibling().find_next_sibling().text.strip()
    results['accuracy'] = accuracy_table.find(text=" Yes").find_parent().find_next_sibling().find_next_sibling().text.strip()


    return results

    



    