from datetime import datetime
import calendar

from django.template import Library

from hackerspace.YOUR_HACKERSPACE import (
    HACKERSPACE_IS_OPEN_BASED_ON_OPENING_HOURS,
    HACKERSPACE_IS_OPEN_CUSTOM_CHECK, HACKERSPACE_OPENING_HOURS,
    HACKERSPACE_TIMEZONE)

register = Library()


@register.filter
def getOpenNowStatus(placeholder):
    today_weekday = calendar.day_name[datetime.now(
        HACKERSPACE_TIMEZONE).weekday()]
    now_hour = datetime.now(HACKERSPACE_TIMEZONE).hour
    now_minute = datetime.now(HACKERSPACE_TIMEZONE).minute
    status = 'Unknown'
    if HACKERSPACE_IS_OPEN_BASED_ON_OPENING_HOURS == True:
        for status_change in HACKERSPACE_OPENING_HOURS[today_weekday]:
            if now_hour >= status_change[0] and now_minute >= status_change[1]:
                status = status_change[2]
                color_indicator = status_change[3]
            else:
                break
        return '<div class="status_code_icon '+color_indicator+'"></div><div>'+status+'</div>'

    else:
        return HACKERSPACE_IS_OPEN_CUSTOM_CHECK