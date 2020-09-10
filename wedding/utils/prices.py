

def mustard_seed(num_guests: int) -> float:
    drink = 26.5  # 21.5 is cheaper option
    drink_service = .2
    drink_tax = .07
    return drink *(1 + drink_service * drink_tax) * num_guests


def smith_farm(num_guests: int) -> float:
    food = 80  # Estimate
    food_tax = 1.07
    food_flat_fee = 250
    return food_flat_fee + food * food_tax * num_guests


def canal_337(num_guests: int) -> float:
    num_guests = 130 if num_guests < 130 else num_guests
    admin_sales_fee = .28
    extra_food_drink_tax = .02
    food_drink = 135
    rental_fee = 4000
    return rental_fee * (1 + admin_sales_fee) + num_guests * food_drink * (1 + extra_food_drink_tax + admin_sales_fee)


def winery_1620(num_guests: int) -> float:
    num_guests = 100 if num_guests < 100 else num_guests
    rental_fee = 7500
    food = 102
    food_upcharge = 1.34

    if num_guests < 119:
        bar_fee = 1000
    elif num_guests < 149:
        bar_fee = 1200
    else:
        bar_fee = 1400

    # Estimate at $15 / hr / guest
    drinks = 15 * num_guests * 5

    return rental_fee + food * food_upcharge + bar_fee + drinks


prices = {
    'MustardSeed': mustard_seed,
    'Canal337': canal_337,
    'Smith': smith_farm,
    'Winery1620': winery_1620
}
