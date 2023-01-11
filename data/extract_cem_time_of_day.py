from bs4 import BeautifulSoup

from util import contains_substring


def extract_cem_time_of_day(file_path):

  with open(file_path) as file:
    soup = BeautifulSoup(file, 'html.parser')

    results = {
      'breakfast_osat': '',
      'lunch_osat': '',
      'mid_osat': '',
      'dinner_osat': '',
      'breakfast_taste': '',
      'lunch_taste': '',
      'mid_taste': '',
      'dinner_taste': '',
      'breakfast_speed': '',
      'lunch_speed': '',
      'mid_speed': '',
      'dinner_speed': '',
      'breakfast_ace': '',
      'lunch_ace': '',
      'mid_ace': '',
      'dinner_ace': '',
      'breakfast_clean': '',
      'lunch_clean': '',
      'mid_clean': '',
      'dinner_clean': '',
      'breakfast_accuracy': '',
      'lunch_accuracy': '',
      'mid_accuracy': '',
      'dinner_accuracy': '',
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

    osat_table = osat_td.parent.parent.parent
    taste_table = taste_td.parent.parent.parent
    speed_table = speed_td.parent.parent.parent
    ace_table = ace_td.parent.parent.parent
    clean_table = clean_td.parent.parent.parent
    accuracy_table = accuracy_td.parent.parent.parent

    # OSAT
    try:
      osat_sub_table = osat_table.find_all(string=lambda text: 'Before 10:30 AM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['breakfast_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      osat_sub_table = osat_table.find_all(string=lambda text: '10:30 AM to 2 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['lunch_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      osat_sub_table = osat_table.find_all(string=lambda text: '2 PM to 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mid_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      osat_sub_table = osat_table.find_all(string=lambda text: 'After 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dinner_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # TASTE
    try:
      taste_sub_table = taste_table.find_all(string=lambda text: 'Before 10:30 AM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['breakfast_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      taste_sub_table = taste_table.find_all(string=lambda text: '10:30 AM to 2 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['lunch_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      taste_sub_table = taste_table.find_all(string=lambda text: '2 PM to 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mid_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      taste_sub_table = taste_table.find_all(string=lambda text: 'After 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dinner_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # SPEED
    try:
      speed_sub_table = speed_table.find_all(string=lambda text: 'Before 10:30 AM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['breakfast_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      speed_sub_table = speed_table.find_all(string=lambda text: '10:30 AM to 2 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['lunch_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      speed_sub_table = speed_table.find_all(string=lambda text: '2 PM to 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mid_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      speed_sub_table = speed_table.find_all(string=lambda text: 'After 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dinner_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # ACE
    try:
      ace_sub_table = ace_table.find_all(string=lambda text: 'Before 10:30 AM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['breakfast_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      ace_sub_table = ace_table.find_all(string=lambda text: '10:30 AM to 2 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['lunch_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      ace_sub_table = ace_table.find_all(string=lambda text: '2 PM to 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mid_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      ace_sub_table = ace_table.find_all(string=lambda text: 'After 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dinner_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # CLEAN
    try:
      clean_sub_table = clean_table.find_all(string=lambda text: 'Before 10:30 AM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['breakfast_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      clean_sub_table = clean_table.find_all(string=lambda text: '10:30 AM to 2 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['lunch_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      clean_sub_table = clean_table.find_all(string=lambda text: '2 PM to 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mid_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      clean_sub_table = clean_table.find_all(string=lambda text: 'After 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dinner_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # ACCURATE
    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: 'Before 10:30 AM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['breakfast_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: '10:30 AM to 2 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['lunch_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: '2 PM to 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mid_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: 'After 5 PM' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dinner_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass



    return results

    

      