class WebObjects:
    site = {
        'Home':'https://www.booking.com',
        '':''
    }
    objects = {
        'FieldSearch':'//*[@id="ss"]',
        'BtnAcceptCookies':'//*[@id="onetrust-accept-btn-handler"]',
        'BtnHotelFromTable':'//*[@id="search_results_table"]/div/div/div/div/div[6]/div[#]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a',
        'LblHotelName':'//*[@id="hp_hotel_name"]',
        'TblFacilities':'//*[@id="hp_facilities_box"]/div[3]'
    }
    
    # //*[@id="hp_hotel_name"]/text()