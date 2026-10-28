def get_phone_num(country: int, area: int, first: int, last: int) -> str:

    return(f"+{country}-{area}{first}-{last}")

print(get_phone_num( area= 1, first= 303, country= 880, last= 943985))