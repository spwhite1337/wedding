

def mustard_seed(num_guests: int) -> float:
    drink = 26.5  # 21.5 is cheaper option
    drink_service = .2
    drink_tax = .07
    food = 9107 / 157  # 59
    rental = 7500 * 1.07
    decor = 200 + 2 * num_guests  # lounge + chairs
    return drink * (1 + drink_service + drink_tax) * num_guests + food * num_guests + rental + decor


def smith_farm(num_guests: int) -> float:
    food = 63 + 12  # Estimate
    food_tax = 1.07
    food_flat_fee = 250
    rental = 5000
    drinks = 10 * 5
    helper = 1000
    return rental + food_flat_fee + food * food_tax * num_guests + drinks * num_guests + helper


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
    drinks = 15 * 5

    return rental_fee + food * food_upcharge * num_guests + bar_fee + drinks * num_guests


def red_lion_inn(num_guests: int) -> float:
    rental_fee = 3000
    admin = 0.22
    tax = 0.0854
    food_drink = 180
    return (rental_fee + food_drink * num_guests) * (1 + admin + tax)


def commons(num_guests: int) -> float:
    rental = 3000
    food_min = 10500
    security = 59.2 * 8
    food_add = 0.08
    sales_tax = 0.07
    gratuity = 0.2
    food = 60 + 12 + 5
    beer = 35 + 10
    food_pre_tax = food * num_guests if food * num_guests > food_min else food_min
    food_pre_tax *= (1 + food_add)
    return (rental + food_pre_tax + security + beer) * (1 + sales_tax + gratuity)


def hamilton_hall(num_guests: int) -> float:
    rental = 3750
    beer = 31
    food = 75 + 15 + 5
    food_tax = 0.07
    sales_tax = 0.07
    return (rental + food * (1 + food_tax) * num_guests + beer * num_guests) * (1 + sales_tax)


prices = {
    'MustardSeed': mustard_seed,
    'Canal337': canal_337,
    'Smith': smith_farm,
    'Winery1620': winery_1620,
    'RedLion': red_lion_inn,
    'Commons': commons,
    'Hamilton': hamilton_hall
}
