

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
      'accuracy': ''
    }

    ############
    #  NEED TO HANDLE FILES WITHOUT DATA
    ############

    # getting all tds with score keywords
    osat_td = soup.find("td", text="Overall Satisfaction")
    taste_td = soup.find('td', text="Taste")
    speed_td = soup.find('td', text="Fast Service")
    ace_td = soup.find('td', text="Attentive/Courteous")
    clean_td = soup.find('td', text="Cleanliness Combined")
    accuracy_td = soup.find('td', text="Order Accuracy")


    # deriving score tables from tds
    osat_table = osat_td.parent.parent.parent
    taste_table = taste_td.parent.parent.parent
    speed_table = speed_td.parent.parent.parent
    ace_table = ace_td.parent.parent.parent
    clean_table = clean_td.parent.parent.parent
    accuracy_table = accuracy_td.parent.parent.parent


    # deriving sub tables within score tables
    osat_sub_tables = osat_table.select('tr.BelowMinResp')
    taste_sub_tables = taste_table.select('tr.BelowMinResp')
    speed_sub_tables = speed_table.select('tr.BelowMinResp')
    ace_sub_tables = ace_table.select('tr.BelowMinResp')
    clean_sub_tables = clean_table.select('tr.BelowMinResp')
    accuracy_sub_tables = accuracy_table.select('tr.BelowMinResp')


    # using osat to get responses
    osat_responses_element = osat_table.select('td.Default_Footer')[0]
    responses = osat_responses_element.text.split(' ')[0]
    results['responses'] = responses

    # function to extract scores out of sub tables
    def extract_score_from_sub_tables(sub_tables):
      for i in range(len(sub_tables)):
        current_text = sub_tables[i].text
        if contains_substring(current_text, "Highly Satisfied"):
          sub_table = sub_tables[i]
          score = sub_table.select('td[align="right"]')[0].text.strip()
          return score

    def extract_accuracy_from_sub_tables(sub_tables):
        for i in range(len(sub_tables)):
          current_text = sub_tables[i].text
          if contains_substring(current_text, "Yes"):
            sub_table = sub_tables[i]
            score = sub_table.select('td[align="right"]')[0].text.strip()
            return score



    results['osat'] = extract_score_from_sub_tables(osat_sub_tables)
    results['taste'] = extract_score_from_sub_tables(taste_sub_tables)
    results['speed'] = extract_score_from_sub_tables(speed_sub_tables)
    results['ace'] = extract_score_from_sub_tables(ace_sub_tables)
    results['clean'] = extract_score_from_sub_tables(clean_sub_tables)
    results['accuracy'] = extract_accuracy_from_sub_tables(accuracy_sub_tables)


    return results

    



    