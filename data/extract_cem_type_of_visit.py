from bs4 import BeautifulSoup

from util import contains_substring


def extract_cem_type_of_visit(file_path):

  with open(file_path) as file:
    soup = BeautifulSoup(file, 'html.parser')

    results = {
      'dine_in_osat': '',
      'drive_thru_osat': '',
      'carry_out_osat': '',
      'mobile_osat': '',
      'dine_in_taste': '',
      'drive_thru_taste': '',
      'carry_out_taste': '',
      'mobile_taste': '',
      'dine_in_speed': '',
      'drive_thru_speed': '',
      'carry_out_speed': '',
      'mobile_speed': '',
      'dine_in_ace': '',
      'drive_thru_ace': '',
      'carry_out_ace': '',
      'mobile_ace': '',
      'dine_in_clean': '',
      'drive_thru_clean': '',
      'carry_out_clean': '',
      'mobile_clean': '',
      'dine_in_accuracy': '',
      'drive_thru_accuracy': '',
      'carry_out_accuracy': '',
      'mobile_accuracy': '',
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
      osat_sub_table = osat_table.find_all(string=lambda text: 'Dine' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dine_in_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      osat_sub_table = osat_table.find_all(string=lambda text: 'Drive-thru' in text)[0].find_parent().find_parent().find_next_sibling()
      results['drive_thru_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      osat_sub_table = osat_table.find_all(string=lambda text: 'Carry Out' in text)[0].find_parent().find_parent().find_next_sibling()
      results['carry_out_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      osat_sub_table = osat_table.find_all(string=lambda text: 'Mobile' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mobile_osat'] =  osat_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # TASTE
    try:
      taste_sub_table = taste_table.find_all(string=lambda text: 'Dine' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dine_in_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      taste_sub_table = taste_table.find_all(string=lambda text: 'Drive-thru' in text)[0].find_parent().find_parent().find_next_sibling()
      results['drive_thru_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      taste_sub_table = taste_table.find_all(string=lambda text: 'Carry Out' in text)[0].find_parent().find_parent().find_next_sibling()
      results['carry_out_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      taste_sub_table = taste_table.find_all(string=lambda text: 'Mobile' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mobile_taste'] =  taste_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # SPEED
    try:
      speed_sub_table = speed_table.find_all(string=lambda text: 'Dine' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dine_in_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      speed_sub_table = speed_table.find_all(string=lambda text: 'Drive-thru' in text)[0].find_parent().find_parent().find_next_sibling()
      results['drive_thru_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      speed_sub_table = speed_table.find_all(string=lambda text: 'Carry Out' in text)[0].find_parent().find_parent().find_next_sibling()
      results['carry_out_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      speed_sub_table = speed_table.find_all(string=lambda text: 'Mobile' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mobile_speed'] =  speed_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # ACE
    try:
      ace_sub_table = ace_table.find_all(string=lambda text: 'Dine' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dine_in_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      ace_sub_table = ace_table.find_all(string=lambda text: 'Drive-thru' in text)[0].find_parent().find_parent().find_next_sibling()
      results['drive_thru_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      ace_sub_table = ace_table.find_all(string=lambda text: 'Carry Out' in text)[0].find_parent().find_parent().find_next_sibling()
      results['carry_out_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      ace_sub_table = ace_table.find_all(string=lambda text: 'Mobile' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mobile_ace'] =  ace_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # CLEAN
    try:
      clean_sub_table = clean_table.find_all(string=lambda text: 'Dine' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dine_in_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      clean_sub_table = clean_table.find_all(string=lambda text: 'Drive-thru' in text)[0].find_parent().find_parent().find_next_sibling()
      results['drive_thru_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      clean_sub_table = clean_table.find_all(string=lambda text: 'Carry Out' in text)[0].find_parent().find_parent().find_next_sibling()
      results['carry_out_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      clean_sub_table = clean_table.find_all(string=lambda text: 'Mobile' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mobile_clean'] =  clean_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    # ACCURATE
    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: 'Dine' in text)[0].find_parent().find_parent().find_next_sibling()
      results['dine_in_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: 'Drive-thru' in text)[0].find_parent().find_parent().find_next_sibling()
      results['drive_thru_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: 'Carry Out' in text)[0].find_parent().find_parent().find_next_sibling()
      results['carry_out_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    try:
      accuracy_sub_table = accuracy_table.find_all(string=lambda text: 'Mobile' in text)[0].find_parent().find_parent().find_next_sibling()
      results['mobile_accuracy'] =  accuracy_sub_table.select('td[align="right"]')[0].text.strip()
    except:
      pass

    return results