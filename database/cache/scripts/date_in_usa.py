from datetime import datetime, timezone, timedelta


def date_now() -> str:
    usa_time = datetime.now(timezone(timedelta(hours=-5)))
    usa_current_date = usa_time.strftime("%Y-%m-%d")
    return usa_current_date


def compare_dates(cached_date: str) -> bool:
    usa_time = datetime.now(timezone(timedelta(hours=-5)))
    current_date = usa_time.strftime("%Y-%m-%d")

    if cached_date == current_date:
        return True
    else:
        return False
