def get_cem_list(cems_for_messaging):


  message_list = [
      'Here is a breakdown of our current CEM scores',
      'BREAK',
      'BREAK',
      '========================',
      'BREAK',
      f"CURRENT MONTH - {cems_for_messaging['mtd_surveys']} surveys",
      "BREAK",
      f"OSAT - {cems_for_messaging['mtd_osat']}",
      "BREAK",
      f"Taste - {cems_for_messaging['mtd_taste']}",
      "BREAK",
      f"Speed - {cems_for_messaging['mtd_speed']}",
      "BREAK",
      f"ACE - {cems_for_messaging['mtd_ace']}",
      "BREAK",
      f"Cleanliness - {cems_for_messaging['mtd_clean']}",
      "BREAK",
      f"Accuracy - {cems_for_messaging['mtd_accuracy']}",
      "BREAK",
      "BREAK",
      '========================',
      "BREAK",
      f"90 DAY ROLLING - {cems_for_messaging['ndr_surveys']} surveys",
      "BREAK",
      f"OSAT - {cems_for_messaging['ndr_osat']}",
      "BREAK",
      f"Taste - {cems_for_messaging['ndr_taste']}",
      "BREAK",
      f"Speed - {cems_for_messaging['ndr_speed']}",
      "BREAK",
      f"ACE - {cems_for_messaging['ndr_ace']}",
      "BREAK",
      f"Cleanliness - {cems_for_messaging['ndr_clean']}",
      "BREAK",
      f"Accuracy - {cems_for_messaging['ndr_accuracy']}",
      "BREAK",
      "BREAK",
      '========================',
      "BREAK",
      f"YEAR TO DATE - {cems_for_messaging['ytd_surveys']} surveys",
      "BREAK",
      f"OSAT - {cems_for_messaging['ytd_osat']}",
      "BREAK",
      f"Taste - {cems_for_messaging['ytd_taste']}",
      "BREAK",
      f"Speed - {cems_for_messaging['ytd_speed']}",
      "BREAK",
      f"ACE - {cems_for_messaging['ytd_ace']}",
      "BREAK",
      f"Cleanliness - {cems_for_messaging['ytd_clean']}",
      "BREAK",
      f"Accuracy - {cems_for_messaging['ytd_accuracy']}",
  ]

  return message_list
